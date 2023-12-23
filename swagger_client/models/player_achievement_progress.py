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

class PlayerAchievementProgress(object):
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
        'completion_info': 'JsonLocalizedName',
        'info': 'JsonLocalizedName',
        'name': 'JsonLocalizedName',
        'stars': 'int',
        'target': 'int',
        'value': 'int',
        'village': 'str'
    }

    attribute_map = {
        'completion_info': 'completionInfo',
        'info': 'info',
        'name': 'name',
        'stars': 'stars',
        'target': 'target',
        'value': 'value',
        'village': 'village'
    }

    def __init__(self, completion_info=None, info=None, name=None, stars=None, target=None, value=None, village=None):  # noqa: E501
        """PlayerAchievementProgress - a model defined in Swagger"""  # noqa: E501
        self._completion_info = None
        self._info = None
        self._name = None
        self._stars = None
        self._target = None
        self._value = None
        self._village = None
        self.discriminator = None
        if completion_info is not None:
            self.completion_info = completion_info
        if info is not None:
            self.info = info
        if name is not None:
            self.name = name
        if stars is not None:
            self.stars = stars
        if target is not None:
            self.target = target
        if value is not None:
            self.value = value
        if village is not None:
            self.village = village

    @property
    def completion_info(self):
        """Gets the completion_info of this PlayerAchievementProgress.  # noqa: E501


        :return: The completion_info of this PlayerAchievementProgress.  # noqa: E501
        :rtype: JsonLocalizedName
        """
        return self._completion_info

    @completion_info.setter
    def completion_info(self, completion_info):
        """Sets the completion_info of this PlayerAchievementProgress.


        :param completion_info: The completion_info of this PlayerAchievementProgress.  # noqa: E501
        :type: JsonLocalizedName
        """

        self._completion_info = completion_info

    @property
    def info(self):
        """Gets the info of this PlayerAchievementProgress.  # noqa: E501


        :return: The info of this PlayerAchievementProgress.  # noqa: E501
        :rtype: JsonLocalizedName
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this PlayerAchievementProgress.


        :param info: The info of this PlayerAchievementProgress.  # noqa: E501
        :type: JsonLocalizedName
        """

        self._info = info

    @property
    def name(self):
        """Gets the name of this PlayerAchievementProgress.  # noqa: E501


        :return: The name of this PlayerAchievementProgress.  # noqa: E501
        :rtype: JsonLocalizedName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlayerAchievementProgress.


        :param name: The name of this PlayerAchievementProgress.  # noqa: E501
        :type: JsonLocalizedName
        """

        self._name = name

    @property
    def stars(self):
        """Gets the stars of this PlayerAchievementProgress.  # noqa: E501


        :return: The stars of this PlayerAchievementProgress.  # noqa: E501
        :rtype: int
        """
        return self._stars

    @stars.setter
    def stars(self, stars):
        """Sets the stars of this PlayerAchievementProgress.


        :param stars: The stars of this PlayerAchievementProgress.  # noqa: E501
        :type: int
        """

        self._stars = stars

    @property
    def target(self):
        """Gets the target of this PlayerAchievementProgress.  # noqa: E501


        :return: The target of this PlayerAchievementProgress.  # noqa: E501
        :rtype: int
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this PlayerAchievementProgress.


        :param target: The target of this PlayerAchievementProgress.  # noqa: E501
        :type: int
        """

        self._target = target

    @property
    def value(self):
        """Gets the value of this PlayerAchievementProgress.  # noqa: E501


        :return: The value of this PlayerAchievementProgress.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PlayerAchievementProgress.


        :param value: The value of this PlayerAchievementProgress.  # noqa: E501
        :type: int
        """

        self._value = value

    @property
    def village(self):
        """Gets the village of this PlayerAchievementProgress.  # noqa: E501


        :return: The village of this PlayerAchievementProgress.  # noqa: E501
        :rtype: str
        """
        return self._village

    @village.setter
    def village(self, village):
        """Sets the village of this PlayerAchievementProgress.


        :param village: The village of this PlayerAchievementProgress.  # noqa: E501
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
        if issubclass(PlayerAchievementProgress, dict):
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
        if not isinstance(other, PlayerAchievementProgress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
