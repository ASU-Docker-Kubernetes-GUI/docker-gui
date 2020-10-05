from flask import Blueprint, request, jsonify
from app.handlers import service_handler as handler
from . import errors
import logging

"""
service_router.py renders all of the backend routes that we are exposing in our
application. 

All of these routes will be prefixed with `/api/v1/`, followed by the route.
"""

service_router = Blueprint(
    'service_router',
    __name__,
    url_prefix="/api/v1"
)


@service_router.route('/')
@service_router.route('/ping')
def service_healthcheck():
    """
    service_healthcheck is a ping that immediately returns an OK
    """
    logging.info('calling service_healthcheck')
    return jsonify(handler.handle_healthcheck())


@service_router.route('/docker-status')
def docker_healthcheck():
    logging.info('calling docker_healthcheck')
    return jsonify(handler.handle_docker_healthcheck())


@service_router.route('/create', methods=["POST"])
def service_create_docker_container():
    logging.info('calling service_create_docker_container')
    message = {}

    if request.method == "POST":
        image_tag = request.args.get('image')
        success = handler.handle_create_container(image_tag)

        message["success"] = success
        message["message"] = "created container successfully" if success else "failed to create"

    else:
        message["message"] = "there was an error"
    return jsonify(message)


@service_router.route('/containers', methods=["GET"])
def service_get_running_containers():
    logging.info('calling service_get_running_containers')
    return handler.handle_get_running_containers()


@service_router.route('/container/<container_id>', methods=["GET"])
def service_get_running_container(container_id):
    if container_id is None:
        return jsonify({
            "message": "invalid container ID"
        })

    return jsonify(handler.handle_get_running_container(container_id))


@service_router.route('/stop/<container_id>', methods=["GET"])
def service_stop_container(container_id):
    if container_id is None:
        return jsonify({
            "message": "invalid container ID"
        })

    return jsonify(handler.handle_stop_container(container_id))


@service_router.route('/start/<container_id>', methods=["GET"])
def service_start_container(container_id):
    if container_id is None:
        return jsonify({
            "message": "invalid container ID"
        })

    return jsonify(handler.handle_start_container(container_id))


@service_router.route('/delete/<container_id>', methods=["DELETE"])
def service_remove_container(container_id):
    """
    Handles removing the container.

    :param container_id: the short/long ID of the container that has to be removed.
    """
    if container_id is None:
        return {
            "message": "invalid container id"
        }

    success = handler.handle_remove_container(container_id)

    return {
        "message":
            "successfully removed {}".format(container_id) if success else "unable to remove container"
    }


@service_router.errorhandler(404)
def service_error_handler(error):
    """
    Handler for 404 errors.
    """
    return errors.error_response(404)


@service_router.errorhandler(500)
def internal_error_handler(error):
    """
    Handler for 500 errors.
    """
    return errors.error_response(500)
