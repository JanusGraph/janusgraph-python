==========================
JanusGraph Geo Predicates
==========================

JanusGraph provides APIs to query the dataset based on Geometric Point. The configuration to setup
Geometric data types on which queries can be done, is dependeng on the Indexing backend being used.

For creating Geo index, refer to `JanusGraph Geo Mapping docs
<https://docs.janusgraph.org/latest/index-parameters.html#geo-search>`_.

----------------------------
Available Geo Predicates
----------------------------

The Geo Predicate provides the following 4 types of predicates for queries the data.

    - geoWithin_
    - geoContains_

While, in current release only geoContains and geoWithin is implemented.

Contributions are invited for development of other following Geo Predicates.

    - geoDisjoint
    - geoIntersect

^^^^^^^^^^^^^^^
geoContains
^^^^^^^^^^^^^^^

This Predicate is part of *Geo* package.
geoContains is used to query a scenario where we want to test weather a Geometric
object contains another.

For example bellow, we create a Geometric Circle object with ``latitude: 7.58, longitude: 21.5
and radius 5km`` naming it as Arcadia. We want to query for Objects (Vertices or Edges) which contains
our query shape ``Circle with latitude: 7.58, longitude: 21.5 and radius 2km`` then the following example
holds true.

For reference, see the docs about `GeoShapes <geo-shapes.html>`_ (Note how latitude and longitude are reversed).

.. code-block:: python

    from janusgraph_python.core.datatypes.GeoShape import GeoShape
    from janusgraph_python.core.attribute import Geo

    arcadia = GeoShape.Circle(7.58, 21.50, 5)
    ==> CIRCLE(lat: 7.58, lon: 21.5, r: 5)

    hercules = g.addV().property("name", "hercules").property("age", 30).property("type", "demigod").next()
    birds = g.addV().property("name", "symphalian birds").property("age", 100).property("type", "monster").next()

    edgeAdded = g.V(birds).as_("to").V(hercules).addE("battled").property("time", 290).\
                property("place", arcadia).to("to").next()
    ==> e[63hf6j-3bs-9hx-36g][4312-battled->4120]

    shape = GeoShape.Circle(21.50, 7.58, 2)
    herculesBattledWith = g.V().has("name", "hercules").outE().has("place", Geo.geoContains(shape)).next()
    ==> e[63hee3-3bs-9hx-36g][4312-battled->4120]

^^^^^^^^^^^^^^^
geoWithin
^^^^^^^^^^^^^^^

This Predicate is part of *Geo* package.
geoWithin is used to query a scenario where we want to test weather a Geometric
object is within another.

For example bellow, we create a Geometric Circle object with ``latitude: 7.58, longitude: 21.5
and radius 5km`` naming it as Arcadia. If we want to query for all objects (Vertices and Edges) contained within
another geometric shape, then the following bellow holds true. For analogy, this is similar to querying
``Capital City within Country``, where `Country` is the object used to query, whereas `Capital` is
returned value of query.

**NOTE** Note the difference in usage of GeoContains and GeoWithin with respect to the GeoShape object
being used to query

.. code-block:: python

    from janusgraph_python.core.datatypes.GeoShape import GeoShape
    from janusgraph_python.core.attribute import Geo

    shape = GeoShape.Circle(37.97, 23.72, 50)
    ==> CIRCLE(lat: 37.97, lon: 23.72, r: 50)

    g.E().has("place", Geo.geoWithin(shape)).next()
    ==> e[555-6dk-9hx-6cw][8264-battled->8240]
