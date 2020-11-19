# Copyright 2018 JanusGraph Python Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pybuilder.core import use_plugin, init, Author, task, depends

authors = [Author("Debasish Kanhar", "dekanhar@in.ibm.com")]
description = "Python client drivers for JanusGraph"
copyright = "Copyright 2018 JanusGraph Python Authors"
license = "Apache License v2.0"

name = "janusgraph_python"

tinkerpop_version = "3.3.3"
janusgraph_version = "0.3.0"
version = "0.1.0"

use_plugin("python.core")
# the python unittest plugin allows running python's standard library unittests
use_plugin("python.unittest")
# this plugin allows installing project dependencies with pip
use_plugin("python.install_dependencies")
# a plugin that measures unit test statement coverage
use_plugin("python.coverage")
# for packaging purposes since we'll build a tarball
use_plugin("python.distutils")
# For generating Docs from docstring using Sphinx
use_plugin("python.sphinx")
# For running integration tests
use_plugin('python.integrationtest')

default_task = ['clean', 'install_dependencies', 'prepare', 'compile_sources', 'package', 'publish']

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
    project.set_property("unittest_module_glob", "_test")

    project.set_property("sphinx_config_path", "docs/")
    project.set_property("sphinx_source_dir", "docs/")
    project.set_property("sphinx_output_dir", "docs/_build")

    project.set_property("dir_dist", "target/dist/" + project.name)
    project.depends_on("gremlinpython", "=={}".format(tinkerpop_version))
