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


class RelationIdentifier(object):
    def __init__(self, relationID):
        """ This class represents the RelationIdentifier object type which represents Edge IDs in JanusGraph.

        Args:
            relationID (str): The string representation, "-" separated of Edge IDs.
        """
        self.relationID = relationID

    def __eq__(self, other):
        """ Overrides default equality method.

        Args:
            other (RelationIdentifier):

        Returns:

        """

        if isinstance(other, RelationIdentifier):
            return self.relationID == other.relationID

        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self.relationID

    def __hash__(self):
        return hash(self.relationID) if self.relationID is not None else 0

    def toDict(self):
        """ Dictify the relationID, with proper JanusGraph Identifier token.

        Returns:

        """
        edgeID = dict()
        edgeID["janusgraph:RelationIdentifier"] = self.toString()
        return edgeID

    def toString(self):
        """ Returns string representation of RelationIdentifier.

        Returns:
            str
        """
        return str(self.relationID)

    def getID(self):
        """ Get the underlaying ID of class.

        Returns:
            str
        """
        return self.toString()
