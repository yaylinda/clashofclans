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

class PlayerLegendStatistics(object):
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
        'previous_builder_base_season': 'LegendLeagueTournamentSeasonResult',
        'best_builder_base_season': 'LegendLeagueTournamentSeasonResult',
        'legend_trophies': 'int',
        'current_season': 'LegendLeagueTournamentSeasonResult',
        'best_season': 'LegendLeagueTournamentSeasonResult',
        'previous_season': 'LegendLeagueTournamentSeasonResult'
    }

    attribute_map = {
        'previous_builder_base_season': 'previousBuilderBaseSeason',
        'best_builder_base_season': 'bestBuilderBaseSeason',
        'legend_trophies': 'legendTrophies',
        'current_season': 'currentSeason',
        'best_season': 'bestSeason',
        'previous_season': 'previousSeason'
    }

    def __init__(self, previous_builder_base_season=None, best_builder_base_season=None, legend_trophies=None, current_season=None, best_season=None, previous_season=None):  # noqa: E501
        """PlayerLegendStatistics - a model defined in Swagger"""  # noqa: E501
        self._previous_builder_base_season = None
        self._best_builder_base_season = None
        self._legend_trophies = None
        self._current_season = None
        self._best_season = None
        self._previous_season = None
        self.discriminator = None
        if previous_builder_base_season is not None:
            self.previous_builder_base_season = previous_builder_base_season
        if best_builder_base_season is not None:
            self.best_builder_base_season = best_builder_base_season
        if legend_trophies is not None:
            self.legend_trophies = legend_trophies
        if current_season is not None:
            self.current_season = current_season
        if best_season is not None:
            self.best_season = best_season
        if previous_season is not None:
            self.previous_season = previous_season

    @property
    def previous_builder_base_season(self):
        """Gets the previous_builder_base_season of this PlayerLegendStatistics.  # noqa: E501


        :return: The previous_builder_base_season of this PlayerLegendStatistics.  # noqa: E501
        :rtype: LegendLeagueTournamentSeasonResult
        """
        return self._previous_builder_base_season

    @previous_builder_base_season.setter
    def previous_builder_base_season(self, previous_builder_base_season):
        """Sets the previous_builder_base_season of this PlayerLegendStatistics.


        :param previous_builder_base_season: The previous_builder_base_season of this PlayerLegendStatistics.  # noqa: E501
        :type: LegendLeagueTournamentSeasonResult
        """

        self._previous_builder_base_season = previous_builder_base_season

    @property
    def best_builder_base_season(self):
        """Gets the best_builder_base_season of this PlayerLegendStatistics.  # noqa: E501


        :return: The best_builder_base_season of this PlayerLegendStatistics.  # noqa: E501
        :rtype: LegendLeagueTournamentSeasonResult
        """
        return self._best_builder_base_season

    @best_builder_base_season.setter
    def best_builder_base_season(self, best_builder_base_season):
        """Sets the best_builder_base_season of this PlayerLegendStatistics.


        :param best_builder_base_season: The best_builder_base_season of this PlayerLegendStatistics.  # noqa: E501
        :type: LegendLeagueTournamentSeasonResult
        """

        self._best_builder_base_season = best_builder_base_season

    @property
    def legend_trophies(self):
        """Gets the legend_trophies of this PlayerLegendStatistics.  # noqa: E501


        :return: The legend_trophies of this PlayerLegendStatistics.  # noqa: E501
        :rtype: int
        """
        return self._legend_trophies

    @legend_trophies.setter
    def legend_trophies(self, legend_trophies):
        """Sets the legend_trophies of this PlayerLegendStatistics.


        :param legend_trophies: The legend_trophies of this PlayerLegendStatistics.  # noqa: E501
        :type: int
        """

        self._legend_trophies = legend_trophies

    @property
    def current_season(self):
        """Gets the current_season of this PlayerLegendStatistics.  # noqa: E501


        :return: The current_season of this PlayerLegendStatistics.  # noqa: E501
        :rtype: LegendLeagueTournamentSeasonResult
        """
        return self._current_season

    @current_season.setter
    def current_season(self, current_season):
        """Sets the current_season of this PlayerLegendStatistics.


        :param current_season: The current_season of this PlayerLegendStatistics.  # noqa: E501
        :type: LegendLeagueTournamentSeasonResult
        """

        self._current_season = current_season

    @property
    def best_season(self):
        """Gets the best_season of this PlayerLegendStatistics.  # noqa: E501


        :return: The best_season of this PlayerLegendStatistics.  # noqa: E501
        :rtype: LegendLeagueTournamentSeasonResult
        """
        return self._best_season

    @best_season.setter
    def best_season(self, best_season):
        """Sets the best_season of this PlayerLegendStatistics.


        :param best_season: The best_season of this PlayerLegendStatistics.  # noqa: E501
        :type: LegendLeagueTournamentSeasonResult
        """

        self._best_season = best_season

    @property
    def previous_season(self):
        """Gets the previous_season of this PlayerLegendStatistics.  # noqa: E501


        :return: The previous_season of this PlayerLegendStatistics.  # noqa: E501
        :rtype: LegendLeagueTournamentSeasonResult
        """
        return self._previous_season

    @previous_season.setter
    def previous_season(self, previous_season):
        """Sets the previous_season of this PlayerLegendStatistics.


        :param previous_season: The previous_season of this PlayerLegendStatistics.  # noqa: E501
        :type: LegendLeagueTournamentSeasonResult
        """

        self._previous_season = previous_season

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
        if issubclass(PlayerLegendStatistics, dict):
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
        if not isinstance(other, PlayerLegendStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
