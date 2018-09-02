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

    - geoIntersect
    - geoWithin_
    - geoDisjoint
    - geoContains_

While, in current release only geoContains and geoWithin is implemented, but geoWithin isn't yet tested.
Contributions are invited for development of other Geo Predicates.

^^^^^^^^^^^^^^^
geoContains
^^^^^^^^^^^^^^^

This Predicate is part of *Geo* package.
geoContains is used to query a scenario where we want to test weather a Geometric
object contains another.
Hence, for example, since New Delhi is capital of India, the query
``GeoShape(India) contains GeoShape(New Delhi)`` holds true.

For scope of example, we have added a point named arcadia with co-ordinates 7.58 21.50 and radius 5km (Circle).
For reference, see the docs about `GeoShapes <geo-shapes.html>`_ (Note how latitude nad longitude are reversed).

.. code-block:: python

    from janusgraph_python.core.datatypes.GeoShape import GeoShape
    from janusgraph_python.core.attribute import Geo

    arcadia = GeoShape.Circle(21.50, 7.58, 5)
    ==> CIRCLE(lat: 7.58, lon: 21.5, r: 5)

    edgeAdded = g.V(birds).as_("to").V(hercules).addE("battled").property("time", 290).property("place", arcadia).to("to").next()
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
Hence, for example, since New Delhi is capital of India, the query
``GeoShape(New Delhi) contains GeoShape(India)`` holds true.

**Note the difference in usage of GeoContains and GeoWithin with respect to the GeoShape object being used to query.**

.. code-block:: python

    from janusgraph_python.core.datatypes.GeoShape import GeoShape
    from janusgraph_python.core.attribute import Geo

    arcadia = GeoShape.Circle(21.50, 7.58, 5)
    ==> CIRCLE(lat: 7.58, lon: 21.5, r: 5)

    edgeAdded = g.V(birds).as_("to").V(hercules).addE("battled").property("time", 290).property("place", arcadia).to("to").next()
    ==> e[63hf6j-3bs-9hx-36g][4312-battled->4120]

    shape = GeoShape.Circle(21.50, 7.58, 100)
    edges = g.V().has("name", "hercules").outE().has("place", Geo.geoWithin(shape)).next()
    ==> e[63hee3-3bs-9hx-36g][4312-battled->4120]
