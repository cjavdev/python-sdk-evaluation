# Safety
(*safety*)

## Overview

### Available Operations

* [get_safety_events](#get_safety_events) - List all safety events.
* [get_safety_activity_event_feed](#get_safety_activity_event_feed) - Fetches safety activity event feed
* [v1get_driver_safety_score](#v1get_driver_safety_score) - Fetch driver safety score
* [v1get_vehicle_harsh_event](#v1get_vehicle_harsh_event) - Fetch harsh events
* [v1get_vehicle_safety_score](#v1get_vehicle_safety_score) - Fetch vehicle safety scores

## get_safety_events

Fetch safety events for the organization in a given time period. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.safety.get_safety_events(start_time="<value>", end_time="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                      | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).                                                           |
| `end_time`                                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                      | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).                                                            |
| `after`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                      | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.                          |
| `tag_ids`                                                                                                                                                                                                                               | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`                                                                                                                                         |
| `parent_tag_ids`                                                                                                                                                                                                                        | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` |
| `vehicle_ids`                                                                                                                                                                                                                           | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`                                                                                                                                 |
| `retries`                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                     |

### Response

**[models.GetSafetyEventsResponse](../../models/getsafetyeventsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_safety_activity_event_feed

Get continuous safety events. The safety activity event feed offers a change-log for safety events. Use this endpoint to subscribe to safety event changes. See documentation below for all supported change-log types.

| ActivityType      | Description |
| ----------- | ----------- |
| CreateSafetyEventActivityType | a new safety event is processed by Samsara      |
| BehaviorLabelActivityType     | a label is added or removed from a safety event |
| CoachingStateActivityType     | a safety event coaching state is updated        |

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

    res = s_client.safety.get_safety_activity_event_feed()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                       | Type                                                                                                                                                                                                            | Required                                                                                                                                                                                                        | Description                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `after`                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              |  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. |
| `start_time`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              |  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). |
| `retries`                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                             |

### Response

**[models.GetSafetyActivityEventFeedResponse](../../models/getsafetyactivityeventfeedresponse.md)**

### Errors

| Error Type                                                                       | Status Code                                                                      | Content Type                                                                     |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| models.SafetyEventsGetSafetyActivityEventFeedUnauthorizedErrorResponseBody       | 401                                                                              | application/json                                                                 |
| models.SafetyEventsGetSafetyActivityEventFeedNotFoundErrorResponseBody           | 404                                                                              | application/json                                                                 |
| models.SafetyEventsGetSafetyActivityEventFeedMethodNotAllowedErrorResponseBody   | 405                                                                              | application/json                                                                 |
| models.SafetyEventsGetSafetyActivityEventFeedTooManyRequestsErrorResponseBody    | 429                                                                              | application/json                                                                 |
| models.SafetyEventsGetSafetyActivityEventFeedInternalServerErrorResponseBody     | 500                                                                              | application/json                                                                 |
| models.SafetyEventsGetSafetyActivityEventFeedNotImplementedErrorResponseBody     | 501                                                                              | application/json                                                                 |
| models.SafetyEventsGetSafetyActivityEventFeedBadGatewayErrorResponseBody         | 502                                                                              | application/json                                                                 |
| models.SafetyEventsGetSafetyActivityEventFeedServiceUnavailableErrorResponseBody | 503                                                                              | application/json                                                                 |
| models.SafetyEventsGetSafetyActivityEventFeedGatewayTimeoutErrorResponseBody     | 504                                                                              | application/json                                                                 |
| models.APIError                                                                  | 4XX, 5XX                                                                         | \*/\*                                                                            |

## v1get_driver_safety_score

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch the safety score for the driver.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.safety.v1get_driver_safety_score(driver_id=300069, start_ms=73935, end_ms=864923)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                     | Type                                                                                                                                                                                          | Required                                                                                                                                                                                      | Description                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `driver_id`                                                                                                                                                                                   | *int*                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                            | ID of the driver. Must contain only digits 0-9.                                                                                                                                               |
| `start_ms`                                                                                                                                                                                    | *int*                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                            | Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. |
| `end_ms`                                                                                                                                                                                      | *int*                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                            | Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. |
| `retries`                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                           |

### Response

**[models.V1getDriverSafetyScoreResponse](../../models/v1getdriversafetyscoreresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## v1get_vehicle_harsh_event

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch harsh event details for a vehicle. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.safety.v1get_vehicle_harsh_event(vehicle_id=250848, timestamp=634869)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `vehicle_id`                                                           | *int*                                                                  | :heavy_check_mark:                                                     | ID of the vehicle. Must contain only digits 0-9.                       |
| `timestamp`                                                            | *int*                                                                  | :heavy_check_mark:                                                     | Timestamp in milliseconds representing the timestamp of a harsh event. |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[models.V1getVehicleHarshEventResponse](../../models/v1getvehicleharsheventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## v1get_vehicle_safety_score

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch the safety score for the vehicle. 

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.safety.v1get_vehicle_safety_score(vehicle_id=331130, start_ms=872404, end_ms=825717)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                     | Type                                                                                                                                                                                          | Required                                                                                                                                                                                      | Description                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `vehicle_id`                                                                                                                                                                                  | *int*                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                            | ID of the vehicle. Must contain only digits 0-9.                                                                                                                                              |
| `start_ms`                                                                                                                                                                                    | *int*                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                            | Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. |
| `end_ms`                                                                                                                                                                                      | *int*                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                            | Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. |
| `retries`                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                           |

### Response

**[models.V1getVehicleSafetyScoreResponse](../../models/v1getvehiclesafetyscoreresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |