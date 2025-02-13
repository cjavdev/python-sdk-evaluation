# VehicleStatsFuelPercent

Vehicle fuel percentage reading.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `time`                                                             | *str*                                                              | :heavy_check_mark:                                                 | UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`. | 2020-01-27T07:06:25Z                                               |
| `value`                                                            | *int*                                                              | :heavy_check_mark:                                                 | The engine fuel level in percentage points (e.g. `99`, `50`, etc). | 54                                                                 |