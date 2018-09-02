# Name: Debasish Kanhar


from pybuilder.core import use_plugin, init, Author, task, depends

authors = [Author("Debasish Kanhar", "dekanhar@in.ibm.com")]
description = "Python client drivers for JanusGraph"
license = "Apache License v2.0"

name = "janusgraph_python"

tinkerpop_version = "3.3.3"
janusgraph_version = "0.3.0"
version = "0.0.9"

use_plugin("python.core")
# the python unittest plugin allows running python's standard library unittests
# use_plugin("python.unittest")
# this plugin allows installing project dependencies with pip
use_plugin("python.install_dependencies")
# a plugin that measures unit test statement coverage
# use_plugin("python.coverage")
# use_plugin('pypi:pybuilder_pytest_coverage')
# for packaging purposes since we'll build a tarball
use_plugin("python.distutils")
# For generating Pycharm project files
use_plugin("python.pycharm")
# For generating Docs from docstring using Spinx
use_plugin("python.sphinx")

# default_task = ['clean', 'install_dependencies', 'publish', 'pycharm_generate']
default_task = ['clean', 'install_dependencies', 'prepare', 'compile_sources', 'pycharm_generate']

# This is an initializer, a block of logic that runs before the project is built.
@init
def initialize(project):
    # Nothing happens here yet, but notice the `project` argument which is automatically injected.
    project.set_property("coverage_break_build", False)  # default is True
    project.set_property("coverage_reset_modules", True)
    project.set_property("coverage_threshold_warn", 50)
    project.set_property("coverage_branch_threshold_warn", 60)
    project.set_property("coverage_branch_partial_threshold_warn", 70)
    project.set_property("coverage_allow_non_imported_modules", True)
    project.set_property("coverage_exceptions", ["__init__"])

    project.set_property("unittest_test_method_prefix", "test")
    project.set_property("unittest_file_suffix", "_test")

    project.set_property("sphinx_config_path", "docs/")
    project.set_property("sphinx_source_dir", "docs/")
    project.set_property("sphinx_output_dir", "docs/_build")

    project.set_property("dir_dist", "target/dist/" + project.name)
    project.depends_on("gremlinpython", "=={}".format(tinkerpop_version))
    pass
