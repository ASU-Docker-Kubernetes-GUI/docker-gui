import logging


class LoggingMiddleware:
    """
    LoggingMiddleware logs out the call to which API endpoint was made
    """
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        logging.info('call to {} - {}'.format(environ['REQUEST_METHOD'], environ["REQUEST_URI"]))
        return self.app(environ, start_response)
