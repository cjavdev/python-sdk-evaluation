# Addresses
(*addresses*)

## Overview

### Available Operations

* [list_addresses](#list_addresses) - List all addresses
* [create_address](#create_address) - Create an address
* [delete_address](#delete_address) - Delete an address
* [get_address](#get_address) - Retrieve an address
* [update_address](#update_address) - Update an address

## list_addresses

Returns a list of all addresses in an organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Addresses** under the Addresses category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.addresses.list_addresses()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                | The limit for how many objects will be in the response. Default and max for this value is 512 objects.                                                                                                                                            |
| `after`                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.                                    |
| `parent_tag_ids`                                                                                                                                                                                                                                  | List[*str*]                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`           |
| `tag_ids`                                                                                                                                                                                                                                         | List[*str*]                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`                                                                                                                                                   |
| `created_after_time`                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                | A filter on data to have a created at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). |
| `retries`                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                               |

### Response

**[models.ListAddressesResponse1](../../models/listaddressesresponse1.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_address

Creates a new address in the organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Addresses** under the Addresses category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
import samsara
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.addresses.create_address(formatted_address="350 Rhode Island St, San Francisco, CA", geofence={
        "circle": {
            "radius_meters": 25,
            "latitude": 37.765363,
            "longitude": -122.4029238,
        },
        "polygon": {
            "vertices": [
                {
                    "latitude": 37.765363,
                    "longitude": -122.403098,
                },
                {
                    "latitude": 38.765363,
                    "longitude": -122.403098,
                },
                {
                    "latitude": 37.765363,
                    "longitude": -123.403098,
                },
            ],
        },
        "settings": {
            "show_addresses": True,
        },
    }, name="Samsara HQ", address_types=[
        samsara.CreateAddressRequestAddressTypes.YARD,
    ], contact_ids=[
        "22408",
    ], external_ids={
        "maintenanceId": "250020",
        "payrollId": "ABFS18600",
    }, latitude=37.765363, longitude=-122.4029238, notes="Hours of operation: 8am - 6pm; Truck entrance on the Rhode Island street side.", tag_ids=[
        "3914",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                              | Type                                                                                                                                                                                   | Required                                                                                                                                                                               | Description                                                                                                                                                                            | Example                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `formatted_address`                                                                                                                                                                    | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | The full street address for this address/geofence, as it might be recognized by Google Maps.                                                                                           | 350 Rhode Island St, San Francisco, CA                                                                                                                                                 |
| `geofence`                                                                                                                                                                             | [models.CreateAddressRequestGeofence](../../models/createaddressrequestgeofence.md)                                                                                                    | :heavy_check_mark:                                                                                                                                                                     | The geofence that defines this address and its bounds. This can either be a circle or a polygon, but not both.                                                                         |                                                                                                                                                                                        |
| `name`                                                                                                                                                                                 | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | Name of the address.                                                                                                                                                                   | Samsara HQ                                                                                                                                                                             |
| `address_types`                                                                                                                                                                        | List[[models.CreateAddressRequestAddressTypes](../../models/createaddressrequestaddresstypes.md)]                                                                                      | :heavy_minus_sign:                                                                                                                                                                     | Reporting location type associated with the address (used for ELD reporting purposes). Valid values: `yard`, `shortHaul`, `workforceSite`, `riskZone`, `industrialSite`, `alertsOnly`. |                                                                                                                                                                                        |
| `contact_ids`                                                                                                                                                                          | List[*str*]                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                     | An array of Contact IDs associated with this Address.                                                                                                                                  |                                                                                                                                                                                        |
| `external_ids`                                                                                                                                                                         | Dict[str, *str*]                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                     | The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.                                                                                             | {<br/>"maintenanceId": "250020",<br/>"payrollId": "ABFS18600"<br/>}                                                                                                                    |
| `latitude`                                                                                                                                                                             | *Optional[float]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                     | Latitude of the address. Will be geocoded from `formattedAddress` if not provided.                                                                                                     | 37.765363                                                                                                                                                                              |
| `longitude`                                                                                                                                                                            | *Optional[float]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                     | Longitude of the address. Will be geocoded from `formattedAddress` if not provided.                                                                                                    | -122.4029238                                                                                                                                                                           |
| `notes`                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                     | Notes about the address.                                                                                                                                                               | Hours of operation: 8am - 6pm; Truck entrance on the Rhode Island street side.                                                                                                         |
| `tag_ids`                                                                                                                                                                              | List[*str*]                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                     | An array of IDs of tags to associate with this address.                                                                                                                                |                                                                                                                                                                                        |
| `retries`                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                    |                                                                                                                                                                                        |

### Response

**[models.CreateAddressResponse](../../models/createaddressresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_address

Delete a specific address. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Addresses** under the Addresses category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.addresses.delete_address(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                     | ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123` |
| `retries`                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                    |

### Response

**[models.DeleteAddressResponse](../../models/deleteaddressresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_address

Returns a specific address. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Addresses** under the Addresses category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.addresses.get_address(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                     | ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123` |
| `retries`                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                    |

### Response

**[models.GetAddressResponse](../../models/getaddressresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_address

Update a specific address. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Addresses** under the Addresses category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
import samsara
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.addresses.update_address(id="<id>", address_types=[
        samsara.UpdateAddressRequestAddressTypes.YARD,
    ], contact_ids=[
        "22408",
    ], external_ids={
        "maintenanceId": "250020",
        "payrollId": "ABFS18600",
    }, formatted_address="350 Rhode Island St, San Francisco, CA", geofence={
        "circle": {
            "radius_meters": 25,
            "latitude": 37.765363,
            "longitude": -122.4029238,
        },
        "polygon": {
            "vertices": [
                {
                    "latitude": 37.765363,
                    "longitude": -122.403098,
                },
                {
                    "latitude": 38.765363,
                    "longitude": -122.403098,
                },
                {
                    "latitude": 37.765363,
                    "longitude": -123.403098,
                },
            ],
        },
        "settings": {
            "show_addresses": False,
        },
    }, latitude=37.765363, longitude=-122.4029238, name="Samsara HQ", notes="Hours of operation: 8am - 6pm; Truck entrance on the Rhode Island street side.", tag_ids=[
        "3914",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                     | ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123` |                                                                                                                                                                                                                                                                                                                        |
| `address_types`                                                                                                                                                                                                                                                                                                        | List[[models.UpdateAddressRequestAddressTypes](../../models/updateaddressrequestaddresstypes.md)]                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                     | Reporting location type associated with the address (used for ELD reporting purposes). Valid values: `yard`, `shortHaul`, `workforceSite`, `riskZone`, `industrialSite`, `alertsOnly`.                                                                                                                                 |                                                                                                                                                                                                                                                                                                                        |
| `contact_ids`                                                                                                                                                                                                                                                                                                          | List[*str*]                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                     | An array of Contact IDs associated with this Address.                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                        |
| `external_ids`                                                                                                                                                                                                                                                                                                         | Dict[str, *str*]                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                     | The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.                                                                                                                                                                                                                             | {<br/>"maintenanceId": "250020",<br/>"payrollId": "ABFS18600"<br/>}                                                                                                                                                                                                                                                    |
| `formatted_address`                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                     | The full street address for this address/geofence, as it might be recognized by Google Maps.                                                                                                                                                                                                                           | 350 Rhode Island St, San Francisco, CA                                                                                                                                                                                                                                                                                 |
| `geofence`                                                                                                                                                                                                                                                                                                             | [Optional[models.UpdateAddressRequestGeofence]](../../models/updateaddressrequestgeofence.md)                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                     | The geofence that defines this address and its bounds. This can either be a circle or a polygon, but not both.                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                        |
| `latitude`                                                                                                                                                                                                                                                                                                             | *Optional[float]*                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                     | Latitude of the address. Will be geocoded from `formattedAddress` if not provided.                                                                                                                                                                                                                                     | 37.765363                                                                                                                                                                                                                                                                                                              |
| `longitude`                                                                                                                                                                                                                                                                                                            | *Optional[float]*                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                     | Longitude of the address. Will be geocoded from `formattedAddress` if not provided.                                                                                                                                                                                                                                    | -122.4029238                                                                                                                                                                                                                                                                                                           |
| `name`                                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                     | Name of the address.                                                                                                                                                                                                                                                                                                   | Samsara HQ                                                                                                                                                                                                                                                                                                             |
| `notes`                                                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                     | Notes about the address.                                                                                                                                                                                                                                                                                               | Hours of operation: 8am - 6pm; Truck entrance on the Rhode Island street side.                                                                                                                                                                                                                                         |
| `tag_ids`                                                                                                                                                                                                                                                                                                              | List[*str*]                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                     | An array of IDs of tags to associate with this address.                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                        |
| `retries`                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.UpdateAddressResponse](../../models/updateaddressresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |