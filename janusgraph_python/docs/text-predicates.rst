==========================
JanusGraph Text Predicates
==========================

JanusGraph provides APIs to query the data using Text Predicates. The types of Text Predicates available
for querying depends on the Indexing backend used.
Hence, be careful with using the Text Predicates, and refer to original JanusGraph docs_.

.. _docs: https://docs.janusgraph.org/latest/


----------------------------
Available Text Predicates
----------------------------

The Text Predicates are broadly divided into 2 categories as:
    - Text search predicates which match against the individual words inside a text string after it has been tokenized.
        These predicates are not case sensitive.

        - TextContains_
        - TextContainsFuzzy_
        - TextContainsPrefix_
        - TextContainsRegex_

    - String search predicates which match against the entire string value

        - TextFuzzy_
        - TextPrefix_
        - TextRegex_

.. note::
    All the bellow examples are based on Graph of the Gods graph which comes pre-packaged with JanusGraph

^^^^^^^^^^^^^^^
TextContains
^^^^^^^^^^^^^^^

This Predicate is part of *Text* package.
TextContains is used to query for partial matches in values of properties.
The query is to find all edges where ``reason`` contains ``breezes``


.. code-block:: python

    from janusgraph_python.core.attribute.Text import Text

    # Find all edges which contains the word breezes
    edges = g.E().has("reason", Text.textContains("breezes")).next()
    print(edges)

    ==> e[55m-6hc-b2t-3bk][8400-lives->4304]

    # Find all edges which contains the word breezes and loves
    edges = g.E().has("reason", Text.textContains("breezes")).has("reason", Text.textContains("loves")).valueMap(True).next()
    print(edges)

    ==> {<T.id: 1>: '2dj-37c-9hx-360', 'reason': 'loves fresh breezes', <T.label: 3>: 'lives'}


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TextContainsFuzzy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This Predicate is part of *Text* package.
TextContainsFuzzy is used to query for partial matches with Fuzzy logic in values of properties.
We know there is a vertex with *hercules* value on property `name`. We query all vertices with value as *hercauleas*
Similarly, we use in Conjugation with multiple other attributes to query edge as in above example.


.. code-block:: python

    from janusgraph_python.core.attribute.Text import Text

    hercules = g.V().has("name", Text.textContainsFuzzy("hercauleas")).valueMap(True).next()
    print(hercules)

    ==> {'name': ['hercules'], <T.id: 1>: 4312, <T.label: 3>: 'demigod', 'age': [30]}

    edges = g.E().has("reason", Text.textContainsFuzzy("breezs")).has("reason", Text.textContains("loves")).valueMap(True).next()
    print(edges)

    ==> {<T.id: 1>: '2dj-37c-9hx-360', 'reason': 'loves fresh breezes', <T.label: 3>: 'lives'}

    edges = g.E().has("reason", Text.textContainsFuzzy("breezs")).has("reason", Text.textContainsFuzzy("luves")).valueMap(True).next()
    print(edges)

    ==> {<T.id: 1>: '2dj-37c-9hx-360', 'reason': 'loves fresh breezes', <T.label: 3>: 'lives'}



^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TextContainsPrefix
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This Predicate is part of *Text* package.
TextContainsPrefix is used to query for where the value
(if sentence, it is segmented, & any word in segment is considered)
contains the string queries in prefix
The difference between TextContains and TextContainsPrefix and TextPrefix can be seen in example bellow.


.. code-block:: python

    from janusgraph_python.core.attribute.Text import Text

    edges = g.E().has("reason", Text.textContainsFuzzy("breezs")).has("reason", Text.textContains("loves")).\
                valueMap().toList()
    print(edges)

    ==> [{'reason': 'loves fresh breezes'}]

    edges = g.E().has("reason", Text.textContainsPrefix("loves")).valueMap().toList()
    print(edges)

    ==> [{'reason': 'loves fresh breezes'}, {'reason': 'loves waves'}]

    edges = g.E().has("reason", Text.textContainsPrefix("breeze")).valueMap().toList()
    print(edges)

    ==> [{'reason': 'loves fresh breezes'}]

    edges = g.E().has("reason", Text.textPrefix("breeze")).valueMap().toList()
    print(edges)

    ==> []


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TextContainsRegex
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This Predicate is part of *Text* package.
TextContainsRegex matches with each individual words in string, according to regex provided.


.. code-block:: python

    from janusgraph_python.core.attribute.Text import Text

    edges = g.E().has("reason", Text.textContainsRegex("br[ez]*s")).valueMap().toList()
    print(edges)

    ==> [{'reason': 'loves fresh breezes'}]


^^^^^^^^^^^^^^^
TextFuzzy
^^^^^^^^^^^^^^^

This Predicate is part of *Text* package.
TextFuzzy is used to query for complete matches with Fuzzy logic in values of properties.
The difference between TextContainsFuzzy and TextFuzzy is seen in example bellow.


.. code-block:: python

    from janusgraph_python.core.attribute.Text import Text

    edges = g.E().has("reason", Text.textContainsFuzzy("breezs")).valueMap(True).toList()
    print(edges)

    ==> [{<T.id: 1>: '2dj-37c-9hx-360', 'reason': 'loves fresh breezes', <T.label: 3>: 'lives'}]

    edges = g.E().has("reason", Text.textFuzzy("luves fresh breezs")).valueMap(True).toList()
    print(edges)

    ==> [{<T.id: 1>: '2dj-37c-9hx-360', 'reason': 'loves fresh breezes', <T.label: 3>: 'lives'}]


^^^^^^^^^^^^^^^
TextPrefix
^^^^^^^^^^^^^^^

This Predicate is part of *Text* package.
TextPrefix returns the objects, where the string value starts with the given query string.
The difference between TextContainsPrefix and TextPrefix is shows in example bellow.


.. code-block:: python

    from janusgraph_python.core.attribute.Text import Text

    edges = g.E().has("reason", Text.textContainsPrefix("breeze")).valueMap().toList()
    print(edges)

    ==> [{'reason': 'loves fresh breezes'}]

    edges = g.E().has("reason", Text.textContainsPrefix("loves")).valueMap().toList()
    print(edges)

    ==> [{'reason': 'loves fresh breezes'}, {'reason': 'loves waves'}]

    edges = g.E().has("reason", Text.textPrefix("breeze")).valueMap().toList()
    print(edges)

    ==> []


^^^^^^^^^^^^^^^
TextRegex
^^^^^^^^^^^^^^^

This Predicate is part of *Text* package.
TextRegex matches the whole string, according to regex provided.


.. code-block:: python

    from janusgraph_python.core.attribute.Text import Text

    edges = g.E().has("reason", Text.textRegex('l[ov]*es\s*w[a-v]*')).valueMap().toList()
    print(edges)

    ==> [{'reason': 'loves waves'}]

