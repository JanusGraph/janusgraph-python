==========================
JanusGraph Geo Shapes
==========================

JanusGraph provides API to create Geometric objects so that they can
be queried using Geo Predicates from `docs
<geo-predicates.html>`_.


----------------------------
Available Geo Shapes
----------------------------

While JanusGraph's JVM based clients provides following shapes:

    - POINT_
    - BOX
    - CIRCLE_
    - LINE
    - POLYGON
    - MULTIPOINT
    - MULTILINESTRING
    - MULTIPOLYGON
    - GEOMETRYCOLLECTION

The current library has only following shapes implemented:

    - POINT_
    - CIRCLE_

Contributions are invited for development of other Geo Predicates.


^^^^^^^^^^^^^^^
POINT
^^^^^^^^^^^^^^^

This data type / Geometric object is part of GeoShape package.
It is equivalent to Geometric Point defined by Latitude & Longitude.

**NOTE, the way JanusGraph expects it,
The format is (Longitude, Latitude) instead of normal convention (Latitude, Longitude)**

.. code-block:: python

    arcadia = GeoShape.Point(21.50, 7.58)
    ==> POINT(lat: 7.58, lon: 21.5)

^^^^^^^^^^^^^^^
CIRCLE
^^^^^^^^^^^^^^^

This data type / Geometric object is part of GeoShape package.
It is equivalent to Geometric Circle defined by Latitude, Longitude and Radius.

**NOTE, the Radius is in KMs**

**NOTE, the way JanusGraph expects it,
The format is (Longitude, Latitude) instead of normal convention (Latitude, Longitude)**

.. code-block:: python

    arcadia = GeoShape.Circle(21.50, 7.58, 5)
    ==> CIRCLE(lat: 7.58, lon: 21.5, r: 5)

