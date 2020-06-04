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
from ....core.datatypes.relation_identifier import RelationIdentifier


class RelationIdentifierSerializer(object):
    """This is serializer class being used to serialize RelationIdentifier object which is used by JanusGraph for edge ID
    """

    GRAPHSON_PREFIX = "janusgraph"
    GRAPHSON_BASE_TYPE = "RelationIdentifier"

    @classmethod
    def dictify(cls, relation_id, writer):
        """Serializes RelationIdentifier object.

        Args:
            relation_id (RelationIdentifier): The RelationID to serialize.
            writer:

        Returns:
            dict
        """

        relation_json = cls.__relation_id_to_dict(relation_id)
        serialized_json = GraphSONUtil.typedValue(cls.GRAPHSON_BASE_TYPE, relation_json, cls.GRAPHSON_PREFIX)
        return serialized_json

    @classmethod
    def __relation_id_to_dict(cls, relation_id):
        """

        Args:
            relation_id (RelationIdentifier):

        Returns:
            dict
        """

        relation_dict = dict()
        relation_dict["relationId"] = relation_id.relationID
        return relation_dict
