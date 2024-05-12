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

from manager_client.models.embedding_request import EmbeddingRequest

class TestEmbeddingRequest(unittest.TestCase):
    """EmbeddingRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EmbeddingRequest:
        """Test EmbeddingRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EmbeddingRequest`
        """
        model = EmbeddingRequest()
        if include_optional:
            return EmbeddingRequest(
                graphql_query = '',
                properties = [
                    ''
                    ]
            )
        else:
            return EmbeddingRequest(
        )
        """

    def testEmbeddingRequest(self):
        """Test EmbeddingRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
