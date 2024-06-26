# manager_client.DataURIApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](DataURIApi.md#get) | **GET** /data-uri | Get the Web Data URI for a Web Page URL.


# **get**
> get(u)

Get the Web Data URI for a Web Page URL.

The service will return a Web Data URI only for existing datasets. The Web Data URI is not guaranteed to exist (i.e. it may return 404). 

### Example


```python
import manager_client
from manager_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io
# See configuration.py for a list of all supported configuration parameters.
configuration = manager_client.Configuration(
    host = "https://api.wordlift.io"
)


# Enter a context with an instance of the API client
async with manager_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = manager_client.DataURIApi(api_client)
    u = 'u_example' # str | The Web Page URL.

    try:
        # Get the Web Data URI for a Web Page URL.
        await api_instance.get(u)
    except Exception as e:
        print("Exception when calling DataURIApi->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **u** | **str**| The Web Page URL. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**303** | See Other |  * Location - ${api.data-uri-controller.get.headers.location.description} <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

