# VehicleLocations
(*vehicle_locations*)

## Overview

### Available Operations

* [get_vehicle_locations](#get_vehicle_locations) - Locations snapshot
* [get_vehicle_locations_feed](#get_vehicle_locations_feed) - Locations feed
* [get_vehicle_locations_history](#get_vehicle_locations_history) - Historical locations

## get_vehicle_locations

***NOTE: The Vehicle Locations API is an older API that does not combine GPS data with onboard diagnostics. Try our new [Vehicle Stats API](ref:getvehiclestats) instead.***

Returns the last known location of all vehicles at the given `time`. If no `time` is specified, the current time is used. This can be optionally filtered by tags or specific vehicle IDs.

Related guide: <a href="/docs/vehicle-locations-1" target="_blank">Vehicle Locations</a>. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Vehicle Statistics** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.vehicle_locations.get_vehicle_locations()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `after`                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                         | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.                                                             |
| `time`                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                         | A filter on the data that returns the last known data points with timestamps less than or equal to this value. Defaults to now if not provided. Must be a string in RFC 3339 format. Millisecond precision and timezones are supported. (Example: `2020-01-27T07:06:25Z`). |
| `parent_tag_ids`                                                                                                                                                                                                                                                           | List[*str*]                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                         | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`                                    |
| `tag_ids`                                                                                                                                                                                                                                                                  | List[*str*]                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                         | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`                                                                                                                                                                            |
| `vehicle_ids`                                                                                                                                                                                                                                                              | List[*str*]                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                         | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`                                                                                                                                                                    |
| `retries`                                                                                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                        |

### Response

**[models.GetVehicleLocationsResponse](../../models/getvehiclelocationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_vehicle_locations_feed

***NOTE: The Vehicle Locations API is an older API that does not combine GPS data with onboard diagnostics. Try our new [Vehicle Stats API](ref:getvehiclestatsfeed) instead.***

Follow a continuous feed of all vehicle locations from Samsara Vehicle Gateways.

Your first call to this endpoint will provide you with the most recent location for each vehicle and a `pagination` object that contains an `endCursor`.

You can provide the `endCursor` to the `after` parameter of this endpoint to get location updates since that `endCursor`. 

If `hasNextPage` is `false`, no updates are readily available yet. We'd suggest waiting a minimum of 5 seconds before requesting updates.

Related guide: <a href="/docs/vehicle-locations-1" target="_blank">Vehicle Locations</a>. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Vehicle Statistics** under the Vehicle category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.vehicle_locations.get_vehicle_locations_feed()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `after`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                      | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.                          |
| `parent_tag_ids`                                                                                                                                                                                                                        | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` |
| `tag_ids`                                                                                                                                                                                                                               | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`                                                                                                                                         |
| `vehicle_ids`                                                                                                                                                                                                                           | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`                                                                                                                                 |
| `retries`                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                     |

### Response

**[models.GetVehicleLocationsFeedResponse](../../models/getvehiclelocationsfeedresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_vehicle_locations_history

***NOTE: The Vehicle Locations API is an older API that does not combine GPS data with onboard diagnostics. Try our new [Vehicle Stats API](ref:getvehiclestatshistory) instead.***

Returns all known vehicle locations during the given time range. This can be optionally filtered by tags or specific vehicle IDs.

Related guide: <a href="/docs/vehicle-locations-1" target="_blank">Vehicle Locations</a>. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Vehicle Statistics** under the Vehicle category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.vehicle_locations.get_vehicle_locations_history(start_time="<value>", end_time="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                      | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).                                                           |
| `end_time`                                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                      | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).                                                            |
| `after`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                      | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.                          |
| `parent_tag_ids`                                                                                                                                                                                                                        | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` |
| `tag_ids`                                                                                                                                                                                                                               | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`                                                                                                                                         |
| `vehicle_ids`                                                                                                                                                                                                                           | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`                                                                                                                                 |
| `retries`                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                     |

### Response

**[models.GetVehicleLocationsHistoryResponse](../../models/getvehiclelocationshistoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |