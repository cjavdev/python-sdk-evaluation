# DriverQRCodes
(*driver_qr_codes*)

## Overview

### Available Operations

* [delete_driver_qr_code](#delete_driver_qr_code) - Revoke driver's QR code
* [get_drivers_qr_codes](#get_drivers_qr_codes) - Get driver QR codes
* [create_driver_qr_code](#create_driver_qr_code) - Create new QR code for driver

## delete_driver_qr_code

Revoke requested driver's currently active QR code.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Drivers** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.driver_qr_codes.delete_driver_qr_code(driver_id=494123)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `driver_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | Unique ID of the driver.                                            | 494123                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DriverQrCodesDeleteDriverQrCodeBadRequestErrorResponseBody](../../models/driverqrcodesdeletedriverqrcodebadrequesterrorresponsebody.md)**

### Errors

| Error Type                                                                | Status Code                                                               | Content Type                                                              |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| models.DriverQrCodesDeleteDriverQrCodeUnauthorizedErrorResponseBody       | 401                                                                       | application/json                                                          |
| models.DriverQrCodesDeleteDriverQrCodeNotFoundErrorResponseBody           | 404                                                                       | application/json                                                          |
| models.DriverQrCodesDeleteDriverQrCodeMethodNotAllowedErrorResponseBody   | 405                                                                       | application/json                                                          |
| models.DriverQrCodesDeleteDriverQrCodeTooManyRequestsErrorResponseBody    | 429                                                                       | application/json                                                          |
| models.DriverQrCodesDeleteDriverQrCodeInternalServerErrorResponseBody     | 500                                                                       | application/json                                                          |
| models.DriverQrCodesDeleteDriverQrCodeNotImplementedErrorResponseBody     | 501                                                                       | application/json                                                          |
| models.DriverQrCodesDeleteDriverQrCodeBadGatewayErrorResponseBody         | 502                                                                       | application/json                                                          |
| models.DriverQrCodesDeleteDriverQrCodeServiceUnavailableErrorResponseBody | 503                                                                       | application/json                                                          |
| models.DriverQrCodesDeleteDriverQrCodeGatewayTimeoutErrorResponseBody     | 504                                                                       | application/json                                                          |
| models.APIError                                                           | 4XX, 5XX                                                                  | \*/\*                                                                     |

## get_drivers_qr_codes

Get details for requested driver(s) QR code, used for driver trip assignment.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Drivers** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.driver_qr_codes.get_drivers_qr_codes(driver_ids=[
        "<value>",
        "<value>",
        "<value>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `driver_ids`                                                                                              | List[*str*]                                                                                               | :heavy_check_mark:                                                                                        | String of comma separated driver IDs. List of driver - QR codes for specified driver(s) will be returned. |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.GetDriversQrCodesResponse](../../models/getdriversqrcodesresponse.md)**

### Errors

| Error Type                                                               | Status Code                                                              | Content Type                                                             |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| models.DriverQrCodesGetDriversQrCodesUnauthorizedErrorResponseBody       | 401                                                                      | application/json                                                         |
| models.DriverQrCodesGetDriversQrCodesNotFoundErrorResponseBody           | 404                                                                      | application/json                                                         |
| models.DriverQrCodesGetDriversQrCodesMethodNotAllowedErrorResponseBody   | 405                                                                      | application/json                                                         |
| models.DriverQrCodesGetDriversQrCodesTooManyRequestsErrorResponseBody    | 429                                                                      | application/json                                                         |
| models.DriverQrCodesGetDriversQrCodesInternalServerErrorResponseBody     | 500                                                                      | application/json                                                         |
| models.DriverQrCodesGetDriversQrCodesNotImplementedErrorResponseBody     | 501                                                                      | application/json                                                         |
| models.DriverQrCodesGetDriversQrCodesBadGatewayErrorResponseBody         | 502                                                                      | application/json                                                         |
| models.DriverQrCodesGetDriversQrCodesServiceUnavailableErrorResponseBody | 503                                                                      | application/json                                                         |
| models.DriverQrCodesGetDriversQrCodesGatewayTimeoutErrorResponseBody     | 504                                                                      | application/json                                                         |
| models.APIError                                                          | 4XX, 5XX                                                                 | \*/\*                                                                    |

## create_driver_qr_code

Assign a new QR code for the requested driver. Return error if an active QR code already exists.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Drivers** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.driver_qr_codes.create_driver_qr_code(driver_id=494123)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `driver_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | Unique ID of the driver.                                            | 494123                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CreateDriverQrCodeResponse](../../models/createdriverqrcoderesponse.md)**

### Errors

| Error Type                                                                | Status Code                                                               | Content Type                                                              |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| models.DriverQrCodesCreateDriverQrCodeUnauthorizedErrorResponseBody       | 401                                                                       | application/json                                                          |
| models.DriverQrCodesCreateDriverQrCodeNotFoundErrorResponseBody           | 404                                                                       | application/json                                                          |
| models.DriverQrCodesCreateDriverQrCodeMethodNotAllowedErrorResponseBody   | 405                                                                       | application/json                                                          |
| models.DriverQrCodesCreateDriverQrCodeTooManyRequestsErrorResponseBody    | 429                                                                       | application/json                                                          |
| models.DriverQrCodesCreateDriverQrCodeInternalServerErrorResponseBody     | 500                                                                       | application/json                                                          |
| models.DriverQrCodesCreateDriverQrCodeNotImplementedErrorResponseBody     | 501                                                                       | application/json                                                          |
| models.DriverQrCodesCreateDriverQrCodeBadGatewayErrorResponseBody         | 502                                                                       | application/json                                                          |
| models.DriverQrCodesCreateDriverQrCodeServiceUnavailableErrorResponseBody | 503                                                                       | application/json                                                          |
| models.DriverQrCodesCreateDriverQrCodeGatewayTimeoutErrorResponseBody     | 504                                                                       | application/json                                                          |
| models.APIError                                                           | 4XX, 5XX                                                                  | \*/\*                                                                     |