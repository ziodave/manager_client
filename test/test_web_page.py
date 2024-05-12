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

from manager_client.models.web_page import WebPage

class TestWebPage(unittest.TestCase):
    """WebPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebPage:
        """Test WebPage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebPage`
        """
        model = WebPage()
        if include_optional:
            return WebPage(
                abstract = '',
                date_published = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                headline = '',
                image = '',
                text = '',
                types = [
                    ''
                    ],
                url = ''
            )
        else:
            return WebPage(
        )
        """

    def testWebPage(self):
        """Test WebPage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
