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
    from gremlin_python.structure.io.graphsonV3d0 import GraphSONUtil
except ImportError:
    from gremlin_python.structure.io.graphson import GraphSONUtil

from ..core.datatypes.RelationIdentifier import RelationIdentifier


class RelationIdentifierSerializer(object):
    """
    This is serializer method being used to serialize RelationIdentifier object which is used by JanusGraph for edge ID
    """

    GRAPHSON_PREFIX = "janusgraph"
    GRAPHSON_BASE_TYPE = "RelationIdentifier"

    @classmethod
    def dictify(cls, relationID, writer):
        """
            This method is used for Serializing RelationIdentifier object.

        Args:
            relationID (RelationIdentifier): The RelationID to serialize.
            writer:

        Returns:
            json
        """

        relationJSON = cls.__relationID_to_json(relationID)

        serializedJSON = GraphSONUtil.typedValue(cls.GRAPHSON_BASE_TYPE, relationJSON, cls.GRAPHSON_PREFIX)

        return serializedJSON

    @classmethod
    def __relationID_to_json(cls, relationID):
        """
            JSONify the string representation of RelationID

        Args:
            relationID (RelationIdentifier): The RelationID object which needs to be dictified.

        Returns:
            dict
        """

        relationIdDict = dict()

        relationIdDict["relationId"] = relationID.toString()

        return relationIdDict
