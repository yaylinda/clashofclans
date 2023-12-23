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

class ClanCapitalRaidSeasonDefenseLogEntry(object):
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
        'attacker': 'ClanCapitalRaidSeasonClanInfo',
        'attack_count': 'int',
        'district_count': 'int',
        'districts_destroyed': 'int',
        'districts': 'ClanCapitalRaidSeasonDistrictList'
    }

    attribute_map = {
        'attacker': 'attacker',
        'attack_count': 'attackCount',
        'district_count': 'districtCount',
        'districts_destroyed': 'districtsDestroyed',
        'districts': 'districts'
    }

    def __init__(self, attacker=None, attack_count=None, district_count=None, districts_destroyed=None, districts=None):  # noqa: E501
        """ClanCapitalRaidSeasonDefenseLogEntry - a model defined in Swagger"""  # noqa: E501
        self._attacker = None
        self._attack_count = None
        self._district_count = None
        self._districts_destroyed = None
        self._districts = None
        self.discriminator = None
        if attacker is not None:
            self.attacker = attacker
        if attack_count is not None:
            self.attack_count = attack_count
        if district_count is not None:
            self.district_count = district_count
        if districts_destroyed is not None:
            self.districts_destroyed = districts_destroyed
        if districts is not None:
            self.districts = districts

    @property
    def attacker(self):
        """Gets the attacker of this ClanCapitalRaidSeasonDefenseLogEntry.  # noqa: E501


        :return: The attacker of this ClanCapitalRaidSeasonDefenseLogEntry.  # noqa: E501
        :rtype: ClanCapitalRaidSeasonClanInfo
        """
        return self._attacker

    @attacker.setter
    def attacker(self, attacker):
        """Sets the attacker of this ClanCapitalRaidSeasonDefenseLogEntry.


        :param attacker: The attacker of this ClanCapitalRaidSeasonDefenseLogEntry.  # noqa: E501
        :type: ClanCapitalRaidSeasonClanInfo
        """

        self._attacker = attacker

    @property
    def attack_count(self):
        """Gets the attack_count of this ClanCapitalRaidSeasonDefenseLogEntry.  # noqa: E501


        :return: The attack_count of this ClanCapitalRaidSeasonDefenseLogEntry.  # noqa: E501
        :rtype: int
        """
        return self._attack_count

    @attack_count.setter
    def attack_count(self, attack_count):
        """Sets the attack_count of this ClanCapitalRaidSeasonDefenseLogEntry.


        :param attack_count: The attack_count of this ClanCapitalRaidSeasonDefenseLogEntry.  # noqa: E501
        :type: int
        """

        self._attack_count = attack_count

    @property
    def district_count(self):
        """Gets the district_count of this ClanCapitalRaidSeasonDefenseLogEntry.  # noqa: E501


        :return: The district_count of this ClanCapitalRaidSeasonDefenseLogEntry.  # noqa: E501
        :rtype: int
        """
        return self._district_count

    @district_count.setter
    def district_count(self, district_count):
        """Sets the district_count of this ClanCapitalRaidSeasonDefenseLogEntry.


        :param district_count: The district_count of this ClanCapitalRaidSeasonDefenseLogEntry.  # noqa: E501
        :type: int
        """

        self._district_count = district_count

    @property
    def districts_destroyed(self):
        """Gets the districts_destroyed of this ClanCapitalRaidSeasonDefenseLogEntry.  # noqa: E501


        :return: The districts_destroyed of this ClanCapitalRaidSeasonDefenseLogEntry.  # noqa: E501
        :rtype: int
        """
        return self._districts_destroyed

    @districts_destroyed.setter
    def districts_destroyed(self, districts_destroyed):
        """Sets the districts_destroyed of this ClanCapitalRaidSeasonDefenseLogEntry.


        :param districts_destroyed: The districts_destroyed of this ClanCapitalRaidSeasonDefenseLogEntry.  # noqa: E501
        :type: int
        """

        self._districts_destroyed = districts_destroyed

    @property
    def districts(self):
        """Gets the districts of this ClanCapitalRaidSeasonDefenseLogEntry.  # noqa: E501


        :return: The districts of this ClanCapitalRaidSeasonDefenseLogEntry.  # noqa: E501
        :rtype: ClanCapitalRaidSeasonDistrictList
        """
        return self._districts

    @districts.setter
    def districts(self, districts):
        """Sets the districts of this ClanCapitalRaidSeasonDefenseLogEntry.


        :param districts: The districts of this ClanCapitalRaidSeasonDefenseLogEntry.  # noqa: E501
        :type: ClanCapitalRaidSeasonDistrictList
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
        if issubclass(ClanCapitalRaidSeasonDefenseLogEntry, dict):
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
        if not isinstance(other, ClanCapitalRaidSeasonDefenseLogEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other