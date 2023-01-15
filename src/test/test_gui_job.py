#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""© Ihor Mirzov, 2019-2023
Distributed under GNU General Public License v3.0

Test for src/gui/job.py - test some Job methods.
"""

# Standard modules
import os
import sys
import unittest

# My modules
sys_path = os.path.abspath(__file__)
sys_path = os.path.dirname(sys_path)
sys_path = os.path.join(sys_path, '..')
sys_path = os.path.normpath(sys_path)
sys_path = os.path.realpath(sys_path)
if sys_path not in sys.path:
    sys.path.insert(0, sys_path)
from gui.job import j


class Test(unittest.TestCase):

    def test_open_inp(self):
        j.generate()
        p = j.open_inp()
        self.assertTrue(p is not None)
        p.kill()

    def test_convert_unv(self):
        j.generate()
        j.convert_unv()

    def test_export_vtu(self):
        j.generate()
        j.export_vtu()


if __name__ == '__main__':
    unittest.main()
