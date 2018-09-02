=======
Installation of Drivers
=======

The library, janusgraph-python can be installed either using PyPi or else can be build from the main repository. 
Currently, it is not yet hosted to PyPi, till version 1.0.0 is out, but you can clone the repository and build the library yourself.

++++
Installation using PyPi
++++

.. code-block:: bash

    pip install janusgraph-python
    # This installs the latest version of JanusGraph-Python drivers. To install specific to JanusGraph version, please use the following syntax

    pip install janusgraph-python==x.y.z
    # Where x.y.z is version number, corresponding to JanusGraph version you are using. Please refer to Compartibility matrix to get version compartible against each JanusGraph version


In version number, x.y.z, "z" is minor version number. Irrespective of minor version change, as long as x.y remains same, the Compartibility for JanusGraph remains same.

Example::
    
    Version 1.0.0 is compartible with JanusGraph 0.3.0. Meaning that 1.0.1/1.0.2/..1.0.x will all be compartible with JanusGraph 0.3.0

++++
Installation by building from repository
++++

.. code-block:: bash

    # Install PyBuilder, build tool needed for building library
    pip install pybuilder

    # Build the library
    pyb

    # To build documentation,
    pyb sphinx_generate_documentation

    # To install the library
    # The library will be found under target/dist/janusgraph_python/dist/
    cd target/dist/janusgraph_python/dist/

    # Install the library
    pip install janusgraph_python-1.0.0.tar.gz

