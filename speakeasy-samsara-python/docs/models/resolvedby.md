# ResolvedBy

Information about the user who is resolving a defect.


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       | Example                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `id`                                                              | *str*                                                             | :heavy_check_mark:                                                | The Id of user who is resolving the defect.                       | 11                                                                |
| `type`                                                            | [models.ResolvedByType](../models/resolvedbytype.md)              | :heavy_check_mark:                                                | The type of user who is resolving the defect. Must be "mechanic". | mechanic                                                          |