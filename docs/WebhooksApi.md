# MimePost.WebhooksApi

All URIs are relative to *https://api.mimepost.com/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhooks_get**](WebhooksApi.md#webhooks_get) | **GET** /webhooks/ | Get the list of all the webhooks
[**webhooks_id_delete**](WebhooksApi.md#webhooks_id_delete) | **DELETE** /webhooks/{id} | Remove a single webhook
[**webhooks_id_get**](WebhooksApi.md#webhooks_id_get) | **GET** /webhooks/{id} | Get the details of a single webhook
[**webhooks_id_put**](WebhooksApi.md#webhooks_id_put) | **PUT** /webhooks/{id} | Update the details of a single webhook
[**webhooks_post**](WebhooksApi.md#webhooks_post) | **POST** /webhooks/ | Add single webhook


# **webhooks_get**
> ApiResponseAllWebhooks webhooks_get()

Get the list of all the webhooks

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
api_instance = MimePost.WebhooksApi(MimePost.ApiClient(configuration))

try:
    # Get the list of all the webhooks
    api_response = api_instance.webhooks_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiResponseAllWebhooks**](ApiResponseAllWebhooks.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_id_delete**
> ApiResponse webhooks_id_delete(id)

Remove a single webhook

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
api_instance = MimePost.WebhooksApi(MimePost.ApiClient(configuration))
id = 56 # int | 

try:
    # Remove a single webhook
    api_response = api_instance.webhooks_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_id_get**
> ApiResponseSingleWebhooks webhooks_id_get(id)

Get the details of a single webhook

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
api_instance = MimePost.WebhooksApi(MimePost.ApiClient(configuration))
id = 56 # int | 

try:
    # Get the details of a single webhook
    api_response = api_instance.webhooks_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ApiResponseSingleWebhooks**](ApiResponseSingleWebhooks.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_id_put**
> ApiResponseSingleWebhooks webhooks_id_put(id, webhook=webhook)

Update the details of a single webhook

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
api_instance = MimePost.WebhooksApi(MimePost.ApiClient(configuration))
id = 56 # int | 
webhook = MimePost.Webhook1() # Webhook1 |  (optional)

try:
    # Update the details of a single webhook
    api_response = api_instance.webhooks_id_put(id, webhook=webhook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **webhook** | [**Webhook1**](Webhook1.md)|  | [optional] 

### Return type

[**ApiResponseSingleWebhooks**](ApiResponseSingleWebhooks.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_post**
> ApiResponseWebhooks webhooks_post(webhook=webhook)

Add single webhook

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
api_instance = MimePost.WebhooksApi(MimePost.ApiClient(configuration))
webhook = MimePost.Webhook() # Webhook |  (optional)

try:
    # Add single webhook
    api_response = api_instance.webhooks_post(webhook=webhook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook** | [**Webhook**](Webhook.md)|  | [optional] 

### Return type

[**ApiResponseWebhooks**](ApiResponseWebhooks.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

