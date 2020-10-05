"""
Handlers will handle things that are passed through the router.
"""
import datetime
from app.services import docker_service_adapter

_client = docker_service_adapter.DockerServiceAdapter()


def handle_healthcheck():
    """
    Verifies that the API is up.
    :return: dict
    """
    return {
        "status": "OK",
        "systemTime": datetime.datetime.now()
    }


def handle_docker_healthcheck():
    payload = dict()

    if _client is not None:
        status = _client.get_info()
        payload["status"] = "UP" if status is not None else "DOWN"
        try:
            payload["containerCount"] = status["containers"]
            # TODO: Add more logging items here as needed
        except Exception:
            pass

    payload["systemTime"] = datetime.datetime.now()

    return dict(payload)


def handle_get_running_containers():
    return {
        "containers": _client.get_containers(),
        "systemTime": datetime.datetime.now()
    }


def handle_get_running_container(container_id):
    if container_id is None:
        return dict()
    else:
        container = {}
        try:
            container = _client.get_container(container_id)
        except Exception:
            return container
        finally:
            return container


def handle_stop_container(container_id):
    if container_id is None:
        return {"message": "invalid container id"}
    return _client.stop_container(container_id)


def handle_start_container(container_id):
    return 'boop!'


def handle_create_container(image_tag):
    return True


def handle_remove_container(container_id):
    return True