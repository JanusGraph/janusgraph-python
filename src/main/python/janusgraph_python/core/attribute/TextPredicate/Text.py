# Name: Debasish Kanhar

from gremlin_python.process.traversal import P


class Text(object):
    """
    Class implementing Gremlin Python's Predicate class, and extending it for JanusGraph based Text Predicates.
    """

    def __init__(self):
        pass

    @staticmethod
    def textContains(value):
        """
        Implements JanusGraph's textContains functionality

        Args:
            value (str):

        Returns:
            P
        """

        predicate = P("textContains", value)
        return predicate

    @staticmethod
    def textContainsPrefix(value):
        """
        Implements JanusGraph's textContainsFuzzy functionality.

        Args:
            value (str):

        Returns:
            P
        """
        predicate = P("textContainsPrefix", value)

        return predicate

    @staticmethod
    def textPrefix(value):
        """
        Implements JanusGraph's textPrefix functionality.

        Args:
            value (str):

        Returns:
            P
        """
        predicate = P("textPrefix", value)

        return predicate

    @staticmethod
    def textContainsRegex(value):
        """
        Implements JanusGraph's textContainsPrefix functionality.

        Args:
            value (str):

        Returns:
            P
        """

        predicate = P("textContainsRegex", value)

        return predicate

    @staticmethod
    def textRegex(value):
        """
        Implements JanusGraph's textRegex functionality.

        Args:
            value (str):

        Returns:
            P
        """

        predicate = P("textRegex", value)

        return predicate

    @staticmethod
    def textFuzzy(value):
        """
        Implements JanusGraph's textFuzzy functionality.

        Args:
            value (str):

        Returns:
            P
        """

        predicate = P("textFuzzy", value)

        return predicate

    @staticmethod
    def textContainsFuzzy(value):
        """
        Implements JanusGraph's textContainsFuzzy functionality.

        Args:
            value (str):

        Returns:
            P
        """

        predicate = P("textContainsFuzzy", value)

        return predicate
