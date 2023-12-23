# swagger_client.PlayersApi

All URIs are relative to *https://api.clashofclans.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player**](PlayersApi.md#get_player) | **GET** /players/{playerTag} | Get player information
[**verify_token**](PlayersApi.md#verify_token) | **POST** /players/{playerTag}/verifytoken | Verify player API token that can be found from the game settings.

# **get_player**
> Player get_player(player_tag)

Get player information

Get information about a single player by player tag. Player tags can be found either in game or by from clan member lists. Note that player tags start with hash character '#' and that needs to be URL-encoded properly to work in URL, so for example player tag '#2ABC' would become '%232ABC' in the URL. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = swagger_client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PlayersApi(swagger_client.ApiClient(configuration))
player_tag = 'player_tag_example' # str | Tag of the player.

try:
    # Get player information
    api_response = api_instance.get_player(player_tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->get_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_tag** | **str**| Tag of the player. | 

### Return type

[**Player**](Player.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_token**
> VerifyTokenResponse verify_token(body, player_tag)

Verify player API token that can be found from the game settings.

Verify player API token that can be found from the game settings. This API call can be used to check that players own the game accounts they claim to own as they need to provide the one-time use API token that exists inside the game. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = swagger_client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PlayersApi(swagger_client.ApiClient(configuration))
body = swagger_client.VerifyTokenRequest() # VerifyTokenRequest | Request body
player_tag = 'player_tag_example' # str | Tag of the player.

try:
    # Verify player API token that can be found from the game settings.
    api_response = api_instance.verify_token(body, player_tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->verify_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyTokenRequest**](VerifyTokenRequest.md)| Request body | 
 **player_tag** | **str**| Tag of the player. | 

### Return type

[**VerifyTokenResponse**](VerifyTokenResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

