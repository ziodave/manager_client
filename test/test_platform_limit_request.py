# coding: utf-8

"""
    Manager

    Subscription management and related services.

    The version of the OpenAPI document: 1.0
    Contact: hello@wordlift.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from manager_client.models.platform_limit_request import PlatformLimitRequest

class TestPlatformLimitRequest(unittest.TestCase):
    """PlatformLimitRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlatformLimitRequest:
        """Test PlatformLimitRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlatformLimitRequest`
        """
        model = PlatformLimitRequest()
        if include_optional:
            return PlatformLimitRequest(
                applies_to = '',
                based_on = 'SKU',
                based_on_value = '',
                description = '',
                limits = 1,
                scope = 'ACCOUNT'
            )
        else:
            return PlatformLimitRequest(
                applies_to = '',
                based_on = 'SKU',
                based_on_value = '',
                limits = 1,
                scope = 'ACCOUNT',
        )
        """

    def testPlatformLimitRequest(self):
        """Test PlatformLimitRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
