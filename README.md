# JanusGraph-Python

JanusGraph-Python extends Apache TinkerPop™'s [Gremlin-Python][gremlinpython] with
support for [JanusGraph][janusgraph]-specific types.

## Usage

To connect to JanusGraph Server, a `DriverRemoteConnection` instance needs to be
created and configured with a message serializer that adds support for
JanusGraph specific types.

This can be done like this for GraphSON 3:

```python
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from janusgraph_python.driver.serializer import JanusGraphSONSerializersV3d0

connection = DriverRemoteConnection(
  'ws://localhost:8182/gremlin', 'g',
  message_serializer=JanusGraphSONSerializersV3d0())
```

This can be done like this for GraphBinary:

```python
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from janusgraph_python.driver.serializer import JanusGraphBinarySerializersV1

connection = DriverRemoteConnection(
 'ws://localhost:8182/gremlin', 'g',
 message_serializer=JanusGraphBinarySerializersV1())
```

Note that the client should be disposed on shut down to release resources and
to close open connections with `connection.close()`.
The connection can then be used to configure a `GraphTraversalSource`:

```python
from gremlin_python.process.anonymous_traversal import traversal

g = traversal().with_remote(connection)
# Reuse 'g' across the application
```

The `GraphTraversalSource` `g` can now be used to spawn Gremlin traversals:

```python
hercules_age = g.V().has("demigod", "name", "hercules").values("age").next()
print(f"Hercules is {hercules_age} years old.")
```

Refer to the chapter [Gremlin Query Language][gremlin-chapter] in the
JanusGraph docs for an introduction to Gremlin and pointers to further
resources.
The main syntactical difference for Gremlin-Python is that it follows Python naming
conventions, e.g., method names use snake_case instead of camelCase. Other difference is that when Python reserved words (e.g. "is") overlap with Gremlin steps or tokens, those gets underscore suffix (e.g. "is_").

### Text Predicates

The `Text` class provides methods for
[full-text and string searches][text-predicates]:

```python
from janusgraph_python.process.traversal import Text

g.V().has("demigod", "name", Text.text_prefix("herc")).to_list()
```

The other text predicates can be used the same way.

## Version Compatibility

The lowest supported JanusGraph version is 1.0.0.
The following table shows the supported JanusGraph versions for each version
of JanusGraph-Python:

| JanusGraph-Python | JanusGraph             |
| ----------------- | ---------------------- |
| 1.0.z             | 1.0.z                  |
| 1.1.z             | (1.0.z,) 1.1.z         |

While it should also be possible to use JanusGraph-Python with other versions of
JanusGraph than mentioned here, compatibility is not tested and some
functionality (like added Gremlin steps) will not work as it is not supported
yet in case of an older JanusGraph version or was removed in a newer JanusGraph
version.

## Serialization Formats

JanusGraph-Python supports GraphSON 3 as well as GraphBinary.

Not all of the JanusGraph-specific types are already supported by the formats:

| Format      | RelationIdentifier | Text predicates | Geoshapes | Geo predicates |
| ----------- | ------------------ | --------------- | --------- | -------------- |
| GraphSON3   | x                  | x               | -         | -              |
| GraphBinary | x                  | x               | -         | -              |

## Community

JanusGraph-Python uses the same communication channels as JanusGraph in general.
So, please refer to the
[_Community_ section in JanusGraph's main repository][janusgraph-community]
for more information about these various channels.

Please use GitHub issues only to report bugs or request features.

## Contributing

Please see
[`CONTRIBUTING.md` in JanusGraph's main repository][janusgraph-contributing]
for more information, including CLAs and best practices for working with
GitHub.

## License

JanusGraph-Python code is provided under the [Apache 2.0 license](APACHE-2.0.txt)
and documentation is provided under the [CC-BY-4.0 license](CC-BY-4.0.txt). For
details about this dual-license structure, please see
[`LICENSE.txt`](LICENSE.txt).

[janusgraph]: https://janusgraph.org/
[gremlinpython]: https://tinkerpop.apache.org/docs/current/reference/#gremlin-python
[gremlin-chapter]: https://docs.janusgraph.org/getting-started/gremlin/
[text-predicates]: https://docs.janusgraph.org/interactions/search-predicates/#text-predicate
[janusgraph-community]: https://github.com/JanusGraph/janusgraph#community
[janusgraph-contributing]: https://github.com/JanusGraph/janusgraph/blob/master/CONTRIBUTING.md