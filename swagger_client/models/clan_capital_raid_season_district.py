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

class ClanCapitalRaidSeasonDistrict(object):
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
        'stars': 'int',
        'name': 'JsonLocalizedName',
        'id': 'int',
        'destruction_percent': 'int',
        'attack_count': 'int',
        'total_looted': 'int',
        'attacks': 'ClanCapitalRaidSeasonAttackList',
        'district_hall_level': 'int'
    }

    attribute_map = {
        'stars': 'stars',
        'name': 'name',
        'id': 'id',
        'destruction_percent': 'destructionPercent',
        'attack_count': 'attackCount',
        'total_looted': 'totalLooted',
        'attacks': 'attacks',
        'district_hall_level': 'districtHallLevel'
    }

    def __init__(self, stars=None, name=None, id=None, destruction_percent=None, attack_count=None, total_looted=None, attacks=None, district_hall_level=None):  # noqa: E501
        """ClanCapitalRaidSeasonDistrict - a model defined in Swagger"""  # noqa: E501
        self._stars = None
        self._name = None
        self._id = None
        self._destruction_percent = None
        self._attack_count = None
        self._total_looted = None
        self._attacks = None
        self._district_hall_level = None
        self.discriminator = None
        if stars is not None:
            self.stars = stars
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if destruction_percent is not None:
            self.destruction_percent = destruction_percent
        if attack_count is not None:
            self.attack_count = attack_count
        if total_looted is not None:
            self.total_looted = total_looted
        if attacks is not None:
            self.attacks = attacks
        if district_hall_level is not None:
            self.district_hall_level = district_hall_level

    @property
    def stars(self):
        """Gets the stars of this ClanCapitalRaidSeasonDistrict.  # noqa: E501


        :return: The stars of this ClanCapitalRaidSeasonDistrict.  # noqa: E501
        :rtype: int
        """
        return self._stars

    @stars.setter
    def stars(self, stars):
        """Sets the stars of this ClanCapitalRaidSeasonDistrict.


        :param stars: The stars of this ClanCapitalRaidSeasonDistrict.  # noqa: E501
        :type: int
        """

        self._stars = stars

    @property
    def name(self):
        """Gets the name of this ClanCapitalRaidSeasonDistrict.  # noqa: E501


        :return: The name of this ClanCapitalRaidSeasonDistrict.  # noqa: E501
        :rtype: JsonLocalizedName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClanCapitalRaidSeasonDistrict.


        :param name: The name of this ClanCapitalRaidSeasonDistrict.  # noqa: E501
        :type: JsonLocalizedName
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this ClanCapitalRaidSeasonDistrict.  # noqa: E501


        :return: The id of this ClanCapitalRaidSeasonDistrict.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClanCapitalRaidSeasonDistrict.


        :param id: The id of this ClanCapitalRaidSeasonDistrict.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def destruction_percent(self):
        """Gets the destruction_percent of this ClanCapitalRaidSeasonDistrict.  # noqa: E501


        :return: The destruction_percent of this ClanCapitalRaidSeasonDistrict.  # noqa: E501
        :rtype: int
        """
        return self._destruction_percent

    @destruction_percent.setter
    def destruction_percent(self, destruction_percent):
        """Sets the destruction_percent of this ClanCapitalRaidSeasonDistrict.


        :param destruction_percent: The destruction_percent of this ClanCapitalRaidSeasonDistrict.  # noqa: E501
        :type: int
        """

        self._destruction_percent = destruction_percent

    @property
    def attack_count(self):
        """Gets the attack_count of this ClanCapitalRaidSeasonDistrict.  # noqa: E501


        :return: The attack_count of this ClanCapitalRaidSeasonDistrict.  # noqa: E501
        :rtype: int
        """
        return self._attack_count

    @attack_count.setter
    def attack_count(self, attack_count):
        """Sets the attack_count of this ClanCapitalRaidSeasonDistrict.


        :param attack_count: The attack_count of this ClanCapitalRaidSeasonDistrict.  # noqa: E501
        :type: int
        """

        self._attack_count = attack_count

    @property
    def total_looted(self):
        """Gets the total_looted of this ClanCapitalRaidSeasonDistrict.  # noqa: E501


        :return: The total_looted of this ClanCapitalRaidSeasonDistrict.  # noqa: E501
        :rtype: int
        """
        return self._total_looted

    @total_looted.setter
    def total_looted(self, total_looted):
        """Sets the total_looted of this ClanCapitalRaidSeasonDistrict.


        :param total_looted: The total_looted of this ClanCapitalRaidSeasonDistrict.  # noqa: E501
        :type: int
        """

        self._total_looted = total_looted

    @property
    def attacks(self):
        """Gets the attacks of this ClanCapitalRaidSeasonDistrict.  # noqa: E501


        :return: The attacks of this ClanCapitalRaidSeasonDistrict.  # noqa: E501
        :rtype: ClanCapitalRaidSeasonAttackList
        """
        return self._attacks

    @attacks.setter
    def attacks(self, attacks):
        """Sets the attacks of this ClanCapitalRaidSeasonDistrict.


        :param attacks: The attacks of this ClanCapitalRaidSeasonDistrict.  # noqa: E501
        :type: ClanCapitalRaidSeasonAttackList
        """

        self._attacks = attacks

    @property
    def district_hall_level(self):
        """Gets the district_hall_level of this ClanCapitalRaidSeasonDistrict.  # noqa: E501


        :return: The district_hall_level of this ClanCapitalRaidSeasonDistrict.  # noqa: E501
        :rtype: int
        """
        return self._district_hall_level

    @district_hall_level.setter
    def district_hall_level(self, district_hall_level):
        """Sets the district_hall_level of this ClanCapitalRaidSeasonDistrict.


        :param district_hall_level: The district_hall_level of this ClanCapitalRaidSeasonDistrict.  # noqa: E501
        :type: int
        """

        self._district_hall_level = district_hall_level

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
        if issubclass(ClanCapitalRaidSeasonDistrict, dict):
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
        if not isinstance(other, ClanCapitalRaidSeasonDistrict):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other