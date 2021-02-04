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


class Email(object):
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
        'html': 'str',
        'subject': 'str',
        'from_email': 'str',
        'from_name': 'str',
        'global_merge_vars': 'list[EmailGlobalMergeVars]',
        'to': 'list[EmailTo]',
        'cc': 'list[str]',
        'bcc': 'list[str]',
        'attachments': 'list[EmailAttachments]',
        'vars': 'dict(str, str)'
    }

    attribute_map = {
        'html': 'html',
        'subject': 'subject',
        'from_email': 'from_email',
        'from_name': 'from_name',
        'global_merge_vars': 'global_merge_vars',
        'to': 'to',
        'cc': 'cc',
        'bcc': 'bcc',
        'attachments': 'attachments',
        'vars': 'vars'
    }

    def __init__(self, html=None, subject=None, from_email=None, from_name=None, global_merge_vars=None, to=None, cc=None, bcc=None, attachments=None, vars=None):  # noqa: E501
        """Email - a model defined in Swagger"""  # noqa: E501

        self._html = None
        self._subject = None
        self._from_email = None
        self._from_name = None
        self._global_merge_vars = None
        self._to = None
        self._cc = None
        self._bcc = None
        self._attachments = None
        self._vars = None
        self.discriminator = None

        self.html = html
        self.subject = subject
        self.from_email = from_email
        if from_name is not None:
            self.from_name = from_name
        if global_merge_vars is not None:
            self.global_merge_vars = global_merge_vars
        self.to = to
        if cc is not None:
            self.cc = cc
        if bcc is not None:
            self.bcc = bcc
        if attachments is not None:
            self.attachments = attachments
        if vars is not None:
            self.vars = vars

    @property
    def html(self):
        """Gets the html of this Email.  # noqa: E501


        :return: The html of this Email.  # noqa: E501
        :rtype: str
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this Email.


        :param html: The html of this Email.  # noqa: E501
        :type: str
        """
        if html is None:
            raise ValueError("Invalid value for `html`, must not be `None`")  # noqa: E501

        self._html = html

    @property
    def subject(self):
        """Gets the subject of this Email.  # noqa: E501


        :return: The subject of this Email.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this Email.


        :param subject: The subject of this Email.  # noqa: E501
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def from_email(self):
        """Gets the from_email of this Email.  # noqa: E501


        :return: The from_email of this Email.  # noqa: E501
        :rtype: str
        """
        return self._from_email

    @from_email.setter
    def from_email(self, from_email):
        """Sets the from_email of this Email.


        :param from_email: The from_email of this Email.  # noqa: E501
        :type: str
        """
        if from_email is None:
            raise ValueError("Invalid value for `from_email`, must not be `None`")  # noqa: E501

        self._from_email = from_email

    @property
    def from_name(self):
        """Gets the from_name of this Email.  # noqa: E501


        :return: The from_name of this Email.  # noqa: E501
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """Sets the from_name of this Email.


        :param from_name: The from_name of this Email.  # noqa: E501
        :type: str
        """

        self._from_name = from_name

    @property
    def global_merge_vars(self):
        """Gets the global_merge_vars of this Email.  # noqa: E501


        :return: The global_merge_vars of this Email.  # noqa: E501
        :rtype: list[EmailGlobalMergeVars]
        """
        return self._global_merge_vars

    @global_merge_vars.setter
    def global_merge_vars(self, global_merge_vars):
        """Sets the global_merge_vars of this Email.


        :param global_merge_vars: The global_merge_vars of this Email.  # noqa: E501
        :type: list[EmailGlobalMergeVars]
        """

        self._global_merge_vars = global_merge_vars

    @property
    def to(self):
        """Gets the to of this Email.  # noqa: E501


        :return: The to of this Email.  # noqa: E501
        :rtype: list[EmailTo]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this Email.


        :param to: The to of this Email.  # noqa: E501
        :type: list[EmailTo]
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def cc(self):
        """Gets the cc of this Email.  # noqa: E501


        :return: The cc of this Email.  # noqa: E501
        :rtype: list[str]
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this Email.


        :param cc: The cc of this Email.  # noqa: E501
        :type: list[str]
        """

        self._cc = cc

    @property
    def bcc(self):
        """Gets the bcc of this Email.  # noqa: E501


        :return: The bcc of this Email.  # noqa: E501
        :rtype: list[str]
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc):
        """Sets the bcc of this Email.


        :param bcc: The bcc of this Email.  # noqa: E501
        :type: list[str]
        """

        self._bcc = bcc

    @property
    def attachments(self):
        """Gets the attachments of this Email.  # noqa: E501


        :return: The attachments of this Email.  # noqa: E501
        :rtype: list[EmailAttachments]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this Email.


        :param attachments: The attachments of this Email.  # noqa: E501
        :type: list[EmailAttachments]
        """

        self._attachments = attachments

    @property
    def vars(self):
        """Gets the vars of this Email.  # noqa: E501


        :return: The vars of this Email.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._vars

    @vars.setter
    def vars(self, vars):
        """Sets the vars of this Email.


        :param vars: The vars of this Email.  # noqa: E501
        :type: dict(str, str)
        """

        self._vars = vars

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
        if issubclass(Email, dict):
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
        if not isinstance(other, Email):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
