from pprint import pprint

import swagger_client
from swagger_client import ClanMemberList
from swagger_client.rest import ApiException

CLAN_TAG = '#28G2Y9L8Y'


def main(api_client: swagger_client.ApiClient):
    clans_api = swagger_client.ClansApi(api_client)

    data = clans_api.get_clan_members(CLAN_TAG)

    people = []

    for key in data:
        person = {}
        for item in data[key]:
            people['name'] = item['name']
            people['donations'] = item['donations']
            people['donationsReceived'] = item['donationsReceived']
            people['role'] = item['role']
            people['tag'] = item['tag']
            people['townHallLevel'] = item['townHallLevel']
            people['trophies'] = item['trophies']
        people.append(person)

    pprint(people)



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
