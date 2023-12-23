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

class PlayerRanking(object):
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
        'league': 'League',
        'clan': 'PlayerRankingClan',
        'attack_wins': 'int',
        'defense_wins': 'int',
        'tag': 'str',
        'name': 'str',
        'exp_level': 'int',
        'rank': 'int',
        'previous_rank': 'int',
        'trophies': 'int'
    }

    attribute_map = {
        'league': 'league',
        'clan': 'clan',
        'attack_wins': 'attackWins',
        'defense_wins': 'defenseWins',
        'tag': 'tag',
        'name': 'name',
        'exp_level': 'expLevel',
        'rank': 'rank',
        'previous_rank': 'previousRank',
        'trophies': 'trophies'
    }

    def __init__(self, league=None, clan=None, attack_wins=None, defense_wins=None, tag=None, name=None, exp_level=None, rank=None, previous_rank=None, trophies=None):  # noqa: E501
        """PlayerRanking - a model defined in Swagger"""  # noqa: E501
        self._league = None
        self._clan = None
        self._attack_wins = None
        self._defense_wins = None
        self._tag = None
        self._name = None
        self._exp_level = None
        self._rank = None
        self._previous_rank = None
        self._trophies = None
        self.discriminator = None
        if league is not None:
            self.league = league
        if clan is not None:
            self.clan = clan
        if attack_wins is not None:
            self.attack_wins = attack_wins
        if defense_wins is not None:
            self.defense_wins = defense_wins
        if tag is not None:
            self.tag = tag
        if name is not None:
            self.name = name
        if exp_level is not None:
            self.exp_level = exp_level
        if rank is not None:
            self.rank = rank
        if previous_rank is not None:
            self.previous_rank = previous_rank
        if trophies is not None:
            self.trophies = trophies

    @property
    def league(self):
        """Gets the league of this PlayerRanking.  # noqa: E501


        :return: The league of this PlayerRanking.  # noqa: E501
        :rtype: League
        """
        return self._league

    @league.setter
    def league(self, league):
        """Sets the league of this PlayerRanking.


        :param league: The league of this PlayerRanking.  # noqa: E501
        :type: League
        """

        self._league = league

    @property
    def clan(self):
        """Gets the clan of this PlayerRanking.  # noqa: E501


        :return: The clan of this PlayerRanking.  # noqa: E501
        :rtype: PlayerRankingClan
        """
        return self._clan

    @clan.setter
    def clan(self, clan):
        """Sets the clan of this PlayerRanking.


        :param clan: The clan of this PlayerRanking.  # noqa: E501
        :type: PlayerRankingClan
        """

        self._clan = clan

    @property
    def attack_wins(self):
        """Gets the attack_wins of this PlayerRanking.  # noqa: E501


        :return: The attack_wins of this PlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._attack_wins

    @attack_wins.setter
    def attack_wins(self, attack_wins):
        """Sets the attack_wins of this PlayerRanking.


        :param attack_wins: The attack_wins of this PlayerRanking.  # noqa: E501
        :type: int
        """

        self._attack_wins = attack_wins

    @property
    def defense_wins(self):
        """Gets the defense_wins of this PlayerRanking.  # noqa: E501


        :return: The defense_wins of this PlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._defense_wins

    @defense_wins.setter
    def defense_wins(self, defense_wins):
        """Sets the defense_wins of this PlayerRanking.


        :param defense_wins: The defense_wins of this PlayerRanking.  # noqa: E501
        :type: int
        """

        self._defense_wins = defense_wins

    @property
    def tag(self):
        """Gets the tag of this PlayerRanking.  # noqa: E501


        :return: The tag of this PlayerRanking.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this PlayerRanking.


        :param tag: The tag of this PlayerRanking.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def name(self):
        """Gets the name of this PlayerRanking.  # noqa: E501


        :return: The name of this PlayerRanking.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlayerRanking.


        :param name: The name of this PlayerRanking.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def exp_level(self):
        """Gets the exp_level of this PlayerRanking.  # noqa: E501


        :return: The exp_level of this PlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._exp_level

    @exp_level.setter
    def exp_level(self, exp_level):
        """Sets the exp_level of this PlayerRanking.


        :param exp_level: The exp_level of this PlayerRanking.  # noqa: E501
        :type: int
        """

        self._exp_level = exp_level

    @property
    def rank(self):
        """Gets the rank of this PlayerRanking.  # noqa: E501


        :return: The rank of this PlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this PlayerRanking.


        :param rank: The rank of this PlayerRanking.  # noqa: E501
        :type: int
        """

        self._rank = rank

    @property
    def previous_rank(self):
        """Gets the previous_rank of this PlayerRanking.  # noqa: E501


        :return: The previous_rank of this PlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._previous_rank

    @previous_rank.setter
    def previous_rank(self, previous_rank):
        """Sets the previous_rank of this PlayerRanking.


        :param previous_rank: The previous_rank of this PlayerRanking.  # noqa: E501
        :type: int
        """

        self._previous_rank = previous_rank

    @property
    def trophies(self):
        """Gets the trophies of this PlayerRanking.  # noqa: E501


        :return: The trophies of this PlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._trophies

    @trophies.setter
    def trophies(self, trophies):
        """Sets the trophies of this PlayerRanking.


        :param trophies: The trophies of this PlayerRanking.  # noqa: E501
        :type: int
        """

        self._trophies = trophies

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
        if issubclass(PlayerRanking, dict):
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
        if not isinstance(other, PlayerRanking):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
