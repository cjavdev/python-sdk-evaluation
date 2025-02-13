# VehicleStatsSpreaderActive

Whether vehicle is actively spreading any material.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            | Example                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `time`                                                                                 | *str*                                                                                  | :heavy_check_mark:                                                                     | UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.                     | 2020-01-27T07:06:25Z                                                                   |
| `value`                                                                                | [models.VehicleStatsSpreaderActiveValue](../models/vehiclestatsspreaderactivevalue.md) | :heavy_check_mark:                                                                     | Whether vehicle is actively spreading any material.                                    | On                                                                                     |