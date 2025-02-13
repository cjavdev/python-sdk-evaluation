# TrailerAssignments
(*trailer_assignments*)

## Overview

### Available Operations

* [v1get_all_trailer_assignments](#v1get_all_trailer_assignments) - List trailer assignments for all trailers
* [v1get_fleet_trailer_assignments](#v1get_fleet_trailer_assignments) - List trailer assignments for a given trailer

## v1get_all_trailer_assignments

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch trailer assignment data for all trailers in your organization. 

 <b>Rate limit:</b> 100 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.trailer_assignments.v1get_all_trailer_assignments()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                  | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `start_ms`                                                                                                                                                                                 | *Optional[int]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | Timestamp in Unix epoch miliseconds representing the start of the period to fetch. Omitting both startMs and endMs only returns current assignments.                                       |
| `end_ms`                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | Timestamp in Unix epoch miliseconds representing the end of the period to fetch. Omitting endMs sets endMs as the current time                                                             |
| `limit`                                                                                                                                                                                    | *Optional[float]*                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                         | Pagination parameter indicating the number of results to return in this request. Used in conjunction with either 'startingAfter' or 'endingBefore'.                                        |
| `starting_after`                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'endingBefore' parameter. |
| `ending_before`                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | Pagination parameter indicating the cursor position to return results before. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'startingAfter' parameter.           |
| `retries`                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                        |

### Response

**[models.V1getAllTrailerAssignmentsResponse](../../models/v1getalltrailerassignmentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## v1get_fleet_trailer_assignments

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch trailer assignment data for a single trailer. 

 <b>Rate limit:</b> 100 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.trailer_assignments.v1get_fleet_trailer_assignments(trailer_id=556673)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                             | Type                                                                                                                                                  | Required                                                                                                                                              | Description                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `trailer_id`                                                                                                                                          | *int*                                                                                                                                                 | :heavy_check_mark:                                                                                                                                    | ID of trailer. Must contain only digits 0-9.                                                                                                          |
| `start_ms`                                                                                                                                            | *Optional[int]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                    | Timestamp in Unix epoch milliseconds representing the start of the period to fetch. Omitting both startMs and endMs only returns current assignments. |
| `end_ms`                                                                                                                                              | *Optional[int]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                    | Timestamp in Unix epoch milliseconds representing the end of the period to fetch. Omitting endMs sets endMs as the current time                       |
| `retries`                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                      | :heavy_minus_sign:                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                   |

### Response

**[models.V1getFleetTrailerAssignmentsResponse](../../models/v1getfleettrailerassignmentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |