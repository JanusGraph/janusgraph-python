import docker
from janusgraph_python.driver.ClientBuilder import JanusGraphClient
from subprocess import Popen, PIPE
import time


class JanusGraphContainer(object):
    def __init__(self):
        self.BASE_IMAGE = "florianhockmann/janusgraph-testing:0.3.0"
        self.PORT = 8182

        self.client = docker.from_env()
        self.container = None

    def start(self):

        self.pull_image()

        self.container = self.client.containers.run(self.BASE_IMAGE, detach=True, hostname="localhost",
                                                    ports={8182: ("localhost", self.PORT)})

        self.wait_for_container_to_start()

        return self.container

    @staticmethod
    def wait_for_container_to_start():
        while True:
            try:
                docker_ip = Popen(["docker-machine", "ip"], stdout=PIPE).communicate()[0]
                docker_ip = docker_ip.strip().decode("utf-8")

                client = JanusGraphClient()

                client.connect(host=str(docker_ip), port="8182",
                                                traversal_source="gods_traversal").get_connection()

                client.close()
                break
            except ConnectionRefusedError:
                time.sleep(0.1)

    def pull_image(self):
        image = self.client.images.pull(self.BASE_IMAGE)
        return image

    def stop(self):
        try:
            self.container.stop()
            return True
        except:
            return False


if __name__ == '__main__':
    container = JanusGraphContainer()
    container.start()
    print("Container started")
    container.stop()
    print("Container stopped")
    print("Tested container")
