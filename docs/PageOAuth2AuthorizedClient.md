# PageOAuth2AuthorizedClient

A page object with links to move to other pages and the list of objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **str** | The link to the first page. | 
**items** | [**List[OAuth2AuthorizedClient]**](OAuth2AuthorizedClient.md) | An array of objects. | 
**last** | **str** | The link to the last page. | 
**next** | **str** | The link to the next page or &#x60;null&#x60; if there&#39;s no page. | 
**prev** | **str** | The link to the previous page or &#x60;null&#x60; if there&#39;s no page. | 
**var_self** | **str** | The link to the current page. | 

## Example

```python
from manager_client.models.page_o_auth2_authorized_client import PageOAuth2AuthorizedClient

# TODO update the JSON string below
json = "{}"
# create an instance of PageOAuth2AuthorizedClient from a JSON string
page_o_auth2_authorized_client_instance = PageOAuth2AuthorizedClient.from_json(json)
# print the JSON string representation of the object
print(PageOAuth2AuthorizedClient.to_json())

# convert the object into a dict
page_o_auth2_authorized_client_dict = page_o_auth2_authorized_client_instance.to_dict()
# create an instance of PageOAuth2AuthorizedClient from a dict
page_o_auth2_authorized_client_from_dict = PageOAuth2AuthorizedClient.from_dict(page_o_auth2_authorized_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


