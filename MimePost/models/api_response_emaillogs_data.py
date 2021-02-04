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


class ApiResponseEmaillogsData(object):
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
        '_datetime': 'str',
        'message_id': 'str',
        'to_email': 'str',
        'status': 'str',
        'details': 'str'
    }

    attribute_map = {
        '_datetime': 'datetime',
        'message_id': 'message_id',
        'to_email': 'to_email',
        'status': 'status',
        'details': 'details'
    }

    def __init__(self, _datetime=None, message_id=None, to_email=None, status=None, details=None):  # noqa: E501
        """ApiResponseEmaillogsData - a model defined in Swagger"""  # noqa: E501

        self.__datetime = None
        self._message_id = None
        self._to_email = None
        self._status = None
        self._details = None
        self.discriminator = None

        if _datetime is not None:
            self._datetime = _datetime
        if message_id is not None:
            self.message_id = message_id
        if to_email is not None:
            self.to_email = to_email
        if status is not None:
            self.status = status
        if details is not None:
            self.details = details

    @property
    def _datetime(self):
        """Gets the _datetime of this ApiResponseEmaillogsData.  # noqa: E501


        :return: The _datetime of this ApiResponseEmaillogsData.  # noqa: E501
        :rtype: str
        """
        return self.__datetime

    @_datetime.setter
    def _datetime(self, _datetime):
        """Sets the _datetime of this ApiResponseEmaillogsData.


        :param _datetime: The _datetime of this ApiResponseEmaillogsData.  # noqa: E501
        :type: str
        """

        self.__datetime = _datetime

    @property
    def message_id(self):
        """Gets the message_id of this ApiResponseEmaillogsData.  # noqa: E501


        :return: The message_id of this ApiResponseEmaillogsData.  # noqa: E501
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this ApiResponseEmaillogsData.


        :param message_id: The message_id of this ApiResponseEmaillogsData.  # noqa: E501
        :type: str
        """

        self._message_id = message_id

    @property
    def to_email(self):
        """Gets the to_email of this ApiResponseEmaillogsData.  # noqa: E501


        :return: The to_email of this ApiResponseEmaillogsData.  # noqa: E501
        :rtype: str
        """
        return self._to_email

    @to_email.setter
    def to_email(self, to_email):
        """Sets the to_email of this ApiResponseEmaillogsData.


        :param to_email: The to_email of this ApiResponseEmaillogsData.  # noqa: E501
        :type: str
        """

        self._to_email = to_email

    @property
    def status(self):
        """Gets the status of this ApiResponseEmaillogsData.  # noqa: E501


        :return: The status of this ApiResponseEmaillogsData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApiResponseEmaillogsData.


        :param status: The status of this ApiResponseEmaillogsData.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def details(self):
        """Gets the details of this ApiResponseEmaillogsData.  # noqa: E501


        :return: The details of this ApiResponseEmaillogsData.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this ApiResponseEmaillogsData.


        :param details: The details of this ApiResponseEmaillogsData.  # noqa: E501
        :type: str
        """

        self._details = details

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
        if issubclass(ApiResponseEmaillogsData, dict):
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
        if not isinstance(other, ApiResponseEmaillogsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
