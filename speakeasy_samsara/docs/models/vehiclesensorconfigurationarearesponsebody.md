# VehicleSensorConfigurationAreaResponseBody

A configured sensor area on the vehicle with its associated sensors


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              | Example                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `position`                                                               | [models.Position](../models/position.md)                                 | :heavy_check_mark:                                                       | Position of the area on vehicle  Valid values: `back`, `front`, `middle` | back                                                                     |
| `cargo_sensors`                                                          | List[[models.SensorResponseBody](../models/sensorresponsebody.md)]       | :heavy_minus_sign:                                                       | N/A                                                                      |                                                                          |
| `humidity_sensors`                                                       | List[[models.SensorResponseBody](../models/sensorresponsebody.md)]       | :heavy_minus_sign:                                                       | N/A                                                                      |                                                                          |
| `temperature_sensors`                                                    | List[[models.SensorResponseBody](../models/sensorresponsebody.md)]       | :heavy_minus_sign:                                                       | N/A                                                                      |                                                                          |