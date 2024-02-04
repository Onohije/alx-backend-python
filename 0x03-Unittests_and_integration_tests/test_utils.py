#!/usr/bin/env python3
"""Utils unit tests"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json,
    memoize
)
from typing import (
    Mapping,
    Any,
    Sequence,
    Dict,
    Callable
)


class TestAccessNestedMap(unittest.TestCase):
    """Test Cases for Access Nested Map Function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence,
                               expected: Any):
        """Tests access_nested_map return expected Values"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence):
        """Tests access_nested_map raisees Exception"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        # self.assertEqual(str(context.exception), "")


class TestGetJson(unittest.TestCase):
    """Unittest Test Case for utils.get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict):
        """Tests get_json return expected Values"""
        with patch('requests.get',
                   return_value=Mock(json=lambda: test_payload))\
                as r_get:
            self.assertEqual(get_json(test_url), test_payload)
            r_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Unittest Test Case for utils.memoize"""

    def test_memoize(self):
        """Test memoize works using TestClass Mock"""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as a_memo:
            test = TestClass()
            self.assertEqual(test.a_property, 42)
            self.assertEqual(test.a_property, 42)
        a_memo.assert_called_once()


if __name__ == '__main__':
    unittest.main()
