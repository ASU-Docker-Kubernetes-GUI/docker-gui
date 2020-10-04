from flask import Flask
from app.routers import client_router, service_router


def create_application():
    # standing up an instance of Flask
    app = Flask(
        __name__,
        instance_relative_config=False
    )

    # Building app from dev config from now
    app.config.from_object('config.DevConfig')

    # Instantiating our routers
    app.register_blueprint(client_router.client_router, url_prefix="")
    app.register_blueprint(service_router.service_router, url_prefix="/api/v1")

    return app

