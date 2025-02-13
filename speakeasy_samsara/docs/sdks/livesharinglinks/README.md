# LiveSharingLinks
(*live_sharing_links*)

## Overview

### Available Operations

* [delete_live_sharing_link](#delete_live_sharing_link) - Delete non-expired Live Sharing Link
* [get_live_sharing_links](#get_live_sharing_links) - Get Live Sharing Links
* [update_live_sharing_link](#update_live_sharing_link) - Update non-expired Live Sharing Link
* [create_live_sharing_link](#create_live_sharing_link) - Create Live Sharing Link

## delete_live_sharing_link

Delete Live Sharing Link.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Live Sharing Links** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.live_sharing_links.delete_live_sharing_link(id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier for the Live Sharing Link.                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LiveSharingLinksDeleteLiveSharingLinkBadRequestErrorResponseBody](../../models/livesharinglinksdeletelivesharinglinkbadrequesterrorresponsebody.md)**

### Errors

| Error Type                                                                      | Status Code                                                                     | Content Type                                                                    |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| models.LiveSharingLinksDeleteLiveSharingLinkUnauthorizedErrorResponseBody       | 401                                                                             | application/json                                                                |
| models.LiveSharingLinksDeleteLiveSharingLinkNotFoundErrorResponseBody           | 404                                                                             | application/json                                                                |
| models.LiveSharingLinksDeleteLiveSharingLinkMethodNotAllowedErrorResponseBody   | 405                                                                             | application/json                                                                |
| models.LiveSharingLinksDeleteLiveSharingLinkTooManyRequestsErrorResponseBody    | 429                                                                             | application/json                                                                |
| models.LiveSharingLinksDeleteLiveSharingLinkInternalServerErrorResponseBody     | 500                                                                             | application/json                                                                |
| models.LiveSharingLinksDeleteLiveSharingLinkNotImplementedErrorResponseBody     | 501                                                                             | application/json                                                                |
| models.LiveSharingLinksDeleteLiveSharingLinkBadGatewayErrorResponseBody         | 502                                                                             | application/json                                                                |
| models.LiveSharingLinksDeleteLiveSharingLinkServiceUnavailableErrorResponseBody | 503                                                                             | application/json                                                                |
| models.LiveSharingLinksDeleteLiveSharingLinkGatewayTimeoutErrorResponseBody     | 504                                                                             | application/json                                                                |
| models.APIError                                                                 | 4XX, 5XX                                                                        | \*/\*                                                                           |

## get_live_sharing_links

Returns all non-expired Live Sharing Links.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Live Sharing Links** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.live_sharing_links.get_live_sharing_links()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                       | Type                                                                                                                                                                                                            | Required                                                                                                                                                                                                        | Description                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ids`                                                                                                                                                                                                           | List[*str*]                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                              | A filter on the data based on this comma-separated list of Live Share Link IDs                                                                                                                                  |
| `type`                                                                                                                                                                                                          | [Optional[models.GetLiveSharingLinksQueryParamType]](../../models/getlivesharinglinksqueryparamtype.md)                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                              | A filter on the data based on the Live Sharing Link type.  Valid values: `all`, `assetsLocation`, `assetsNearLocation`, `assetsOnRoute`                                                                         |
| `limit`                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              | The limit for how many objects will be in the response. Default and max for this value is 100 objects.                                                                                                          |
| `after`                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              |  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. |
| `retries`                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                             |

### Response

**[models.GetLiveSharingLinksResponse](../../models/getlivesharinglinksresponse.md)**

### Errors

| Error Type                                                                    | Status Code                                                                   | Content Type                                                                  |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| models.LiveSharingLinksGetLiveSharingLinksUnauthorizedErrorResponseBody       | 401                                                                           | application/json                                                              |
| models.LiveSharingLinksGetLiveSharingLinksNotFoundErrorResponseBody           | 404                                                                           | application/json                                                              |
| models.LiveSharingLinksGetLiveSharingLinksMethodNotAllowedErrorResponseBody   | 405                                                                           | application/json                                                              |
| models.LiveSharingLinksGetLiveSharingLinksTooManyRequestsErrorResponseBody    | 429                                                                           | application/json                                                              |
| models.LiveSharingLinksGetLiveSharingLinksInternalServerErrorResponseBody     | 500                                                                           | application/json                                                              |
| models.LiveSharingLinksGetLiveSharingLinksNotImplementedErrorResponseBody     | 501                                                                           | application/json                                                              |
| models.LiveSharingLinksGetLiveSharingLinksBadGatewayErrorResponseBody         | 502                                                                           | application/json                                                              |
| models.LiveSharingLinksGetLiveSharingLinksServiceUnavailableErrorResponseBody | 503                                                                           | application/json                                                              |
| models.LiveSharingLinksGetLiveSharingLinksGatewayTimeoutErrorResponseBody     | 504                                                                           | application/json                                                              |
| models.APIError                                                               | 4XX, 5XX                                                                      | \*/\*                                                                         |

## update_live_sharing_link

Update Live Sharing Link.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Live Sharing Links** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.live_sharing_links.update_live_sharing_link(id="<id>", name="Example Live Sharing Link name", description="Sample description", expires_at_time="2020-01-27T07:06:25Z")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            | Example                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                   | *str*                                                                                                                  | :heavy_check_mark:                                                                                                     | Unique identifier for the Live Sharing Link.                                                                           |                                                                                                                        |
| `name`                                                                                                                 | *str*                                                                                                                  | :heavy_check_mark:                                                                                                     | Name of the Live Sharing Link.                                                                                         | Example Live Sharing Link name                                                                                         |
| `description`                                                                                                          | *Optional[str]*                                                                                                        | :heavy_minus_sign:                                                                                                     | Description for the Live Sharing Link (not applicable for 'assetsOnRoute' type).                                       | Sample description                                                                                                     |
| `expires_at_time`                                                                                                      | *Optional[str]*                                                                                                        | :heavy_minus_sign:                                                                                                     | Date that this link expires in RFC 3339 format. Can't be set in the past. If not provided then link will never expire. | 2020-01-27T07:06:25Z                                                                                                   |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |                                                                                                                        |

### Response

**[models.UpdateLiveSharingLinkResponse](../../models/updatelivesharinglinkresponse.md)**

### Errors

| Error Type                                                                      | Status Code                                                                     | Content Type                                                                    |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| models.LiveSharingLinksUpdateLiveSharingLinkUnauthorizedErrorResponseBody       | 401                                                                             | application/json                                                                |
| models.LiveSharingLinksUpdateLiveSharingLinkNotFoundErrorResponseBody           | 404                                                                             | application/json                                                                |
| models.LiveSharingLinksUpdateLiveSharingLinkMethodNotAllowedErrorResponseBody   | 405                                                                             | application/json                                                                |
| models.LiveSharingLinksUpdateLiveSharingLinkTooManyRequestsErrorResponseBody    | 429                                                                             | application/json                                                                |
| models.LiveSharingLinksUpdateLiveSharingLinkInternalServerErrorResponseBody     | 500                                                                             | application/json                                                                |
| models.LiveSharingLinksUpdateLiveSharingLinkNotImplementedErrorResponseBody     | 501                                                                             | application/json                                                                |
| models.LiveSharingLinksUpdateLiveSharingLinkBadGatewayErrorResponseBody         | 502                                                                             | application/json                                                                |
| models.LiveSharingLinksUpdateLiveSharingLinkServiceUnavailableErrorResponseBody | 503                                                                             | application/json                                                                |
| models.LiveSharingLinksUpdateLiveSharingLinkGatewayTimeoutErrorResponseBody     | 504                                                                             | application/json                                                                |
| models.APIError                                                                 | 4XX, 5XX                                                                        | \*/\*                                                                           |

## create_live_sharing_link

Create Live Sharing Link.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Live Sharing Links** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
import samsara
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.live_sharing_links.create_live_sharing_link(name="Example Live Sharing Link name", type_=samsara.LiveSharingLinksCreateLiveSharingLinkRequestBodyType.ASSETS_LOCATION, assets_location_link_config={
        "asset_id": "1234",
        "location": {
            "formatted_address": "1990 Alameda Street, San Francisco, CA 94103",
            "latitude": 37.456345,
            "longitude": 34.5633749,
            "name": "Suburbs",
        },
    }, assets_near_location_link_config={
        "address_id": "1234",
    }, assets_on_route_link_config={
        "recurring_route_id": "1234",
    }, description="Sample description", expires_at_time="2020-01-27T07:06:25Z")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                      | Type                                                                                                                                                                                                           | Required                                                                                                                                                                                                       | Description                                                                                                                                                                                                    | Example                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                                                                                         | *str*                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                             | Name of the Live Sharing Link.                                                                                                                                                                                 | Example Live Sharing Link name                                                                                                                                                                                 |
| `type`                                                                                                                                                                                                         | [models.LiveSharingLinksCreateLiveSharingLinkRequestBodyType](../../models/livesharinglinkscreatelivesharinglinkrequestbodytype.md)                                                                            | :heavy_check_mark:                                                                                                                                                                                             | Type of the Live Sharing Link. This field specifies which one of '<type>LinkConfig' objects will be used to configure the sharing link.  Valid values: `assetsLocation`, `assetsNearLocation`, `assetsOnRoute` | assetsLocation                                                                                                                                                                                                 |
| `assets_location_link_config`                                                                                                                                                                                  | [Optional[models.AssetsLocationLinkConfigObject]](../../models/assetslocationlinkconfigobject.md)                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                             | Configuration details specific to the 'By Asset' Live Sharing Link.                                                                                                                                            |                                                                                                                                                                                                                |
| `assets_near_location_link_config`                                                                                                                                                                             | [Optional[models.AssetsNearLocationLinkConfigObject]](../../models/assetsnearlocationlinkconfigobject.md)                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                             | Configuration details specific to the 'By Location' Live Sharing Link.                                                                                                                                         |                                                                                                                                                                                                                |
| `assets_on_route_link_config`                                                                                                                                                                                  | [Optional[models.AssetsOnRouteLinkConfigObject]](../../models/assetsonroutelinkconfigobject.md)                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                             | Configuration details specific to the 'By Recurring Route' Live Sharing Link.                                                                                                                                  |                                                                                                                                                                                                                |
| `description`                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                             | Description for the Live Sharing Link (not applicable for 'assetsOnRoute' type).                                                                                                                               | Sample description                                                                                                                                                                                             |
| `expires_at_time`                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                             | Date that this link expires in RFC 3339 format. Can't be set in the past. If not provided then link will never expire.                                                                                         | 2020-01-27T07:06:25Z                                                                                                                                                                                           |
| `retries`                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                            |                                                                                                                                                                                                                |

### Response

**[models.CreateLiveSharingLinkResponse](../../models/createlivesharinglinkresponse.md)**

### Errors

| Error Type                                                                      | Status Code                                                                     | Content Type                                                                    |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| models.LiveSharingLinksCreateLiveSharingLinkUnauthorizedErrorResponseBody       | 401                                                                             | application/json                                                                |
| models.LiveSharingLinksCreateLiveSharingLinkNotFoundErrorResponseBody           | 404                                                                             | application/json                                                                |
| models.LiveSharingLinksCreateLiveSharingLinkMethodNotAllowedErrorResponseBody   | 405                                                                             | application/json                                                                |
| models.LiveSharingLinksCreateLiveSharingLinkTooManyRequestsErrorResponseBody    | 429                                                                             | application/json                                                                |
| models.LiveSharingLinksCreateLiveSharingLinkInternalServerErrorResponseBody     | 500                                                                             | application/json                                                                |
| models.LiveSharingLinksCreateLiveSharingLinkNotImplementedErrorResponseBody     | 501                                                                             | application/json                                                                |
| models.LiveSharingLinksCreateLiveSharingLinkBadGatewayErrorResponseBody         | 502                                                                             | application/json                                                                |
| models.LiveSharingLinksCreateLiveSharingLinkServiceUnavailableErrorResponseBody | 503                                                                             | application/json                                                                |
| models.LiveSharingLinksCreateLiveSharingLinkGatewayTimeoutErrorResponseBody     | 504                                                                             | application/json                                                                |
| models.APIError                                                                 | 4XX, 5XX                                                                        | \*/\*                                                                           |