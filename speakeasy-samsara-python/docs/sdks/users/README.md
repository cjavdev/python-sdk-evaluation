# Users
(*users*)

## Overview

### Available Operations

* [list_user_roles](#list_user_roles) - List all user roles
* [list_users](#list_users) - List all users
* [create_user](#create_user) - Create a user
* [delete_user](#delete_user) - Delete a user
* [get_user](#get_user) - Retrieve a user
* [update_user](#update_user) - Update a user

## list_user_roles

Returns a list of all user roles in an organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Users** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.users.list_user_roles()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                      | Type                                                                                                                                                                                                           | Required                                                                                                                                                                                                       | Description                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                             | The limit for how many objects will be in the response. Default and max for this value is 512 objects.                                                                                                         |
| `after`                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                             | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. |
| `retries`                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                            |

### Response

**[models.ListUserRolesResponse1](../../models/listuserrolesresponse1.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_users

Returns a list of all users in an organization. Users that have expired access will not be returned. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Users** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.users.list_users()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                      | Type                                                                                                                                                                                                           | Required                                                                                                                                                                                                       | Description                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                             | The limit for how many objects will be in the response. Default and max for this value is 512 objects.                                                                                                         |
| `after`                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                             | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. |
| `retries`                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                            |

### Response

**[models.ListUsersResponse1](../../models/listusersresponse1.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_user

Add a user to the organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Users** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
import samsara
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.users.create_user(auth_type=samsara.AuthType.SAML, email="user@company.com", name="Bob Smith", roles=[

    ], expire_at="2025-08-13T19:08:25Z")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                    | Type                                                                                                                                                                                                         | Required                                                                                                                                                                                                     | Description                                                                                                                                                                                                  | Example                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `auth_type`                                                                                                                                                                                                  | [models.AuthType](../../models/authtype.md)                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                           | The authentication type the user uses to authenticate. To use SAML this organization must have a configured SAML integration. Valid values: `default`, `saml`.                                               |                                                                                                                                                                                                              |
| `email`                                                                                                                                                                                                      | *str*                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                           | The email address of this user.                                                                                                                                                                              | user@company.com                                                                                                                                                                                             |
| `name`                                                                                                                                                                                                       | *str*                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                           | The first and last name of the user.                                                                                                                                                                         | Bob Smith                                                                                                                                                                                                    |
| `roles`                                                                                                                                                                                                      | List[[models.CreateUserRequestRoles](../../models/createuserrequestroles.md)]                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                           | The list of roles that applies to this user. A user may have "organizational" roles, which apply to the user at the organizational level, and "tag-specific" roles, which apply to the user for a given tag. |                                                                                                                                                                                                              |
| `expire_at`                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                           | For users with temporary access, this is the expiration datetime in RFC3339 format                                                                                                                           | 2025-08-13T19:08:25Z                                                                                                                                                                                         |
| `retries`                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                          |                                                                                                                                                                                                              |

### Response

**[models.CreateUserResponse](../../models/createuserresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_user

Delete the given user. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Users** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.users.delete_user(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier for the user.                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteUserResponse](../../models/deleteuserresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_user

Get a specific user's information. Users that have expired access will not be returned. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Users** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.users.get_user(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier for the user.                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetUserResponse](../../models/getuserresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_user

Update a specific user's information. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Users** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.users.update_user(id="<id>", expire_at="2025-08-13T19:08:25Z", name="Bob Smith", roles=[
        {
            "role_id": "8a9371af-82d1-4158-bf91-4ecc8d3a114c",
            "tag_id": "3914",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                    | Type                                                                                                                                                                                                         | Required                                                                                                                                                                                                     | Description                                                                                                                                                                                                  | Example                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                                                                                                         | *str*                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                           | Unique identifier for the user.                                                                                                                                                                              |                                                                                                                                                                                                              |
| `auth_type`                                                                                                                                                                                                  | [Optional[models.UpdateUserRequestAuthType]](../../models/updateuserrequestauthtype.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                           | The authentication type the user uses to authenticate. To use SAML this organization must have a configured SAML integration. Valid values: `default`, `saml`.                                               |                                                                                                                                                                                                              |
| `expire_at`                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                           | For users with temporary access, this is the expiration datetime in RFC3339 format                                                                                                                           | 2025-08-13T19:08:25Z                                                                                                                                                                                         |
| `name`                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                           | The first and last name of the user.                                                                                                                                                                         | Bob Smith                                                                                                                                                                                                    |
| `roles`                                                                                                                                                                                                      | List[[models.CreateUserRequestRoles](../../models/createuserrequestroles.md)]                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                           | The list of roles that applies to this user. A user may have "organizational" roles, which apply to the user at the organizational level, and "tag-specific" roles, which apply to the user for a given tag. |                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                          |                                                                                                                                                                                                              |

### Response

**[models.UpdateUserResponse](../../models/updateuserresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |