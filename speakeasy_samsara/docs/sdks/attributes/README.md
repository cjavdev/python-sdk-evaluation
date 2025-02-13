# Attributes
(*attributes*)

## Overview

### Available Operations

* [get_attributes_by_entity_type](#get_attributes_by_entity_type) - List all attributes by entity type
* [create_attribute](#create_attribute) - Create an attribute
* [delete_attribute](#delete_attribute) - Deleting an attribute
* [get_attribute](#get_attribute) - Retrieve an attribute
* [update_attribute](#update_attribute) - Update an attribute

## get_attributes_by_entity_type

Fetch all attributes in an organization associated with either drivers or assets. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Attributes** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
import samsara
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.attributes.get_attributes_by_entity_type(entity_type=samsara.QueryParamEntityType.ASSET)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                      | Type                                                                                                                                                                                                           | Required                                                                                                                                                                                                       | Description                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `entity_type`                                                                                                                                                                                                  | [models.QueryParamEntityType](../../models/queryparamentitytype.md)                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                             | Denotes the type of entity, driver or asset.                                                                                                                                                                   |
| `limit`                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                             | The limit for how many objects will be in the response. Default and max for this value is 512 objects.                                                                                                         |
| `after`                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                             | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. |
| `retries`                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                            |

### Response

**[models.GetAttributesByEntityTypeResponse1](../../models/getattributesbyentitytyperesponse1.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_attribute

Creates a new attribute in the organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Attributes** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
import samsara
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.attributes.create_attribute(entity_type=samsara.CreateAttributeRequestEntityType.ASSET, name="License Certifications", entities=[
        {
            "external_ids": {
                "maintenanceId": "250020",
                "payrollId": "ABFS18600",
            },
        },
        {
            "external_ids": {
                "maintenanceId": "250020",
                "payrollId": "ABFS18600",
            },
        },
        {
            "external_ids": {
                "maintenanceId": "250020",
                "payrollId": "ABFS18600",
            },
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               | Example                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `entity_type`                                                                                                                             | [models.CreateAttributeRequestEntityType](../../models/createattributerequestentitytype.md)                                               | :heavy_check_mark:                                                                                                                        | Denotes the type of entity, driver or asset.                                                                                              | asset                                                                                                                                     |
| `name`                                                                                                                                    | *str*                                                                                                                                     | :heavy_check_mark:                                                                                                                        | Name                                                                                                                                      | License Certifications                                                                                                                    |
| `attribute_type`                                                                                                                          | [Optional[models.CreateAttributeRequestAttributeType]](../../models/createattributerequestattributetype.md)                               | :heavy_minus_sign:                                                                                                                        | Denotes the data type of the attribute's values. Valid values: `string`, `number`.                                                        | string                                                                                                                                    |
| `attribute_value_quantity`                                                                                                                | [Optional[models.CreateAttributeRequestAttributeValueQuantity]](../../models/createattributerequestattributevaluequantity.md)             | :heavy_minus_sign:                                                                                                                        | Defines whether or not this attribute can be used on the same entity many times (with different values). Valid values: `single`, `multi`. | multi                                                                                                                                     |
| `entities`                                                                                                                                | List[[models.CreateAttributeRequestEntities](../../models/createattributerequestentities.md)]                                             | :heavy_minus_sign:                                                                                                                        | Entities that will be applied to this attribute                                                                                           |                                                                                                                                           |
| `number_values`                                                                                                                           | List[*float*]                                                                                                                             | :heavy_minus_sign:                                                                                                                        | Number values that can be associated with this attribute                                                                                  |                                                                                                                                           |
| `string_values`                                                                                                                           | List[*str*]                                                                                                                               | :heavy_minus_sign:                                                                                                                        | String values that can be associated with this attribute                                                                                  |                                                                                                                                           |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |

### Response

**[models.CreateAttributeResponse](../../models/createattributeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_attribute

Delete an attribute by id, including all of its applications. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Attributes** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
import samsara
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.attributes.delete_attribute(id="<id>", entity_type=samsara.DeleteAttributeQueryParamEntityType.DRIVER)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `id`                                                                                              | *str*                                                                                             | :heavy_check_mark:                                                                                | Samsara-provided UUID of the attribute.                                                           |
| `entity_type`                                                                                     | [models.DeleteAttributeQueryParamEntityType](../../models/deleteattributequeryparamentitytype.md) | :heavy_check_mark:                                                                                | Denotes the type of entity, driver or asset.                                                      |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.DeleteAttributeResponse](../../models/deleteattributeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_attribute

Fetch an attribute by id, including all of its applications. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Attributes** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
import samsara
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.attributes.get_attribute(id="<id>", entity_type=samsara.GetAttributeQueryParamEntityType.DRIVER)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `id`                                                                                        | *str*                                                                                       | :heavy_check_mark:                                                                          | Samsara-provided UUID of the attribute.                                                     |
| `entity_type`                                                                               | [models.GetAttributeQueryParamEntityType](../../models/getattributequeryparamentitytype.md) | :heavy_check_mark:                                                                          | Denotes the type of entity, driver or asset.                                                |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.GetAttributeResponse](../../models/getattributeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_attribute

Updates an attribute in the organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Attributes** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
import samsara
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.attributes.update_attribute(id="<id>", entity_type=samsara.UpdateAttributeRequestEntityType.ASSET, entities=[
        {
            "external_ids": {
                "maintenanceId": "250020",
                "payrollId": "ABFS18600",
            },
        },
        {
            "external_ids": {
                "maintenanceId": "250020",
                "payrollId": "ABFS18600",
            },
        },
    ], name="License Certifications")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                              | Type                                                                                                                                                                                   | Required                                                                                                                                                                               | Description                                                                                                                                                                            | Example                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                   | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | Samsara-provided UUID of the attribute.                                                                                                                                                |                                                                                                                                                                                        |
| `entity_type`                                                                                                                                                                          | [models.UpdateAttributeRequestEntityType](../../models/updateattributerequestentitytype.md)                                                                                            | :heavy_check_mark:                                                                                                                                                                     | Denotes the type of entity, driver or asset.                                                                                                                                           | asset                                                                                                                                                                                  |
| `attribute_type`                                                                                                                                                                       | [Optional[models.UpdateAttributeRequestAttributeType]](../../models/updateattributerequestattributetype.md)                                                                            | :heavy_minus_sign:                                                                                                                                                                     | Denotes the data type of the attribute's values. Valid values: `string`, `number`.                                                                                                     | string                                                                                                                                                                                 |
| `attribute_value_quantity`                                                                                                                                                             | [Optional[models.UpdateAttributeRequestAttributeValueQuantity]](../../models/updateattributerequestattributevaluequantity.md)                                                          | :heavy_minus_sign:                                                                                                                                                                     | Defines whether or not this attribute can be used on the same entity many times (with different values). Denotes the type of entity, driver or asset. Valid values: `driver`, `asset`. | multi                                                                                                                                                                                  |
| `entities`                                                                                                                                                                             | List[[models.CreateAttributeRequestEntities](../../models/createattributerequestentities.md)]                                                                                          | :heavy_minus_sign:                                                                                                                                                                     | Entities that will be applied to this attribute                                                                                                                                        |                                                                                                                                                                                        |
| `name`                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                     | Name                                                                                                                                                                                   | License Certifications                                                                                                                                                                 |
| `number_values`                                                                                                                                                                        | List[*float*]                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                     | Number values that can be associated with this attribute                                                                                                                               |                                                                                                                                                                                        |
| `string_values`                                                                                                                                                                        | List[*str*]                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                     | String values that can be associated with this attribute                                                                                                                               |                                                                                                                                                                                        |
| `retries`                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                    |                                                                                                                                                                                        |

### Response

**[models.UpdateAttributeResponse](../../models/updateattributeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |