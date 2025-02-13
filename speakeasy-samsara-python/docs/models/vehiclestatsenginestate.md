# VehicleStatsEngineState

Vehicle engine state event.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          | Example                                                                              |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `time`                                                                               | *str*                                                                                | :heavy_check_mark:                                                                   | UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.                   | 2020-01-27T07:06:25Z                                                                 |
| `value`                                                                              | [models.VehicleStatsEngineStateSetting](../models/vehiclestatsenginestatesetting.md) | :heavy_check_mark:                                                                   | The state of the engine.                                                             | On                                                                                   |