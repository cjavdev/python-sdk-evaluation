# Assets
(*assets*)

## Overview

### Available Operations

* [v1get_all_assets](#v1get_all_assets) - List all assets
* [v1get_all_asset_current_locations](#v1get_all_asset_current_locations) - List current location for all assets
* [v1get_assets_reefers](#v1get_assets_reefers) - List stats for all reefers
* [v1get_asset_location](#v1get_asset_location) - List historical locations for a given asset
* [v1get_asset_reefer](#v1get_asset_reefer) - List stats for a given reefer

## v1get_all_assets

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch all of the assets. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.assets.v1get_all_assets()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.V1getAllAssetsResponse](../../models/v1getallassetsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## v1get_all_asset_current_locations

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch current locations of all assets. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.assets.v1get_all_asset_current_locations()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                  | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `starting_after`                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'endingBefore' parameter. |
| `ending_before`                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | Pagination parameter indicating the cursor position to return results before. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'startingAfter' parameter.           |
| `limit`                                                                                                                                                                                    | *Optional[float]*                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                         | Pagination parameter indicating the number of results to return in this request. Used in conjunction with either 'startingAfter' or 'endingBefore'.                                        |
| `retries`                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                        |

### Response

**[models.V1getAllAssetCurrentLocationsResponse](../../models/v1getallassetcurrentlocationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## v1get_assets_reefers

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetches all reefers and reefer-specific stats. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Trailers** under the Trailers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.assets.v1get_assets_reefers(start_ms=709669, end_ms=741931)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                  | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `start_ms`                                                                                                                                                                                 | *int*                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                         | Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs.                                                                        |
| `end_ms`                                                                                                                                                                                   | *int*                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                         | Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs.                                                                        |
| `starting_after`                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'endingBefore' parameter. |
| `ending_before`                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | Pagination parameter indicating the cursor position to return results before. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'startingAfter' parameter.           |
| `limit`                                                                                                                                                                                    | *Optional[float]*                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                         | Pagination parameter indicating the number of results to return in this request. Used in conjunction with either 'startingAfter' or 'endingBefore'.                                        |
| `retries`                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                        |

### Response

**[models.V1getAssetsReefersResponse](../../models/v1getassetsreefersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## v1get_asset_location

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

List historical locations for a given asset. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.assets.v1get_asset_location(asset_id=93242, start_ms=837411, end_ms=560723)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `asset_id`                                                                                                          | *int*                                                                                                               | :heavy_check_mark:                                                                                                  | ID of the asset. Must contain only digits 0-9.                                                                      |
| `start_ms`                                                                                                          | *int*                                                                                                               | :heavy_check_mark:                                                                                                  | Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. |
| `end_ms`                                                                                                            | *int*                                                                                                               | :heavy_check_mark:                                                                                                  | Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.V1getAssetLocationResponse](../../models/v1getassetlocationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## v1get_asset_reefer

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch the reefer-specific stats of an asset. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Trailers** under the Trailers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.assets.v1get_asset_reefer(asset_id=490744, start_ms=880776, end_ms=339328)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `asset_id`                                                                                                          | *int*                                                                                                               | :heavy_check_mark:                                                                                                  | ID of the asset. Must contain only digits 0-9.                                                                      |
| `start_ms`                                                                                                          | *int*                                                                                                               | :heavy_check_mark:                                                                                                  | Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. |
| `end_ms`                                                                                                            | *int*                                                                                                               | :heavy_check_mark:                                                                                                  | Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.V1getAssetReeferResponse](../../models/v1getassetreeferresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |