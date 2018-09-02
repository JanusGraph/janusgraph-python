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

try:
    from gremlin_python.structure.io.graphsonV3d0 import GraphSONWriter
except ImportError:
    from gremlin_python.structure.io.graphson import GraphSONWriter

from ...serializer.PointSerializer import PointSerializer
from ...serializer.CircleSerializer import CircleSerializer
from ...serializer.RelationIdentifierSerializer import RelationIdentifierSerializer
from ...core.datatypes.GeoShape import Point, Circle
from ...core.datatypes.RelationIdentifier import RelationIdentifier


class JanusGraphSONWriter(object):
    """
    This class registers JanusGraph specific serializers so that Python objects like GeoShape, RelationIdentifier
    can be interpreted on Gremlin server side.
    """

    serializers = dict()

    def __init__(self):
        self.writer = None
        pass

    def __register_default_serializers(self):
        """
            This method is used to register the Default serializers for JanusGraph's python client.
            Currently the serializer registers GeoShape and RelationIdentifier classes.

        Returns:

        """

        janusSerializers = self.__build_serializers()

        self.serializers.update(janusSerializers)

    def __build_serializers(self):
        """
            The actual method which takes care of adding JanusGraph specific serializers.
        Returns:
            dict
        """
        # Currently the default serializers registered.

        janusSerializers = {
            Circle: CircleSerializer,
            Point: PointSerializer,
            RelationIdentifier: RelationIdentifierSerializer
        }

        return janusSerializers

    def build(self):
        """
            The method registers JanusGraph specific serializers into Gremlin GraphSON Writer class.

        Returns:
            GraphSONWriter
        """
        self.__register_default_serializers()
        self.writer = GraphSONWriter(self.serializers)
        return self.writer

    def register_serializer(self, typeClass, serializer):
        """
            This method is used to registering any additional JanusGraph serializers.
        Args:
            typeClass (type):
            serializer:

        Returns:

        """

        self.serializers[typeClass] = serializer
