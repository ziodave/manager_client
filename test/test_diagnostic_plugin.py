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

from manager_client.models.diagnostic_plugin import DiagnosticPlugin

class TestDiagnosticPlugin(unittest.TestCase):
    """DiagnosticPlugin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiagnosticPlugin:
        """Test DiagnosticPlugin
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiagnosticPlugin`
        """
        model = DiagnosticPlugin()
        if include_optional:
            return DiagnosticPlugin(
                account_id = 56,
                active = True,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = 56,
                name = '',
                version = ''
            )
        else:
            return DiagnosticPlugin(
        )
        """

    def testDiagnosticPlugin(self):
        """Test DiagnosticPlugin"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
