import docker


class DockerServiceAdapter:

    def __init__(self):
        # Client is private, should not be called
        # Any consuming class
        self._client = docker.client.from_env()

    def get_info(self):
        """
        Gets the info of the user's Docker environment
        :return:
        """
        return self._client.info()

    def get_images(self):
        """
        Returns a list of images that are in the local environment
        :return:
        """
        return self._client.images.list()

    def get_containers(self):
        """
        Returns a list of relevant information on the containers that are
        currently running.
        :return:
        """
        container_listing = []
        containers = self._client.containers.list()
        for container in containers:
            container_info = {
                "id": container.id,
                "shortId": container.short_id,
                "tags": container.image.tags,
                "status": container.status
            }
            container_listing.append(container_info)
        return container_listing

    def stop_container(self, container_id):
        """
        Stops a container if it exists
        :return: stuff
        """
        if container_id is None:
            return {}  # or raise exception?
        # search for this container
        try:
            stopped_container = self._client.containers.get(container_id).stop()
        except Exception:
            return {}

        return {
            "message": 'Container {container_id} stopped successfullly.'.format(container_id=container_id)
        }

    def get_container(self, container_id):
        """
        Returns information on a specific container
        :param container_id: the id of the container that we wish to get
        :return:
        """
        container_info = {}

        try:
            container = self._client.containers.get(container_id)

            container_info = {
                "id": container.id,
                "shortId": container.short_id,
                "tags": container.image.tags,
                "status": container.status
            }

        except docker.errors.NotFound:
            return
        except docker.errors.APIError:
            return
        finally:
            return container_info

    def create_container(self, config):
        """
        Creates and returns the ID of a container
        :param config:
        """
        if config is None:
            raise Exception

        return {
            "status": "Created container",
            "containerId": "1234"
        }

    def start_container(self, container_id):
        if container_id is None:
            return {}
        container = self._client.containers.get(container_id)
        container.start()


class CreateContainerConfig:
    def __init__(self, image, hostname, user_id, volumes, ports):
        self.image = image
        self.hostname = hostname
        self.user_id = user_id
        self.volumes = volumes
        self.ports = ports
