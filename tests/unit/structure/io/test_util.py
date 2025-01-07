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

from pytest import mark, param, raises
from sys import maxsize
from janusgraph_python.structure.io.util import LongEncoding

class TestLongEncoding(object):

    @mark.parametrize(
        'to_encode',
        [
            param(0, id='Zero'),
            param(1, id='One'),
            param(1234567890, id='huge number'),
            param(maxsize, id='max sized number')
        ]
    )
    def test_encode_and_decode__valid_value__same_value(self, to_encode):
        encoded = LongEncoding.encode(to_encode)
        decoded = LongEncoding.decode(encoded)

        assert to_encode == decoded

    def test_decode_invalid_char(self):
        value_with_invalid_char = '33!'

        with raises(ValueError) as exception_info:
            LongEncoding.decode(value_with_invalid_char)

        assert str(exception_info.value) == 'Symbol ! not allowed, only these symbols are: 0123456789abcdefghijklmnopqrstuvwxyz'