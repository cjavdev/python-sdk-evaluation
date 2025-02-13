# Coaching
(*coaching*)

## Overview

### Available Operations

* [get_driver_coach_assignment](#get_driver_coach_assignment) - Get driver coach assignments.
* [put_driver_coach_assignment](#put_driver_coach_assignment) - Put driver coach assignments.
* [get_coaching_sessions](#get_coaching_sessions) - Get coaching sessions.

## get_driver_coach_assignment

This endpoint will return coach assignments for your organization based on the parameters passed in. Results are paginated.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Coaching** under the Coaching category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.coaching.get_driver_coach_assignment()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                       | Type                                                                                                                                                                                                            | Required                                                                                                                                                                                                        | Description                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `driver_ids`                                                                                                                                                                                                    | List[*str*]                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                              | Optional string of comma separated IDs of the drivers. This can be either a unique Samsara driver ID or an external ID for the driver.                                                                          |
| `coach_ids`                                                                                                                                                                                                     | List[*str*]                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                              | Optional string of comma separated IDs of the coaches.                                                                                                                                                          |
| `include_external_ids`                                                                                                                                                                                          | *Optional[bool]*                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Optional boolean indicating whether to return external IDs on supported entities                                                                                                                                |
| `after`                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              |  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. |
| `retries`                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                             |

### Response

**[models.GetDriverCoachAssignmentResponse](../../models/getdrivercoachassignmentresponse.md)**

### Errors

| Error Type                                                                               | Status Code                                                                              | Content Type                                                                             |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| models.DriverCoachAssignmentsGetDriverCoachAssignmentUnauthorizedErrorResponseBody       | 401                                                                                      | application/json                                                                         |
| models.DriverCoachAssignmentsGetDriverCoachAssignmentNotFoundErrorResponseBody           | 404                                                                                      | application/json                                                                         |
| models.DriverCoachAssignmentsGetDriverCoachAssignmentMethodNotAllowedErrorResponseBody   | 405                                                                                      | application/json                                                                         |
| models.DriverCoachAssignmentsGetDriverCoachAssignmentTooManyRequestsErrorResponseBody    | 429                                                                                      | application/json                                                                         |
| models.DriverCoachAssignmentsGetDriverCoachAssignmentInternalServerErrorResponseBody     | 500                                                                                      | application/json                                                                         |
| models.DriverCoachAssignmentsGetDriverCoachAssignmentNotImplementedErrorResponseBody     | 501                                                                                      | application/json                                                                         |
| models.DriverCoachAssignmentsGetDriverCoachAssignmentBadGatewayErrorResponseBody         | 502                                                                                      | application/json                                                                         |
| models.DriverCoachAssignmentsGetDriverCoachAssignmentServiceUnavailableErrorResponseBody | 503                                                                                      | application/json                                                                         |
| models.DriverCoachAssignmentsGetDriverCoachAssignmentGatewayTimeoutErrorResponseBody     | 504                                                                                      | application/json                                                                         |
| models.APIError                                                                          | 4XX, 5XX                                                                                 | \*/\*                                                                                    |

## put_driver_coach_assignment

This endpoint will update an existing or create a new coach-to-driver assignment for your organization based on the parameters passed in. This endpoint should only be used for existing Coach to Driver assignments. In order to remove a driver-coach-assignment for a given driver, set coachId to null

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Coaching** under the Coaching category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.coaching.put_driver_coach_assignment(driver_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `driver_id`                                                                                                                    | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | Required string ID of the driver. This is a unique Samsara ID of a driver.                                                     |
| `coach_id`                                                                                                                     | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Optional string ID of the coach. This is a unique Samsara user ID. If not provided, existing coach assignment will be removed. |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |

### Response

**[models.PutDriverCoachAssignmentResponse](../../models/putdrivercoachassignmentresponse.md)**

### Errors

| Error Type                                                                               | Status Code                                                                              | Content Type                                                                             |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| models.DriverCoachAssignmentsPutDriverCoachAssignmentUnauthorizedErrorResponseBody       | 401                                                                                      | application/json                                                                         |
| models.DriverCoachAssignmentsPutDriverCoachAssignmentNotFoundErrorResponseBody           | 404                                                                                      | application/json                                                                         |
| models.DriverCoachAssignmentsPutDriverCoachAssignmentMethodNotAllowedErrorResponseBody   | 405                                                                                      | application/json                                                                         |
| models.DriverCoachAssignmentsPutDriverCoachAssignmentTooManyRequestsErrorResponseBody    | 429                                                                                      | application/json                                                                         |
| models.DriverCoachAssignmentsPutDriverCoachAssignmentInternalServerErrorResponseBody     | 500                                                                                      | application/json                                                                         |
| models.DriverCoachAssignmentsPutDriverCoachAssignmentNotImplementedErrorResponseBody     | 501                                                                                      | application/json                                                                         |
| models.DriverCoachAssignmentsPutDriverCoachAssignmentBadGatewayErrorResponseBody         | 502                                                                                      | application/json                                                                         |
| models.DriverCoachAssignmentsPutDriverCoachAssignmentServiceUnavailableErrorResponseBody | 503                                                                                      | application/json                                                                         |
| models.DriverCoachAssignmentsPutDriverCoachAssignmentGatewayTimeoutErrorResponseBody     | 504                                                                                      | application/json                                                                         |
| models.APIError                                                                          | 4XX, 5XX                                                                                 | \*/\*                                                                                    |

## get_coaching_sessions

This endpoint will return coaching sessions for your organization based on the time parameters passed in. Results are paginated by sessions. If you include an endTime, the endpoint will return data up until that point. If you don’t include an endTime, you can continue to poll the API real-time with the pagination cursor that gets returned on every call.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Coaching** under the Coaching category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import dateutil.parser
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.coaching.get_coaching_sessions(start_time=dateutil.parser.isoparse("2025-12-28T14:38:57.179Z"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                                                                                                                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                      | Required RFC 3339 timestamp that indicates when to begin receiving data. Value is compared against `updatedAtTime`                                                                                                                                                                      |
| `driver_ids`                                                                                                                                                                                                                                                                            | List[*str*]                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                      | Optional string of comma separated driver IDs. If driver ID is present, sessions for the specified driver(s) will be returned.                                                                                                                                                          |
| `coach_ids`                                                                                                                                                                                                                                                                             | List[*str*]                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                      | Optional string of comma separated user IDs. If coach ID is present, sessions for the specified coach(s) will be returned for either assignedCoach or completedCoach. If both driverId(s) and coachId(s) are present, sessions with specified driver(s) and coach(es) will be returned. |
| `session_statuses`                                                                                                                                                                                                                                                                      | List[*str*]                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                      | Optional string of comma separated statuses. Valid values:  “upcoming”, “completed”, “deleted”.                                                                                                                                                                                         |
| `include_coachable_events`                                                                                                                                                                                                                                                              | *Optional[bool]*                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                      | Optional boolean to control whether behaviors will include coachableEvents in the response. Defaults to false.                                                                                                                                                                          |
| `end_time`                                                                                                                                                                                                                                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                      | Optional RFC 3339 timestamp. If not provided then the endpoint behaves as an unending feed of changes. If endTime is set the same as startTime, the most recent data point before that time will be returned per asset. Value is compared against `updatedAtTime`                       |
| `after`                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                      |  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.                                                                         |
| `include_external_ids`                                                                                                                                                                                                                                                                  | *Optional[bool]*                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                      | Optional boolean indicating whether to return external IDs on supported entities                                                                                                                                                                                                        |
| `retries`                                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                     |

### Response

**[models.GetCoachingSessionsResponse](../../models/getcoachingsessionsresponse.md)**

### Errors

| Error Type                                                                    | Status Code                                                                   | Content Type                                                                  |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| models.CoachingSessionsGetCoachingSessionsUnauthorizedErrorResponseBody       | 401                                                                           | application/json                                                              |
| models.CoachingSessionsGetCoachingSessionsNotFoundErrorResponseBody           | 404                                                                           | application/json                                                              |
| models.CoachingSessionsGetCoachingSessionsMethodNotAllowedErrorResponseBody   | 405                                                                           | application/json                                                              |
| models.CoachingSessionsGetCoachingSessionsTooManyRequestsErrorResponseBody    | 429                                                                           | application/json                                                              |
| models.CoachingSessionsGetCoachingSessionsInternalServerErrorResponseBody     | 500                                                                           | application/json                                                              |
| models.CoachingSessionsGetCoachingSessionsNotImplementedErrorResponseBody     | 501                                                                           | application/json                                                              |
| models.CoachingSessionsGetCoachingSessionsBadGatewayErrorResponseBody         | 502                                                                           | application/json                                                              |
| models.CoachingSessionsGetCoachingSessionsServiceUnavailableErrorResponseBody | 503                                                                           | application/json                                                              |
| models.CoachingSessionsGetCoachingSessionsGatewayTimeoutErrorResponseBody     | 504                                                                           | application/json                                                              |
| models.APIError                                                               | 4XX, 5XX                                                                      | \*/\*                                                                         |