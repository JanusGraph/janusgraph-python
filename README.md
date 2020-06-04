# JanusGraph-Python

## Python Client drivers for [JanusGraph](http://janusgraph.org)

JanusGraph-Python is the Python driver for connecting to JanusGraph. 
It extends Apache TinkerPop™'s [Gremlin-Python](http://tinkerpop.apache.org/docs/current/reference/#gremlin-python) 
as its core dependency with additional support for JanusGraph-specific types and predicates.

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a643a483556740c1b87ba29e160d37b6)](https://www.codacy.com/app/JanusGraph/janusgraph-python?utm_source=github.com&utm_medium=referral&utm_content=JanusGraph/janusgraph-python&utm_campaign=Badge_Grade)

### Pre-Requisites

The following Python versions are supported by Library:

-   [Python 3.4](https://www.python.org/downloads/release/python-340/).
-   [Python 3.5](https://www.python.org/downloads/release/python-350/).
-   [Python 3.6](https://www.python.org/downloads/release/python-360/).

### Building Library

You can build the library yourself to test out the functionality of library. Refer to 
[Building docs](BUILDING.md) for documentation on how to build the library.

### Installing the Library

-   Though Installation of library is built as a functionality of the automated build scripts provided,
      but if needed, user can follow the bellow instructions to install the library to environment of their choice.

-   To install library using Pip (It is not yet hosted):

    ```bash
    # X is version number of JanusGraph Python client supported based on JanusGraph version chosen.
    pip install janusgraph_python=X
    ```
    
-   To install library from tarball, once it is built:

    ```bash
    pip install target/dist/janusgraph_python/dist/janusgraph_python-X.tar.gz
    # X is version number of JanusGraph Python client supported based on JanusGraph version chosen.
    ```

### Compatibility Matrix

| Client Version | JanusGraph Version |
| :----------------: | :------------: |
|        0.1.x       |      0.3.x     |
|    Not Released    |  0.4.x  |


### Community

JanusGraph-Python uses the same communication channels as JanusGraph in general. 
So, please refer to the 
[Community section in JanusGraph's main repository](https://github.com/JanusGraph/janusgraph#community) 
for more information about these various channels.

### Contributing

Please see 
[`CONTRIBUTING.md` in JanusGraph's main repository](https://github.com/JanusGraph/janusgraph/blob/master/CONTRIBUTING.md) 
for more information, including CLAs and best practices for working with GitHub.

### License

JanusGraph Python driver code is provided under the [Apache 2.0
license](APACHE-2.0.txt) and documentation is provided under the [CC-BY-4.0
license](CC-BY-4.0.txt). For details about this dual-license structure, please
see [`LICENSE.txt`](LICENSE.txt).
