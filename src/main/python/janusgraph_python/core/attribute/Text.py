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

from gremlin_python.process.traversal import P


class Text(object):
    """ This class implements all the JanusGraph-based Text Predicates. """

    @staticmethod
    def textContains(value):
        """
        Implements JanusGraph's textContains functionality.
        Returns true if (at least) one word inside the text string matches the query string

        Args:
            value (str):

        Returns:
            bool: Returns true iff one word (at least) inside the text string matches the query string.
        """

        return P("textContains", value)

    @staticmethod
    def textContainsPrefix(value):
        """
        Implements JanusGraph's textContainsFuzzy functionality.
        Returns true if (at least) one word inside the text string begins with the query string

        Args:
            value (str):

        Returns:
            bool: Returns true iff one word (at least) inside the text string begins with the query string.
        """
        return P("textContainsPrefix", value)

    @staticmethod
    def textPrefix(value):
        """
        Implements JanusGraph's textPrefix functionality.
        Returns true if the string value starts with the given query string

        Args:
            value (str):

        Returns:
            bool: Returns true iff the string value starts with the given query string.
        """
        return P("textPrefix", value)

    @staticmethod
    def textContainsRegex(value):
        """
        Implements JanusGraph's textContainsPrefix functionality.
        Returns true if (at least) one word inside the text string matches the given regular expression

        Args:
            value (str):

        Returns:
            bool: Returns true iff one word (at least) inside the text string matches the given regular expression.
        """

        return P("textContainsRegex", value)

    @staticmethod
    def textRegex(value):
        """
        Implements JanusGraph's textRegex functionality.
        Returns if the string value matches the given regular expression in its entirety

        Args:
            value (str):

        Returns:
            bool: Returns true iff the string value matches the given regular expression in its entirety.
        """

        return P("textRegex", value)

    @staticmethod
    def textFuzzy(value):
        """
        Implements JanusGraph's textFuzzy functionality.
        Returns if the string value is similar to the given query string (based on Levenshtein edit distance)

        Args:
            value (str):

        Returns:
            bool: Returns true iff the string value is similar to the given query string.
        """

        return P("textFuzzy", value)

    @staticmethod
    def textContainsFuzzy(value):
        """
        Implements JanusGraph's textContainsFuzzy functionality.
        Returns true if (at least) one word inside the text string is similar to the query String
        (based on Levenshtein edit distance)

        Args:
            value (str):

        Returns:
            bool: Returns true iff one word inside the text string is similar to the query String.
        """

        return P("textContainsFuzzy", value)
