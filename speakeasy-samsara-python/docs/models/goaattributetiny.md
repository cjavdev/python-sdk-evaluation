# GoaAttributeTiny

Attribute properties.


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `id`                                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | Id of the attribute                                  | 494123                                               |
| `name`                                               | *Optional[str]*                                      | :heavy_minus_sign:                                   | Name of the attribute                                | Compliance/ELD                                       |
| `number_values`                                      | List[*float*]                                        | :heavy_minus_sign:                                   | List of number values associated with the attribute  | [<br/>867,<br/>5309<br/>]                            |
| `string_values`                                      | List[*str*]                                          | :heavy_minus_sign:                                   | List of string values associated with the attribute. | [<br/>"HQ",<br/>"Leased"<br/>]                       |