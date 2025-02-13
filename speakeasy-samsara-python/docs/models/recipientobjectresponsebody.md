# RecipientObjectResponseBody

Recipient of an Action. One of userId contactId or roleId needs to be set.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      | Example                                                          |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `type`                                                           | [models.Type](../models/type.md)                                 | :heavy_check_mark:                                               | The type of recipients  Valid values: `user`, `contact`, `role`  | user                                                             |
| `contact_id`                                                     | *Optional[str]*                                                  | :heavy_minus_sign:                                               | The ID of the contact.                                           | 1234                                                             |
| `notification_types`                                             | List[[models.NotificationTypes](../models/notificationtypes.md)] | :heavy_minus_sign:                                               | How the user/contact/role should be notified.                    | [<br/>"push",<br/>"sms"<br/>]                                    |
| `role_id`                                                        | *Optional[str]*                                                  | :heavy_minus_sign:                                               | The ID of the role.                                              | 67004a16-be3c-4ef6-a51b-1c45a2c27a92                             |
| `user_id`                                                        | *Optional[str]*                                                  | :heavy_minus_sign:                                               | The ID of the user.                                              | 1234                                                             |