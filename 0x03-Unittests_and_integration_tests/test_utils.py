#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError)
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_output):
        with self.assertRaises(expected_output) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    @parameterized.expand(
        [
            ('http://example.com', {'payload': True}),
            ('http://holberton.io', {'payload': False})
        ]
    )
    def test_get_json(self, url, expected_output):
        mock_response = Mock()
        mock_response.json.return_value = expected_output
        with patch('requests.get', return_value=mock_response):
            response = get_json(url)

            self.assertEqual(response, expected_output)


class TestClass:

    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()


class TestMemoize(unittest.TestCase):

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        test_instance = TestClass()

        # First call to a_property
        result_1 = test_instance.a_property()

        # Second call to a_property
        result_2 = test_instance.a_property()

        # Assert that a_method was only called once
        mock_a_method.assert_called_once()

        # Assert that the results are correct
        self.assertEqual(result_1, 42)
        self.assertEqual(result_2, 42)
        self.assertEqual(result_1, result_2)
