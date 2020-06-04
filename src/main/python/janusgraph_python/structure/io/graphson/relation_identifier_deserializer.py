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

from ....core.datatypes.relation_identifier import RelationIdentifier


class RelationIdentifierDeserializer(object):
    """This is deserializer class to be used to de-serialize RelationIdentifier objects which is used by JanusGraph
    for encoding Edge IDs
    """

    @classmethod
    def objectify(cls, graphson_obj, reader):
        """This method to de-serialize a RelationIdentifier into corresponding Python object.

        Args:
            graphson_obj (dict): The serialized JSON returned from JanusGraph Server.
            reader: The reader class to use for de-serializing the JanusGraph Relation object.

        Returns:
            RelationIdentifier
        """

        relation_id = RelationIdentifier(str(graphson_obj["relationId"]))
        return relation_id
