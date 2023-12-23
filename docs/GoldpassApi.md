# swagger_client.GoldpassApi

All URIs are relative to *https://api.clashofclans.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_gold_pass_season**](GoldpassApi.md#get_current_gold_pass_season) | **GET** /goldpass/seasons/current | Get information about the current gold pass season.

# **get_current_gold_pass_season**
> GoldPassSeason get_current_gold_pass_season()

Get information about the current gold pass season.

Get information about the current gold pass season.

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
api_instance = swagger_client.GoldpassApi(swagger_client.ApiClient(configuration))

try:
    # Get information about the current gold pass season.
    api_response = api_instance.get_current_gold_pass_season()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoldpassApi->get_current_gold_pass_season: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GoldPassSeason**](GoldPassSeason.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

