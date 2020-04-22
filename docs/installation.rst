========================
Installation of Drivers
========================

The library, janusgraph-python can be installed either using PyPi or else can be build from the main repository. 
Currently, it is not yet hosted to PyPi, till version 1.0.0 is out, but you can clone the repository and build the
library yourself.

++++++++++++++++++++++++
Installation using PyPi
++++++++++++++++++++++++

.. code-block:: bash

    pip install janusgraph-python
    # This installs the latest version of JanusGraph-Python drivers. To install specific to JanusGraph version,
    # please use the following syntax

    pip install janusgraph-python==x.y.z
    # Where x.y.z is version number, corresponding to JanusGraph version you are using.
    # Please refer to compatibility matrix to get version compatible against each JanusGraph version


++++++++++++++++++++++++++++++++++++++++++++
Installation by building from repository
++++++++++++++++++++++++++++++++++++++++++++

If you are planning to build the library by cloning the repository, then a set of automated build scripts
are created to make the like of the user easier.

For docs on how to build the library after cloning from repository, refer to `Building Docs
<../BUILDING.md>`_ for building the library.

**NOTE**: For installing the library once it is built using any of above scripts, run the following to install it

.. code-block:: bash

    pip install target/dist/janusgraph_python/dist/janusgraph_python-*.tar.gz
