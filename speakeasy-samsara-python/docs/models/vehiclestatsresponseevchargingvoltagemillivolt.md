# VehicleStatsResponseEvChargingVoltageMilliVolt

Charging voltage for electric and hybrid vehicles in milli volts. Not all EV and HEVs may report this field.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `time`                                                             | *str*                                                              | :heavy_check_mark:                                                 | UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`. | 2020-01-27T07:06:25Z                                               |
| `value`                                                            | *int*                                                              | :heavy_check_mark:                                                 | Charging voltage for electric and hybrid vehicles in milli volts.  | 1000                                                               |