# CreateUserRequestRoles

A role that applies to a user. If the role has a `tagId`, then the role applies for that tag. If there is no `tagId`, then the role applies at the organizational level. A user may have many tag-specific roles, but may only have one organizational role. If the organizational level role has higher privileges than a tag-specific role, then the organizational role privileges will take precedence.


## Fields

| Field                                | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `role_id`                            | *str*                                | :heavy_check_mark:                   | The unique ID for the role.          | 8a9371af-82d1-4158-bf91-4ecc8d3a114c |
| `tag_id`                             | *Optional[str]*                      | :heavy_minus_sign:                   | ID of the tag this role applies to.  | 3914                                 |