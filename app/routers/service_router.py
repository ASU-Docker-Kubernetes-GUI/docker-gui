from flask import Blueprint, request, jsonify

"""
service_router.py renders all of the backend routes that we are exposing in our
application. 

All of these routes will be prefixed with `/api/v1/`, followed by the route
These routes are as follows:

/status - renders the status of Docker
/create (create a container)
/get (get all containers)
/get/{id} (get a specific container)
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
    return jsonify("Service is alive")


@service_router.route('/status')
def docker_healthcheck():
    return jsonify("Docker is up")


@service_router.route('/create', methods=["POST"])
def service_create_docker_container():
    if request.method == "POST":
        return "Docker container created!"
    else:
        return "this is an error"


@service_router.route('/containers', methods=["GET"])
def service_get_running_containers():
    return jsonify(["container1", "container2", "container3"])


@service_router.route('/container/<container>', methods=["GET"])
def service_get_running_container(container):
    return jsonify(container)

