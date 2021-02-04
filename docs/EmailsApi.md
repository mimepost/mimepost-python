# MimePost.EmailsApi

All URIs are relative to *https://api.mimepost.com/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_email**](EmailsApi.md#send_email) | **POST** /emails/ | Send email


# **send_email**
> ApiResponse send_email(body)

Send email



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
api_instance = MimePost.EmailsApi(MimePost.ApiClient(configuration))
body = MimePost.Email() # Email | Single Email object 

try:
    # Send email
    api_response = api_instance.send_email(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailsApi->send_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Email**](Email.md)| Single Email object  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

