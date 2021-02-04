# MimePost.AccountsApi

All URIs are relative to *https://api.mimepost.com/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_profile_get**](AccountsApi.md#account_profile_get) | **GET** /account/profile/ | Get account profile details
[**account_profile_post**](AccountsApi.md#account_profile_post) | **POST** /account/profile/ | Update account profile details
[**settings_get**](AccountsApi.md#settings_get) | **GET** /settings/ | Get all the settings
[**settings_post**](AccountsApi.md#settings_post) | **POST** /settings/ | Set a setting


# **account_profile_get**
> AccountProfileResponse account_profile_get()

Get account profile details



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
api_instance = MimePost.AccountsApi(MimePost.ApiClient(configuration))

try:
    # Get account profile details
    api_response = api_instance.account_profile_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->account_profile_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountProfileResponse**](AccountProfileResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_profile_post**
> ApiResponse account_profile_post(body)

Update account profile details



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
api_instance = MimePost.AccountsApi(MimePost.ApiClient(configuration))
body = MimePost.AccountProfile() # AccountProfile | 

try:
    # Update account profile details
    api_response = api_instance.account_profile_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->account_profile_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountProfile**](AccountProfile.md)|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_get**
> AccountSettings settings_get()

Get all the settings



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
api_instance = MimePost.AccountsApi(MimePost.ApiClient(configuration))

try:
    # Get all the settings
    api_response = api_instance.settings_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->settings_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountSettings**](AccountSettings.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_post**
> ApiResponse settings_post(body)

Set a setting



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
api_instance = MimePost.AccountsApi(MimePost.ApiClient(configuration))
body = MimePost.AccountSettings() # AccountSettings | 

try:
    # Set a setting
    api_response = api_instance.settings_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->settings_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountSettings**](AccountSettings.md)|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

