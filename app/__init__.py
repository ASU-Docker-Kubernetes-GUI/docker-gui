from flask import Flask
from app.routers import client_router, service_router
from app.middlewares import logging_middleware
import logging


def create_application():
    # standing up an instance of Flask
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

    app = Flask(
        __name__,
        instance_relative_config=False
    )

    # Building app from dev config from now
    config = 'config.DevConfig'
    logging.info('Starting app from {}'.format(config))
    app.config.from_object(config)

    # Instantiating our routers
    app.register_blueprint(client_router.client_router, url_prefix="")
    app.register_blueprint(service_router.service_router, url_prefix="/api/v1")

    # Adding middlewares
    app.wsgi_app = logging_middleware.LoggingMiddleware(app.wsgi_app)

    logging.info('App is done being built')
    return app
