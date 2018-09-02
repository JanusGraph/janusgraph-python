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
    from gremlin_python.structure.io.graphsonV3d0 import GraphSONReader
    from gremlin_python.structure.io.graphsonV3d0 import GraphSONUtil
except ImportError:
    from gremlin_python.structure.io.graphson import GraphSONReader
    from gremlin_python.structure.io.graphson import GraphSONUtil

from ...serializer.RelationIdentifierDeserializer import RelationIdentifierDeserializer
from ...serializer.GeoShapeDeserializer import GeoShapeDeserializer


class JanusGraphSONReader(object):
    """
    This class registers JanusGraph specific de-serializers so that objects like GeoShape, RelationIdentifier
    can be interpreted on Python client side.
    """

    GRAPHSON_PREFIX = "janusgraph"
    GEO_GRAPHSON_BASE_TYPE = "Geoshape"
    RELATIONID_BASE_TYPE = "RelationIdentifier"
    GeoShape_GRAPHSON_TYPE = GraphSONUtil.formatType(GRAPHSON_PREFIX, GEO_GRAPHSON_BASE_TYPE)
    RelationID_GRAPHSON_TYPE = GraphSONUtil.formatType(GRAPHSON_PREFIX, RELATIONID_BASE_TYPE)

    deserializers = dict()

    def __init__(self):
        self.reader = None
        pass

    def __register_default_deserializers(self):
        """
            This method is used to register the Default de-serializers for JanusGraph's python client.
            Currently the deserializer registers GeoShape and RelationIdentifier classes.

        Returns:

        """
        janusDeSerializers = self.__build_deserializers()

        self.deserializers.update(janusDeSerializers)

    def __build_deserializers(self):
        """
            The actual method which takes care of adding JanusGraph specific de-serializers.
        Returns:
            dict
        """
        # Currently the default de-serializers registered.

        janusDeSerializers = {
            self.GeoShape_GRAPHSON_TYPE: GeoShapeDeserializer,
            self.RelationID_GRAPHSON_TYPE: RelationIdentifierDeserializer
        }

        return janusDeSerializers

    def build(self):
        """
            The method registers JanusGraph specific de-serializers into Gremlin GraphSON Reader class.

        Returns:
            GraphSONReader
        """
        self.__register_default_deserializers()
        self.reader = GraphSONReader(self.deserializers)
        return self.reader

    def register_deserializer(self, typeClass, serializer):
        """
            This method is used to registering any additional JanusGraph de-serializers.

        Args:
            typeClass (type): The identifier to be used with underlaying graph to register the De-serializer against.
            serializer: The De-serializer class.

        Returns:

        """

        self.deserializers[typeClass] = serializer
