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

from gremlin_python.structure.io.graphsonV3d0 import GraphSONWriter

from .relation_identifier_serializer import RelationIdentifierSerializer
from ....core.datatypes.relation_identifier import RelationIdentifier


class JanusGraphSONWriterBuilder(object):
    """Registers JanusGraph specific serializers so that Python objects like RelationIdentifier which
    can be interpreted on JanusGraph Server side.
    """

    serializers = dict()

    def __init__(self):
        self.writer = None

    def __register_default_serializers(self):
        """This method is used to register the Default serializers for JanusGraph's python client.
            Currently the serializer registers RelationIdentifier classes.

        Returns:
            None
        """

        janus_serializers = self.__build_serializers()
        self.serializers.update(janus_serializers)

    @staticmethod
    def __build_serializers():
        """The actual method which takes care of adding JanusGraph specific serializers.
        Returns:
            dict
        """
        # Currently the default serializers registered.

        janus_serializers = {
            RelationIdentifier: RelationIdentifierSerializer
        }

        return janus_serializers

    def build(self):
        """The method registers JanusGraph specific serializers into Gremlin GraphSON Writer class.

        Returns:
            GraphSONWriter
        """

        self.__register_default_serializers()
        self.writer = GraphSONWriter(self.serializers)
        return self.writer

    def register_serializer(self, type_, serializer):
        """This method is used to registering any additional JanusGraph serializers.

        Args:
            type_ (type):
            serializer:

        Returns:

        """

        self.serializers[type_] = serializer
        return self
