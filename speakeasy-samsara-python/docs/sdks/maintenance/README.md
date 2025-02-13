# Maintenance
(*maintenance*)

## Overview

### Available Operations

* [get_defect_types](#get_defect_types) - Get DVIR defect types.
* [stream_defects](#stream_defects) - Stream DVIR defects.
* [get_dvirs](#get_dvirs) - Stream DVIRs
* [get_dvir_defects](#get_dvir_defects) - Get all defects
* [update_dvir_defect](#update_dvir_defect) - Update a defect
* [create_dvir](#create_dvir) - Create a mechanic DVIR
* [get_dvir_history](#get_dvir_history) - Get all DVIRs
* [update_dvir](#update_dvir) - Resolve a DVIR
* [v1get_fleet_maintenance_list](#v1get_fleet_maintenance_list) - Get vehicles with engine faults or check lights

## get_defect_types

Get DVIR defect types.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Defect Types** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.maintenance.get_defect_types()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                       | Type                                                                                                                                                                                                            | Required                                                                                                                                                                                                        | Description                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `after`                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              |  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. |
| `limit`                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              | The limit for how many objects will be in the response. Default and max for this value is 512 objects.                                                                                                          |
| `ids`                                                                                                                                                                                                           | List[*str*]                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                              | A filter on the data based on this comma-separated list of defect type IDs.                                                                                                                                     |
| `retries`                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                             |

### Response

**[models.GetDefectTypesResponse](../../models/getdefecttypesresponse.md)**

### Errors

| Error Type                                                             | Status Code                                                            | Content Type                                                           |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| models.DvirDefectTypeGetDefectTypesUnauthorizedErrorResponseBody       | 401                                                                    | application/json                                                       |
| models.DvirDefectTypeGetDefectTypesNotFoundErrorResponseBody           | 404                                                                    | application/json                                                       |
| models.DvirDefectTypeGetDefectTypesMethodNotAllowedErrorResponseBody   | 405                                                                    | application/json                                                       |
| models.DvirDefectTypeGetDefectTypesTooManyRequestsErrorResponseBody    | 429                                                                    | application/json                                                       |
| models.DvirDefectTypeGetDefectTypesInternalServerErrorResponseBody     | 500                                                                    | application/json                                                       |
| models.DvirDefectTypeGetDefectTypesNotImplementedErrorResponseBody     | 501                                                                    | application/json                                                       |
| models.DvirDefectTypeGetDefectTypesBadGatewayErrorResponseBody         | 502                                                                    | application/json                                                       |
| models.DvirDefectTypeGetDefectTypesServiceUnavailableErrorResponseBody | 503                                                                    | application/json                                                       |
| models.DvirDefectTypeGetDefectTypesGatewayTimeoutErrorResponseBody     | 504                                                                    | application/json                                                       |
| models.APIError                                                        | 4XX, 5XX                                                               | \*/\*                                                                  |

## stream_defects

Stream DVIR defects.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Defects** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.maintenance.stream_defects(start_time="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                       | Type                                                                                                                                                                                                            | Required                                                                                                                                                                                                        | Description                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                                                                                                    | *str*                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                              | Required RFC 3339 timestamp to begin the feed or history by `updatedAtTime` at `startTime`.                                                                                                                     |
| `after`                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              |  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. |
| `limit`                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              | The limit for how many objects will be in the response. Default and max for this value is 200 objects.                                                                                                          |
| `end_time`                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              | Optional RFC 3339 timestamp. If not provided then the endpoint behaves as an unending feed of changes.                                                                                                          |
| `include_external_ids`                                                                                                                                                                                          | *Optional[bool]*                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Optional boolean indicating whether to return external IDs on supported entities                                                                                                                                |
| `is_resolved`                                                                                                                                                                                                   | *Optional[bool]*                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Boolean value for whether filter defects by resolved status.                                                                                                                                                    |
| `retries`                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                             |

### Response

**[models.StreamDefectsResponse](../../models/streamdefectsresponse.md)**

### Errors

| Error Type                                                        | Status Code                                                       | Content Type                                                      |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| models.DvirDefectStreamDefectsUnauthorizedErrorResponseBody       | 401                                                               | application/json                                                  |
| models.DvirDefectStreamDefectsNotFoundErrorResponseBody           | 404                                                               | application/json                                                  |
| models.DvirDefectStreamDefectsMethodNotAllowedErrorResponseBody   | 405                                                               | application/json                                                  |
| models.DvirDefectStreamDefectsTooManyRequestsErrorResponseBody    | 429                                                               | application/json                                                  |
| models.DvirDefectStreamDefectsInternalServerErrorResponseBody     | 500                                                               | application/json                                                  |
| models.DvirDefectStreamDefectsNotImplementedErrorResponseBody     | 501                                                               | application/json                                                  |
| models.DvirDefectStreamDefectsBadGatewayErrorResponseBody         | 502                                                               | application/json                                                  |
| models.DvirDefectStreamDefectsServiceUnavailableErrorResponseBody | 503                                                               | application/json                                                  |
| models.DvirDefectStreamDefectsGatewayTimeoutErrorResponseBody     | 504                                                               | application/json                                                  |
| models.APIError                                                   | 4XX, 5XX                                                          | \*/\*                                                             |

## get_dvirs

Returns a history/feed of changed DVIRs by updatedAtTime between startTime and endTime parameters. In case of missing `endTime` parameter it will return a never ending stream of data.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read DVIRs** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.maintenance.get_dvirs(start_time="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                       | Type                                                                                                                                                                                                            | Required                                                                                                                                                                                                        | Description                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                                                                                                    | *str*                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                              | Required RFC 3339 timestamp to begin the feed or history by `updatedAtTime` at `startTime`.                                                                                                                     |
| `after`                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              |  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. |
| `limit`                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              | The limit for how many objects will be in the response. Default and max for this value is 200 objects.                                                                                                          |
| `include_external_ids`                                                                                                                                                                                          | *Optional[bool]*                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Optional boolean indicating whether to return external IDs on supported entities                                                                                                                                |
| `end_time`                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              | Optional RFC 3339 timestamp. If not provided then the endpoint behaves as an unending feed of changes.                                                                                                          |
| `safety_status`                                                                                                                                                                                                 | List[*str*]                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                              | Optional list of safety statuses. Valid values: [safe, unsafe, resolved]                                                                                                                                        |
| `retries`                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                             |

### Response

**[models.GetDvirsResponse](../../models/getdvirsresponse.md)**

### Errors

| Error Type                                             | Status Code                                            | Content Type                                           |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| models.DvirGetDvirsUnauthorizedErrorResponseBody       | 401                                                    | application/json                                       |
| models.DvirGetDvirsNotFoundErrorResponseBody           | 404                                                    | application/json                                       |
| models.DvirGetDvirsMethodNotAllowedErrorResponseBody   | 405                                                    | application/json                                       |
| models.DvirGetDvirsTooManyRequestsErrorResponseBody    | 429                                                    | application/json                                       |
| models.DvirGetDvirsInternalServerErrorResponseBody     | 500                                                    | application/json                                       |
| models.DvirGetDvirsNotImplementedErrorResponseBody     | 501                                                    | application/json                                       |
| models.DvirGetDvirsBadGatewayErrorResponseBody         | 502                                                    | application/json                                       |
| models.DvirGetDvirsServiceUnavailableErrorResponseBody | 503                                                    | application/json                                       |
| models.DvirGetDvirsGatewayTimeoutErrorResponseBody     | 504                                                    | application/json                                       |
| models.APIError                                        | 4XX, 5XX                                               | \*/\*                                                  |

## get_dvir_defects

Returns a list of DVIR defects in an organization, filtered by creation time. The maximum time period you can query for is 30 days. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Defects** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.maintenance.get_dvir_defects(start_time="<value>", end_time="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                    | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). *The maximum time period you can query for is 30 days.* |
| `end_time`                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                    | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). *The maximum time period you can query for is 30 days.*  |
| `limit`                                                                                                                                                                                                                               | *Optional[int]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | The limit for how many objects will be in the response. Default and max for this value is 512 objects.                                                                                                                                |
| `after`                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                    | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.                        |
| `is_resolved`                                                                                                                                                                                                                         | *Optional[bool]*                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                    | A filter on the data based on resolution status. Example: `isResolved=true`                                                                                                                                                           |
| `retries`                                                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                                                   |

### Response

**[models.GetDvirDefectsResponse](../../models/getdvirdefectsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_dvir_defect

Updates a given defect. Can be used to resolve a defect by marking its `isResolved` field to `true`. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Defects** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
import samsara
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.maintenance.update_dvir_defect(id="<id>", mechanic_notes="Extremely large oddly shaped hole in passenger side window.", resolved_at_time="2020-01-27T07:06:25Z", resolved_by={
        "id": "11",
        "type": samsara.ResolvedByType.MECHANIC,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        | Example                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                               | *str*                                                                                                                              | :heavy_check_mark:                                                                                                                 | ID of the defect.                                                                                                                  |                                                                                                                                    |
| `is_resolved`                                                                                                                      | *Optional[bool]*                                                                                                                   | :heavy_minus_sign:                                                                                                                 | Resolves the defect. Must be `true`.                                                                                               |                                                                                                                                    |
| `mechanic_notes`                                                                                                                   | *Optional[str]*                                                                                                                    | :heavy_minus_sign:                                                                                                                 | The mechanics notes on the defect.                                                                                                 | Extremely large oddly shaped hole in passenger side window.                                                                        |
| `resolved_at_time`                                                                                                                 | *Optional[str]*                                                                                                                    | :heavy_minus_sign:                                                                                                                 | Time when defect was resolved. Defaults to now if not provided. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`. | 2020-01-27T07:06:25Z                                                                                                               |
| `resolved_by`                                                                                                                      | [Optional[models.ResolvedBy]](../../models/resolvedby.md)                                                                          | :heavy_minus_sign:                                                                                                                 | Information about the user who is resolving a defect.                                                                              |                                                                                                                                    |
| `retries`                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                   | :heavy_minus_sign:                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                |                                                                                                                                    |

### Response

**[models.UpdateDvirDefectResponse](../../models/updatedvirdefectresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_dvir

Creates a new mechanic DVIR in the organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write DVIRs** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
import samsara
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.maintenance.create_dvir(request={
        "author_id": "11",
        "safety_status": samsara.CreateDvirRequestSafetyStatus.SAFE,
        "type": samsara.CreateDvirRequestType.MECHANIC,
        "license_plate": "XHK1234",
        "location": "350 Rhode Island St Ste. 400S, San Francisco, CA 94103",
        "mechanic_notes": "Replaced headlight on passenger side.",
        "odometer_meters": 14010293,
        "trailer_id": "11",
        "vehicle_id": "10",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CreateDvirRequest](../../models/createdvirrequest.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateDvirResponse](../../models/createdvirresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_dvir_history

Returns a list of all DVIRs in an organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read DVIRs** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.maintenance.get_dvir_history(start_time="<value>", end_time="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                      | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).                                                           |
| `end_time`                                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                      | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).                                                            |
| `limit`                                                                                                                                                                                                                                 | *Optional[int]*                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                      | The limit for how many objects will be in the response. Default and max for this value is 512 objects.                                                                                                                                  |
| `after`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                      | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.                          |
| `parent_tag_ids`                                                                                                                                                                                                                        | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` |
| `tag_ids`                                                                                                                                                                                                                               | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`                                                                                                                                         |
| `retries`                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                     |

### Response

**[models.GetDvirHistoryResponse](../../models/getdvirhistoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_dvir

Resolves a given DVIR by marking its `isResolved` field to `true`. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write DVIRs** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.maintenance.update_dvir(id="<id>", author_id="11", is_resolved=False, mechanic_notes="Replaced headlight on passenger side.", signed_at_time="2020-01-27T07:06:25Z")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          | Example                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                 | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | ID of the DVIR.                                                                                                      |                                                                                                                      |
| `author_id`                                                                                                          | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | The user who is resolving the dvir.                                                                                  | 11                                                                                                                   |
| `is_resolved`                                                                                                        | *bool*                                                                                                               | :heavy_check_mark:                                                                                                   | Resolves the DVIR. Must be `true`.                                                                                   |                                                                                                                      |
| `mechanic_notes`                                                                                                     | *Optional[str]*                                                                                                      | :heavy_minus_sign:                                                                                                   | The mechanics notes on the DVIR.                                                                                     | Replaced headlight on passenger side.                                                                                |
| `signed_at_time`                                                                                                     | *Optional[str]*                                                                                                      | :heavy_minus_sign:                                                                                                   | Time when user signed this DVIR. Defaults to now. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`. | 2020-01-27T07:06:25Z                                                                                                 |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |                                                                                                                      |

### Response

**[models.UpdateDvirResponse](../../models/updatedvirresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## v1get_fleet_maintenance_list

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get list of the vehicles with any engine faults or check light data. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read DVIRs** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.maintenance.v1get_fleet_maintenance_list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.V1getFleetMaintenanceListResponse](../../models/v1getfleetmaintenancelistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |