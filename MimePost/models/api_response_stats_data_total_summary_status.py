# coding: utf-8

"""
    MimePost API Reference (Beta)

    MimePost API for sending email.  You can find out more about MimePost at [https://mimepost.com](http://mimepost.com). For this sample, you can use the api key `special-key` to test the authorization     filters.  # noqa: E501

    OpenAPI spec version: 0.1.0
    Contact: support@mimepost.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ApiResponseStatsDataTotalSummaryStatus(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'count': 'int',
        'perc': 'str'
    }

    attribute_map = {
        'count': 'count',
        'perc': 'perc'
    }

    def __init__(self, count=None, perc=None):  # noqa: E501
        """ApiResponseStatsDataTotalSummaryStatus - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._perc = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if perc is not None:
            self.perc = perc

    @property
    def count(self):
        """Gets the count of this ApiResponseStatsDataTotalSummaryStatus.  # noqa: E501


        :return: The count of this ApiResponseStatsDataTotalSummaryStatus.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ApiResponseStatsDataTotalSummaryStatus.


        :param count: The count of this ApiResponseStatsDataTotalSummaryStatus.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def perc(self):
        """Gets the perc of this ApiResponseStatsDataTotalSummaryStatus.  # noqa: E501


        :return: The perc of this ApiResponseStatsDataTotalSummaryStatus.  # noqa: E501
        :rtype: str
        """
        return self._perc

    @perc.setter
    def perc(self, perc):
        """Sets the perc of this ApiResponseStatsDataTotalSummaryStatus.


        :param perc: The perc of this ApiResponseStatsDataTotalSummaryStatus.  # noqa: E501
        :type: str
        """

        self._perc = perc

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ApiResponseStatsDataTotalSummaryStatus, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiResponseStatsDataTotalSummaryStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
