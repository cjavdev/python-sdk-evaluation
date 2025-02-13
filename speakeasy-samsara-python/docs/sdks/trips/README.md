# Trips
(*trips*)

## Overview

### Available Operations

* [v1get_fleet_trips](#v1get_fleet_trips) - Get vehicle trips

## v1get_fleet_trips

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get historical trips data for specified vehicle. This method returns a set of historical trips data for the specified vehicle in the specified time range. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Vehicle Trips** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.trips.v1get_fleet_trips(vehicle_id=124331, start_ms=3074, end_ms=381925)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `vehicle_id`                                                                                                                   | *int*                                                                                                                          | :heavy_check_mark:                                                                                                             | Vehicle ID to query.                                                                                                           |
| `start_ms`                                                                                                                     | *int*                                                                                                                          | :heavy_check_mark:                                                                                                             | Beginning of the time range, specified in milliseconds UNIX time. Limited to a 90 day window with respect to startMs and endMs |
| `end_ms`                                                                                                                       | *int*                                                                                                                          | :heavy_check_mark:                                                                                                             | End of the time range, specified in milliseconds UNIX time.                                                                    |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |

### Response

**[models.V1getFleetTripsResponse](../../models/v1getfleettripsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |