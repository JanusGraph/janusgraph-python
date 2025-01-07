# Copyright 2024 JanusGraph-Python Authors
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

from gremlin_python.structure.io.graphbinaryV1 import (
    _GraphBinaryTypeIO, StringIO, GraphBinaryReader, GraphBinaryWriter, DataType,
    _make_packer,
    uint64_pack, uint64_unpack, uint8_pack, uint8_unpack,
)
from janusgraph_python.process.traversal import _JanusGraphP, RelationIdentifier

uint16_pack, uint16_unpack = _make_packer('>H')
uint32_pack, uint32_unpack = _make_packer('>I')

class JanusGraphBinaryReader(GraphBinaryReader):
    def __init__(self):
        # register JanusGraph-specific deserializer for custom type code
        deserializer_map = {
            DataType.custom: JanusGraphBinaryTypeIO
        }

        GraphBinaryReader.__init__(self, deserializer_map)

class JanusGraphBinaryWriter(GraphBinaryWriter):
    def __init__(self):
        # register JanusGraph-specific RelationIdentifier and text-predicate serializer
        serializer_map = [
            (RelationIdentifier, JanusGraphRelationIdentifierIO),
            (_JanusGraphP, JanusGraphPSerializer)
        ]

        GraphBinaryWriter.__init__(self, serializer_map)

class JanusGraphBinaryTypeIO(_GraphBinaryTypeIO):
    # registry of JanusGraph-specific types with their type_id, type_name and class for deserialization
    io_registry = {}

    @classmethod
    def register_deserializer(cls, type_class):
        """
        Method to register a deserializer for a JanusGraph-specific type
        """
        cls.io_registry[type_class.graphbinary_type_id] = (type_class.graphbinary_type_name, type_class)

    @classmethod
    def objectify(cls, buff, reader, nullable=True):
        """
        Method used for deserialization of JanusGraph-specific type
        """
        return cls.is_null(buff, reader, cls._read_data, nullable)
    
    @classmethod
    def _read_data(cls, b, r):
        """
        Method used for identifying a JanusGraph-specific type and
        find a deserializer class for it
        """
        # check if first byte is custom type code byte
        if uint8_unpack(b.read(1)) != DataType.custom.value:
            return None

        # get the custom type name length
        custom_type_name_length = uint16_unpack(b.read(2))
        custom_type_name = b.read(custom_type_name_length).decode()

        # read the custom type id
        custom_type_id = uint32_unpack(b.read(4))

        # try to get a deserializer class for the JanusGraph-specific type
        custom_serializer = cls.io_registry.get(custom_type_id)
        if not custom_serializer:
            raise NotImplementedError(f"No deserializer found for JanusGraph type with id: {custom_type_id}")

        # check the type name
        if custom_serializer[0] != custom_type_name:
            raise NotImplementedError(f"No deserializer found for JanusGraph type with name: {custom_type_name}")

        return custom_serializer[1].objectify(b, r)
    
    @classmethod
    def prefix_bytes_custom_type(cls, writer, to_extend, as_value=False):
        """
        Helper method to add a specific byte array prefix while serializing
        JanusGraph-specific type as custom type
        """
        if to_extend is None:
            to_extend = bytearray()

        # use the custom type code
        if not as_value:
            to_extend += uint8_pack(DataType.custom.value)

        # add the name of the custom JanusGraph type
        StringIO.dictify(cls.graphbinary_type_name, writer, to_extend, True, False)

        # add the id of the custom JanusGraph type
        to_extend += uint32_pack(cls.graphbinary_type_id)

        # use the custom type code
        if not as_value:
            to_extend += uint8_pack(DataType.custom.value)

class JanusGraphPSerializer(JanusGraphBinaryTypeIO):
    graphbinary_type_id = 0x1002
    graphbinary_type_name = "janusgraph.P"
    python_type = _JanusGraphP

    @classmethod
    def dictify(cls, obj, writer, to_extend, as_value=False, nullable=True):
        """
        Method to serialize JanusGraph-specific Text predicate
        """
        cls.prefix_bytes_custom_type(writer, to_extend, as_value)

        # serialize the custom JanusGraph operator
        StringIO.dictify(obj.operator, writer, to_extend, True, False)

        # serialize the value
        writer.to_dict(obj.value, to_extend)

        return to_extend

