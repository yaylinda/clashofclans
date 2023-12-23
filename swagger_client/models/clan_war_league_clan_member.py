# coding: utf-8

"""
    Clash of Clans API

    Clash of Clans API  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ClanWarLeagueClanMember(object):
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
        'name': 'str',
        'tag': 'str',
        'town_hall_level': 'int'
    }

    attribute_map = {
        'name': 'name',
        'tag': 'tag',
        'town_hall_level': 'townHallLevel'
    }

    def __init__(self, name=None, tag=None, town_hall_level=None):  # noqa: E501
        """ClanWarLeagueClanMember - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._tag = None
        self._town_hall_level = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if tag is not None:
            self.tag = tag
        if town_hall_level is not None:
            self.town_hall_level = town_hall_level

    @property
    def name(self):
        """Gets the name of this ClanWarLeagueClanMember.  # noqa: E501


        :return: The name of this ClanWarLeagueClanMember.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClanWarLeagueClanMember.


        :param name: The name of this ClanWarLeagueClanMember.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tag(self):
        """Gets the tag of this ClanWarLeagueClanMember.  # noqa: E501


        :return: The tag of this ClanWarLeagueClanMember.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ClanWarLeagueClanMember.


        :param tag: The tag of this ClanWarLeagueClanMember.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def town_hall_level(self):
        """Gets the town_hall_level of this ClanWarLeagueClanMember.  # noqa: E501


        :return: The town_hall_level of this ClanWarLeagueClanMember.  # noqa: E501
        :rtype: int
        """
        return self._town_hall_level

    @town_hall_level.setter
    def town_hall_level(self, town_hall_level):
        """Sets the town_hall_level of this ClanWarLeagueClanMember.


        :param town_hall_level: The town_hall_level of this ClanWarLeagueClanMember.  # noqa: E501
        :type: int
        """

        self._town_hall_level = town_hall_level

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
        if issubclass(ClanWarLeagueClanMember, dict):
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
        if not isinstance(other, ClanWarLeagueClanMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
