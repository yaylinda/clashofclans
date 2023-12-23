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

class ClanWar(object):
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
        'attacks_per_member': 'int',
        'clan': 'WarClan',
        'end_time': 'str',
        'opponent': 'WarClan',
        'preparation_start_time': 'str',
        'start_time': 'str',
        'state': 'str',
        'team_size': 'int'
    }

    attribute_map = {
        'attacks_per_member': 'attacksPerMember',
        'clan': 'clan',
        'end_time': 'endTime',
        'opponent': 'opponent',
        'preparation_start_time': 'preparationStartTime',
        'start_time': 'startTime',
        'state': 'state',
        'team_size': 'teamSize'
    }

    def __init__(self, attacks_per_member=None, clan=None, end_time=None, opponent=None, preparation_start_time=None, start_time=None, state=None, team_size=None):  # noqa: E501
        """ClanWar - a model defined in Swagger"""  # noqa: E501
        self._attacks_per_member = None
        self._clan = None
        self._end_time = None
        self._opponent = None
        self._preparation_start_time = None
        self._start_time = None
        self._state = None
        self._team_size = None
        self.discriminator = None
        if attacks_per_member is not None:
            self.attacks_per_member = attacks_per_member
        if clan is not None:
            self.clan = clan
        if end_time is not None:
            self.end_time = end_time
        if opponent is not None:
            self.opponent = opponent
        if preparation_start_time is not None:
            self.preparation_start_time = preparation_start_time
        if start_time is not None:
            self.start_time = start_time
        if state is not None:
            self.state = state
        if team_size is not None:
            self.team_size = team_size

    @property
    def attacks_per_member(self):
        """Gets the attacks_per_member of this ClanWar.  # noqa: E501


        :return: The attacks_per_member of this ClanWar.  # noqa: E501
        :rtype: int
        """
        return self._attacks_per_member

    @attacks_per_member.setter
    def attacks_per_member(self, attacks_per_member):
        """Sets the attacks_per_member of this ClanWar.


        :param attacks_per_member: The attacks_per_member of this ClanWar.  # noqa: E501
        :type: int
        """

        self._attacks_per_member = attacks_per_member

    @property
    def clan(self):
        """Gets the clan of this ClanWar.  # noqa: E501


        :return: The clan of this ClanWar.  # noqa: E501
        :rtype: WarClan
        """
        return self._clan

    @clan.setter
    def clan(self, clan):
        """Sets the clan of this ClanWar.


        :param clan: The clan of this ClanWar.  # noqa: E501
        :type: WarClan
        """

        self._clan = clan

    @property
    def end_time(self):
        """Gets the end_time of this ClanWar.  # noqa: E501


        :return: The end_time of this ClanWar.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ClanWar.


        :param end_time: The end_time of this ClanWar.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def opponent(self):
        """Gets the opponent of this ClanWar.  # noqa: E501


        :return: The opponent of this ClanWar.  # noqa: E501
        :rtype: WarClan
        """
        return self._opponent

    @opponent.setter
    def opponent(self, opponent):
        """Sets the opponent of this ClanWar.


        :param opponent: The opponent of this ClanWar.  # noqa: E501
        :type: WarClan
        """

        self._opponent = opponent

    @property
    def preparation_start_time(self):
        """Gets the preparation_start_time of this ClanWar.  # noqa: E501


        :return: The preparation_start_time of this ClanWar.  # noqa: E501
        :rtype: str
        """
        return self._preparation_start_time

    @preparation_start_time.setter
    def preparation_start_time(self, preparation_start_time):
        """Sets the preparation_start_time of this ClanWar.


        :param preparation_start_time: The preparation_start_time of this ClanWar.  # noqa: E501
        :type: str
        """

        self._preparation_start_time = preparation_start_time

    @property
    def start_time(self):
        """Gets the start_time of this ClanWar.  # noqa: E501


        :return: The start_time of this ClanWar.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ClanWar.


        :param start_time: The start_time of this ClanWar.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def state(self):
        """Gets the state of this ClanWar.  # noqa: E501


        :return: The state of this ClanWar.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ClanWar.


        :param state: The state of this ClanWar.  # noqa: E501
        :type: str
        """
        allowed_values = ["clanNotFound", "accessDenied", "notInWar", "inMatchmaking", "enterWar", "matched", "preparation", "war", "inWar", "ended", "warEnded"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def team_size(self):
        """Gets the team_size of this ClanWar.  # noqa: E501


        :return: The team_size of this ClanWar.  # noqa: E501
        :rtype: int
        """
        return self._team_size

    @team_size.setter
    def team_size(self, team_size):
        """Sets the team_size of this ClanWar.


        :param team_size: The team_size of this ClanWar.  # noqa: E501
        :type: int
        """

        self._team_size = team_size

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
        if issubclass(ClanWar, dict):
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
        if not isinstance(other, ClanWar):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
