# Copyright 2018 JanusGraph Python Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import docker
from janusgraph_python.driver.janusgraph_remote_connection_builder import JanusGraphRemoteConnectionBuilder
import time


class JanusGraphContainer(object):
    def __init__(self):
        self.BASE_IMAGE = "florianhockmann/janusgraph-testing:0.3.0"
        self.PORT = 8182

        self.client = docker.from_env()
        self.container = None

    def start(self):

        self.pull_image()

        self.container = self.client.containers.run(self.BASE_IMAGE, detach=True, hostname=JanusGraphContainer.get_host_ip(),
                                                    ports={8182: (JanusGraphContainer.get_host_ip(), self.PORT)})

        self.wait_for_container_to_start()

        return self.container

    @staticmethod
    def wait_for_container_to_start():
        while True:
            try:
                client = JanusGraphRemoteConnectionBuilder()

                client.connect(host=JanusGraphContainer.get_host_ip(), port=8182,
                                                traversal_source="gods_traversal").get_connection()

                client.close()
                break
            except ConnectionRefusedError:
                time.sleep(0.1)

    def pull_image(self):
        image = self.client.images.pull(self.BASE_IMAGE)
        return image

    @staticmethod
    def get_host_ip():
        return "localhost"

    def stop(self):
        try:
            self.container.stop()
            return True
        except Exception:
            return False


if __name__ == '__main__':
    container = JanusGraphContainer()
    container.start()
    print("Container started")
    container.stop()
    print("Container stopped")
    print("Tested container")
