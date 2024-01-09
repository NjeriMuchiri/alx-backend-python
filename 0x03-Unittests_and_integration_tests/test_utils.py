#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map


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


if __name__ == '__main__':
    unittest.main()
