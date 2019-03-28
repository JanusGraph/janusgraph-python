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

from gremlin_python.structure.io.graphsonV3d0 import GraphSONUtil


class RelationIdentifierSerializer(object):
    """
    This is serializer method being used to serialize RelationIdentifier object which is used by JanusGraph for edge ID
    """

    GRAPHSON_PREFIX = "janusgraph"
    GRAPHSON_BASE_TYPE = "RelationIdentifier"

    @classmethod
    def dictify(cls, relationID, writer):
        """ Serializes RelationIdentifier object.

        Args:
            relationID (RelationIdentifier): The RelationID to serialize.
            writer:

        Returns:
            json
        """

        relationJSON = cls.__relationID_to_dict(relationID)

        serializedJSON = GraphSONUtil.typedValue(cls.GRAPHSON_BASE_TYPE, relationJSON, cls.GRAPHSON_PREFIX)

        return serializedJSON

    @classmethod
    def __relationID_to_dict(cls, relationID):

        relationIdDict = dict()

        relationIdDict["relationId"] = relationID.toString()

        return relationIdDict
