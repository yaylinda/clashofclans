# swagger_client.ClansApi

All URIs are relative to *https://api.clashofclans.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_capital_raid_seasons**](ClansApi.md#get_capital_raid_seasons) | **GET** /clans/{clanTag}/capitalraidseasons | Retrieve clan&#x27;s capital raid seasons
[**get_clan**](ClansApi.md#get_clan) | **GET** /clans/{clanTag} | Get clan information
[**get_clan_members**](ClansApi.md#get_clan_members) | **GET** /clans/{clanTag}/members | List clan members
[**get_clan_war_league_group**](ClansApi.md#get_clan_war_league_group) | **GET** /clans/{clanTag}/currentwar/leaguegroup | Retrieve information about clan&#x27;s current clan war league group
[**get_clan_war_league_war**](ClansApi.md#get_clan_war_league_war) | **GET** /clanwarleagues/wars/{warTag} | Retrieve information about individual clan war league war
[**get_clan_war_log**](ClansApi.md#get_clan_war_log) | **GET** /clans/{clanTag}/warlog | Retrieve clan&#x27;s clan war log
[**get_current_war**](ClansApi.md#get_current_war) | **GET** /clans/{clanTag}/currentwar | Retrieve information about clan&#x27;s current clan war
[**search_clans**](ClansApi.md#search_clans) | **GET** /clans | Search clans

# **get_capital_raid_seasons**
> ClanCapitalRaidSeasons get_capital_raid_seasons(clan_tag, limit=limit, after=after, before=before)

Retrieve clan's capital raid seasons

Retrieve clan's capital raid seasons

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
api_instance = swagger_client.ClansApi(swagger_client.ApiClient(configuration))
clan_tag = 'clan_tag_example' # str | Tag of the clan.
limit = 56 # int | Limit the number of items returned in the response. (optional)
after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

try:
    # Retrieve clan's capital raid seasons
    api_response = api_instance.get_capital_raid_seasons(clan_tag, limit=limit, after=after, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClansApi->get_capital_raid_seasons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_tag** | **str**| Tag of the clan. | 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**ClanCapitalRaidSeasons**](ClanCapitalRaidSeasons.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clan**
> Clan get_clan(clan_tag)

Get clan information

Get information about a single clan by clan tag. Clan tags can be found using clan search operation. Note that clan tags start with hash character '#' and that needs to be URL-encoded properly to work in URL, so for example clan tag '#2ABC' would become '%232ABC' in the URL. 

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
api_instance = swagger_client.ClansApi(swagger_client.ApiClient(configuration))
clan_tag = 'clan_tag_example' # str | Tag of the clan.

try:
    # Get clan information
    api_response = api_instance.get_clan(clan_tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClansApi->get_clan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_tag** | **str**| Tag of the clan. | 

### Return type

[**Clan**](Clan.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clan_members**
> ClanMemberList get_clan_members(clan_tag, limit=limit, after=after, before=before)

List clan members

List clan members.

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
api_instance = swagger_client.ClansApi(swagger_client.ApiClient(configuration))
clan_tag = 'clan_tag_example' # str | Tag of the clan.
limit = 56 # int | Limit the number of items returned in the response. (optional)
after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

try:
    # List clan members
    api_response = api_instance.get_clan_members(clan_tag, limit=limit, after=after, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClansApi->get_clan_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_tag** | **str**| Tag of the clan. | 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**ClanMemberList**](ClanMemberList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clan_war_league_group**
> ClanWarLeagueGroup get_clan_war_league_group(clan_tag)

Retrieve information about clan's current clan war league group

Retrieve information about clan's current clan war league group

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
api_instance = swagger_client.ClansApi(swagger_client.ApiClient(configuration))
clan_tag = 'clan_tag_example' # str | Tag of the clan.

try:
    # Retrieve information about clan's current clan war league group
    api_response = api_instance.get_clan_war_league_group(clan_tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClansApi->get_clan_war_league_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_tag** | **str**| Tag of the clan. | 

### Return type

[**ClanWarLeagueGroup**](ClanWarLeagueGroup.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clan_war_league_war**
> ClanWarLeagueGroup get_clan_war_league_war(war_tag)

Retrieve information about individual clan war league war

Retrieve information about individual clan war league war

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
api_instance = swagger_client.ClansApi(swagger_client.ApiClient(configuration))
war_tag = 'war_tag_example' # str | Tag of the war.

try:
    # Retrieve information about individual clan war league war
    api_response = api_instance.get_clan_war_league_war(war_tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClansApi->get_clan_war_league_war: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **war_tag** | **str**| Tag of the war. | 

### Return type

[**ClanWarLeagueGroup**](ClanWarLeagueGroup.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clan_war_log**
> ClanWarLog get_clan_war_log(clan_tag, limit=limit, after=after, before=before)

Retrieve clan's clan war log

Retrieve clan's clan war log

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
api_instance = swagger_client.ClansApi(swagger_client.ApiClient(configuration))
clan_tag = 'clan_tag_example' # str | Tag of the clan.
limit = 56 # int | Limit the number of items returned in the response. (optional)
after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

try:
    # Retrieve clan's clan war log
    api_response = api_instance.get_clan_war_log(clan_tag, limit=limit, after=after, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClansApi->get_clan_war_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_tag** | **str**| Tag of the clan. | 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**ClanWarLog**](ClanWarLog.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_war**
> ClanWar get_current_war(clan_tag)

Retrieve information about clan's current clan war

Retrieve information about clan's current clan war

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
api_instance = swagger_client.ClansApi(swagger_client.ApiClient(configuration))
clan_tag = 'clan_tag_example' # str | Tag of the clan.

try:
    # Retrieve information about clan's current clan war
    api_response = api_instance.get_current_war(clan_tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClansApi->get_current_war: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_tag** | **str**| Tag of the clan. | 

### Return type

[**ClanWar**](ClanWar.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_clans**
> ClanList search_clans(name=name, war_frequency=war_frequency, location_id=location_id, min_members=min_members, max_members=max_members, min_clan_points=min_clan_points, min_clan_level=min_clan_level, limit=limit, after=after, before=before, label_ids=label_ids)

Search clans

Search all clans by name and/or filtering the results using various criteria. At least one filtering criteria must be defined and if name is used as part of search, it is required to be at least three characters long. It is not possible to specify ordering for results so clients should not rely on any specific ordering as that may change in the future releases of the API. 

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
api_instance = swagger_client.ClansApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Search clans by name. If name is used as part of search query, it needs to be at least three characters long. Name search parameter is interpreted as wild card search, so it may appear anywhere in the clan name.  (optional)
war_frequency = 'war_frequency_example' # str | Filter by clan war frequency (optional)
location_id = 56 # int | Filter by clan location identifier. For list of available locations, refer to getLocations operation.  (optional)
min_members = 56 # int | Filter by minimum number of clan members (optional)
max_members = 56 # int | Filter by maximum number of clan members (optional)
min_clan_points = 56 # int | Filter by minimum amount of clan points. (optional)
min_clan_level = 56 # int | Filter by minimum clan level. (optional)
limit = 56 # int | Limit the number of items returned in the response. (optional)
after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
label_ids = 'label_ids_example' # str | Comma separatered list of label IDs to use for filtering results. (optional)

try:
    # Search clans
    api_response = api_instance.search_clans(name=name, war_frequency=war_frequency, location_id=location_id, min_members=min_members, max_members=max_members, min_clan_points=min_clan_points, min_clan_level=min_clan_level, limit=limit, after=after, before=before, label_ids=label_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClansApi->search_clans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Search clans by name. If name is used as part of search query, it needs to be at least three characters long. Name search parameter is interpreted as wild card search, so it may appear anywhere in the clan name.  | [optional] 
 **war_frequency** | **str**| Filter by clan war frequency | [optional] 
 **location_id** | **int**| Filter by clan location identifier. For list of available locations, refer to getLocations operation.  | [optional] 
 **min_members** | **int**| Filter by minimum number of clan members | [optional] 
 **max_members** | **int**| Filter by maximum number of clan members | [optional] 
 **min_clan_points** | **int**| Filter by minimum amount of clan points. | [optional] 
 **min_clan_level** | **int**| Filter by minimum clan level. | [optional] 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **label_ids** | **str**| Comma separatered list of label IDs to use for filtering results. | [optional] 

### Return type

[**ClanList**](ClanList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

