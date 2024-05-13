#!/usr/bin/env python3
"""
utils.access_nested_map function
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit tests for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test access_nested_map function with various inputs.

        Args:
            nested_map: The nested dictionary to be accessed.
            path: Tuple representing the path to the desired value.
            expected_result: The expected value retrieved from the nested_map.

        Returns:
            None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in nested map"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in nested map")
    ])
    def test_access_nested_map_exception(
            self,
            nested_map,
            path,
            expected_exception_message
            ):
        """
        Test access_nested_map function raises KeyError for invalid paths.

        Args:
            nested_map: The nested dictionary to be accessed.
            path: Tuple representing the path to the desired value.
            expected_exception_message: The expected error message
            for the raised exception.

        Returns:
            None
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_exception_message)


class TestGetJson(unittest.TestCase):
    """
    Unit tests for the get_json function.
    """

    @patch('utils.requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test get_json function with mocked requests.get.

        Args:
            test_url: The URL to be passed to get_json.
            test_payload: The expected payload to be returned.
            mock_get: Mock object for requests.get.

        Returns:
            None
        """
        # Create a Mock object for the response
        response_mock = Mock()
        response_mock.json.return_value = test_payload
        mock_get.return_value = response_mock

        # Call the get_json function
        result = get_json(test_url)

        # Assert that requests.get was called once with the test_url
        mock_get.assert_called_once_with(test_url)

        # Assert that the result matches the expected payload
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Unit tests for the memoize decorator.
    """

    class TestClass:
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        """
        Test that the memoize decorator caches the result of a method.

        Args:
            mock_a_method: Mock object for a_method.

        Returns:
            None
        """
        # Create an instance of TestClass
        test_instance = self.TestClass()

        # Call a_property twice
        result1 = test_instance.a_property()
        result2 = test_instance.a_property()

        # Assert that a_method was called only once
        mock_a_method.assert_called_once()

        # Assert that the results are the same
        self.assertEqual(result1, result2)


if __name__ == "__main__":
    unittest.main()
