# VehicleStatsEcuSpeedMph

The speed of the vehicle in miles per hour, as reported by the ECU.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `time`                                                             | *str*                                                              | :heavy_check_mark:                                                 | UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`. | 2020-01-27T07:06:25Z                                               |
| `value`                                                            | *float*                                                            | :heavy_check_mark:                                                 | The speed of the vehicle in miles per hour.                        | 32.1                                                               |