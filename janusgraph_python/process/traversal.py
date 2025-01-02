
# Copyright 2024 JanusGraph-Python Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from numbers import Number
from gremlin_python.process.traversal import P
from janusgraph_python.structure.io.util import LongEncoding

# Marked as 'private' class as it should not be used directly.
# If one uses _JanusGraphP.eq(), this will result invalid operator error.
class _JanusGraphP(P):    
    def __init__(self, operator, value, other=None):
        self.operator = operator
        self.value = value
        self.other = other
    
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.operator == other.operator and self.value == other.value and self.other == other.other

    def __repr__(self):
        return self.operator + "(" + str(self.value) + ")" if self.other is None else self.operator + "(" + str(self.value) + "," + str(self.other) + ")"

class Text(object):
    """
    Provides text search predicates.
    """

    @staticmethod
    def text_contains(*args):
        """
        Is true if (at least) one word inside the text string matches the query string.

        :param query: string, The query to search.
        :return The text predicate.
        """
        return _JanusGraphP("textContains", *args)
    
    @staticmethod
    def text_not_contains(*args):
        """
        Is true if no words inside the text string match the query string.

        :param query: string, The query to search.
        :return The text predicate.
        """
        return _JanusGraphP("textNotContains", *args)

    @staticmethod
    def text_contains_prefix(*args):
        """
        Is true if (at least) one word inside the text string begins with the query string.

        :param query: string, The query to search.
        :return The text predicate.
        """
        return _JanusGraphP("textContainsPrefix", *args)
    
    @staticmethod
    def text_not_contains_prefix(*args):
        """
        Is true if no words inside the text string begin with the query string.

        :param query: string, The query to search.
        :return The text predicate.
        """
        return _JanusGraphP("textNotContainsPrefix", *args)

    @staticmethod
    def text_contains_regex(*args):
        """
        Is true if (at least) one word inside the text string matches the given regular expression.

        :param query: string, The query to search.
        :return The text predicate.
        """
        return _JanusGraphP("textContainsRegex", *args)
    
    @staticmethod
    def text_not_contains_regex(*args):
        """
        Is true if no words inside the text string match the given regular expression.

        :param query: string, The query to search.
        :return The text predicate.
        """
        return _JanusGraphP("textNotContainsRegex", *args)

    @staticmethod
    def text_contains_fuzzy(*args):
        """
        Is true if (at least) one word inside the text string is similar to the query String (based on
        Levenshtein edit distance).

        :param query: string, The query to search.
        :return The text predicate.
        """
        return _JanusGraphP("textContainsFuzzy", *args)
    
    @staticmethod
    def text_not_contains_fuzzy(*args):
        """
        Is true if no words inside the text string are similar to the query string
        (based on Levenshtein edit distance).

        :param query: string, The query to search.
        :return The text predicate.
        """
        return _JanusGraphP("textNotContainsFuzzy", *args)

    @staticmethod
    def text_contains_phrase(*args):
        """
        Is true if the text string does contain the sequence of words in the query string.

        :param query: string, The query to search.
        :return The text predicate.
        """
        return _JanusGraphP("textContainsPhrase", *args)

    @staticmethod
    def text_not_contains_phrase(*args):
        """
        Is true if the text string does not contain the sequence of words in the query string.

        :param query: string, The query to search.
        :return The text predicate.
        """
        return _JanusGraphP("textNotContainsPhrase", *args)

    @staticmethod
    def text_prefix(*args):
        """
        Is true if the string value starts with the given query string.

        :param query: string, The query to search.
        :return The text predicate.
        """
        return _JanusGraphP("textPrefix", *args)
    
    @staticmethod
    def text_not_prefix(*args):
        """
        Is true if the string value does not start with the given query string.

        :param query: string, The query to search.
        :return The text predicate.
        """
        return _JanusGraphP("textNotPrefix", *args)

    @staticmethod
    def text_regex(*args):
        """
        Is true if the string value matches the given regular expression in its entirety.

        :param query: string, The query to search.
        :return The text predicate.
        """
        return _JanusGraphP("textRegex", *args)

    @staticmethod
    def text_not_regex(*args):
        """
        Is true if the string value does not match the given regular expression in its entirety.

        :param query: string, The query to search.
        :return The text predicate.
        """
        return _JanusGraphP("textNotRegex", *args)

    @staticmethod
    def text_fuzzy(*args):
        """
        Is true if the string value is similar to the given query string (based on Levenshtein edit distance).

        :param query: string, The query to search.
        :return The text predicate.
        """
        return _JanusGraphP("textFuzzy", *args)

    @staticmethod
    def text_not_fuzzy(*args):
        """
        Is true if the string value is not similar to the given query string (based on Levenshtein edit distance).

        :param query: string, The query to search.
        :return The text predicate.
        """
        return _JanusGraphP("textNotFuzzy", *args)

