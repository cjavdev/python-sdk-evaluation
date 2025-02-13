# Settings
(*settings*)

## Overview

### Available Operations

* [get_compliance_settings](#get_compliance_settings) - Get compliance settings
* [patch_compliance_settings](#patch_compliance_settings) - Update compliance settings
* [get_driver_app_settings](#get_driver_app_settings) - Get driver app settings
* [patch_driver_app_settings](#patch_driver_app_settings) - Update driver app settings
* [get_safety_settings](#get_safety_settings) - Get safety settings

## get_compliance_settings

Get organization's compliance settings, including carrier name, office address, and DOT number

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read ELD Compliance Settings (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.settings.get_compliance_settings()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetComplianceSettingsResponse](../../models/getcompliancesettingsresponse.md)**

### Errors

| Error Type                                                              | Status Code                                                             | Content Type                                                            |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| models.SettingsGetComplianceSettingsUnauthorizedErrorResponseBody       | 401                                                                     | application/json                                                        |
| models.SettingsGetComplianceSettingsNotFoundErrorResponseBody           | 404                                                                     | application/json                                                        |
| models.SettingsGetComplianceSettingsMethodNotAllowedErrorResponseBody   | 405                                                                     | application/json                                                        |
| models.SettingsGetComplianceSettingsTooManyRequestsErrorResponseBody    | 429                                                                     | application/json                                                        |
| models.SettingsGetComplianceSettingsInternalServerErrorResponseBody     | 500                                                                     | application/json                                                        |
| models.SettingsGetComplianceSettingsNotImplementedErrorResponseBody     | 501                                                                     | application/json                                                        |
| models.SettingsGetComplianceSettingsBadGatewayErrorResponseBody         | 502                                                                     | application/json                                                        |
| models.SettingsGetComplianceSettingsServiceUnavailableErrorResponseBody | 503                                                                     | application/json                                                        |
| models.SettingsGetComplianceSettingsGatewayTimeoutErrorResponseBody     | 504                                                                     | application/json                                                        |
| models.APIError                                                         | 4XX, 5XX                                                                | \*/\*                                                                   |

## patch_compliance_settings

Update organization's compliance settings, including carrier name, office address, and DOT number

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write ELD Compliance Settings (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.settings.patch_compliance_settings(request={
        "allow_unregulated_vehicles_enabled": False,
        "canada_hos_enabled": True,
        "carrier_name": "ABC Trucking",
        "dot_number": 12345678,
        "driver_auto_duty_enabled": True,
        "edit_certified_logs_enabled": True,
        "force_manual_location_for_duty_status_changes_enabled": True,
        "force_review_unassigned_hos_enabled": True,
        "main_office_formatted_address": "123 Main Street",
        "persistent_duty_status_enabled": True,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                       | [models.SettingsPatchComplianceSettingsRequestBody](../../models/settingspatchcompliancesettingsrequestbody.md) | :heavy_check_mark:                                                                                              | The request object to use for the request.                                                                      |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.PatchComplianceSettingsResponse](../../models/patchcompliancesettingsresponse.md)**

### Errors

| Error Type                                                                | Status Code                                                               | Content Type                                                              |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| models.SettingsPatchComplianceSettingsUnauthorizedErrorResponseBody       | 401                                                                       | application/json                                                          |
| models.SettingsPatchComplianceSettingsNotFoundErrorResponseBody           | 404                                                                       | application/json                                                          |
| models.SettingsPatchComplianceSettingsMethodNotAllowedErrorResponseBody   | 405                                                                       | application/json                                                          |
| models.SettingsPatchComplianceSettingsTooManyRequestsErrorResponseBody    | 429                                                                       | application/json                                                          |
| models.SettingsPatchComplianceSettingsInternalServerErrorResponseBody     | 500                                                                       | application/json                                                          |
| models.SettingsPatchComplianceSettingsNotImplementedErrorResponseBody     | 501                                                                       | application/json                                                          |
| models.SettingsPatchComplianceSettingsBadGatewayErrorResponseBody         | 502                                                                       | application/json                                                          |
| models.SettingsPatchComplianceSettingsServiceUnavailableErrorResponseBody | 503                                                                       | application/json                                                          |
| models.SettingsPatchComplianceSettingsGatewayTimeoutErrorResponseBody     | 504                                                                       | application/json                                                          |
| models.APIError                                                           | 4XX, 5XX                                                                  | \*/\*                                                                     |

## get_driver_app_settings

Get driver app settings.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Driver App Settings** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.settings.get_driver_app_settings()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetDriverAppSettingsResponse](../../models/getdriverappsettingsresponse.md)**

### Errors

| Error Type                                                             | Status Code                                                            | Content Type                                                           |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| models.SettingsGetDriverAppSettingsUnauthorizedErrorResponseBody       | 401                                                                    | application/json                                                       |
| models.SettingsGetDriverAppSettingsNotFoundErrorResponseBody           | 404                                                                    | application/json                                                       |
| models.SettingsGetDriverAppSettingsMethodNotAllowedErrorResponseBody   | 405                                                                    | application/json                                                       |
| models.SettingsGetDriverAppSettingsTooManyRequestsErrorResponseBody    | 429                                                                    | application/json                                                       |
| models.SettingsGetDriverAppSettingsInternalServerErrorResponseBody     | 500                                                                    | application/json                                                       |
| models.SettingsGetDriverAppSettingsNotImplementedErrorResponseBody     | 501                                                                    | application/json                                                       |
| models.SettingsGetDriverAppSettingsBadGatewayErrorResponseBody         | 502                                                                    | application/json                                                       |
| models.SettingsGetDriverAppSettingsServiceUnavailableErrorResponseBody | 503                                                                    | application/json                                                       |
| models.SettingsGetDriverAppSettingsGatewayTimeoutErrorResponseBody     | 504                                                                    | application/json                                                       |
| models.APIError                                                        | 4XX, 5XX                                                               | \*/\*                                                                  |

## patch_driver_app_settings

Update driver app settings.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Driver App Settings** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.settings.patch_driver_app_settings(request={
        "driver_fleet_id": "abc-trucking-co",
        "gamification": True,
        "gamification_config": {
            "anonymize_driver_names": False,
        },
        "org_vehicle_search": True,
        "trailer_selection": True,
        "trailer_selection_config": {
            "driver_trailer_creation_enabled": False,
            "org_trailer_search": True,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                     | [models.SettingsPatchDriverAppSettingsRequestBody](../../models/settingspatchdriverappsettingsrequestbody.md) | :heavy_check_mark:                                                                                            | The request object to use for the request.                                                                    |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.PatchDriverAppSettingsResponse](../../models/patchdriverappsettingsresponse.md)**

### Errors

| Error Type                                                               | Status Code                                                              | Content Type                                                             |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| models.SettingsPatchDriverAppSettingsUnauthorizedErrorResponseBody       | 401                                                                      | application/json                                                         |
| models.SettingsPatchDriverAppSettingsNotFoundErrorResponseBody           | 404                                                                      | application/json                                                         |
| models.SettingsPatchDriverAppSettingsMethodNotAllowedErrorResponseBody   | 405                                                                      | application/json                                                         |
| models.SettingsPatchDriverAppSettingsTooManyRequestsErrorResponseBody    | 429                                                                      | application/json                                                         |
| models.SettingsPatchDriverAppSettingsInternalServerErrorResponseBody     | 500                                                                      | application/json                                                         |
| models.SettingsPatchDriverAppSettingsNotImplementedErrorResponseBody     | 501                                                                      | application/json                                                         |
| models.SettingsPatchDriverAppSettingsBadGatewayErrorResponseBody         | 502                                                                      | application/json                                                         |
| models.SettingsPatchDriverAppSettingsServiceUnavailableErrorResponseBody | 503                                                                      | application/json                                                         |
| models.SettingsPatchDriverAppSettingsGatewayTimeoutErrorResponseBody     | 504                                                                      | application/json                                                         |
| models.APIError                                                          | 4XX, 5XX                                                                 | \*/\*                                                                    |

## get_safety_settings

Get safety settings

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.settings.get_safety_settings()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetSafetySettingsResponse](../../models/getsafetysettingsresponse.md)**

### Errors

| Error Type                                                                | Status Code                                                               | Content Type                                                              |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| models.SafetySettingsGetSafetySettingsUnauthorizedErrorResponseBody       | 401                                                                       | application/json                                                          |
| models.SafetySettingsGetSafetySettingsNotFoundErrorResponseBody           | 404                                                                       | application/json                                                          |
| models.SafetySettingsGetSafetySettingsMethodNotAllowedErrorResponseBody   | 405                                                                       | application/json                                                          |
| models.SafetySettingsGetSafetySettingsTooManyRequestsErrorResponseBody    | 429                                                                       | application/json                                                          |
| models.SafetySettingsGetSafetySettingsInternalServerErrorResponseBody     | 500                                                                       | application/json                                                          |
| models.SafetySettingsGetSafetySettingsNotImplementedErrorResponseBody     | 501                                                                       | application/json                                                          |
| models.SafetySettingsGetSafetySettingsBadGatewayErrorResponseBody         | 502                                                                       | application/json                                                          |
| models.SafetySettingsGetSafetySettingsServiceUnavailableErrorResponseBody | 503                                                                       | application/json                                                          |
| models.SafetySettingsGetSafetySettingsGatewayTimeoutErrorResponseBody     | 504                                                                       | application/json                                                          |
| models.APIError                                                           | 4XX, 5XX                                                                  | \*/\*                                                                     |