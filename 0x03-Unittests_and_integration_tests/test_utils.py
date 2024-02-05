#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({}, ("a",), KeyError, "Key 'a' not found in nested map"),
        ({"a": 1}, ("a", "b"), KeyError, "Key 'b' not found in nested map"),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map,
            path,
            expected_exception,
            expected_message):
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_message)
