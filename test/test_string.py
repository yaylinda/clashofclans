# coding: utf-8

"""
    Clash of Clans API

    Check out <a href=\"https://developer.clashofclans.com/#/getting-started\" target=\"_parent\">Getting Started</a> for instructions and links to other resources. Clash of Clans API uses <a href=\"https://jwt.io/\" target=\"_blank\">JSON Web Tokens</a> for authorizing the requests. Tokens are created by developers on <a href=\"https://developer.clashofclans.com/#/account\" target=\"_parent\">My Account</a> page and must be passed in every API request in Authorization HTTP header using Bearer authentication scheme. Correct Authorization header looks like this: \"Authorization: Bearer API_TOKEN\".   # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.string import String  # noqa: E501
from swagger_client.rest import ApiException


class TestString(unittest.TestCase):
    """String unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testString(self):
        """Test String"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.string.String()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
