#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch, Mock
import utils


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({}, ("a",), KeyError, "Key 'a' not found in the nested map"),
        ({"a": 1}, ("a", "b"), KeyError, "Key 'b' not found in the nested map"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception, expected_message):
        with self.assertRaises(expected_exception, msg=expected_message):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):

    @patch('your_module.utils.requests.get')
    def test_get_json(self, mock_requests_get):
        # Test data
        test_data = [
            {"test_url": "http://example.com", "test_payload": {"payload": True}},
            {"test_url": "http://holberton.io", "test_payload": {"payload": False}},
        ]

        for data in test_data:
            with self.subTest(data=data):
                # Set up the mock response
                mock_response = Mock()
                mock_response.json.return_value = data['test_payload']
                mock_requests_get.return_value = mock_response

                # Call the function with the test data
                result = utils.get_json(data['test_url'])

                # Assert that the mocked get method was called exactly once with test_url as argument
                mock_requests_get.assert_called_once_with(data['test_url'])

                # Assert that the output of get_json is equal to test_payload
                self.assertEqual(result, data['test_payload'])

                # Reset the mock for the next iteration
                mock_requests_get.reset_mock()


if __name__ == '__main__':
    unittest.main()
