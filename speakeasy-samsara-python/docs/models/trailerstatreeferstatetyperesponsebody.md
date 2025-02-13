# TrailerStatReeferStateTypeResponseBody

Reefer state event.


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `time`                                                      | *str*                                                       | :heavy_check_mark:                                          | UTC timestamp in RFC 3339 format.                           | 2020-01-27T07:06:25Z                                        |
| `value`                                                     | *str*                                                       | :heavy_check_mark:                                          | The overall state of the multizone carrier reefer.          | `Off`, `On`                                                 |
| `substate_value`                                            | *Optional[str]*                                             | :heavy_minus_sign:                                          | The substate of the multizone carrier reefer, if available. | `Pretrip`, `Defrost`                                        |