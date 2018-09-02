
# JanusGraph Python driver

## License

JanusGraph Python driver code is provided under the [Apache 2.0
license](APACHE-2.0.txt) and documentation is provided under the [CC-BY-4.0
license](CC-BY-4.0.txt). For details about this dual-license structure, please
see [`LICENSE.txt`](LICENSE.txt).


Python Client for connecting to JanusGraph and executing JanusGraph specific features.


For building the library, the pre requisite is that PyBuilder needs to be installed on system.

For installing PyBuilder, the following needs to be run:

```pip install pybuilder```

Once PyBuilder is installed, run the following commands to build the Library:

```pyb package publish```

Running the above command deletes the <b>target</b> folder, installs dependencies, and generates Project files to be used with PyCharm.

For building documentation, the following command needs to be run:

- First, build <b>.rst</b> files from docstrings so that the same can be consumed by Sphinx auto-doc generator to generate HTML docs.
- Second, run the pybuilder spinx generator plugin to generate html files from .rst files.

```
# Generate rst files using sphinx-apidoc
sphinx-apidoc -o docs/ src/main/python/janusgraph_python
```

```
# Build HTML files from .rst source files
pyb sphinx_generate_documentation
```

Once done, you can see the build HTML files under ```docs/_build``` directory.
 