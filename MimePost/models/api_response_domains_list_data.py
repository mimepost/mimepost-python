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


class ApiResponseDomainsListData(object):
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
        'id': 'int',
        'domain': 'str',
        'selector': 'str',
        'instance_name': 'str',
        'spf_verified': 'int',
        'dkim_verified': 'int',
        'tracking_verified': 'int',
        'verified': 'int',
        'approved': 'int',
        'status': 'str',
        'status_desc': 'str',
        'entered': 'str',
        'active': 'int'
    }

    attribute_map = {
        'id': 'id',
        'domain': 'domain',
        'selector': 'selector',
        'instance_name': 'instance_name',
        'spf_verified': 'spf_verified',
        'dkim_verified': 'dkim_verified',
        'tracking_verified': 'tracking_verified',
        'verified': 'verified',
        'approved': 'approved',
        'status': 'status',
        'status_desc': 'status_desc',
        'entered': 'entered',
        'active': 'active'
    }

    def __init__(self, id=None, domain=None, selector=None, instance_name=None, spf_verified=None, dkim_verified=None, tracking_verified=None, verified=None, approved=None, status=None, status_desc=None, entered=None, active=None):  # noqa: E501
        """ApiResponseDomainsListData - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._domain = None
        self._selector = None
        self._instance_name = None
        self._spf_verified = None
        self._dkim_verified = None
        self._tracking_verified = None
        self._verified = None
        self._approved = None
        self._status = None
        self._status_desc = None
        self._entered = None
        self._active = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if domain is not None:
            self.domain = domain
        if selector is not None:
            self.selector = selector
        if instance_name is not None:
            self.instance_name = instance_name
        if spf_verified is not None:
            self.spf_verified = spf_verified
        if dkim_verified is not None:
            self.dkim_verified = dkim_verified
        if tracking_verified is not None:
            self.tracking_verified = tracking_verified
        if verified is not None:
            self.verified = verified
        if approved is not None:
            self.approved = approved
        if status is not None:
            self.status = status
        if status_desc is not None:
            self.status_desc = status_desc
        if entered is not None:
            self.entered = entered
        if active is not None:
            self.active = active

    @property
    def id(self):
        """Gets the id of this ApiResponseDomainsListData.  # noqa: E501


        :return: The id of this ApiResponseDomainsListData.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiResponseDomainsListData.


        :param id: The id of this ApiResponseDomainsListData.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def domain(self):
        """Gets the domain of this ApiResponseDomainsListData.  # noqa: E501


        :return: The domain of this ApiResponseDomainsListData.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ApiResponseDomainsListData.


        :param domain: The domain of this ApiResponseDomainsListData.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def selector(self):
        """Gets the selector of this ApiResponseDomainsListData.  # noqa: E501


        :return: The selector of this ApiResponseDomainsListData.  # noqa: E501
        :rtype: str
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this ApiResponseDomainsListData.


        :param selector: The selector of this ApiResponseDomainsListData.  # noqa: E501
        :type: str
        """

        self._selector = selector

    @property
    def instance_name(self):
        """Gets the instance_name of this ApiResponseDomainsListData.  # noqa: E501


        :return: The instance_name of this ApiResponseDomainsListData.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this ApiResponseDomainsListData.


        :param instance_name: The instance_name of this ApiResponseDomainsListData.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def spf_verified(self):
        """Gets the spf_verified of this ApiResponseDomainsListData.  # noqa: E501


        :return: The spf_verified of this ApiResponseDomainsListData.  # noqa: E501
        :rtype: int
        """
        return self._spf_verified

    @spf_verified.setter
    def spf_verified(self, spf_verified):
        """Sets the spf_verified of this ApiResponseDomainsListData.


        :param spf_verified: The spf_verified of this ApiResponseDomainsListData.  # noqa: E501
        :type: int
        """

        self._spf_verified = spf_verified

    @property
    def dkim_verified(self):
        """Gets the dkim_verified of this ApiResponseDomainsListData.  # noqa: E501


        :return: The dkim_verified of this ApiResponseDomainsListData.  # noqa: E501
        :rtype: int
        """
        return self._dkim_verified

    @dkim_verified.setter
    def dkim_verified(self, dkim_verified):
        """Sets the dkim_verified of this ApiResponseDomainsListData.


        :param dkim_verified: The dkim_verified of this ApiResponseDomainsListData.  # noqa: E501
        :type: int
        """

        self._dkim_verified = dkim_verified

    @property
    def tracking_verified(self):
        """Gets the tracking_verified of this ApiResponseDomainsListData.  # noqa: E501


        :return: The tracking_verified of this ApiResponseDomainsListData.  # noqa: E501
        :rtype: int
        """
        return self._tracking_verified

    @tracking_verified.setter
    def tracking_verified(self, tracking_verified):
        """Sets the tracking_verified of this ApiResponseDomainsListData.


        :param tracking_verified: The tracking_verified of this ApiResponseDomainsListData.  # noqa: E501
        :type: int
        """

        self._tracking_verified = tracking_verified

    @property
    def verified(self):
        """Gets the verified of this ApiResponseDomainsListData.  # noqa: E501


        :return: The verified of this ApiResponseDomainsListData.  # noqa: E501
        :rtype: int
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this ApiResponseDomainsListData.


        :param verified: The verified of this ApiResponseDomainsListData.  # noqa: E501
        :type: int
        """

        self._verified = verified

    @property
    def approved(self):
        """Gets the approved of this ApiResponseDomainsListData.  # noqa: E501


        :return: The approved of this ApiResponseDomainsListData.  # noqa: E501
        :rtype: int
        """
        return self._approved

    @approved.setter
    def approved(self, approved):
        """Sets the approved of this ApiResponseDomainsListData.


        :param approved: The approved of this ApiResponseDomainsListData.  # noqa: E501
        :type: int
        """

        self._approved = approved

    @property
    def status(self):
        """Gets the status of this ApiResponseDomainsListData.  # noqa: E501


        :return: The status of this ApiResponseDomainsListData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApiResponseDomainsListData.


        :param status: The status of this ApiResponseDomainsListData.  # noqa: E501
        :type: str
        """
        allowed_values = ["WAITING_APPROVA", "NOT_VERIFIED", "APPROVED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def status_desc(self):
        """Gets the status_desc of this ApiResponseDomainsListData.  # noqa: E501


        :return: The status_desc of this ApiResponseDomainsListData.  # noqa: E501
        :rtype: str
        """
        return self._status_desc

    @status_desc.setter
    def status_desc(self, status_desc):
        """Sets the status_desc of this ApiResponseDomainsListData.


        :param status_desc: The status_desc of this ApiResponseDomainsListData.  # noqa: E501
        :type: str
        """

        self._status_desc = status_desc

    @property
    def entered(self):
        """Gets the entered of this ApiResponseDomainsListData.  # noqa: E501


        :return: The entered of this ApiResponseDomainsListData.  # noqa: E501
        :rtype: str
        """
        return self._entered

    @entered.setter
    def entered(self, entered):
        """Sets the entered of this ApiResponseDomainsListData.


        :param entered: The entered of this ApiResponseDomainsListData.  # noqa: E501
        :type: str
        """

        self._entered = entered

    @property
    def active(self):
        """Gets the active of this ApiResponseDomainsListData.  # noqa: E501


        :return: The active of this ApiResponseDomainsListData.  # noqa: E501
        :rtype: int
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this ApiResponseDomainsListData.


        :param active: The active of this ApiResponseDomainsListData.  # noqa: E501
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
        if issubclass(ApiResponseDomainsListData, dict):
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
        if not isinstance(other, ApiResponseDomainsListData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
