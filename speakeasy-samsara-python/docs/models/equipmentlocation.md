# EquipmentLocation

Location reading.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `latitude`                                                         | *float*                                                            | :heavy_check_mark:                                                 | GPS latitude represented in degrees                                | 122.142                                                            |
| `longitude`                                                        | *float*                                                            | :heavy_check_mark:                                                 | GPS longitude represented in degrees                               | -93.343                                                            |
| `time`                                                             | *str*                                                              | :heavy_check_mark:                                                 | UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`. | 2020-01-27T07:06:25Z                                               |
| `heading`                                                          | *Optional[float]*                                                  | :heavy_minus_sign:                                                 | Heading of the unit of equipment in degrees.                       | 120                                                                |
| `speed`                                                            | *Optional[float]*                                                  | :heavy_minus_sign:                                                 | GPS speed of the unit of equipment in miles per hour.              | 48.3                                                               |