class RelationIdentifier(object):
    _TO_STRING_DELIMITER = '-'

    out_vertex_id = None
    type_id = 0
    relation_id = 0
    in_vertex_id = None
    string_representation = None

    def __init__(self, out_vertex_id, type_id, relation_id, in_vertex_id, string_representation):
        """
        Initializes a new instance of the RelationIdentifier class

        :param out_vertex_id: object, The id of the outgoing vertex.
        :param type_id: long, The JanusGraph internal type id.
        :param relation_id: long, The JanusGraph internal relation id.
        :param in_vertex_id: object, The id of the incoming vertex.
        :param string_representation: string, The underlying relation id.
        """
        self.out_vertex_id = out_vertex_id
        self.type_id = type_id
        self.relation_id = relation_id
        self.in_vertex_id = in_vertex_id
        self.string_representation = string_representation

    @classmethod
    def from_string(cls, string_representation):
        """
        Initializes a new instance of the RelationIdentifier class.

        :param string_representation: string, The underlying relation id.
        """
        in_vertex_id = None

        elements = string_representation.split(cls._TO_STRING_DELIMITER)
        
        if len(elements) != 3 and len(elements) != 4:
            raise ValueError(f"Not a valid relation identifier: {string_representation}")
        
        if elements[1][0] == LongEncoding.STRING_ENCODING_MARKER:
            out_vertex_id = elements[1][1:]
        else:
            out_vertex_id = LongEncoding.decode(elements[1])
        
        type_id = LongEncoding.decode(elements[2])
        relation_id = LongEncoding.decode(elements[0])

        if len(elements) == 4:
            if elements[3][0] == LongEncoding.STRING_ENCODING_MARKER:
                in_vertex_id = elements[3][1:]
            else:
                in_vertex_id = LongEncoding.decode(elements[3])

        return cls(out_vertex_id, type_id, relation_id, in_vertex_id, string_representation)

    @classmethod
    def from_ids(cls, out_vertex_id, type_id, relation_id, in_vertex_id):
        """
        Initializes a new instance of the RelationIdentifier class.

        :param out_vertex_id: object, The id of the outgoing vertex.
        :param type_id: long, The JanusGraph internal type id.
        :param relation_id: long, The JanusGraph internal relation id.
        :param in_vertex_id: object, The id of the incoming vertex.
        """

        parts = []

        parts.append(LongEncoding.encode(relation_id))
        parts.append(cls._TO_STRING_DELIMITER)

        if isinstance(out_vertex_id, Number):
            parts.append(LongEncoding.encode(out_vertex_id))
        else:
            parts.append(LongEncoding.STRING_ENCODING_MARKER)
            parts.append(out_vertex_id)

        parts.append(cls._TO_STRING_DELIMITER)
        parts.append(LongEncoding.encode(type_id))

        if in_vertex_id:
            parts.append(cls._TO_STRING_DELIMITER)

            if isinstance(in_vertex_id, Number):
                parts.append(LongEncoding.encode(in_vertex_id))
            else:
                parts.append(LongEncoding.STRING_ENCODING_MARKER)
                parts.append(in_vertex_id)
        
        string_representation = ''.join(parts)

        return cls(out_vertex_id, type_id, relation_id, in_vertex_id, string_representation)

    def __eq__(self, other):
        if other is None:
            return False
        
        if other is self:
            return True
        
        return self.string_representation == other.string_representation

    def __repr__(self):
        return self.string_representation
    
    def __hash__(self):
        return hash(self.string_representation)
    