==========================
JanusGraph Text Predicates
==========================

JanusGraph provides APIs to query the data using Text Predicates. The types of Text Predicates available
for querying depends on the Indexing backend used. While using Elasticsearch as Indexing backend exposes
all types of Text Predicates, but using some other backend like Solr won't expose all the Text Predicates. 
Hence, be careful with using the Text Predicates, and refer to original JanusGraph docs_.

.. _docs: https://docs.janusgraph.org/latest/


----------------------------
Available Text Predicates
----------------------------

The Text Predicates are broadly divided into 2 categories as:
    - Text search predicates which match against the individual words inside a text string after it has been tokenized. These predicates are not case sensitive.

        - TextContains_
        - TextContainsFuzzy_
        - TextContainsPrefix_
        - TextContainsRegex_

    - String search predicates which match against the entire string value

        - TextFuzzy_
        - TextPrefix_
        - TextRegex_

^^^^^^^^^^^^^^^
TextContains
^^^^^^^^^^^^^^^

This Predicate is part of *Text* package.
TextContains is used to query for partial matches in values of properties. 
The following example is based on GodsOfGraph which comes pre-packaged with JanusGraph.
The query is to find all edges where ``reason`` contains ``breezes``


.. code-block:: python

    from janusgraph_python.core.attribute.TextPredicate.Text import Text

    # Find all edges which contains the word breezes
    edges = g.E().has("reason", Text.textContains("breezes")).next()
    print(edges)

    ==> e[55m-6hc-b2t-3bk][8400-lives->4304]

    # Find all edges which contains the word breezes and loves
    edges = g.E().has("reason", Text.textContains("breezes")).has("reason", Text.textContains("loves")).next()
    print(edges)

    ==> e[55m-6hc-b2t-3bk][8400-lives->4304]


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TextContainsFuzzy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This Predicate is part of *Text* package.
TextContainsFuzzy is used to query for partial matches with Fuzzy logic in values of properties.
The following example is based on GodsOfGraph which comes pre-packaged with JanusGraph.
We know there is a vertex with *Hercules* value on property `name`. We query all vertices with value as *Herculies*
Similarly, we use in Conjugation with multiple other attributes to query edge as in above example.


.. code-block:: python

    from janusgraph_python.core.attribute.TextPredicate.Text import Text

    hercules = g.V().has("name", Text.textContainsFuzzy("hercauleas")).valueMap(True).next()
    print(hercules)

    ==> {'name': ['hercules'], <T.id: 1>: 4312, <T.label: 3>: 'demigod', 'age': [30]}

    edges = g.E().has("reason", Text.textContainsFuzzy("breezs")).has("reason", Text.textContains("loves")).next()
    print(edges)

    ==> e[55m-6hc-b2t-3bk][8400-lives->4304]

    edges = g.E().has("reason", Text.textContainsFuzzy("breezs")).has("reason", Text.textContainsFuzzy("luves")).next()
    print(edges)

    ==> e[55m-6hc-b2t-3bk][8400-lives->4304]



^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TextContainsPrefix
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This Predicate is part of *Text* package.
TextContainsPrefix is used to query for where the value (if sentence, it is segmented, & any word in segment is considered)
contains the string queries in prefix
The following example is based on GodsOfGraph which comes pre-packaged with JanusGraph and shows the difference
between TextContains and TextContainsPrefix and TextPrefix.


.. code-block:: python

    from janusgraph_python.core.attribute.TextPredicate.Text import Text

    edges = g.E().has("reason", Text.textContainsFuzzy("breezs")).has("reason", Text.textContains("loves")).valueMap().toList()
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
The following example is based on GodsOfGraph which comes pre-packaged with JanusGraph.


.. code-block:: python

    from janusgraph_python.core.attribute.TextPredicate.Text import Text

    edges = g.E().has("reason", Text.textContainsRegex("br[ez]*s")).valueMap().toList()
    print(edges)

    ==> [{'reason': 'loves fresh breezes'}]


^^^^^^^^^^^^^^^
TextFuzzy
^^^^^^^^^^^^^^^

This Predicate is part of *Text* package.
TextFuzzy is used to query for complete matches with Fuzzy logic in values of properties.
The following example is based on GodsOfGraph which comes pre-packaged with JanusGraph and shows the difference
between TextContainsFuzzy and TextFuzzy.


.. code-block:: python

    from janusgraph_python.core.attribute.TextPredicate.Text import Text

    edges = g.E().has("reason", Text.textContainsFuzzy("breezs")).next()
    print(edges)

    ==> e[55m-6hc-b2t-3bk][8400-lives->4304]

    edges = g.E().has("reason", Text.textFuzzy("luves fresh breezs")).next()
    print(edges)

    ==> e[55m-6hc-b2t-3bk][8400-lives->4304]


^^^^^^^^^^^^^^^
TextPrefix
^^^^^^^^^^^^^^^

This Predicate is part of *Text* package.
TextPrefix returns the objects, where the string being queries is at the beginning and at prefix of the property's value.
The following example is based on GodsOfGraph which comes pre-packaged with JanusGraph and shows the difference
between TextContainsPrefix and TextPrefix.


.. code-block:: python

    from janusgraph_python.core.attribute.TextPredicate.Text import Text

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
The following example is based on GodsOfGraph which comes pre-packaged with JanusGraph.


.. code-block:: python

    from janusgraph_python.core.attribute.TextPredicate.Text import Text

    edges = g.E().has("reason", Text.textRegex('l[ov]*es\s*w[a-v]*')).valueMap().toList()
    print(edges)

    ==> [{'reason': 'loves waves'}]

