# MimePost.DomainsApi

All URIs are relative to *https://api.mimepost.com/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domains_get**](DomainsApi.md#domains_get) | **GET** /domains/ | Get a list of all the domains
[**domains_id_approve_post**](DomainsApi.md#domains_id_approve_post) | **POST** /domains/{id}/approve/ | Submit request for the approval of a verified domain
[**domains_id_delete**](DomainsApi.md#domains_id_delete) | **DELETE** /domains/{id} | Remove a single domain
[**domains_id_get**](DomainsApi.md#domains_id_get) | **GET** /domains/{id} | Get the details of a single domain
[**domains_id_verify_dkim_post**](DomainsApi.md#domains_id_verify_dkim_post) | **POST** /domains/{id}/verify_dkim/ | Request for the verification of DKIM record for a single domain
[**domains_id_verify_spf_post**](DomainsApi.md#domains_id_verify_spf_post) | **POST** /domains/{id}/verify_spf/ | Request for the verification of SPF record for a single domain
[**domains_id_verify_tracking_post**](DomainsApi.md#domains_id_verify_tracking_post) | **POST** /domains/{id}/verify_tracking/ | Request for the verification of tracking record for a single domain
[**domains_post**](DomainsApi.md#domains_post) | **POST** /domains/ | Add single domain


# **domains_get**
> ApiResponseDomainsList domains_get()

Get a list of all the domains

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
api_instance = MimePost.DomainsApi(MimePost.ApiClient(configuration))

try:
    # Get a list of all the domains
    api_response = api_instance.domains_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiResponseDomainsList**](ApiResponseDomainsList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_id_approve_post**
> ApiResponse domains_id_approve_post(id)

Submit request for the approval of a verified domain

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
api_instance = MimePost.DomainsApi(MimePost.ApiClient(configuration))
id = 56 # int | 

try:
    # Submit request for the approval of a verified domain
    api_response = api_instance.domains_id_approve_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_id_approve_post: %s\n" % e)
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

# **domains_id_delete**
> ApiResponse domains_id_delete(id)

Remove a single domain

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
api_instance = MimePost.DomainsApi(MimePost.ApiClient(configuration))
id = 56 # int | 

try:
    # Remove a single domain
    api_response = api_instance.domains_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_id_delete: %s\n" % e)
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

# **domains_id_get**
> ApiResponseDomainsList domains_id_get(id)

Get the details of a single domain

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
api_instance = MimePost.DomainsApi(MimePost.ApiClient(configuration))
id = 56 # int | 

try:
    # Get the details of a single domain
    api_response = api_instance.domains_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ApiResponseDomainsList**](ApiResponseDomainsList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_id_verify_dkim_post**
> ApiResponse domains_id_verify_dkim_post(id)

Request for the verification of DKIM record for a single domain

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
api_instance = MimePost.DomainsApi(MimePost.ApiClient(configuration))
id = 56 # int | 

try:
    # Request for the verification of DKIM record for a single domain
    api_response = api_instance.domains_id_verify_dkim_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_id_verify_dkim_post: %s\n" % e)
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

# **domains_id_verify_spf_post**
> ApiResponse domains_id_verify_spf_post(id)

Request for the verification of SPF record for a single domain

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
api_instance = MimePost.DomainsApi(MimePost.ApiClient(configuration))
id = 56 # int | 

try:
    # Request for the verification of SPF record for a single domain
    api_response = api_instance.domains_id_verify_spf_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_id_verify_spf_post: %s\n" % e)
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

# **domains_id_verify_tracking_post**
> ApiResponse domains_id_verify_tracking_post(id)

Request for the verification of tracking record for a single domain

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
api_instance = MimePost.DomainsApi(MimePost.ApiClient(configuration))
id = 56 # int | 

try:
    # Request for the verification of tracking record for a single domain
    api_response = api_instance.domains_id_verify_tracking_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_id_verify_tracking_post: %s\n" % e)
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

# **domains_post**
> ApiResponse domains_post(domain=domain)

Add single domain

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
api_instance = MimePost.DomainsApi(MimePost.ApiClient(configuration))
domain = MimePost.Domain() # Domain | The name of the domain name (optional)

try:
    # Add single domain
    api_response = api_instance.domains_post(domain=domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | [**Domain**](Domain.md)| The name of the domain name | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

