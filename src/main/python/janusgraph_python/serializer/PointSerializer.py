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

from gremlin_python.structure.io.graphsonV3d0 import GraphSONUtil
from ..utils.toGeoJSON import toGeoJSON


class PointSerializer(object):
    """ Serialize a GeoShape Point object so that the same can be passed to Gremlin Server """

    GRAPHSON_PREFIX = "janusgraph"
    GRAPHSON_BASE_TYPE = "Geoshape"

    @classmethod
    def dictify(cls, point, writer):
        """ This is serializer method for Point class.

        Args:
            point (Point): The GeoShape Point class to serialize into.
            writer:

        Returns:
            json
        """

        geometryJSON = toGeoJSON(point).convert()

        serializedJSON = GraphSONUtil.typedValue(cls.GRAPHSON_BASE_TYPE, geometryJSON, cls.GRAPHSON_PREFIX)

        return serializedJSON
