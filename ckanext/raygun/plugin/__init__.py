from __future__ import print_function

import logging

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from raygun4py.middleware import wsgi
from raygun4py.raygunprovider import RaygunSender

log = logging.getLogger(__name__)
no_key_warning = 'ckanext.raygun.api_key is not defined in config: {} {}'

api_key_name = 'ckanext.raygun.api_key'
sender_config_name = 'ckanext.raygun.sender_config'

class RaygunExtensionException(Exception):
    pass

class RaygunPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IMiddleware, inherit=True)
    plugins.implements(plugins.IConfigurable, inherit=True)
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.ITemplateHelpers)
    api_key = ''
    sender_config = None
    has_warned = False

    def _set_config(self, config, method_name):
        if api_key_name not in config:
            if not self.has_warned:
                log.warning(no_key_warning.format('RaygunPlugin', method_name))
                self.has_warned = True
            return

        self.api_key = config.get(api_key_name)

        # Convert config string into dict
        sender_config_string = config.get(sender_config_name, None)
        if not sender_config_string:
            return
        self.sender_config = eval(sender_config_string)

    def make_error_log_middleware(self, app, config):
        if not self.api_key:
            return app

        raygun_wrapped_app = wsgi.Provider(app, self.api_key, config=self.sender_config)
        print('Raygun wsgi error logger set up with api key {} and config {}'.format(self.api_key, self.sender_config))
        return raygun_wrapped_app

    def configure(self, config):
        '''Load config settings for this extension from config file.
        See IConfigurable.
        '''
        self._set_config(config, 'configure')

    def update_config(self, config):
        '''Change the CKAN (Pylons) environment configuration.
        See IConfigurer.
        '''
        self._set_config(config, 'update_config')
        toolkit.add_template_directory(config, 'templates')

    def get_helpers(self):
        '''Return the CKAN 2.0 template helper functions this plugin provides.
        See ITemplateHelpers.
        '''
        return {'get_api_key': self.get_api_key}

    def get_api_key(self):
        return self.api_key


# Taken from https://github.com/MindscapeHQ/raygun4py/blob/f65727a8cc8c6e4b089a68efcd906d6dd7080568/python2/raygun4py/raygunprovider.py#L178
# and modified to accept arguments to RaygunSender
class RaygunHandler(logging.Handler):
    def __init__(self, api_key, config, version=None):
        logging.Handler.__init__(self)

        if api_key != '':
            self.sender = RaygunSender(api_key, config=config)
            self.version = version
            print('Raygun console/paster error logger set up with api key {} and config {}'.format(api_key, config))
        else:
            log.warning(no_key_warning.format('RaygunHandler', '__init__'))

    def emit(self, record):
        userCustomData = {
            "Logger Message": record.msg
        }
        if self.sender is not None:
            self.sender.send_exception(userCustomData=userCustomData)
        else:
            log.warning(record.msg)
