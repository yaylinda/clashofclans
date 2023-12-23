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

class DeepLinkCreationRequest(object):
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
        'player_tags': 'StringList',
        'clan_tag': 'str',
        'opponent_clan_tag': 'str'
    }

    attribute_map = {
        'player_tags': 'playerTags',
        'clan_tag': 'clanTag',
        'opponent_clan_tag': 'opponentClanTag'
    }

    def __init__(self, player_tags=None, clan_tag=None, opponent_clan_tag=None):  # noqa: E501
        """DeepLinkCreationRequest - a model defined in Swagger"""  # noqa: E501
        self._player_tags = None
        self._clan_tag = None
        self._opponent_clan_tag = None
        self.discriminator = None
        if player_tags is not None:
            self.player_tags = player_tags
        if clan_tag is not None:
            self.clan_tag = clan_tag
        if opponent_clan_tag is not None:
            self.opponent_clan_tag = opponent_clan_tag

    @property
    def player_tags(self):
        """Gets the player_tags of this DeepLinkCreationRequest.  # noqa: E501


        :return: The player_tags of this DeepLinkCreationRequest.  # noqa: E501
        :rtype: StringList
        """
        return self._player_tags

    @player_tags.setter
    def player_tags(self, player_tags):
        """Sets the player_tags of this DeepLinkCreationRequest.


        :param player_tags: The player_tags of this DeepLinkCreationRequest.  # noqa: E501
        :type: StringList
        """

        self._player_tags = player_tags

    @property
    def clan_tag(self):
        """Gets the clan_tag of this DeepLinkCreationRequest.  # noqa: E501


        :return: The clan_tag of this DeepLinkCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._clan_tag

    @clan_tag.setter
    def clan_tag(self, clan_tag):
        """Sets the clan_tag of this DeepLinkCreationRequest.


        :param clan_tag: The clan_tag of this DeepLinkCreationRequest.  # noqa: E501
        :type: str
        """

        self._clan_tag = clan_tag

    @property
    def opponent_clan_tag(self):
        """Gets the opponent_clan_tag of this DeepLinkCreationRequest.  # noqa: E501


        :return: The opponent_clan_tag of this DeepLinkCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._opponent_clan_tag

    @opponent_clan_tag.setter
    def opponent_clan_tag(self, opponent_clan_tag):
        """Sets the opponent_clan_tag of this DeepLinkCreationRequest.


        :param opponent_clan_tag: The opponent_clan_tag of this DeepLinkCreationRequest.  # noqa: E501
        :type: str
        """

        self._opponent_clan_tag = opponent_clan_tag

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
        if issubclass(DeepLinkCreationRequest, dict):
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
        if not isinstance(other, DeepLinkCreationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
