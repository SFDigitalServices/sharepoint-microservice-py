"""Main application module"""
import os
import json
import jsend
import sentry_sdk
import falcon
from service.resources.welcome import Welcome
from service.resources.sharepoint import File

def start_service():
    """Start this service
    set SENTRY_DSN environmental variable to enable logging with Sentry
    """
    # Initialize Sentry
    sentry_sdk.init(os.environ.get('SENTRY_DSN'))
    # Initialize Falcon
    api = falcon.App()
    api.add_route('/welcome', Welcome())
    api.add_route('/sharepoint/{site_name}/files', File())
    api.add_sink(default_error, '')
    return api

def default_error(_req, resp):
    """Handle default error"""
    resp.status = falcon.HTTP_404
    msg_error = jsend.error('404 - Not Found')

    sentry_sdk.capture_message(msg_error)
    resp.text = json.dumps(msg_error)
