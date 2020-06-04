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

from ..structure.io.graphson.graphson_writer_builder import JanusGraphSONWriterBuilder
from ..structure.io.graphson.graphson_reader_builder import JanusGraphSONReaderBuilder

from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection


class JanusGraphRemoteConnectionBuilder(object):
    """ JanusGraph Remote Client Builder which adds the Serializers for JanusGraph specific objects, predicates etc. """

    REMOTE_CONNECTION = None

    def __init__(self, graphson_version=3.0):
        """ Initializing with GraphSON version which defaults to 3.0 if nothing is specified.

        Args:
            graphson_version (float):
        """

        self.graphson_version = graphson_version
        self.graphson_reader = None
        self.graphson_writer = None
        self.traversal_source = None
        self.URL = None

    def connect(self, host="localhost", port=8182, traversal_source="g"):
        """ Connect to JanusGraph Server instance. Takes Host, Port and Traversal source

        Args:
            host (str): The HOST of JanusGraph Server instance. Defaults to localhost
            port (int): The PORT of JanusGraph Server instance. Defaults to 8182.
            traversal_source (str): The GraphTraversalSource being exposed from JanusGraph Server instance. Defaults to g

        Raises:
            AttributeError: When invalid Keyword arguments is provided. The expected key needs to be
            `graphson_reader` and `graphson_writer`.

        Returns:
            JanusGraphRemoteConnectionBuilder
        """

        self.URL = "ws://{}:{}/gremlin".format(host, port)
        self.traversal_source = traversal_source

        self.__set_defaults__()

        return self

    def __build_connection__(self):
        self.REMOTE_CONNECTION = DriverRemoteConnection(self.URL, self.traversal_source,
                                                        graphson_reader=self.graphson_reader,
                                                        graphson_writer=self.graphson_writer)
        return self

    def __set_defaults__(self):
        self.graphson_reader = JanusGraphSONReaderBuilder().build()
        self.graphson_writer = JanusGraphSONWriterBuilder().build()
        return self

    def with_serializer(self, reader):
        """

        Args:
            reader (JanusGraphSONReaderBuilder):

        Returns:

        """

        self.graphson_reader = reader
        return self

    def with_deserializer(self, writer):
        """

        Args:
            writer (JanusGraphSONWriterBuilder):

        Returns:

        """

        self.graphson_writer = writer
        return self

    def get_connection(self):
        """ Get the RemoteConnection object, so that same can be used to create GraphTraversalSource.

        Returns:
            DriverRemoteConnection
        """
        self.__build_connection__()
        return self.REMOTE_CONNECTION

    def close(self):
        self.REMOTE_CONNECTION.close()
