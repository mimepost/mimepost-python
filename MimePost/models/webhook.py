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


class Webhook(object):
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
        'desc': 'str',
        'url': 'str',
        'events': 'list[str]',
        'active': 'int'
    }

    attribute_map = {
        'desc': 'desc',
        'url': 'url',
        'events': 'events',
        'active': 'active'
    }

    def __init__(self, desc=None, url=None, events=None, active=None):  # noqa: E501
        """Webhook - a model defined in Swagger"""  # noqa: E501

        self._desc = None
        self._url = None
        self._events = None
        self._active = None
        self.discriminator = None

        self.desc = desc
        self.url = url
        if events is not None:
            self.events = events
        if active is not None:
            self.active = active

    @property
    def desc(self):
        """Gets the desc of this Webhook.  # noqa: E501


        :return: The desc of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this Webhook.


        :param desc: The desc of this Webhook.  # noqa: E501
        :type: str
        """
        if desc is None:
            raise ValueError("Invalid value for `desc`, must not be `None`")  # noqa: E501

        self._desc = desc

    @property
    def url(self):
        """Gets the url of this Webhook.  # noqa: E501


        :return: The url of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Webhook.


        :param url: The url of this Webhook.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def events(self):
        """Gets the events of this Webhook.  # noqa: E501


        :return: The events of this Webhook.  # noqa: E501
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this Webhook.


        :param events: The events of this Webhook.  # noqa: E501
        :type: list[str]
        """

        self._events = events

    @property
    def active(self):
        """Gets the active of this Webhook.  # noqa: E501


        :return: The active of this Webhook.  # noqa: E501
        :rtype: int
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Webhook.


        :param active: The active of this Webhook.  # noqa: E501
        :type: int
        """

        self._active = active

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
        if issubclass(Webhook, dict):
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
        if not isinstance(other, Webhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other