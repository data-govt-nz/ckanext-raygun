import logging

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from raygun4py.middleware import wsgi

log = logging.getLogger(__name__)


class RaygunExtensionException(Exception):
    pass

class RaygunPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IMiddleware, inherit=True)
    plugins.implements(plugins.IConfigurable, inherit=True)
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.ITemplateHelpers)
    api_key = ''

    def make_error_log_middleware(self, app, config):
        api_key = config.get('raygun.api_key', None)
        if not api_key:
            log.warning('API_KEY is not defined in error logging middleware')
            return app
        raygun_wrapped_app = wsgi.Provider(app, api_key)
        return raygun_wrapped_app

    def configure(self, config):
        '''Load config settings for this extension from config file.
        See IConfigurable.
        '''
        if 'raygun.api_key' not in config:
            log.warning('API_KEY is not defined in error logging middleware')
            return

        self.api_key = config['raygun.api_key']

    def update_config(self, config):
        '''Change the CKAN (Pylons) environment configuration.
        See IConfigurer.
        '''
        toolkit.add_template_directory(config, 'templates')

    def get_helpers(self):
        '''Return the CKAN 2.0 template helper functions this plugin provides.

        See ITemplateHelpers.

        '''
        return {'get_api_key': self.get_api_key}

    def get_api_key(self):
        return self.api_key
    
