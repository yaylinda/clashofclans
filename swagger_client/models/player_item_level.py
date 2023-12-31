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

class PlayerItemLevel(object):
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
        'equipment': 'PlayerItemLevelList',
        'level': 'int',
        'max_level': 'int',
        'name': 'JsonLocalizedName',
        'super_troop_is_active': 'bool',
        'village': 'str'
    }

    attribute_map = {
        'equipment': 'equipment',
        'level': 'level',
        'max_level': 'maxLevel',
        'name': 'name',
        'super_troop_is_active': 'superTroopIsActive',
        'village': 'village'
    }

    def __init__(self, equipment=None, level=None, max_level=None, name=None, super_troop_is_active=None, village=None):  # noqa: E501
        """PlayerItemLevel - a model defined in Swagger"""  # noqa: E501
        self._equipment = None
        self._level = None
        self._max_level = None
        self._name = None
        self._super_troop_is_active = None
        self._village = None
        self.discriminator = None
        if equipment is not None:
            self.equipment = equipment
        if level is not None:
            self.level = level
        if max_level is not None:
            self.max_level = max_level
        if name is not None:
            self.name = name
        if super_troop_is_active is not None:
            self.super_troop_is_active = super_troop_is_active
        if village is not None:
            self.village = village

    @property
    def equipment(self):
        """Gets the equipment of this PlayerItemLevel.  # noqa: E501


        :return: The equipment of this PlayerItemLevel.  # noqa: E501
        :rtype: PlayerItemLevelList
        """
        return self._equipment

    @equipment.setter
    def equipment(self, equipment):
        """Sets the equipment of this PlayerItemLevel.


        :param equipment: The equipment of this PlayerItemLevel.  # noqa: E501
        :type: PlayerItemLevelList
        """

        self._equipment = equipment

    @property
    def level(self):
        """Gets the level of this PlayerItemLevel.  # noqa: E501


        :return: The level of this PlayerItemLevel.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this PlayerItemLevel.


        :param level: The level of this PlayerItemLevel.  # noqa: E501
        :type: int
        """

        self._level = level

    @property
    def max_level(self):
        """Gets the max_level of this PlayerItemLevel.  # noqa: E501


        :return: The max_level of this PlayerItemLevel.  # noqa: E501
        :rtype: int
        """
        return self._max_level

    @max_level.setter
    def max_level(self, max_level):
        """Sets the max_level of this PlayerItemLevel.


        :param max_level: The max_level of this PlayerItemLevel.  # noqa: E501
        :type: int
        """

        self._max_level = max_level

    @property
    def name(self):
        """Gets the name of this PlayerItemLevel.  # noqa: E501


        :return: The name of this PlayerItemLevel.  # noqa: E501
        :rtype: JsonLocalizedName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlayerItemLevel.


        :param name: The name of this PlayerItemLevel.  # noqa: E501
        :type: JsonLocalizedName
        """

        self._name = name

    @property
    def super_troop_is_active(self):
        """Gets the super_troop_is_active of this PlayerItemLevel.  # noqa: E501


        :return: The super_troop_is_active of this PlayerItemLevel.  # noqa: E501
        :rtype: bool
        """
        return self._super_troop_is_active

    @super_troop_is_active.setter
    def super_troop_is_active(self, super_troop_is_active):
        """Sets the super_troop_is_active of this PlayerItemLevel.


        :param super_troop_is_active: The super_troop_is_active of this PlayerItemLevel.  # noqa: E501
        :type: bool
        """

        self._super_troop_is_active = super_troop_is_active

    @property
    def village(self):
        """Gets the village of this PlayerItemLevel.  # noqa: E501


        :return: The village of this PlayerItemLevel.  # noqa: E501
        :rtype: str
        """
        return self._village

    @village.setter
    def village(self, village):
        """Sets the village of this PlayerItemLevel.


        :param village: The village of this PlayerItemLevel.  # noqa: E501
        :type: str
        """
        allowed_values = ["homeVillage", "builderBase", "clanCapital"]  # noqa: E501
        if village not in allowed_values:
            raise ValueError(
                "Invalid value for `village` ({0}), must be one of {1}"  # noqa: E501
                .format(village, allowed_values)
            )

        self._village = village

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
        if issubclass(PlayerItemLevel, dict):
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
        if not isinstance(other, PlayerItemLevel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
