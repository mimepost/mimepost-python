# coding: utf-8

"""
    MimePost API Reference (Beta)

    MimePost API for sending email.  You can find out more about MimePost at [https://mimepost.com](http://mimepost.com). For this sample, you can use the api key `special-key` to test the authorization     filters.  # noqa: E501

    OpenAPI spec version: 0.1.0
    Contact: support@mimepost.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import MimePost
from MimePost.api.emails_api import EmailsApi  # noqa: E501
from MimePost.rest import ApiException


class TestEmailsApi(unittest.TestCase):
    """EmailsApi unit test stubs"""

    def setUp(self):
        self.api = MimePost.api.emails_api.EmailsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_send_email(self):
        """Test case for send_email

        Send email  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
