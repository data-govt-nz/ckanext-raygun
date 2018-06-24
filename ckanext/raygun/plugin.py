import logging

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from raygun4py.middleware import wsgi

log = logging.getLogger(__name__)


class RaygunExtensionException(Exception):
    pass


class RaygunPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IMiddleware, inherit=True)

    def make_error_log_middleware(self, app, config):
        api_key = config.get('raygun.api_key', None)
        if not api_key:
	    log.warning('API_KEY is not defined in error logging middleware')
        raygun_wrapped_app = wsgi.Provider(app, api_key)
        return raygun_wrapped_app
