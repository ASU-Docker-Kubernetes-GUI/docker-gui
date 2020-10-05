from flask import Blueprint, request, jsonify
from app.handlers import service_handler as handler

"""
service_router.py renders all of the backend routes that we are exposing in our
application. 

All of these routes will be prefixed with `/api/v1/`, followed by the route
These routes are as follows:

/create (create a container)
/update/{id} (update a specific container)
/run/{id} (run a specific container)
/logs/{id} (get the logs for a specific container)
/stop/{id} (stop a container)
/delete/{id} (delete a specific container)
/pull (pull a container) POST request
/settings (get the settings)
/settings (post a new setting)
"""

service_router = Blueprint(
    'service_router',
    __name__,
    url_prefix="/api/v1"
)


@service_router.route('/')
@service_router.route('/ping')
def service_healthcheck():
    return jsonify(handler.handle_healthcheck())


@service_router.route('/docker-status')
def docker_healthcheck():
    return jsonify(handler.handle_docker_healthcheck())


@service_router.route('/create', methods=["POST"])
def service_create_docker_container():
    if request.method == "POST":
        return "Docker container created!"
    else:
        return "this is an error"


@service_router.route('/containers', methods=["GET"])
def service_get_running_containers():
    return handler.handle_get_running_containers()


@service_router.route('/container/<container_id>', methods=["GET"])
def service_get_running_container(container_id):
    return jsonify(handler.handle_get_running_container(container_id))


@service_router.route('/stop/<container_id>', methods=["GET"])
def service_stop_container(container_id):
    return jsonify(handler.handle_stop_container(container_id))


@service_router.route('/start/<container_id>', method=["GET"])
def service_start_container(container_id):
    return jsonify(handler.handle_start_container(container_id))