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

from manager_client.models.page_merchant_sync import PageMerchantSync

class TestPageMerchantSync(unittest.TestCase):
    """PageMerchantSync unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageMerchantSync:
        """Test PageMerchantSync
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageMerchantSync`
        """
        model = PageMerchantSync()
        if include_optional:
            return PageMerchantSync(
                first = '',
                items = [
                    manager_client.models.merchant_sync.MerchantSync(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        has_errors = True, 
                        id = 56, 
                        merchant_id = 56, 
                        modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        products_created = 56, 
                        products_deleted = 56, 
                        products_errored = 56, 
                        products_skipped = 56, 
                        products_total = 56, 
                        products_updated = 56, 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        stopped_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                last = '',
                next = '',
                prev = '',
                var_self = ''
            )
        else:
            return PageMerchantSync(
                first = '',
                items = [
                    manager_client.models.merchant_sync.MerchantSync(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        has_errors = True, 
                        id = 56, 
                        merchant_id = 56, 
                        modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        products_created = 56, 
                        products_deleted = 56, 
                        products_errored = 56, 
                        products_skipped = 56, 
                        products_total = 56, 
                        products_updated = 56, 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        stopped_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                last = '',
                next = '',
                prev = '',
                var_self = '',
        )
        """

    def testPageMerchantSync(self):
        """Test PageMerchantSync"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()