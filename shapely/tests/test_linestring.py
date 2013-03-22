# Copyright (c) 2013, Lars Butler
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of Lars Butler nor the names of
#      its contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import unittest

from shapely.geometry import LineString
from shapely import wkt


class LineStringTestCase(unittest.TestCase):

    def test_linestring_wkt_2d(self):
        ls = LineString([(1, 2), (3, 4), (5, 6)])
        expected_wkt = (
            'LINESTRING (1.0000000000000000 2.0000000000000000, '
            '3.0000000000000000 4.0000000000000000, '
            '5.0000000000000000 6.0000000000000000)'
        )
        self.assertEqual(expected_wkt, ls.wkt)
        self.assertEqual(expected_wkt, wkt.dumps(ls))
        self.assertTrue(ls.equals(wkt.loads(expected_wkt)))

    def test_linearring_wkt_2d(self):
        ls = LineString([(0, 0), (2, 3), (3, 2), (0, 0)])
        expected_wkt = (
            'LINEARRING (0.0000000000000000 0.0000000000000000, '
            '2.0000000000000000 3.0000000000000000, '
            '3.0000000000000000 2.0000000000000000, '
            '0.0000000000000000 0.0000000000000000)'
        )
        self.assertEqual(expected_wkt, ls.wkt)
        self.assertEqual(expected_wkt, wkt.dumps(ls))
        self.assertTrue(ls.equals(wkt.loads(expected_wkt)))

    def test_linestring_wkt_3d(self):
        ls = LineString([(1, 2, 10), (3, 4, 11), (5, 6, 12)])
        expected_wkt = (
            'LINESTRING ('
            '1.0000000000000000 2.0000000000000000 10.0000000000000000, '
            '3.0000000000000000 4.0000000000000000 11.0000000000000000, '
            '5.0000000000000000 6.0000000000000000 12.0000000000000000)'
        )
        self.assertEqual(expected_wkt, ls.wkt)
        self.assertEqual(expected_wkt, wkt.dumps(ls))
        self.assertTrue(ls.equals(wkt.loads(expected_wkt)))

    def test_linearring_wkt_3d(self):
        ls = LineString([(0, 0, 10), (2, 3, 11), (3, 2, 12), (0, 0, 10)])
        expected_wkt = (
            'LINEARRING ('
            '0.0000000000000000 0.0000000000000000 10.0000000000000000, '
            '2.0000000000000000 3.0000000000000000 11.0000000000000000, '
            '3.0000000000000000 2.0000000000000000 12.0000000000000000, '
            '0.0000000000000000 0.0000000000000000 10.0000000000000000)'
        )
        self.assertEqual(expected_wkt, ls.wkt)
        self.assertEqual(expected_wkt, wkt.dumps(ls))
        self.assertTrue(ls.equals(wkt.loads(expected_wkt)))


def test_suite():
    return unittest.TestLoader().loadTestsFromTestCase(LineStringTestCase)
