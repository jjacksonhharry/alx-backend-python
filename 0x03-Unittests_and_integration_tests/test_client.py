#!/usr/bin/env python3
"""
Module for testing the client module.
"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)
from typing import Dict
from requests import HTTPError
from fixtures import TEST_PAYLOAD
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """_summary_

    Args:
            unittest (_type_): _description_
    """
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        """

        # Set up the mock response
        expected_result = {"org_name": org_name}
        mock_get_json.return_value = expected_result

        # Instantiate GithubOrgClient with the specified org_name
        github_org_client = GithubOrgClient(org_name)

        # Call the org method
        result = github_org_client.org

        # Assert that get_json is called once with the expected argument
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)

        # Assert that the result is correct
        self.assertEqual(result, expected_result)

    def test_public_repos_url(self) -> None:
        """
        Test GithubOrgClient._public_repos_url method.
        """
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock,
        ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )
