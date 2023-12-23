from pprint import pprint

import swagger_client
from swagger_client.rest import ApiException

CLAN_TAG = '#28G2Y9L8Y'


def main(api_client: swagger_client.ApiClient):
    clans_api = swagger_client.ClansApi(api_client)

    try:
        # Get clan information
        api_response = clans_api.get_clan(CLAN_TAG)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClansApi->get_clan: %s\n" % e)


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
