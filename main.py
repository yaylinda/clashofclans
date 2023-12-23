from pprint import pprint
from typing import List

import swagger_client
from swagger_client import ClanMemberList, ClansApi, ClanMember, ClanWarLogEntry
from swagger_client.rest import ApiException

CLAN_TAG = '#28G2Y9L8Y'


def get_members(clans_api: ClansApi) -> List[ClanMember]:
    data = clans_api.get_clan_members(CLAN_TAG)

    members: List[ClanMember] = []

    for item in data['items']:
        members.append(item)

    return members


def get_war_log(clans_api: ClansApi) -> List[ClanWarLogEntry]:
    data = clans_api.get_clan_war_log(CLAN_TAG)

    war_log: List[ClanWarLogEntry] = []

    for item in data['items']:
        war_log.append(item)

    return war_log


def main(api_client: swagger_client.ApiClient):
    members = get_members(swagger_client.ClansApi(api_client))
    war_log = get_war_log(swagger_client.ClansApi(api_client))

    pprint(war_log[0].clan.members)


if __name__ == '__main__':
    # It's okay (but bad practice) to have this token in the code.
    # But since this token only works with my local IP address, it's okay for now.
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImU2YTZmYmMwLTJlNmYtNDcwNi04YjY3LTA4ZWNkNTk0NDFiOSIsImlhdCI6MTcwMzI5MjUyNCwic3ViIjoiZGV2ZWxvcGVyLzhkZGRiZmVmLWM5ODUtYTA1MC0xMDg5LWU2ZjhjYWQ4Yjk5YyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjY1LjM2LjYzLjE2MiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.UcvXbd4CZTwRZBzsdbz4aCKbxByv9kWekHge3GcR-cCq8Oy1VzmlMsi3rkvrwmrqDI21wyBCI4zpz1LYBJqr7w'

    # Set up api client config with bearer auth
    configuration = swagger_client.Configuration()
    configuration.api_key['authorization'] = token
    configuration.api_key_prefix['authorization'] = 'Bearer'
    api_client = swagger_client.ApiClient(configuration)

    main(api_client)
