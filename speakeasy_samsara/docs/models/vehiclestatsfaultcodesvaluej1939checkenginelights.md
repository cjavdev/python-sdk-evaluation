# VehicleStatsFaultCodesValueJ1939CheckEngineLights

Status of engine lights on J1939 vehicles.


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `emissions_is_on`                                  | *bool*                                             | :heavy_check_mark:                                 | True if the MIL status is nonzero.                 | true                                               |
| `protect_is_on`                                    | *bool*                                             | :heavy_check_mark:                                 | True if the engine protect lamp status is nonzero. | false                                              |
| `stop_is_on`                                       | *bool*                                             | :heavy_check_mark:                                 | True if the red lamp status is nonzero.            | false                                              |
| `warning_is_on`                                    | *bool*                                             | :heavy_check_mark:                                 | True if the amber lamp status is nonzero.          | false                                              |