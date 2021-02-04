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

