# coding: utf-8

# flake8: noqa
"""
    Clash of Clans API

    Check out <a href=\"https://developer.clashofclans.com/#/getting-started\" target=\"_parent\">Getting Started</a> for instructions and links to other resources. Clash of Clans API uses <a href=\"https://jwt.io/\" target=\"_blank\">JSON Web Tokens</a> for authorizing the requests. Tokens are created by developers on <a href=\"https://developer.clashofclans.com/#/account\" target=\"_parent\">My Account</a> page and must be passed in every API request in Authorization HTTP header using Bearer authentication scheme. Correct Authorization header looks like this: \"Authorization: Bearer API_TOKEN\".   # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from swagger_client.models.builder_base_league import BuilderBaseLeague
from swagger_client.models.builder_base_league_list import BuilderBaseLeagueList
from swagger_client.models.capital_league import CapitalLeague
from swagger_client.models.capital_league_list import CapitalLeagueList
from swagger_client.models.clan import Clan
from swagger_client.models.clan_builder_base_ranking import ClanBuilderBaseRanking
from swagger_client.models.clan_builder_base_ranking_list import ClanBuilderBaseRankingList
from swagger_client.models.clan_capital import ClanCapital
from swagger_client.models.clan_capital_raid_season import ClanCapitalRaidSeason
from swagger_client.models.clan_capital_raid_season_attack import ClanCapitalRaidSeasonAttack
from swagger_client.models.clan_capital_raid_season_attack_list import ClanCapitalRaidSeasonAttackList
from swagger_client.models.clan_capital_raid_season_attack_log_entry import ClanCapitalRaidSeasonAttackLogEntry
from swagger_client.models.clan_capital_raid_season_attack_log_list import ClanCapitalRaidSeasonAttackLogList
from swagger_client.models.clan_capital_raid_season_attacker import ClanCapitalRaidSeasonAttacker
from swagger_client.models.clan_capital_raid_season_clan_info import ClanCapitalRaidSeasonClanInfo
from swagger_client.models.clan_capital_raid_season_defense_log_entry import ClanCapitalRaidSeasonDefenseLogEntry
from swagger_client.models.clan_capital_raid_season_defense_log_list import ClanCapitalRaidSeasonDefenseLogList
from swagger_client.models.clan_capital_raid_season_district import ClanCapitalRaidSeasonDistrict
from swagger_client.models.clan_capital_raid_season_district_list import ClanCapitalRaidSeasonDistrictList
from swagger_client.models.clan_capital_raid_season_member import ClanCapitalRaidSeasonMember
from swagger_client.models.clan_capital_raid_season_member_list import ClanCapitalRaidSeasonMemberList
from swagger_client.models.clan_capital_raid_seasons import ClanCapitalRaidSeasons
from swagger_client.models.clan_capital_ranking import ClanCapitalRanking
from swagger_client.models.clan_capital_ranking_list import ClanCapitalRankingList
from swagger_client.models.clan_district_data import ClanDistrictData
from swagger_client.models.clan_district_data_list import ClanDistrictDataList
from swagger_client.models.clan_list import ClanList
from swagger_client.models.clan_member import ClanMember
from swagger_client.models.clan_member_list import ClanMemberList
from swagger_client.models.clan_ranking import ClanRanking
from swagger_client.models.clan_ranking_list import ClanRankingList
from swagger_client.models.clan_war import ClanWar
from swagger_client.models.clan_war_attack import ClanWarAttack
from swagger_client.models.clan_war_attack_list import ClanWarAttackList
from swagger_client.models.clan_war_league_clan import ClanWarLeagueClan
from swagger_client.models.clan_war_league_clan_list import ClanWarLeagueClanList
from swagger_client.models.clan_war_league_clan_member import ClanWarLeagueClanMember
from swagger_client.models.clan_war_league_clan_member_list import ClanWarLeagueClanMemberList
from swagger_client.models.clan_war_league_group import ClanWarLeagueGroup
from swagger_client.models.clan_war_league_round import ClanWarLeagueRound
from swagger_client.models.clan_war_league_round_list import ClanWarLeagueRoundList
from swagger_client.models.clan_war_log import ClanWarLog
from swagger_client.models.clan_war_log_entry import ClanWarLogEntry
from swagger_client.models.clan_war_member import ClanWarMember
from swagger_client.models.clan_war_member_list import ClanWarMemberList
from swagger_client.models.client_error import ClientError
from swagger_client.models.deep_link_creation_request import DeepLinkCreationRequest
from swagger_client.models.deep_link_creation_response import DeepLinkCreationResponse
from swagger_client.models.gold_pass_season import GoldPassSeason
from swagger_client.models.json_localized_name import JsonLocalizedName
from swagger_client.models.json_node import JsonNode
from swagger_client.models.label import Label
from swagger_client.models.label_list import LabelList
from swagger_client.models.language import Language
from swagger_client.models.league import League
from swagger_client.models.league_list import LeagueList
from swagger_client.models.league_season import LeagueSeason
from swagger_client.models.league_season_list import LeagueSeasonList
from swagger_client.models.legend_league_tournament_season_result import LegendLeagueTournamentSeasonResult
from swagger_client.models.location import Location
from swagger_client.models.location_list import LocationList
from swagger_client.models.model_float import ModelFloat
from swagger_client.models.player import Player
from swagger_client.models.player_achievement_progress import PlayerAchievementProgress
from swagger_client.models.player_achievement_progress_list import PlayerAchievementProgressList
from swagger_client.models.player_builder_base_ranking import PlayerBuilderBaseRanking
from swagger_client.models.player_builder_base_ranking_list import PlayerBuilderBaseRankingList
from swagger_client.models.player_clan import PlayerClan
from swagger_client.models.player_house import PlayerHouse
from swagger_client.models.player_house_element import PlayerHouseElement
from swagger_client.models.player_house_element_list import PlayerHouseElementList
from swagger_client.models.player_item_level import PlayerItemLevel
from swagger_client.models.player_item_level_list import PlayerItemLevelList
from swagger_client.models.player_legend_statistics import PlayerLegendStatistics
from swagger_client.models.player_ranking import PlayerRanking
from swagger_client.models.player_ranking_clan import PlayerRankingClan
from swagger_client.models.player_ranking_list import PlayerRankingList
from swagger_client.models.replay import Replay
from swagger_client.models.service_version import ServiceVersion
from swagger_client.models.string import String
from swagger_client.models.string_list import StringList
from swagger_client.models.verify_token_request import VerifyTokenRequest
from swagger_client.models.verify_token_response import VerifyTokenResponse
from swagger_client.models.war_clan import WarClan
from swagger_client.models.war_league import WarLeague
from swagger_client.models.war_league_list import WarLeagueList
from swagger_client.models.war_status import WarStatus
from swagger_client.models.war_status_list import WarStatusList
