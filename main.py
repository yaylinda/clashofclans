# This is a sample Python script.
import requests
import urllib.parse


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    # Your Bearer token
    # token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjcyOGViMzQ0LTNkOGEtNGMwMi1hNTIyLTg4NjJkZjE5ZjcxZCIsImlhdCI6MTcwMzI5MTc0MCwic3ViIjoiZGV2ZWxvcGVyLzhkZGRiZmVmLWM5ODUtYTA1MC0xMDg5LWU2ZjhjYWQ4Yjk5YyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjY1LjM2LjYzLjE2MiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.LfqXmE3yvlrcfTWls3CX6tXXPDjQPqbkuPutaqmhDlfqHF7n00Q4PNTUvywphyZoYw41nsivAfrrwH6KQZ7GSA'
    # token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImRkOTBiMGUwLTdlNTMtNDA5Yy05MDJiLWVkNzBmNGU1ODA1ZSIsImlhdCI6MTcwMzI5MTQyNSwic3ViIjoiZGV2ZWxvcGVyLzhkZGRiZmVmLWM5ODUtYTA1MC0xMDg5LWU2ZjhjYWQ4Yjk5YyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjAuMC4wLjAiXSwidHlwZSI6ImNsaWVudCJ9XX0.os0llMhrB-ZhiJDqXrgv2HJOOHGtGiM2gG-JxaYMXrBumFbFejIjHAFB_fp-Y-TEvanCDShvb6mgXaIhSu77_A'
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImU2YTZmYmMwLTJlNmYtNDcwNi04YjY3LTA4ZWNkNTk0NDFiOSIsImlhdCI6MTcwMzI5MjUyNCwic3ViIjoiZGV2ZWxvcGVyLzhkZGRiZmVmLWM5ODUtYTA1MC0xMDg5LWU2ZjhjYWQ4Yjk5YyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjY1LjM2LjYzLjE2MiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.UcvXbd4CZTwRZBzsdbz4aCKbxByv9kWekHge3GcR-cCq8Oy1VzmlMsi3rkvrwmrqDI21wyBCI4zpz1LYBJqr7w'

    # Your actual parameter here
    param = '#28G2Y9L8Y'
    escaped_param = urllib.parse.quote(param)  # URL encoding

    # Here we create the full URL including the path parameter
    url = f'https://api.clashofclans.com/v1/clans/{escaped_param}/warlog'
    # url = f'https://api.clashofclans.com/v1/clans/{escaped_param}/currentwar'
    # url = f'https://api.clashofclans.com/v1/clans/{escaped_param}'

    # We create the headers with the bearer token
    headers = {
        'Authorization': f'Bearer {token}'
    }

    # We make the GET request
    response = requests.get(url, headers=headers)

    # You can process the response here
    print(response.json())
    print(response.headers)
    print(response.url)
    print(response.reason)
    print(response.status_code)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
