==========================
JanusGraph Geo Shapes
==========================

JanusGraph provides API to create Geometric objects so that they can
be queried using Geo Predicates from `docs
<geo-predicates.html>`_.


----------------------------
Available Geo Shapes
----------------------------

The current library has only following shapes implemented:

    - POINT_
    - CIRCLE_

While JanusGraph's JVM based clients provides following shapes,
Contributions are invited to implement the following shapes:

    - BOX
    - LINE
    - POLYGON
    - MULTIPOINT
    - MULTILINESTRING
    - MULTIPOLYGON
    - GEOMETRYCOLLECTION

^^^^^^^^^^^^^^^
POINT
^^^^^^^^^^^^^^^

This data type / Geometric object is part of GeoShape package.
It is equivalent to Geometric Point defined by Latitude & Longitude.

.. code-block:: python

    arcadia = GeoShape.Point(7.58, 21.50)
    ==> POINT(lat: 7.58, lon: 21.5)

^^^^^^^^^^^^^^^
CIRCLE
^^^^^^^^^^^^^^^

This data type / Geometric object is part of GeoShape package.
It is equivalent to Geometric Circle defined by Latitude, Longitude and Radius.

**NOTE** The Radius is in KMs

.. code-block:: python

    arcadia = GeoShape.Circle(7.58, 21.50, 5)
    ==> CIRCLE(lat: 7.58, lon: 21.5, r: 5)

