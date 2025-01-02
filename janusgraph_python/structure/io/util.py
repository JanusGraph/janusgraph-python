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

class LongEncoding(object):
    """
    Utility class for encoding longs in strings, re-implemented from its Java equivalent.
    JanusGraph encodes long IDs in the RelationIdentifier as strings.
    """
    
    # The symbols used for the encoding.
    BASE_SYMBOLS = "0123456789abcdefghijklmnopqrstuvwxyz"
    NR_SYMBOLS = len(BASE_SYMBOLS)
    
    # Encoding used to indicate that an id is a string.
    STRING_ENCODING_MARKER = 'S'
    
    @staticmethod
    def decode(s):
        """
        Decodes a string back into a long.

        :param s: string, The string to decode.
        :return The decoded long value.

        exception: Thrown if the string contains any invalid characters. Only base_symbols are allowed.
        """
        num = 0

        for ch in s:
            num *= LongEncoding.NR_SYMBOLS

            pos = LongEncoding.BASE_SYMBOLS.find(ch)

            if pos < 0:
                raise ValueError(f"Symbol {ch} not allowed, only these symbols are: {LongEncoding.BASE_SYMBOLS}")

            num += pos

        return num
    
    @staticmethod
    def encode(num):
        """
        Encodes a long value as a string

        :param num: long, The long value to encode.
        :return The encoded string value.
        """
        
        char_list = []

        while num != 0:
            char_list.append(LongEncoding.BASE_SYMBOLS[int(num % LongEncoding.NR_SYMBOLS)])
            num //= LongEncoding.NR_SYMBOLS

        char_list.reverse()

        return ''.join(char_list)