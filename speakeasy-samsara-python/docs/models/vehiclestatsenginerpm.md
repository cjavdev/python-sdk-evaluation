# VehicleStatsEngineRpm

Vehicle engine RPM reading.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `time`                                                             | *str*                                                              | :heavy_check_mark:                                                 | UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`. | 2020-01-27T07:06:25Z                                               |
| `value`                                                            | *int*                                                              | :heavy_check_mark:                                                 | The revolutions per minute of the engine.                          | 1000                                                               |