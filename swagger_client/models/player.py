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

class Player(object):
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
        'builder_base_league': 'BuilderBaseLeague',
        'clan': 'PlayerClan',
        'role': 'str',
        'war_preference': 'str',
        'attack_wins': 'int',
        'defense_wins': 'int',
        'town_hall_level': 'int',
        'town_hall_weapon_level': 'int',
        'legend_statistics': 'PlayerLegendStatistics',
        'troops': 'PlayerItemLevelList',
        'heroes': 'PlayerItemLevelList',
        'hero_equipment': 'PlayerItemLevelList',
        'spells': 'PlayerItemLevelList',
        'labels': 'LabelList',
        'tag': 'str',
        'name': 'str',
        'exp_level': 'int',
        'trophies': 'int',
        'best_trophies': 'int',
        'donations': 'int',
        'donations_received': 'int',
        'builder_hall_level': 'int',
        'builder_base_trophies': 'int',
        'best_builder_base_trophies': 'int',
        'war_stars': 'int',
        'achievements': 'PlayerAchievementProgressList',
        'clan_capital_contributions': 'int',
        'player_house': 'PlayerHouse'
    }

    attribute_map = {
        'league': 'league',
        'builder_base_league': 'builderBaseLeague',
        'clan': 'clan',
        'role': 'role',
        'war_preference': 'warPreference',
        'attack_wins': 'attackWins',
        'defense_wins': 'defenseWins',
        'town_hall_level': 'townHallLevel',
        'town_hall_weapon_level': 'townHallWeaponLevel',
        'legend_statistics': 'legendStatistics',
        'troops': 'troops',
        'heroes': 'heroes',
        'hero_equipment': 'heroEquipment',
        'spells': 'spells',
        'labels': 'labels',
        'tag': 'tag',
        'name': 'name',
        'exp_level': 'expLevel',
        'trophies': 'trophies',
        'best_trophies': 'bestTrophies',
        'donations': 'donations',
        'donations_received': 'donationsReceived',
        'builder_hall_level': 'builderHallLevel',
        'builder_base_trophies': 'builderBaseTrophies',
        'best_builder_base_trophies': 'bestBuilderBaseTrophies',
        'war_stars': 'warStars',
        'achievements': 'achievements',
        'clan_capital_contributions': 'clanCapitalContributions',
        'player_house': 'playerHouse'
    }

    def __init__(self, league=None, builder_base_league=None, clan=None, role=None, war_preference=None, attack_wins=None, defense_wins=None, town_hall_level=None, town_hall_weapon_level=None, legend_statistics=None, troops=None, heroes=None, hero_equipment=None, spells=None, labels=None, tag=None, name=None, exp_level=None, trophies=None, best_trophies=None, donations=None, donations_received=None, builder_hall_level=None, builder_base_trophies=None, best_builder_base_trophies=None, war_stars=None, achievements=None, clan_capital_contributions=None, player_house=None):  # noqa: E501
        """Player - a model defined in Swagger"""  # noqa: E501
        self._league = None
        self._builder_base_league = None
        self._clan = None
        self._role = None
        self._war_preference = None
        self._attack_wins = None
        self._defense_wins = None
        self._town_hall_level = None
        self._town_hall_weapon_level = None
        self._legend_statistics = None
        self._troops = None
        self._heroes = None
        self._hero_equipment = None
        self._spells = None
        self._labels = None
        self._tag = None
        self._name = None
        self._exp_level = None
        self._trophies = None
        self._best_trophies = None
        self._donations = None
        self._donations_received = None
        self._builder_hall_level = None
        self._builder_base_trophies = None
        self._best_builder_base_trophies = None
        self._war_stars = None
        self._achievements = None
        self._clan_capital_contributions = None
        self._player_house = None
        self.discriminator = None
        if league is not None:
            self.league = league
        if builder_base_league is not None:
            self.builder_base_league = builder_base_league
        if clan is not None:
            self.clan = clan
        if role is not None:
            self.role = role
        if war_preference is not None:
            self.war_preference = war_preference
        if attack_wins is not None:
            self.attack_wins = attack_wins
        if defense_wins is not None:
            self.defense_wins = defense_wins
        if town_hall_level is not None:
            self.town_hall_level = town_hall_level
        if town_hall_weapon_level is not None:
            self.town_hall_weapon_level = town_hall_weapon_level
        if legend_statistics is not None:
            self.legend_statistics = legend_statistics
        if troops is not None:
            self.troops = troops
        if heroes is not None:
            self.heroes = heroes
        if hero_equipment is not None:
            self.hero_equipment = hero_equipment
        if spells is not None:
            self.spells = spells
        if labels is not None:
            self.labels = labels
        if tag is not None:
            self.tag = tag
        if name is not None:
            self.name = name
        if exp_level is not None:
            self.exp_level = exp_level
        if trophies is not None:
            self.trophies = trophies
        if best_trophies is not None:
            self.best_trophies = best_trophies
        if donations is not None:
            self.donations = donations
        if donations_received is not None:
            self.donations_received = donations_received
        if builder_hall_level is not None:
            self.builder_hall_level = builder_hall_level
        if builder_base_trophies is not None:
            self.builder_base_trophies = builder_base_trophies
        if best_builder_base_trophies is not None:
            self.best_builder_base_trophies = best_builder_base_trophies
        if war_stars is not None:
            self.war_stars = war_stars
        if achievements is not None:
            self.achievements = achievements
        if clan_capital_contributions is not None:
            self.clan_capital_contributions = clan_capital_contributions
        if player_house is not None:
            self.player_house = player_house

    @property
    def league(self):
        """Gets the league of this Player.  # noqa: E501


        :return: The league of this Player.  # noqa: E501
        :rtype: League
        """
        return self._league

    @league.setter
    def league(self, league):
        """Sets the league of this Player.


        :param league: The league of this Player.  # noqa: E501
        :type: League
        """

        self._league = league

    @property
    def builder_base_league(self):
        """Gets the builder_base_league of this Player.  # noqa: E501


        :return: The builder_base_league of this Player.  # noqa: E501
        :rtype: BuilderBaseLeague
        """
        return self._builder_base_league

    @builder_base_league.setter
    def builder_base_league(self, builder_base_league):
        """Sets the builder_base_league of this Player.


        :param builder_base_league: The builder_base_league of this Player.  # noqa: E501
        :type: BuilderBaseLeague
        """

        self._builder_base_league = builder_base_league

    @property
    def clan(self):
        """Gets the clan of this Player.  # noqa: E501


        :return: The clan of this Player.  # noqa: E501
        :rtype: PlayerClan
        """
        return self._clan

    @clan.setter
    def clan(self, clan):
        """Sets the clan of this Player.


        :param clan: The clan of this Player.  # noqa: E501
        :type: PlayerClan
        """

        self._clan = clan

    @property
    def role(self):
        """Gets the role of this Player.  # noqa: E501


        :return: The role of this Player.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Player.


        :param role: The role of this Player.  # noqa: E501
        :type: str
        """
        allowed_values = ["NOT_MEMBER", "MEMBER", "LEADER", "ADMIN", "COLEADER"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def war_preference(self):
        """Gets the war_preference of this Player.  # noqa: E501


        :return: The war_preference of this Player.  # noqa: E501
        :rtype: str
        """
        return self._war_preference

    @war_preference.setter
    def war_preference(self, war_preference):
        """Sets the war_preference of this Player.


        :param war_preference: The war_preference of this Player.  # noqa: E501
        :type: str
        """
        allowed_values = ["OUT", "IN"]  # noqa: E501
        if war_preference not in allowed_values:
            raise ValueError(
                "Invalid value for `war_preference` ({0}), must be one of {1}"  # noqa: E501
                .format(war_preference, allowed_values)
            )

        self._war_preference = war_preference

    @property
    def attack_wins(self):
        """Gets the attack_wins of this Player.  # noqa: E501


        :return: The attack_wins of this Player.  # noqa: E501
        :rtype: int
        """
        return self._attack_wins

    @attack_wins.setter
    def attack_wins(self, attack_wins):
        """Sets the attack_wins of this Player.


        :param attack_wins: The attack_wins of this Player.  # noqa: E501
        :type: int
        """

        self._attack_wins = attack_wins

    @property
    def defense_wins(self):
        """Gets the defense_wins of this Player.  # noqa: E501


        :return: The defense_wins of this Player.  # noqa: E501
        :rtype: int
        """
        return self._defense_wins

    @defense_wins.setter
    def defense_wins(self, defense_wins):
        """Sets the defense_wins of this Player.


        :param defense_wins: The defense_wins of this Player.  # noqa: E501
        :type: int
        """

        self._defense_wins = defense_wins

    @property
    def town_hall_level(self):
        """Gets the town_hall_level of this Player.  # noqa: E501


        :return: The town_hall_level of this Player.  # noqa: E501
        :rtype: int
        """
        return self._town_hall_level

    @town_hall_level.setter
    def town_hall_level(self, town_hall_level):
        """Sets the town_hall_level of this Player.


        :param town_hall_level: The town_hall_level of this Player.  # noqa: E501
        :type: int
        """

        self._town_hall_level = town_hall_level

    @property
    def town_hall_weapon_level(self):
        """Gets the town_hall_weapon_level of this Player.  # noqa: E501


        :return: The town_hall_weapon_level of this Player.  # noqa: E501
        :rtype: int
        """
        return self._town_hall_weapon_level

    @town_hall_weapon_level.setter
    def town_hall_weapon_level(self, town_hall_weapon_level):
        """Sets the town_hall_weapon_level of this Player.


        :param town_hall_weapon_level: The town_hall_weapon_level of this Player.  # noqa: E501
        :type: int
        """

        self._town_hall_weapon_level = town_hall_weapon_level

    @property
    def legend_statistics(self):
        """Gets the legend_statistics of this Player.  # noqa: E501


        :return: The legend_statistics of this Player.  # noqa: E501
        :rtype: PlayerLegendStatistics
        """
        return self._legend_statistics

    @legend_statistics.setter
    def legend_statistics(self, legend_statistics):
        """Sets the legend_statistics of this Player.


        :param legend_statistics: The legend_statistics of this Player.  # noqa: E501
        :type: PlayerLegendStatistics
        """

        self._legend_statistics = legend_statistics

    @property
    def troops(self):
        """Gets the troops of this Player.  # noqa: E501


        :return: The troops of this Player.  # noqa: E501
        :rtype: PlayerItemLevelList
        """
        return self._troops

    @troops.setter
    def troops(self, troops):
        """Sets the troops of this Player.


        :param troops: The troops of this Player.  # noqa: E501
        :type: PlayerItemLevelList
        """

        self._troops = troops

    @property
    def heroes(self):
        """Gets the heroes of this Player.  # noqa: E501


        :return: The heroes of this Player.  # noqa: E501
        :rtype: PlayerItemLevelList
        """
        return self._heroes

    @heroes.setter
    def heroes(self, heroes):
        """Sets the heroes of this Player.


        :param heroes: The heroes of this Player.  # noqa: E501
        :type: PlayerItemLevelList
        """

        self._heroes = heroes

    @property
    def hero_equipment(self):
        """Gets the hero_equipment of this Player.  # noqa: E501


        :return: The hero_equipment of this Player.  # noqa: E501
        :rtype: PlayerItemLevelList
        """
        return self._hero_equipment

    @hero_equipment.setter
    def hero_equipment(self, hero_equipment):
        """Sets the hero_equipment of this Player.


        :param hero_equipment: The hero_equipment of this Player.  # noqa: E501
        :type: PlayerItemLevelList
        """

        self._hero_equipment = hero_equipment

    @property
    def spells(self):
        """Gets the spells of this Player.  # noqa: E501


        :return: The spells of this Player.  # noqa: E501
        :rtype: PlayerItemLevelList
        """
        return self._spells

    @spells.setter
    def spells(self, spells):
        """Sets the spells of this Player.


        :param spells: The spells of this Player.  # noqa: E501
        :type: PlayerItemLevelList
        """

        self._spells = spells

    @property
    def labels(self):
        """Gets the labels of this Player.  # noqa: E501


        :return: The labels of this Player.  # noqa: E501
        :rtype: LabelList
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this Player.


        :param labels: The labels of this Player.  # noqa: E501
        :type: LabelList
        """

        self._labels = labels

    @property
    def tag(self):
        """Gets the tag of this Player.  # noqa: E501


        :return: The tag of this Player.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Player.


        :param tag: The tag of this Player.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def name(self):
        """Gets the name of this Player.  # noqa: E501


        :return: The name of this Player.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Player.


        :param name: The name of this Player.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def exp_level(self):
        """Gets the exp_level of this Player.  # noqa: E501


        :return: The exp_level of this Player.  # noqa: E501
        :rtype: int
        """
        return self._exp_level

    @exp_level.setter
    def exp_level(self, exp_level):
        """Sets the exp_level of this Player.


        :param exp_level: The exp_level of this Player.  # noqa: E501
        :type: int
        """

        self._exp_level = exp_level

    @property
    def trophies(self):
        """Gets the trophies of this Player.  # noqa: E501


        :return: The trophies of this Player.  # noqa: E501
        :rtype: int
        """
        return self._trophies

    @trophies.setter
    def trophies(self, trophies):
        """Sets the trophies of this Player.


        :param trophies: The trophies of this Player.  # noqa: E501
        :type: int
        """

        self._trophies = trophies

    @property
    def best_trophies(self):
        """Gets the best_trophies of this Player.  # noqa: E501


        :return: The best_trophies of this Player.  # noqa: E501
        :rtype: int
        """
        return self._best_trophies

    @best_trophies.setter
    def best_trophies(self, best_trophies):
        """Sets the best_trophies of this Player.


        :param best_trophies: The best_trophies of this Player.  # noqa: E501
        :type: int
        """

        self._best_trophies = best_trophies

    @property
    def donations(self):
        """Gets the donations of this Player.  # noqa: E501


        :return: The donations of this Player.  # noqa: E501
        :rtype: int
        """
        return self._donations

    @donations.setter
    def donations(self, donations):
        """Sets the donations of this Player.


        :param donations: The donations of this Player.  # noqa: E501
        :type: int
        """

        self._donations = donations

    @property
    def donations_received(self):
        """Gets the donations_received of this Player.  # noqa: E501


        :return: The donations_received of this Player.  # noqa: E501
        :rtype: int
        """
        return self._donations_received

    @donations_received.setter
    def donations_received(self, donations_received):
        """Sets the donations_received of this Player.


        :param donations_received: The donations_received of this Player.  # noqa: E501
        :type: int
        """

        self._donations_received = donations_received

    @property
    def builder_hall_level(self):
        """Gets the builder_hall_level of this Player.  # noqa: E501


        :return: The builder_hall_level of this Player.  # noqa: E501
        :rtype: int
        """
        return self._builder_hall_level

    @builder_hall_level.setter
    def builder_hall_level(self, builder_hall_level):
        """Sets the builder_hall_level of this Player.


        :param builder_hall_level: The builder_hall_level of this Player.  # noqa: E501
        :type: int
        """

        self._builder_hall_level = builder_hall_level

    @property
    def builder_base_trophies(self):
        """Gets the builder_base_trophies of this Player.  # noqa: E501


        :return: The builder_base_trophies of this Player.  # noqa: E501
        :rtype: int
        """
        return self._builder_base_trophies

    @builder_base_trophies.setter
    def builder_base_trophies(self, builder_base_trophies):
        """Sets the builder_base_trophies of this Player.


        :param builder_base_trophies: The builder_base_trophies of this Player.  # noqa: E501
        :type: int
        """

        self._builder_base_trophies = builder_base_trophies

    @property
    def best_builder_base_trophies(self):
        """Gets the best_builder_base_trophies of this Player.  # noqa: E501


        :return: The best_builder_base_trophies of this Player.  # noqa: E501
        :rtype: int
        """
        return self._best_builder_base_trophies

    @best_builder_base_trophies.setter
    def best_builder_base_trophies(self, best_builder_base_trophies):
        """Sets the best_builder_base_trophies of this Player.


        :param best_builder_base_trophies: The best_builder_base_trophies of this Player.  # noqa: E501
        :type: int
        """

        self._best_builder_base_trophies = best_builder_base_trophies

    @property
    def war_stars(self):
        """Gets the war_stars of this Player.  # noqa: E501


        :return: The war_stars of this Player.  # noqa: E501
        :rtype: int
        """
        return self._war_stars

    @war_stars.setter
    def war_stars(self, war_stars):
        """Sets the war_stars of this Player.


        :param war_stars: The war_stars of this Player.  # noqa: E501
        :type: int
        """

        self._war_stars = war_stars

    @property
    def achievements(self):
        """Gets the achievements of this Player.  # noqa: E501


        :return: The achievements of this Player.  # noqa: E501
        :rtype: PlayerAchievementProgressList
        """
        return self._achievements

    @achievements.setter
    def achievements(self, achievements):
        """Sets the achievements of this Player.


        :param achievements: The achievements of this Player.  # noqa: E501
        :type: PlayerAchievementProgressList
        """

        self._achievements = achievements

    @property
    def clan_capital_contributions(self):
        """Gets the clan_capital_contributions of this Player.  # noqa: E501


        :return: The clan_capital_contributions of this Player.  # noqa: E501
        :rtype: int
        """
        return self._clan_capital_contributions

    @clan_capital_contributions.setter
    def clan_capital_contributions(self, clan_capital_contributions):
        """Sets the clan_capital_contributions of this Player.


        :param clan_capital_contributions: The clan_capital_contributions of this Player.  # noqa: E501
        :type: int
        """

        self._clan_capital_contributions = clan_capital_contributions

    @property
    def player_house(self):
        """Gets the player_house of this Player.  # noqa: E501


        :return: The player_house of this Player.  # noqa: E501
        :rtype: PlayerHouse
        """
        return self._player_house

    @player_house.setter
    def player_house(self, player_house):
        """Sets the player_house of this Player.


        :param player_house: The player_house of this Player.  # noqa: E501
        :type: PlayerHouse
        """

        self._player_house = player_house

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
        if issubclass(Player, dict):
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
        if not isinstance(other, Player):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
