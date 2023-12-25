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
import time
import pathlib
import configparser

from pytest import fixture
from testcontainers.core.container import DockerContainer
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from janusgraph_python.driver.serializer import JanusGraphSONSerializersV3d0

@fixture(scope='session')
def graph_connection_graphson(request, graph_container):
    """
    Fixture for creating connection with JanusGraphSONSerializersV3d0 serializer
    to the JanusGraph container
    """
    return graph_connection(request, graph_container, JanusGraphSONSerializersV3d0())

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
    container = None
    current_path = pathlib.Path(__file__).parent.resolve()

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

    config = configparser.ConfigParser()
    config.read(os.path.join(current_path, 'config.ini'))

    container = (
        DockerContainer(config['docker']['image'])
            .with_name('janusgraph')
            .with_exposed_ports(8182)
            .with_volume_mapping(os.path.join(current_path, 'load_data.groovy'), '/docker-entrypoint-initdb.d/load_data.groovy')
            .start()
    )
    is_server_ready()

    def drop_container():
        container.stop()
    
    request.addfinalizer(drop_container)

    return container
