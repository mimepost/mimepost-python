# MimePost.StatsApi

All URIs are relative to *https://api.mimepost.com/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**emaillogs_get**](StatsApi.md#emaillogs_get) | **GET** /emaillogs/ | Get the logs of a particular date
[**stats_get**](StatsApi.md#stats_get) | **GET** /stats/ | Get the summary of stats for a range of dates


# **emaillogs_get**
> ApiResponseEmaillogs emaillogs_get(start_date, end_date, status=status, to=to, page=page, limit=limit)

Get the logs of a particular date

### Example
```python
from __future__ import print_function
import time
import MimePost
from MimePost.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = MimePost.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = MimePost.StatsApi(MimePost.ApiClient(configuration))
start_date = 'start_date_example' # str | Start Date in yyyymmdd format example 20190801
end_date = 'end_date_example' # str | End Date in yyyymmdd format example 20190803
status = 'status_example' # str |  (optional)
to = 'to_example' # str |  (optional)
page = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    # Get the logs of a particular date
    api_response = api_instance.emaillogs_get(start_date, end_date, status=status, to=to, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->emaillogs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Start Date in yyyymmdd format example 20190801 | 
 **end_date** | **str**| End Date in yyyymmdd format example 20190803 | 
 **status** | **str**|  | [optional] 
 **to** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**ApiResponseEmaillogs**](ApiResponseEmaillogs.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats_get**
> ApiResponseStats stats_get(start_date, end_date)

Get the summary of stats for a range of dates

### Example
```python
from __future__ import print_function
import time
import MimePost
from MimePost.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = MimePost.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = MimePost.StatsApi(MimePost.ApiClient(configuration))
start_date = 'start_date_example' # str | Start Date in yyyymmdd format example 20190801
end_date = 'end_date_example' # str | End Date in yyyymmdd format example 20190803

try:
    # Get the summary of stats for a range of dates
    api_response = api_instance.stats_get(start_date, end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->stats_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Start Date in yyyymmdd format example 20190801 | 
 **end_date** | **str**| End Date in yyyymmdd format example 20190803 | 

### Return type

[**ApiResponseStats**](ApiResponseStats.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

