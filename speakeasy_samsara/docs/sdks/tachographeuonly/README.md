# TachographEUOnly
(*tachograph_eu_only*)

## Overview

### Available Operations

* [get_driver_tachograph_activity](#get_driver_tachograph_activity) - Get driver tachograph activity
* [get_driver_tachograph_files](#get_driver_tachograph_files) - Get tachograph driver files
* [get_vehicle_tachograph_files](#get_vehicle_tachograph_files) - Get tachograph vehicle files

## get_driver_tachograph_activity

Returns all known tachograph activity for all specified drivers in the time range. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Tachograph (EU)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.tachograph_eu_only.get_driver_tachograph_activity(start_time="<value>", end_time="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                      | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).                                                           |
| `end_time`                                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                      | An end time in RFC 3339 format. It can't be more than 30 days past startTime. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).              |
| `after`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                      | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.                          |
| `driver_ids`                                                                                                                                                                                                                            | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of driver IDs. Example: `driverIds=1234,5678`                                                                                                                                   |
| `parent_tag_ids`                                                                                                                                                                                                                        | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` |
| `tag_ids`                                                                                                                                                                                                                               | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`                                                                                                                                         |
| `retries`                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                     |

### Response

**[models.GetDriverTachographActivityResponse](../../models/getdrivertachographactivityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_driver_tachograph_files

Returns all known tachograph files for all specified drivers in the time range. 

 <b>Rate limit:</b> 50 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Tachograph (EU)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.tachograph_eu_only.get_driver_tachograph_files(start_time="<value>", end_time="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                      | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).                                                           |
| `end_time`                                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                      | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).                                                            |
| `after`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                      | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.                          |
| `driver_ids`                                                                                                                                                                                                                            | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of driver IDs. Example: `driverIds=1234,5678`                                                                                                                                   |
| `parent_tag_ids`                                                                                                                                                                                                                        | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` |
| `tag_ids`                                                                                                                                                                                                                               | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`                                                                                                                                         |
| `retries`                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                     |

### Response

**[models.GetDriverTachographFilesResponse](../../models/getdrivertachographfilesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_vehicle_tachograph_files

Returns all known tachograph files for all specified vehicles in the time range. 

 <b>Rate limit:</b> 150 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Tachograph (EU)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.tachograph_eu_only.get_vehicle_tachograph_files(start_time="<value>", end_time="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                      | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).                                                           |
| `end_time`                                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                      | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).                                                            |
| `after`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                      | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.                          |
| `vehicle_ids`                                                                                                                                                                                                                           | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`                                                                                                                                 |
| `parent_tag_ids`                                                                                                                                                                                                                        | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` |
| `tag_ids`                                                                                                                                                                                                                               | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`                                                                                                                                         |
| `retries`                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                     |

### Response

**[models.GetVehicleTachographFilesResponse](../../models/getvehicletachographfilesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |