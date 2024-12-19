# Copyright 2023 JanusGraph-Python Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import json
import time
import pathlib
import configparser

from pytest import fixture, param, skip, exit
from testcontainers.core.container import DockerContainer
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from janusgraph_python.driver.serializer import JanusGraphSONSerializersV3d0

current_path = pathlib.Path(__file__).parent.resolve()
JANUSGRAPH_REPOSITORY = None
JANUSGRAPH_VERSION_PARAMS = []

# read integration tests config from JSON
with open(os.path.join(current_path, "config.json")) as f:
    config = json.load(f)
    JANUSGRAPH_REPOSITORY = config.get("dockerRepository", None)
    docker_tags = config.get("dockerTags", [])
    JANUSGRAPH_VERSION_PARAMS = [param(t, id=t) for t in docker_tags]

def pytest_configure(config):
    # registering custom marker to be able to skip integration tests
    # that are incompatible with older JanusGraph version
    config.addinivalue_line(
        "markers", "minimum_janusgraph_version(version): mark integration test with minimum required JanusGraph version"
    )

# this fixture should be used for all test methods in the integration tests
@fixture(autouse=True, scope='function')
def janusgraph_compatibility(request):
    """
    Fixture to check if a given integration test is allowed to run on a given
    JanusGraph version. If the version is not satisfied, the test will be skipped.
    """
    # get minimum desired JanusGraph version for the test if defined
    marker = request.node.get_closest_marker("minimum_janusgraph_version")
    # if no minimum desired JanusGraph version is defined, no need to check compatibility
    if not marker or not marker.args:
        return

    min_jg_version = marker.args[0]

    # get version of JanusGraph used by the current test run
    if len(request.fixturenames) == 0:
        exit("Fixtures are not used on the expected way")

    top_fixture = request.fixturenames[0]
    current_jg_version = request.node.callspec.params.get(top_fixture)
    if not current_jg_version:
        exit(f"{top_fixture} fixture needs to be parametrized with the list of JanusGraph versions to test with")

    if current_jg_version == min_jg_version:
        return

    jg_v_list = [int(num) for num in current_jg_version.split('.')]
    min_v_list = [int(num) for num in min_jg_version.split('.')]

    for jg_v, min_v in zip(jg_v_list, min_v_list):
        if jg_v < min_v:
            return skip(f"not compatible with JanusGraph {current_jg_version}")

@fixture(scope='session')
def graph_connection_graphson(request, graph_container):
    """
    Fixture for creating connection with JanusGraphSONSerializersV3d0 serializer
    to the JanusGraph container
    """
    # NOTE: this is a workaround to be able to pass the session fixture param
    # to the graph_container fixture
    container = graph_container(request)
    return graph_connection(request, container, JanusGraphSONSerializersV3d0())

def graph_connection(request, graph_container, serializer):
    """
    Fixture for creating connection with given serializer to the
    JanusGraph container
    """
    connection = DriverRemoteConnection(
        f'ws://{graph_container.get_container_host_ip()}:{graph_container.get_exposed_port(8182)}/gremlin',
        'g',
        message_serializer=serializer
    )

    def close_connection():
        connection.close()
    
    request.addfinalizer(close_connection)

    g = traversal().with_remote(connection)

    return g


@fixture(scope='session')
def graph_container(request):
    """
    Fixture for creating JanusGraph container before first test and dropping
    container after last test in the test session
    """

    def create_container(passed_request):
        container = None

        def is_server_ready():
            """
            Method to test if JanusGraph server is up and running and filled with test data
            """
            connection = None
            
            while True:
                try:
                    connection = DriverRemoteConnection(
                        f'ws://{container.get_container_host_ip()}:{container.get_exposed_port(8182)}/gremlin',
                        'g',
                        message_serializer=JanusGraphSONSerializersV3d0()
                    )
                    g = traversal().with_remote(connection)

                    if g.V().has('name', 'hercules').has_next():
                        break
                except Exception as e:
                    pass
                finally:
                    if connection:
                        connection.close()

                time.sleep(2)

        if not hasattr(passed_request, "param"):
            top_fixture = passed_request.fixturenames[0]
            exit(f"{top_fixture} fixture needs to be parametrized with the list of JanusGraph versions to test with")

        tag = passed_request.param
        image = f"{JANUSGRAPH_REPOSITORY}:{tag}"

        container = (
            DockerContainer(image)
                .with_name(f'janusgraph_{tag}')
                .with_exposed_ports(8182)
                .with_volume_mapping(os.path.join(current_path, 'load_data.groovy'), '/docker-entrypoint-initdb.d/load_data.groovy')
                .start()
        )
        is_server_ready()

        def drop_container():
            container.stop()

        request.addfinalizer(drop_container)

        return container
    return create_container