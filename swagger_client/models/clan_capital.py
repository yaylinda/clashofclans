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

class ClanCapital(object):
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
        'capital_hall_level': 'int',
        'districts': 'ClanDistrictDataList'
    }

    attribute_map = {
        'capital_hall_level': 'capitalHallLevel',
        'districts': 'districts'
    }

    def __init__(self, capital_hall_level=None, districts=None):  # noqa: E501
        """ClanCapital - a model defined in Swagger"""  # noqa: E501
        self._capital_hall_level = None
        self._districts = None
        self.discriminator = None
        if capital_hall_level is not None:
            self.capital_hall_level = capital_hall_level
        if districts is not None:
            self.districts = districts

    @property
    def capital_hall_level(self):
        """Gets the capital_hall_level of this ClanCapital.  # noqa: E501


        :return: The capital_hall_level of this ClanCapital.  # noqa: E501
        :rtype: int
        """
        return self._capital_hall_level

    @capital_hall_level.setter
    def capital_hall_level(self, capital_hall_level):
        """Sets the capital_hall_level of this ClanCapital.


        :param capital_hall_level: The capital_hall_level of this ClanCapital.  # noqa: E501
        :type: int
        """

        self._capital_hall_level = capital_hall_level

    @property
    def districts(self):
        """Gets the districts of this ClanCapital.  # noqa: E501


        :return: The districts of this ClanCapital.  # noqa: E501
        :rtype: ClanDistrictDataList
        """
        return self._districts

    @districts.setter
    def districts(self, districts):
        """Sets the districts of this ClanCapital.


        :param districts: The districts of this ClanCapital.  # noqa: E501
        :type: ClanDistrictDataList
        """

        self._districts = districts

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
        if issubclass(ClanCapital, dict):
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
        if not isinstance(other, ClanCapital):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
