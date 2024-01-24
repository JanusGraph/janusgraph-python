from janusgraph_python.driver.serializer import JanusGraphSONSerializersV3d0
from janusgraph_python.structure.io import graphsonV3d0


def test_graphson_serializer_v3():
    graphson_serializer_v3 = JanusGraphSONSerializersV3d0()
    
    assert graphson_serializer_v3.version == b"application/vnd.gremlin-v3.0+json"
    assert isinstance(graphson_serializer_v3._graphson_reader, graphsonV3d0.JanusGraphSONReader)
    assert isinstance(graphson_serializer_v3.standard._writer, graphsonV3d0.JanusGraphSONWriter)
    assert isinstance(graphson_serializer_v3.traversal._writer, graphsonV3d0.JanusGraphSONWriter)