class JanusGraphRelationIdentifierIO(JanusGraphBinaryTypeIO):
    graphbinary_type_id = 0x1001
    graphbinary_type_name = "janusgraph.RelationIdentifier"
    python_type = RelationIdentifier

    long_marker = 0
    string_marker = 1

    @classmethod
    def dictify(cls, obj, writer, to_extend, as_value=False, nullable=True):
        """
        Method to serialize JanusGraph-specific RelationIdentifier
        """
        cls.prefix_bytes_custom_type(writer, to_extend, as_value)

        # serialize out vertex ID
        if isinstance(obj.out_vertex_id, int):
            to_extend += uint8_pack(cls.long_marker)
            to_extend += uint64_pack(obj.out_vertex_id)
        else:
            to_extend += uint8_pack(cls.string_marker)
            cls._write_string(obj.out_vertex_id, writer, to_extend)

        # serialize edge type ID and relation ID
        to_extend += uint64_pack(obj.type_id)
        to_extend += uint64_pack(obj.relation_id)

        # serialize in vertex ID
        if obj.in_vertex_id is None:
            to_extend += uint8_pack(cls.long_marker)
            to_extend += uint64_pack(0)
        elif isinstance(obj.in_vertex_id, int):
            to_extend += uint8_pack(cls.long_marker)
            to_extend += uint64_pack(obj.in_vertex_id)
        else:
            to_extend += uint8_pack(cls.string_marker)
            cls._write_string(obj.in_vertex_id, writer, to_extend)

        return to_extend

    @classmethod
    def objectify(cls, b, r):
        """
        Method to deserialize JanusGraph-specific RelationIdentifier
        """
        if uint8_unpack(b.read(1)) != DataType.custom.value:
            raise Exception("Unexpected type while deserializing JanusGraph RelationIdentifier")

        # read the next byte that shows if the out vertex id is string or long
        out_vertex_id_marker = uint8_unpack(b.read(1))

        # deserialize out vertex ID
        if out_vertex_id_marker == cls.string_marker:
            out_vertex_id = cls._read_string(b)
        else:
            out_vertex_id = uint64_unpack(b.read(8))

        # deserialize edge type ID and relation ID
        type_id = uint64_unpack(b.read(8))
        relation_id = uint64_unpack(b.read(8))

        # deserialize in vertex ID
        in_vertex_id_marker = uint8_unpack(b.read(1))
        if in_vertex_id_marker == cls.string_marker:
            in_vertex_id = cls._read_string(b)
        else:
            in_vertex_id = uint64_unpack(b.read(8))
            if in_vertex_id == 0:
                in_vertex_id = None

        return RelationIdentifier.from_ids(out_vertex_id, type_id, relation_id, in_vertex_id)
    
    @classmethod
    def _read_string(cls, buff):
        """
        Helper method to read a string represented as byte array.
        The length of the string is not known upfront so the byte
        array needs to be red until a byte occurs that is marked
        with a special end marker
        """
        final_string = ""
        while True:
            c = 0xFF & uint8_unpack(buff.read(1))
            final_string += chr(c & 0x7F)

            # check if the character is marked with end marker
            # if yes that is the end of the string
            if c & 0x80 > 0:
                break

        return final_string
    
    @classmethod
    def _write_string(cls, string, writer, to_extend):
        """
        Helper method to create a byte array from a string and
        mark the string's last character with special end marker
        """
        b = bytearray()
        b.extend(map(ord, string))

        # add end marker to the last character
        b[-1] |= 0x80

        to_extend += b

# register the JanusGraph-specific RelationIdentifier as deserializer
JanusGraphBinaryTypeIO.register_deserializer(JanusGraphRelationIdentifierIO)