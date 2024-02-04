#!/usr/bin/env python3
"""Unittest for Client Module"""

from client import GithubOrgClient
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock, Mock
from fixtures import TEST_PAYLOAD
from typing import Callable, Dict


class TestGithubOrgClient(unittest.TestCase):
    """Test Caseses for client.GithubOrgClient"""

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    def test_org(self, name: str):
        """Tests client.GithubOrgClient works correctly with get_json"""
        with patch('client.get_json', return_value=None) as p_get_json:
            org = GithubOrgClient(name)
            org.org
            url = 'https://api.github.com/orgs/{name}'
            p_get_json.assert_called_once_with(url.format(name=name))

    def test_public_repos_url(self):
        """Tests client.GithubOrgClient._public_repos_url"""
        resp = {'repos_url': 'https://api.github.com/orgs/Google/repos'}
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock, return_value=resp):
            org = GithubOrgClient('Google')
            self.assertEqual(org._public_repos_url, resp['repos_url'])

    @patch('client.get_json', return_value=TEST_PAYLOAD[0][1])
    def test_public_repos(self, p_get_json: Callable):
        """Tests client.GithubOrgClient.public_repos"""

        resp = {'repos_url': 'https://api.github.com/orgs/Google/repos'}
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock, return_value=resp)\
                as m_org:
            org = GithubOrgClient('Google')
            # self.assertEqual(org._public_repos_url, resp['repos_url'])
            self.assertEqual(org.public_repos(),
                             ['episodes.dart', 'cpp-netlib',
                              'dagger', 'ios-webkit-debug-proxy',
                              'google.github.io', 'kratu',
                              'build-debian-cloud', 'traceur-compiler',
                              'firmata.py'])
            m_org.assert_called_once()
            p_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict, license_key: str,
                         expected: bool):
        """Tests GithubOrgClient.has_license"""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integratiion Tests for GithubOrgClient"""

    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            raise Exception

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the class fixtures after running all tests."""
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """Tests the `public_repos` method."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a license."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )


if __name__ == '__main__':
    unittest.main()
