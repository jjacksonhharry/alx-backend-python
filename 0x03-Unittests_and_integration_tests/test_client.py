#!/usr/bin/env python3
"""
method should test that GithubOrgClient.org returns the correct value
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Unit tests for the GithubOrgClient class.
    """

    @patch('client.get_json')
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.

        Args:
            org_name: Name of the organization.
            mock_get_json: Mock object for get_json.

        Returns:
            None
        """
        # Instantiate GithubOrgClient with the org name
        client = GithubOrgClient(org_name)

        # Call the org method
        client.org()

        # Assert that get_json was called once with the correct argument
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}"
                )

    def test_public_repos_url(self):
        """
        Test GithubOrgClient._public_repos_url method.

        Returns:
            None
        """
        # Define a known payload for the org property
        payload = {'repos_url': 'https://api.github.com/orgs/google/repos'}

        # Patch the org property to return the known payload
        with patch.object(
                GithubOrgClient,
                'org',
                new_callable=PropertyMock(return_value=payload)
                ):
            # Instantiate GithubOrgClient
            client = GithubOrgClient("google")

        # Call the _public_repos_url method
        result = client._public_repos_url

        # Assert that the result is the expected repos_url
        self.assertEqual(result, 'https://api.github.com/orgs/google/repos')

    @patch('client.get_json')
    @patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock(
                return_value='https://api.github.com/orgs/google/repos'
                ))
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """
        Test GithubOrgClient.public_repos method.

        Args:
            mock_public_repos_url: Mock object for _public_repos_url property.
            mock_get_json: Mock object for get_json function.

        Returns:
            None
        """
        # Define a payload for the mocked get_json function
        payload = [{'name': 'repo1'}, {'name': 'repo2'}]

        # Patch get_json to return the known payload
        mock_get_json.return_value = payload

        # Instantiate GithubOrgClient
        client = GithubOrgClient("google")

        # Call the public_repos method
        result = client.public_repos()

        # Assert that get_json was called once with the correct argument
        mock_get_json.assert_called_once_with(
                'https://api.github.com/orgs/google/repos'
                )

        # Assert that the mocked property was accessed once
        mock_public_repos_url.assert_called_once()

        # Assert that the result is the expected list of repos
        self.assertEqual(result, [{'name': 'repo1'}, {'name': 'repo2'}])

        @patch('client.GithubOrgClient.get_json')
    def test_has_license(self, mock_get_json):
        """
        Test GithubOrgClient.has_license method.

        Args:
            mock_get_json: Mock object for get_json method.

        Returns:
            None
        """
        # Define test inputs and expected outputs
        test_inputs = [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False)
        ]

        # Patch get_json to return the known payload for each input
        for repo, license_key, expected_result in test_inputs:
            mock_get_json.return_value = repo

            # Instantiate GithubOrgClient
            client = GithubOrgClient("google")

            # Call the has_license method
            result = client.has_license(
                    repo_name="repo",
                    license_key=license_key
                    )

            # Assert that get_json was called once with the correct argument
            mock_get_json.assert_called_once_with(
                    'https://api.github.com/repos/google/repo'
                    )

            # Assert that the result matches the expected value
            self.assertEqual(result, expected_result)

            # Reset the mock for the next iteration
            mock_get_json.reset_mock()


@parameterized_class((
    'org_payload',
    'repos_payload',
    'expected_repos',
    'apache2_repos'
    ), [
    (org_payload, :repos_payload, expected_repos, apache2_repos)
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for the GithubOrgClient class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method to mock requests.get.

        Returns:
            None
        """
        # Start a patcher named get_patcher
        cls.get_patcher = patch('client.requests.get')

        # Start the patcher and use side_effect to return the correct fixture
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = [cls.org_payload, cls.repos_payload]

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method to stop the patcher.

        Returns:
            None
        """
        # Stop the patcher
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test GithubOrgClient.public_repos method.

        Returns:
            None
        """
        # Instantiate GithubOrgClient
        client = GithubOrgClient("google")

        # Call the public_repos method
        result = client.public_repos()

        # Assert that the result matches the expected repos
        self.assertEqual(result, self.expected_repos)

        # Additional test for repos with Apache License 2.0
        apache2_repos_result = client.public_repos("apache2")
        self.assertEqual(apache2_repos_result, self.apache2_repos)


@parameterized_class((
    'org_payload',
    'repos_payload',
    'expected_repos',
    'apache2_repos'
    ), [
    (org_payload, repos_payload, expected_repos, apache2_repos)
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for the GithubOrgClient class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method to mock requests.get.

        Returns:
            None
        """
        # Start a patcher named get_patcher
        cls.get_patcher = patch('client.requests.get')

        # Start the patcher and use side_effect to return the correct fixture
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = [cls.org_payload, cls.repos_payload]

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method to stop the patcher.

        Returns:
            None
        """
        # Stop the patcher
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test GithubOrgClient.public_repos method.

        Returns:
            None
        """
        # Instantiate GithubOrgClient
        client = GithubOrgClient("google")

        # Call the public_repos method
        result = client.public_repos()

        # Assert that the result matches the expected repos
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test GithubOrgClient.public_repos method with license parameter.

        Returns:
            None
        """
        # Instantiate GithubOrgClient
        client = GithubOrgClient("google")

        # Call the public_repos method with license parameter
        result = client.public_repos(license="apache-2.0")

        # Assert that the result matches the expected repos
        self.assertEqual(result, self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
