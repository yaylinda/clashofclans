# coding: utf-8

"""
    Clash of Clans API

    Check out <a href=\"https://developer.clashofclans.com/#/getting-started\" target=\"_parent\">Getting Started</a> for instructions and links to other resources. Clash of Clans API uses <a href=\"https://jwt.io/\" target=\"_blank\">JSON Web Tokens</a> for authorizing the requests. Tokens are created by developers on <a href=\"https://developer.clashofclans.com/#/account\" target=\"_parent\">My Account</a> page and must be passed in every API request in Authorization HTTP header using Bearer authentication scheme. Correct Authorization header looks like this: \"Authorization: Bearer API_TOKEN\".   # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PlayerClan(object):
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
        'tag': 'str',
        'clan_level': 'int',
        'name': 'str',
        'badge_urls': 'object'
    }

    attribute_map = {
        'tag': 'tag',
        'clan_level': 'clanLevel',
        'name': 'name',
        'badge_urls': 'badgeUrls'
    }

    def __init__(self, tag=None, clan_level=None, name=None, badge_urls=None):  # noqa: E501
        """PlayerClan - a model defined in Swagger"""  # noqa: E501
        self._tag = None
        self._clan_level = None
        self._name = None
        self._badge_urls = None
        self.discriminator = None
        if tag is not None:
            self.tag = tag
        if clan_level is not None:
            self.clan_level = clan_level
        if name is not None:
            self.name = name
        if badge_urls is not None:
            self.badge_urls = badge_urls

    @property
    def tag(self):
        """Gets the tag of this PlayerClan.  # noqa: E501


        :return: The tag of this PlayerClan.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this PlayerClan.


        :param tag: The tag of this PlayerClan.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def clan_level(self):
        """Gets the clan_level of this PlayerClan.  # noqa: E501


        :return: The clan_level of this PlayerClan.  # noqa: E501
        :rtype: int
        """
        return self._clan_level

    @clan_level.setter
    def clan_level(self, clan_level):
        """Sets the clan_level of this PlayerClan.


        :param clan_level: The clan_level of this PlayerClan.  # noqa: E501
        :type: int
        """

        self._clan_level = clan_level

    @property
    def name(self):
        """Gets the name of this PlayerClan.  # noqa: E501


        :return: The name of this PlayerClan.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlayerClan.


        :param name: The name of this PlayerClan.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def badge_urls(self):
        """Gets the badge_urls of this PlayerClan.  # noqa: E501


        :return: The badge_urls of this PlayerClan.  # noqa: E501
        :rtype: object
        """
        return self._badge_urls

    @badge_urls.setter
    def badge_urls(self, badge_urls):
        """Sets the badge_urls of this PlayerClan.


        :param badge_urls: The badge_urls of this PlayerClan.  # noqa: E501
        :type: object
        """

        self._badge_urls = badge_urls

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
        if issubclass(PlayerClan, dict):
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
        if not isinstance(other, PlayerClan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
