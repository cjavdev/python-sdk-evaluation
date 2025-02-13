# Industrial
(*industrial*)

## Overview

### Available Operations

* [get_industrial_assets](#get_industrial_assets) - List all assets
* [create_industrial_asset](#create_industrial_asset) - Create an asset
* [delete_industrial_asset](#delete_industrial_asset) - Delete an existing asset
* [patch_industrial_asset](#patch_industrial_asset) - Update an asset
* [patch_asset_data_outputs](#patch_asset_data_outputs) - Writes to data outputs on an asset
* [get_data_inputs](#get_data_inputs) - List all data inputs
* [get_data_input_data_snapshot](#get_data_input_data_snapshot) - List most recent data points for data inputs
* [get_data_input_data_feed](#get_data_input_data_feed) - Follow a real-time feed of data points for data inputs
* [get_data_input_data_history](#get_data_input_data_history) - List historical data points for data inputs
* [v1get_cameras](#v1get_cameras) - Fetch industrial cameras
* [v1get_vision_programs_by_camera](#v1get_vision_programs_by_camera) - Fetch industrial camera programs
* [v1get_vision_latest_run_camera](#v1get_vision_latest_run_camera) - Fetch the latest run for a camera or program
* [v1get_vision_runs](#v1get_vision_runs) - Fetch runs
* [get_vision_runs_by_camera](#get_vision_runs_by_camera) - Fetch runs by camera
* [v1get_vision_runs_by_camera_and_program](#v1get_vision_runs_by_camera_and_program) - Fetch runs by camera and program
* [v1get_machines_history](#v1get_machines_history) - Get machine history
* [v1get_machines](#v1get_machines) - Get machines

## get_industrial_assets

List all assets in the organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.industrial.get_industrial_assets()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                                                                                                                 | *Optional[int]*                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                      | The limit for how many objects will be in the response. Default and max for this value is 512 objects.                                                                                                                                  |
| `after`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                      | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.                          |
| `parent_tag_ids`                                                                                                                                                                                                                        | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` |
| `tag_ids`                                                                                                                                                                                                                               | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`                                                                                                                                         |
| `asset_ids`                                                                                                                                                                                                                             | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A comma-separated list of industrial asset UUIDs. Example: `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`                                                                                         |
| `retries`                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                     |

### Response

**[models.GetIndustrialAssetsResponse](../../models/getindustrialassetsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_industrial_asset

Create an asset with optional configuration parameters. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Equipment** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.industrial.create_industrial_asset(request={
        "name": "<value>",
        "custom_metadata": {
            "manufacturer": "Samsara",
            "serialNumber": "123ABC",
        },
        "location": {
            "formatted_address": "350 Rhode Island St, San Francisco CA, 94103",
            "latitude": 37.765363,
            "longitude": -122.403098,
        },
        "location_data_input_id": "12345",
        "parent_id": "123abcde-4567-8910-1112-fghi1314jklm",
        "running_status_data_input_id": "67890",
        "tag_ids": [
            "123",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.AssetCreate](../../models/assetcreate.md)                   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateIndustrialAssetResponse](../../models/createindustrialassetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_industrial_asset

Delete asset. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Equipment** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.industrial.delete_industrial_asset(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Id of the asset to be deleted.                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteIndustrialAssetResponse](../../models/deleteindustrialassetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## patch_industrial_asset

Update an existing asset. Only the provided fields will be updated. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Equipment** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.industrial.patch_industrial_asset(id="<id>", custom_metadata={
        "manufacturer": "Samsara",
        "serialNumber": "123ABC",
    }, location={
        "formatted_address": "350 Rhode Island St, San Francisco CA, 94103",
        "latitude": 37.765363,
        "longitude": -122.403098,
    }, location_data_input_id="12345", parent_id="", running_status_data_input_id="67890", tag_ids=[
        "123",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                     | Id of the asset to be updated                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                        |
| `custom_metadata`                                                                                                                                                                                                                                      | Dict[str, *str*]                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                     | The custom fields of an asset.                                                                                                                                                                                                                         | {<br/>"manufacturer": "Samsara",<br/>"serialNumber": "123ABC"<br/>}                                                                                                                                                                                    |
| `location`                                                                                                                                                                                                                                             | [Optional[models.AssetLocation]](../../models/assetlocation.md)                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                     | For locationType "point", latitude and longitude are required. For "address", formattedAddress must be provided, and lat/long can be optionally included for displaying a dot on the assets map. For "dataInput", this object should not be passed in. |                                                                                                                                                                                                                                                        |
| `location_data_input_id`                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                     | Required if locationType is "dataInput". Specifies the id of a location data input which will determine the asset's location. The data input must be in the asset.                                                                                     | 12345                                                                                                                                                                                                                                                  |
| `location_type`                                                                                                                                                                                                                                        | [Optional[models.LocationType]](../../models/locationtype.md)                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                     | The format of the location. This field is required if a location is provided. Valid values: `point`, `address`, `dataInput`.                                                                                                                           |                                                                                                                                                                                                                                                        |
| `name`                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                     | The name of the asset.                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                        |
| `parent_id`                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                     | The id of the parent asset that the asset belongs to. Pass in an empty string to remove the child from the parent.                                                                                                                                     |                                                                                                                                                                                                                                                        |
| `running_status_data_input_id`                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                     | The asset's isRunning status will be true when the associated data input's value is 1. Data input cannot be of location format. The data input must be in the asset.                                                                                   | 67890                                                                                                                                                                                                                                                  |
| `tag_ids`                                                                                                                                                                                                                                              | List[*str*]                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                     | The ids of the tags that the asset should belong to.                                                                                                                                                                                                   |                                                                                                                                                                                                                                                        |
| `retries`                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                    |                                                                                                                                                                                                                                                        |

### Response

**[models.PatchIndustrialAssetResponse](../../models/patchindustrialassetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## patch_asset_data_outputs

Writes values to multiple data outputs on an asset simultaneously. Only the provided data outputs will be updated.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.industrial.patch_asset_data_outputs(id="<id>", values={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    | Example                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                           | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | Asset ID                                                                                                                       |                                                                                                                                |
| `values`                                                                                                                       | [models.Values](../../models/values.md)                                                                                        | :heavy_check_mark:                                                                                                             | A map of data output IDs to values. All data outputs must belong to the same asset. Only the specified IDs will be written to. |                                                                                                                                |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |                                                                                                                                |

### Response

**[models.PatchAssetDataOutputsResponse](../../models/patchassetdataoutputsresponse.md)**

### Errors

| Error Type                                                                      | Status Code                                                                     | Content Type                                                                    |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| models.AssetDataOutputsPatchAssetDataOutputsUnauthorizedErrorResponseBody       | 401                                                                             | application/json                                                                |
| models.AssetDataOutputsPatchAssetDataOutputsNotFoundErrorResponseBody           | 404                                                                             | application/json                                                                |
| models.AssetDataOutputsPatchAssetDataOutputsMethodNotAllowedErrorResponseBody   | 405                                                                             | application/json                                                                |
| models.AssetDataOutputsPatchAssetDataOutputsTooManyRequestsErrorResponseBody    | 429                                                                             | application/json                                                                |
| models.AssetDataOutputsPatchAssetDataOutputsInternalServerErrorResponseBody     | 500                                                                             | application/json                                                                |
| models.AssetDataOutputsPatchAssetDataOutputsNotImplementedErrorResponseBody     | 501                                                                             | application/json                                                                |
| models.AssetDataOutputsPatchAssetDataOutputsBadGatewayErrorResponseBody         | 502                                                                             | application/json                                                                |
| models.AssetDataOutputsPatchAssetDataOutputsServiceUnavailableErrorResponseBody | 503                                                                             | application/json                                                                |
| models.AssetDataOutputsPatchAssetDataOutputsGatewayTimeoutErrorResponseBody     | 504                                                                             | application/json                                                                |
| models.APIError                                                                 | 4XX, 5XX                                                                        | \*/\*                                                                           |

## get_data_inputs

Returns all data inputs, optionally filtered by tags or asset ids. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.industrial.get_data_inputs()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                                                                                                                 | *Optional[int]*                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                      | The limit for how many objects will be in the response. Default and max for this value is 512 objects.                                                                                                                                  |
| `after`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                      | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.                          |
| `parent_tag_ids`                                                                                                                                                                                                                        | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` |
| `tag_ids`                                                                                                                                                                                                                               | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`                                                                                                                                         |
| `asset_ids`                                                                                                                                                                                                                             | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A comma-separated list of industrial asset UUIDs. Example: `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`                                                                                         |
| `retries`                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                     |

### Response

**[models.GetDataInputsResponse](../../models/getdatainputsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_data_input_data_snapshot

Returns last known data points for all data inputs. This can be filtered by optional tags, specific data input IDs or asset IDs. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.industrial.get_data_input_data_snapshot()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `after`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                      | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.                          |
| `parent_tag_ids`                                                                                                                                                                                                                        | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` |
| `tag_ids`                                                                                                                                                                                                                               | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`                                                                                                                                         |
| `data_input_ids`                                                                                                                                                                                                                        | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A comma-separated list of data input IDs. Example: `dataInputIds=1234,5678`                                                                                                                                                             |
| `asset_ids`                                                                                                                                                                                                                             | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A comma-separated list of industrial asset UUIDs. Example: `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`                                                                                         |
| `retries`                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                     |

### Response

**[models.GetDataInputDataSnapshotResponse](../../models/getdatainputdatasnapshotresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_data_input_data_feed

Follow a continuous feed of all data input data points.

Your first call to this endpoint will provide you with the most recent data points for each data input and a `pagination` object that contains an `endCursor`.

You can provide the `endCursor` to the `after` parameter of this endpoint to get data point updates since that `endCursor`.

If `hasNextPage` is `false`, no updates are readily available yet. We suggest waiting a minimum of 5 seconds before requesting updates. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.industrial.get_data_input_data_feed()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `after`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                      | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.                          |
| `parent_tag_ids`                                                                                                                                                                                                                        | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` |
| `tag_ids`                                                                                                                                                                                                                               | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`                                                                                                                                         |
| `data_input_ids`                                                                                                                                                                                                                        | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A comma-separated list of data input IDs. Example: `dataInputIds=1234,5678`                                                                                                                                                             |
| `asset_ids`                                                                                                                                                                                                                             | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A comma-separated list of industrial asset UUIDs. Example: `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`                                                                                         |
| `retries`                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                     |

### Response

**[models.GetDataInputDataFeedResponse](../../models/getdatainputdatafeedresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_data_input_data_history

Returns all known data points during the given time range for all data inputs. This can be filtered by optional tags, specific data input IDs or asset IDs. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.industrial.get_data_input_data_history(start_time="<value>", end_time="<value>")

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
| `data_input_ids`                                                                                                                                                                                                                        | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A comma-separated list of data input IDs. Example: `dataInputIds=1234,5678`                                                                                                                                                             |
| `asset_ids`                                                                                                                                                                                                                             | List[*str*]                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                      | A comma-separated list of industrial asset UUIDs. Example: `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`                                                                                         |
| `retries`                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                     |

### Response

**[models.GetDataInputDataHistoryResponse](../../models/getdatainputdatahistoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## v1get_cameras

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch all cameras. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.industrial.v1get_cameras()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.V1getCamerasResponse](../../models/v1getcamerasresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## v1get_vision_programs_by_camera

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch configured programs on the camera. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.industrial.v1get_vision_programs_by_camera(camera_id=638205)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `camera_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The camera_id should be valid for the given accessToken.            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.V1getVisionProgramsByCameraResponse](../../models/v1getvisionprogramsbycameraresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## v1get_vision_latest_run_camera

Fetch the latest run for a camera or program by default. If startedAtMs is supplied, fetch the specific run that corresponds to that start time. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.industrial.v1get_vision_latest_run_camera(camera_id=274970)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `camera_id`                                                           | *int*                                                                 | :heavy_check_mark:                                                    | The camera_id should be valid for the given accessToken.              |
| `program_id`                                                          | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | The configured program's ID on the camera.                            |
| `started_at_ms`                                                       | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | EndMs is an optional param. It will default to the current time.      |
| `include`                                                             | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Include is a filter parameter. Accepts 'pass', 'reject' or 'no_read'. |
| `limit`                                                               | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | Limit is an integer value from 1 to 1,000.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.V1getVisionLatestRunCameraResponse](../../models/v1getvisionlatestruncameraresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## v1get_vision_runs

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch runs. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.industrial.v1get_vision_runs(duration_ms=351708)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `duration_ms`                                                                                                                       | *int*                                                                                                                               | :heavy_check_mark:                                                                                                                  | DurationMs is a required param. This works with the EndMs parameter. Indicates the duration in which the visionRuns will be fetched |
| `end_ms`                                                                                                                            | *Optional[int]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | EndMs is an optional param. It will default to the current time.                                                                    |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |

### Response

**[models.V1getVisionRunsResponse](../../models/v1getvisionrunsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_vision_runs_by_camera

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch runs by camera. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.industrial.get_vision_runs_by_camera(camera_id=672862, duration_ms=973746)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `camera_id`                                                                                                                         | *int*                                                                                                                               | :heavy_check_mark:                                                                                                                  | The camera_id should be valid for the given accessToken.                                                                            |
| `duration_ms`                                                                                                                       | *int*                                                                                                                               | :heavy_check_mark:                                                                                                                  | DurationMs is a required param. This works with the EndMs parameter. Indicates the duration in which the visionRuns will be fetched |
| `end_ms`                                                                                                                            | *Optional[int]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | EndMs is an optional param. It will default to the current time.                                                                    |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |

### Response

**[models.GetVisionRunsByCameraResponse](../../models/getvisionrunsbycameraresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## v1get_vision_runs_by_camera_and_program

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch runs by camera and program. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.industrial.v1get_vision_runs_by_camera_and_program(camera_id=223195, program_id=90522, started_at_ms=19084)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `camera_id`                                                                           | *int*                                                                                 | :heavy_check_mark:                                                                    | The camera_id should be valid for the given accessToken.                              |
| `program_id`                                                                          | *int*                                                                                 | :heavy_check_mark:                                                                    | The configured program's ID on the camera.                                            |
| `started_at_ms`                                                                       | *int*                                                                                 | :heavy_check_mark:                                                                    | Started_at_ms is a required param. Indicates the start time of the run to be fetched. |
| `include`                                                                             | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Include is a filter parameter. Accepts 'pass', 'reject' or 'no_read'.                 |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.V1getVisionRunsByCameraAndProgramResponse](../../models/v1getvisionrunsbycameraandprogramresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## v1get_machines_history

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get historical data for machine objects. This method returns a set of historical data for all machines. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.industrial.v1get_machines_history(end_ms=1462881998034, start_ms=1462878398034)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `end_ms`                                                            | *int*                                                               | :heavy_check_mark:                                                  | End of the time range, specified in milliseconds UNIX time.         | 1462881998034                                                       |
| `start_ms`                                                          | *int*                                                               | :heavy_check_mark:                                                  | Beginning of the time range, specified in milliseconds UNIX time.   | 1462878398034                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.V1getMachinesHistoryResponse](../../models/v1getmachineshistoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## v1get_machines

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get machine objects. This method returns a list of the machine objects in the Samsara Cloud and information about them. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.industrial.v1get_machines()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.V1getMachinesResponse](../../models/v1getmachinesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |