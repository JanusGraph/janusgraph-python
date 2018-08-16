=========================
Connecting to JanusGraph
=========================

The library provides a client to connect to JanusGraph running in
Gremlin Server mode.

For information about Gremlin Server, refer to `JanusGraph docs
<https://docs.janusgraph.org/latest/server.html>`_.


-------------------------
Build JanusGraph Client
-------------------------

The client provided to connect to JanusGraph takes care of registering the
required serializers and deserializers like GeoShape, RelationIdentifier
and any objects specific to JanusGraph.


.. code-block:: python

    from janusgraph_python.driver.ClientBuilder import JanusGraphClient
    from gremlin_python.structure.graph import Graph
    # Create JanusGraph connection providing required parameters.
    connection = JanusGraphClient().connect(host="0.0.0.0", port="8182", traversal_source="g").get_connection()
    # Create Traversal with JanusGraph connection object
    g = Graph().traversal().withRemote(connection)


-----------------------------------------
Register Custom Serializer/Deserializer
-----------------------------------------

JanusGraph Python client provides API to register your custom Serializer/Deserializer

    - Serializer: Serializes a Python object into corresponding JanusGraph object.
                    Currently implemented for Point,
                    Circle and
                    RelationIdentifier

    - Deserializer: Deserializes response from Gremlin Server into corresponding Python objects.
                    Currently implemented for above mentioned data types
                    see docs.


**NOTE**: It is safe to add Serializer and Deserializer for a particular object together, else we
might run into unforeseen errors.


.. code-block:: python

    # Create custom objects, and its serializer and deserializer methods. (Follows example from Gremlin-Python)
    class MyType(object):
        GRAPHSON_PREFIX = "janusgraph"
        GRAPHSON_BASE_TYPE = "MyType"
        GRAPHSON_TYPE = GraphSONUtil.formatType(GRAPHSON_PREFIX, GRAPHSON_BASE_TYPE)

        def __init__(self, x, y):
            self.x = x
            self.y = y

        @classmethod
        def objectify(cls, value, reader):
            return cls(value['x'], value['y'])

        @classmethod
        def dictify(cls, value, writer):
            return GraphSONUtil.typedValue(cls.GRAPHSON_BASE_TYPE, {'x': value.x, 'y': value.y}, cls.GRAPHSON_PREFIX)

    # Register Serializer and Deserializer with JanusGraphReader and Writer service
    from janusgraph_python.structure.io.GraphsonWriter import JanusGraphSONWriter
    from janusgraph_python.structure.io.GraphsonReader import JanusGraphSONReader
    from gremlin_python.structure.io.graphsonV3d0 import GraphSONUtil

    # Registering it
    reader_builder = JanusGraphSONReader().register_deserializer(MyType.GRAPHSON_BASE_TYPE, MyType)
    reader = reader_builder.get()

    writer_builder = JanusGraphSONWriter().register_serializer(MyType, MyType)
    writer = writer_builder.get()

    # Apply the connected reader and writer service while creating JanusGraph connection
    from gremlin_python.structure.graph import Graph
    from janusgraph_python.driver.ClientBuilder import JanusGraphClient

    client = JanusGraphClient().connect(host="0.0.0.0", port="8182",
                                        traversal_source="g", graphson_reader=reader, graphson_writer=writer)
    connection = client.get_connection()
    g = Graph().traversal().withRemote(client)

