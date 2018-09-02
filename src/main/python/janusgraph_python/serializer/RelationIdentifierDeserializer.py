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


from ..core.datatypes.RelationIdentifier import RelationIdentifier


class RelationIdentifierDeserializer(object):
    """
    This is de-serializer method to be used to de-serialize RelationIdentifier objects which is used by JanusGraph
    for encoding Edge IDs
    """

    @classmethod
    def objectify(cls, graphsonObj, reader):
        """
            The De-serializer method to de-serialize a RelationIdentifier into corresponding Python object.

        Args:
            graphsonObj (dict): The serialized JSON returned from JanusGraph's gremlin-server.
            reader: The reader class to use for de-serializing the GeoShape object.

        Returns:
            RelationIdentifier
        """

        relationID = str(graphsonObj["relationId"])

        relationID = RelationIdentifier(relationID)

        return relationID.toString()
