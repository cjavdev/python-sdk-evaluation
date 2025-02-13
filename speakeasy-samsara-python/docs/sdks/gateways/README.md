# Gateways
(*gateways*)

## Overview

### Available Operations

* [get_gateways](#get_gateways) - List all gateways
* [post_gateway](#post_gateway) - Activate a new gateway
* [delete_gateway](#delete_gateway) - Deactivate a gateway

## get_gateways

List all gateways

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Gateways** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.gateways.get_gateways()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                       | Type                                                                                                                                                                                                            | Required                                                                                                                                                                                                        | Description                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `models`                                                                                                                                                                                                        | List[*str*]                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                              | Filter by a comma separated list of gateway models.                                                                                                                                                             |
| `after`                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              |  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. |
| `retries`                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                             |

### Response

**[models.GetGatewaysResponse](../../models/getgatewaysresponse.md)**

### Errors

| Error Type                                                    | Status Code                                                   | Content Type                                                  |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| models.GatewaysGetGatewaysUnauthorizedErrorResponseBody       | 401                                                           | application/json                                              |
| models.GatewaysGetGatewaysNotFoundErrorResponseBody           | 404                                                           | application/json                                              |
| models.GatewaysGetGatewaysMethodNotAllowedErrorResponseBody   | 405                                                           | application/json                                              |
| models.GatewaysGetGatewaysTooManyRequestsErrorResponseBody    | 429                                                           | application/json                                              |
| models.GatewaysGetGatewaysInternalServerErrorResponseBody     | 500                                                           | application/json                                              |
| models.GatewaysGetGatewaysNotImplementedErrorResponseBody     | 501                                                           | application/json                                              |
| models.GatewaysGetGatewaysBadGatewayErrorResponseBody         | 502                                                           | application/json                                              |
| models.GatewaysGetGatewaysServiceUnavailableErrorResponseBody | 503                                                           | application/json                                              |
| models.GatewaysGetGatewaysGatewayTimeoutErrorResponseBody     | 504                                                           | application/json                                              |
| models.APIError                                               | 4XX, 5XX                                                      | \*/\*                                                         |

## post_gateway

Activate a new gateway. To activate a device and associate it with your organization, enter its serial number. Each device's serial number can also be found on its label or packaging, or from your order confirmation email. A Not Found error could mean that the serial was not found or it has already been activated

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Gateways** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.gateways.post_gateway(serial="GFRV-43N-VGX")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `serial`                                                            | *str*                                                               | :heavy_check_mark:                                                  | Gateway serial number                                               | GFRV-43N-VGX                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PostGatewayResponse](../../models/postgatewayresponse.md)**

### Errors

| Error Type                                                    | Status Code                                                   | Content Type                                                  |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| models.GatewaysPostGatewayUnauthorizedErrorResponseBody       | 401                                                           | application/json                                              |
| models.GatewaysPostGatewayNotFoundErrorResponseBody           | 404                                                           | application/json                                              |
| models.GatewaysPostGatewayMethodNotAllowedErrorResponseBody   | 405                                                           | application/json                                              |
| models.GatewaysPostGatewayTooManyRequestsErrorResponseBody    | 429                                                           | application/json                                              |
| models.GatewaysPostGatewayInternalServerErrorResponseBody     | 500                                                           | application/json                                              |
| models.GatewaysPostGatewayNotImplementedErrorResponseBody     | 501                                                           | application/json                                              |
| models.GatewaysPostGatewayBadGatewayErrorResponseBody         | 502                                                           | application/json                                              |
| models.GatewaysPostGatewayServiceUnavailableErrorResponseBody | 503                                                           | application/json                                              |
| models.GatewaysPostGatewayGatewayTimeoutErrorResponseBody     | 504                                                           | application/json                                              |
| models.APIError                                               | 4XX, 5XX                                                      | \*/\*                                                         |

## delete_gateway

Deactivate a gateway

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Gateways** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.gateways.delete_gateway(id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Gateway serial number                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GatewaysDeleteGatewayBadRequestErrorResponseBody](../../models/gatewaysdeletegatewaybadrequesterrorresponsebody.md)**

### Errors

| Error Type                                                      | Status Code                                                     | Content Type                                                    |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| models.GatewaysDeleteGatewayUnauthorizedErrorResponseBody       | 401                                                             | application/json                                                |
| models.GatewaysDeleteGatewayNotFoundErrorResponseBody           | 404                                                             | application/json                                                |
| models.GatewaysDeleteGatewayMethodNotAllowedErrorResponseBody   | 405                                                             | application/json                                                |
| models.GatewaysDeleteGatewayTooManyRequestsErrorResponseBody    | 429                                                             | application/json                                                |
| models.GatewaysDeleteGatewayInternalServerErrorResponseBody     | 500                                                             | application/json                                                |
| models.GatewaysDeleteGatewayNotImplementedErrorResponseBody     | 501                                                             | application/json                                                |
| models.GatewaysDeleteGatewayBadGatewayErrorResponseBody         | 502                                                             | application/json                                                |
| models.GatewaysDeleteGatewayServiceUnavailableErrorResponseBody | 503                                                             | application/json                                                |
| models.GatewaysDeleteGatewayGatewayTimeoutErrorResponseBody     | 504                                                             | application/json                                                |
| models.APIError                                                 | 4XX, 5XX                                                        | \*/\*                                                           |