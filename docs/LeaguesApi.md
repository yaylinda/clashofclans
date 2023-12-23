# swagger_client.LeaguesApi

All URIs are relative to *https://api.clashofclans.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_builder_base_league**](LeaguesApi.md#get_builder_base_league) | **GET** /builderbaseleagues/{leagueId} | Get Builder Base league information
[**get_builder_base_leagues**](LeaguesApi.md#get_builder_base_leagues) | **GET** /builderbaseleagues | List Builder Base leagues
[**get_capital_league**](LeaguesApi.md#get_capital_league) | **GET** /capitalleagues/{leagueId} | Get capital league information
[**get_capital_leagues**](LeaguesApi.md#get_capital_leagues) | **GET** /capitalleagues | List capital leagues
[**get_league**](LeaguesApi.md#get_league) | **GET** /leagues/{leagueId} | Get league information
[**get_league_season_rankings**](LeaguesApi.md#get_league_season_rankings) | **GET** /leagues/{leagueId}/seasons/{seasonId} | Get league season rankings
[**get_league_seasons**](LeaguesApi.md#get_league_seasons) | **GET** /leagues/{leagueId}/seasons | Get league seasons
[**get_leagues**](LeaguesApi.md#get_leagues) | **GET** /leagues | List leagues
[**get_war_league**](LeaguesApi.md#get_war_league) | **GET** /warleagues/{leagueId} | Get war league information
[**get_war_leagues**](LeaguesApi.md#get_war_leagues) | **GET** /warleagues | List war leagues

# **get_builder_base_league**
> BuilderBaseLeague get_builder_base_league(league_id)

Get Builder Base league information

Get Builder Base league information

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
api_instance = swagger_client.LeaguesApi(swagger_client.ApiClient(configuration))
league_id = 'league_id_example' # str | Identifier of the league.

try:
    # Get Builder Base league information
    api_response = api_instance.get_builder_base_league(league_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaguesApi->get_builder_base_league: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **str**| Identifier of the league. | 

### Return type

[**BuilderBaseLeague**](BuilderBaseLeague.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_builder_base_leagues**
> BuilderBaseLeagueList get_builder_base_leagues(limit=limit, after=after, before=before)

List Builder Base leagues

List Builder Base leagues

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
api_instance = swagger_client.LeaguesApi(swagger_client.ApiClient(configuration))
limit = 56 # int | Limit the number of items returned in the response. (optional)
after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

try:
    # List Builder Base leagues
    api_response = api_instance.get_builder_base_leagues(limit=limit, after=after, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaguesApi->get_builder_base_leagues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**BuilderBaseLeagueList**](BuilderBaseLeagueList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_capital_league**
> CapitalLeague get_capital_league(league_id)

Get capital league information

Get capital league information

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
api_instance = swagger_client.LeaguesApi(swagger_client.ApiClient(configuration))
league_id = 'league_id_example' # str | Identifier of the league.

try:
    # Get capital league information
    api_response = api_instance.get_capital_league(league_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaguesApi->get_capital_league: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **str**| Identifier of the league. | 

### Return type

[**CapitalLeague**](CapitalLeague.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_capital_leagues**
> CapitalLeagueList get_capital_leagues(limit=limit, after=after, before=before)

List capital leagues

List capital leagues

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
api_instance = swagger_client.LeaguesApi(swagger_client.ApiClient(configuration))
limit = 56 # int | Limit the number of items returned in the response. (optional)
after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

try:
    # List capital leagues
    api_response = api_instance.get_capital_leagues(limit=limit, after=after, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaguesApi->get_capital_leagues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**CapitalLeagueList**](CapitalLeagueList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_league**
> League get_league(league_id)

Get league information

Get league information

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
api_instance = swagger_client.LeaguesApi(swagger_client.ApiClient(configuration))
league_id = 'league_id_example' # str | Identifier of the league.

try:
    # Get league information
    api_response = api_instance.get_league(league_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaguesApi->get_league: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **str**| Identifier of the league. | 

### Return type

[**League**](League.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_league_season_rankings**
> PlayerRankingList get_league_season_rankings(league_id, season_id, limit=limit, after=after, before=before)

Get league season rankings

Get league season rankings. Note that league season information is available only for Legend League. 

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
api_instance = swagger_client.LeaguesApi(swagger_client.ApiClient(configuration))
league_id = 'league_id_example' # str | Identifier of the league.
season_id = 'season_id_example' # str | Identifier of the season.
limit = 56 # int | Limit the number of items returned in the response. (optional)
after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

try:
    # Get league season rankings
    api_response = api_instance.get_league_season_rankings(league_id, season_id, limit=limit, after=after, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaguesApi->get_league_season_rankings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **str**| Identifier of the league. | 
 **season_id** | **str**| Identifier of the season. | 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**PlayerRankingList**](PlayerRankingList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_league_seasons**
> LeagueSeasonList get_league_seasons(league_id, limit=limit, after=after, before=before)

Get league seasons

Get league seasons. Note that league season information is available only for Legend League. 

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
api_instance = swagger_client.LeaguesApi(swagger_client.ApiClient(configuration))
league_id = 'league_id_example' # str | Identifier of the league.
limit = 56 # int | Limit the number of items returned in the response. (optional)
after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

try:
    # Get league seasons
    api_response = api_instance.get_league_seasons(league_id, limit=limit, after=after, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaguesApi->get_league_seasons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **str**| Identifier of the league. | 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**LeagueSeasonList**](LeagueSeasonList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leagues**
> LeagueList get_leagues(limit=limit, after=after, before=before)

List leagues

List leagues

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
api_instance = swagger_client.LeaguesApi(swagger_client.ApiClient(configuration))
limit = 56 # int | Limit the number of items returned in the response. (optional)
after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

try:
    # List leagues
    api_response = api_instance.get_leagues(limit=limit, after=after, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaguesApi->get_leagues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**LeagueList**](LeagueList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_war_league**
> WarLeague get_war_league(league_id)

Get war league information

Get war league information

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
api_instance = swagger_client.LeaguesApi(swagger_client.ApiClient(configuration))
league_id = 'league_id_example' # str | Identifier of the league.

try:
    # Get war league information
    api_response = api_instance.get_war_league(league_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaguesApi->get_war_league: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **str**| Identifier of the league. | 

### Return type

[**WarLeague**](WarLeague.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_war_leagues**
> WarLeagueList get_war_leagues(limit=limit, after=after, before=before)

List war leagues

List war leagues

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
api_instance = swagger_client.LeaguesApi(swagger_client.ApiClient(configuration))
limit = 56 # int | Limit the number of items returned in the response. (optional)
after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

try:
    # List war leagues
    api_response = api_instance.get_war_leagues(limit=limit, after=after, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaguesApi->get_war_leagues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**WarLeagueList**](WarLeagueList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

