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

from ..structure.io.GraphsonReader import JanusGraphSONReader
from ..structure.io.GraphsonWriter import JanusGraphSONWriter

from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection


class JanusGraphClient(object):
    """ JanusGraph Client Builder which adds the Serializers for JanusGraph specific objects, predicates etc. """

    REMOTE_CONNECTION = None

    def __init__(self, version=3.0):
        """ Initializing with GraphSON version 3.0

        Args:
            version (int):
        """

        self.graphsonVersion = version

    def connect(self, host="localhost", port="8182", traversal_source="g", **kwargs):
        """ Connect to JanusGraph's gremlin-server instance. Takes Host, Port and Graph

        Args:
            host (str): The HOST of JanusGraph gremlin-server instance. Defaults to localhost
            port (str): The PORT of JanusGraph gremlin-server instance. Defaults to 8182.
            graph (str): The GraphTraversalSource being exposed from gremlin-server instance. Defaults to g

        Keyword Args:
            graphson_reader (GraphSONReader): GraphSONReader object with required Deserializers registered
            graphson_writer (GraphSONWriter): GraphSONWriter object with required Serializers registered

        Raises:
            AttributeError: When invalid Keyword arguments is provided. The expected key needs to be
            `graphson_reader` and `graphson_writer`.

        Returns:
            JanusGraphClient
        """

        URL = "ws://{}:{}/gremlin".format(host, port)

        if not kwargs:

            graphson_reader = JanusGraphSONReader().build()
            graphson_writer = JanusGraphSONWriter().build()

        else:
            if "graphson_reader" in kwargs and "graphson_writer" in kwargs:
                graphson_reader = kwargs["graphson_reader"]
                graphson_writer = kwargs["graphson_writer"]
            else:
                raise AttributeError("Additional parameters if provided needs to be keywords arguments of "
                                     "`graphson_reader` and `graphson_writer`")

        self.REMOTE_CONNECTION = DriverRemoteConnection(URL, traversal_source, graphson_reader=graphson_reader,
                                                        graphson_writer=graphson_writer)

        return self

    def get_connection(self):
        """ Get the RemoteConnection object, so that same can be used to create GraphTraversalSource.

        Returns:
            DriverRemoteConnection
        """

        return self.REMOTE_CONNECTION

    def close(self):
        try:
            self.REMOTE_CONNECTION.close()
            return True
        except:
            return False
