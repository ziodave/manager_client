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

from manager_client.models.platform_limit import PlatformLimit

class TestPlatformLimit(unittest.TestCase):
    """PlatformLimit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlatformLimit:
        """Test PlatformLimit
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlatformLimit`
        """
        model = PlatformLimit()
        if include_optional:
            return PlatformLimit(
                applies_to = '',
                based_on = 'SKU',
                based_on_value = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                description = '',
                id = 56,
                limits = 1,
                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                scope = 'ACCOUNT'
            )
        else:
            return PlatformLimit(
                applies_to = '',
                based_on = 'SKU',
                based_on_value = '',
                limits = 1,
                scope = 'ACCOUNT',
        )
        """

    def testPlatformLimit(self):
        """Test PlatformLimit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
