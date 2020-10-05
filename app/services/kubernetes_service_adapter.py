from kubernetes import client, config


class KubernetesServiceAdapter:
    def __init__(self):
        config.load_kube_config()
        self._client = client.CoreV1Api()
        self._apps = client.AppsV1Api()

    def create_deployment(self):
        pass

    def update_deployment(self):
        pass

    def delete_deployment(self):
        pass
