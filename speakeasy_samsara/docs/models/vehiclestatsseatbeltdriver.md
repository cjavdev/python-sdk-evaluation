# VehicleStatsSeatbeltDriver

Seatbelt Driver Status as read from the vehicle. `Buckled` or `Unbuckled`.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            | Example                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `time`                                                                                 | *str*                                                                                  | :heavy_check_mark:                                                                     | UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.                     | 2020-01-27T07:06:25Z                                                                   |
| `value`                                                                                | [models.VehicleStatsSeatbeltDriverValue](../models/vehiclestatsseatbeltdrivervalue.md) | :heavy_check_mark:                                                                     | Seatbelt Driver Status as read from the vehicle. `Buckled` or `Unbuckled`.             | Buckled                                                                                |