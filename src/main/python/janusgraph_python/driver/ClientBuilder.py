"""
Copyright 2018 Debasish Kanhar

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

__author__ = "Debasish Kanhar (https://github.com/debasishdebs)"
__credits__ = ["Florian Hockman", "Jason Plurad", "Dave Brown", "Marko Rodriguez"]
__license__ = "Apache-2.0"
__version__ = "0.0.1"
__email__ = ["d.kanhar@gmail.com", "dekanhar@in.ibm.com"]


from ..structure.io.GraphsonReader import JanusGraphSONReader
from ..structure.io.GraphsonWriter import JanusGraphSONWriter

from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection


class JanusGraphClient(object):
    """
        JanusGraph Client Builder which adds the Serializers for JanusGraph specific objects, predicates etc.
    """

    REMOTE_CONNECTION = None

    def __init__(self, version=3.0):
        """
            Initializing with GraphSON version 3.0
        Args:
            version (int):
        """

        self.graphsonVersion = version
        pass

    def connect(self, url="loclahost", port="8182", graph="g"):
        """
            Connect to JanusGraph's gremlin-server instance. Takes URL, Port and Graph

        Args:
            url (str): The URL of JanusGraph gremlin-server instance. Default to localhost
            port (str): The PORT of JanusGraph gremlin-server instance. Default to 8182.
            graph (str): The GraphTraversalSource being exposed from gremlin-server instance. Defaults to g

        Returns:
            JanusGraphClient
        """

        URL = "ws://{}:{}/gremlin".format(url, port)

        graphson_reader = JanusGraphSONReader().build()
        graphson_writer = JanusGraphSONWriter().build()

        self.REMOTE_CONNECTION = DriverRemoteConnection(URL, graph, graphson_reader=graphson_reader,
                                                        graphson_writer=graphson_writer)

        return self

    def get_connection(self):
        """
            Get the RemoteConnection object, so that same can be used to create GraphTraversalSource.
        Returns:
            DriverRemoteConnection
        """

        return self.REMOTE_CONNECTION
