# Webhooks
(*webhooks*)

## Overview

### Available Operations

* [list_webhooks](#list_webhooks) - List all webhooks belonging to a specific org.
* [post_webhooks](#post_webhooks) - Create a webhook
* [delete_webhook](#delete_webhook) - Delete a webhook with the given ID
* [get_webhook](#get_webhook) - Retrieve a webhook with given ID
* [patch_webhook](#patch_webhook) - Update a specific webhook's information.

## list_webhooks

List all webhooks belonging to a specific org.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Webhooks** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.webhooks.list_webhooks()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                       | Type                                                                                                                                                                                                            | Required                                                                                                                                                                                                        | Description                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ids`                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              |  A filter on the data based on this comma-separated list of webhook IDs. Example: `ids=49412323223,49412329928`                                                                                                 |
| `limit`                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              | The limit for how many objects will be in the response. Default and max for this value is 512 objects.                                                                                                          |
| `after`                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              |  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. |
| `retries`                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                             |

### Response

**[models.ListWebhooksResponse](../../models/listwebhooksresponse.md)**

### Errors

| Error Type                                                     | Status Code                                                    | Content Type                                                   |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| models.WebhooksListWebhooksUnauthorizedErrorResponseBody       | 401                                                            | application/json                                               |
| models.WebhooksListWebhooksNotFoundErrorResponseBody           | 404                                                            | application/json                                               |
| models.WebhooksListWebhooksMethodNotAllowedErrorResponseBody   | 405                                                            | application/json                                               |
| models.WebhooksListWebhooksTooManyRequestsErrorResponseBody    | 429                                                            | application/json                                               |
| models.WebhooksListWebhooksInternalServerErrorResponseBody     | 500                                                            | application/json                                               |
| models.WebhooksListWebhooksNotImplementedErrorResponseBody     | 501                                                            | application/json                                               |
| models.WebhooksListWebhooksBadGatewayErrorResponseBody         | 502                                                            | application/json                                               |
| models.WebhooksListWebhooksServiceUnavailableErrorResponseBody | 503                                                            | application/json                                               |
| models.WebhooksListWebhooksGatewayTimeoutErrorResponseBody     | 504                                                            | application/json                                               |
| models.APIError                                                | 4XX, 5XX                                                       | \*/\*                                                          |

## post_webhooks

Create a webhook

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Webhooks** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
import samsara
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.webhooks.post_webhooks(name="Webhook-123", url="https://www.Webhook-123.com/webhook/listener", custom_headers=[
        {
            "key": "format",
            "value": "xcmol-532",
        },
        {
            "key": "format",
            "value": "xcmol-532",
        },
        {
            "key": "format",
            "value": "xcmol-532",
        },
    ], event_types=[
        samsara.WebhooksPostWebhooksRequestBodyEventTypes.DRIVER_CREATED,
    ], version=samsara.WebhooksPostWebhooksRequestBodyVersion.TWO_THOUSAND_AND_EIGHTEEN_01_01)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                        | Type                                                                                                                                                                             | Required                                                                                                                                                                         | Description                                                                                                                                                                      | Example                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                                                           | *str*                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                               | The  name of the webhook. This will appear in both Samsara’s cloud dashboard and the API. It can be set or updated through the Samsara Dashboard or through the API at any time. | Webhook-123                                                                                                                                                                      |
| `url`                                                                                                                                                                            | *str*                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                               | The url of the webhook. This will appear in both Samsara’s cloud dashboard and the API. It can be set or updated through the Samsara Dashboard or through the API at any time.   | https://www.Webhook-123.com/webhook/listener                                                                                                                                     |
| `custom_headers`                                                                                                                                                                 | List[[models.CustomHeadersObjectRequestBody](../../models/customheadersobjectrequestbody.md)]                                                                                    | :heavy_minus_sign:                                                                                                                                                               | The list of custom headers that users can include with their request                                                                                                             |                                                                                                                                                                                  |
| `event_types`                                                                                                                                                                    | List[[models.WebhooksPostWebhooksRequestBodyEventTypes](../../models/webhookspostwebhooksrequestbodyeventtypes.md)]                                                              | :heavy_minus_sign:                                                                                                                                                               | [beta] The list of event types associated with a particular event type                                                                                                           | [<br/>"DriverCreated",<br/>"DriverCreated"<br/>]                                                                                                                                 |
| `version`                                                                                                                                                                        | [Optional[models.WebhooksPostWebhooksRequestBodyVersion]](../../models/webhookspostwebhooksrequestbodyversion.md)                                                                | :heavy_minus_sign:                                                                                                                                                               | The version of the webhook.  Valid values: `2018-01-01`, `2021-06-09`, `2022-09-13`, `2024-02-27`                                                                                | 2018-01-01                                                                                                                                                                       |
| `retries`                                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                 | :heavy_minus_sign:                                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                                              |                                                                                                                                                                                  |

### Response

**[models.PostWebhooksResponse](../../models/postwebhooksresponse.md)**

### Errors

| Error Type                                                     | Status Code                                                    | Content Type                                                   |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| models.WebhooksPostWebhooksUnauthorizedErrorResponseBody       | 401                                                            | application/json                                               |
| models.WebhooksPostWebhooksNotFoundErrorResponseBody           | 404                                                            | application/json                                               |
| models.WebhooksPostWebhooksMethodNotAllowedErrorResponseBody   | 405                                                            | application/json                                               |
| models.WebhooksPostWebhooksTooManyRequestsErrorResponseBody    | 429                                                            | application/json                                               |
| models.WebhooksPostWebhooksInternalServerErrorResponseBody     | 500                                                            | application/json                                               |
| models.WebhooksPostWebhooksNotImplementedErrorResponseBody     | 501                                                            | application/json                                               |
| models.WebhooksPostWebhooksBadGatewayErrorResponseBody         | 502                                                            | application/json                                               |
| models.WebhooksPostWebhooksServiceUnavailableErrorResponseBody | 503                                                            | application/json                                               |
| models.WebhooksPostWebhooksGatewayTimeoutErrorResponseBody     | 504                                                            | application/json                                               |
| models.APIError                                                | 4XX, 5XX                                                       | \*/\*                                                          |

## delete_webhook

Delete a webhook with the given ID.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Webhooks** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.webhooks.delete_webhook(id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier for the webhook to delete.                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WebhooksDeleteWebhookBadRequestErrorResponseBody](../../models/webhooksdeletewebhookbadrequesterrorresponsebody.md)**

### Errors

| Error Type                                                      | Status Code                                                     | Content Type                                                    |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| models.WebhooksDeleteWebhookUnauthorizedErrorResponseBody       | 401                                                             | application/json                                                |
| models.WebhooksDeleteWebhookNotFoundErrorResponseBody           | 404                                                             | application/json                                                |
| models.WebhooksDeleteWebhookMethodNotAllowedErrorResponseBody   | 405                                                             | application/json                                                |
| models.WebhooksDeleteWebhookTooManyRequestsErrorResponseBody    | 429                                                             | application/json                                                |
| models.WebhooksDeleteWebhookInternalServerErrorResponseBody     | 500                                                             | application/json                                                |
| models.WebhooksDeleteWebhookNotImplementedErrorResponseBody     | 501                                                             | application/json                                                |
| models.WebhooksDeleteWebhookBadGatewayErrorResponseBody         | 502                                                             | application/json                                                |
| models.WebhooksDeleteWebhookServiceUnavailableErrorResponseBody | 503                                                             | application/json                                                |
| models.WebhooksDeleteWebhookGatewayTimeoutErrorResponseBody     | 504                                                             | application/json                                                |
| models.APIError                                                 | 4XX, 5XX                                                        | \*/\*                                                           |

## get_webhook

Retrieve a webhook with given ID.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Webhooks** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.webhooks.get_webhook(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | ID of the webhook. This is the Samsara-specified ID.                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetWebhookResponse](../../models/getwebhookresponse.md)**

### Errors

| Error Type                                                   | Status Code                                                  | Content Type                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| models.WebhooksGetWebhookUnauthorizedErrorResponseBody       | 401                                                          | application/json                                             |
| models.WebhooksGetWebhookNotFoundErrorResponseBody           | 404                                                          | application/json                                             |
| models.WebhooksGetWebhookMethodNotAllowedErrorResponseBody   | 405                                                          | application/json                                             |
| models.WebhooksGetWebhookTooManyRequestsErrorResponseBody    | 429                                                          | application/json                                             |
| models.WebhooksGetWebhookInternalServerErrorResponseBody     | 500                                                          | application/json                                             |
| models.WebhooksGetWebhookNotImplementedErrorResponseBody     | 501                                                          | application/json                                             |
| models.WebhooksGetWebhookBadGatewayErrorResponseBody         | 502                                                          | application/json                                             |
| models.WebhooksGetWebhookServiceUnavailableErrorResponseBody | 503                                                          | application/json                                             |
| models.WebhooksGetWebhookGatewayTimeoutErrorResponseBody     | 504                                                          | application/json                                             |
| models.APIError                                              | 4XX, 5XX                                                     | \*/\*                                                        |

## patch_webhook

Update a specific webhook's information.  **Note** this implementation of patch uses [the JSON merge patch](https://tools.ietf.org/html/rfc7396) proposed standard.
 This means that any fields included in the patch request will _overwrite_ fields which exist on the target resource.
 For arrays, this means any array included in the request will _replace_ the array that exists at the specified path, it will not _add_ to the existing array

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Webhooks** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
import samsara
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.webhooks.patch_webhook(id="<id>", custom_headers=[
        {
            "key": "format",
            "value": "xcmol-532",
        },
        {
            "key": "format",
            "value": "xcmol-532",
        },
        {
            "key": "format",
            "value": "xcmol-532",
        },
    ], name="Webhook-123", url="https://www.webhook-123.com/webhook/listener", version=samsara.WebhooksPatchWebhookRequestBodyVersion.TWO_THOUSAND_AND_EIGHTEEN_01_01)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                        | Type                                                                                                                                                                             | Required                                                                                                                                                                         | Description                                                                                                                                                                      | Example                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                             | *str*                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                               | Unique identifier for the webhook to update.                                                                                                                                     |                                                                                                                                                                                  |
| `custom_headers`                                                                                                                                                                 | List[[models.CustomHeadersObjectRequestBody](../../models/customheadersobjectrequestbody.md)]                                                                                    | :heavy_minus_sign:                                                                                                                                                               | The list of custom headers that users can include with their request                                                                                                             |                                                                                                                                                                                  |
| `name`                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                               | The  name of the webhook. This will appear in both Samsara’s cloud dashboard and the API. It can be set or updated through the Samsara Dashboard or through the API at any time. | Webhook-123                                                                                                                                                                      |
| `url`                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                               | The url of the webhook. This will appear in both Samsara’s cloud dashboard and the API. It can be set or updated through the Samsara Dashboard or through the API at any time.   | https://www.webhook-123.com/webhook/listener                                                                                                                                     |
| `version`                                                                                                                                                                        | [Optional[models.WebhooksPatchWebhookRequestBodyVersion]](../../models/webhookspatchwebhookrequestbodyversion.md)                                                                | :heavy_minus_sign:                                                                                                                                                               | The version of the webhook.  Valid values: `2018-01-01`, `2021-06-09`, `2022-09-13`, `2024-02-27`                                                                                | 2018-01-01                                                                                                                                                                       |
| `retries`                                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                 | :heavy_minus_sign:                                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                                              |                                                                                                                                                                                  |

### Response

**[models.PatchWebhookResponse](../../models/patchwebhookresponse.md)**

### Errors

| Error Type                                                     | Status Code                                                    | Content Type                                                   |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| models.WebhooksPatchWebhookUnauthorizedErrorResponseBody       | 401                                                            | application/json                                               |
| models.WebhooksPatchWebhookNotFoundErrorResponseBody           | 404                                                            | application/json                                               |
| models.WebhooksPatchWebhookMethodNotAllowedErrorResponseBody   | 405                                                            | application/json                                               |
| models.WebhooksPatchWebhookTooManyRequestsErrorResponseBody    | 429                                                            | application/json                                               |
| models.WebhooksPatchWebhookInternalServerErrorResponseBody     | 500                                                            | application/json                                               |
| models.WebhooksPatchWebhookNotImplementedErrorResponseBody     | 501                                                            | application/json                                               |
| models.WebhooksPatchWebhookBadGatewayErrorResponseBody         | 502                                                            | application/json                                               |
| models.WebhooksPatchWebhookServiceUnavailableErrorResponseBody | 503                                                            | application/json                                               |
| models.WebhooksPatchWebhookGatewayTimeoutErrorResponseBody     | 504                                                            | application/json                                               |
| models.APIError                                                | 4XX, 5XX                                                       | \*/\*                                                          |