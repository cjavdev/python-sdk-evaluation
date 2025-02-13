# VehicleStatsFaultCodesJ1939

Vehicle fault codes for J1939 vehicles.


## Fields

| Field                                                                                                      | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `check_engine_lights`                                                                                      | [Optional[models.VehicleStatsFaultCodesJ1939Lights]](../models/vehiclestatsfaultcodesj1939lights.md)       | :heavy_minus_sign:                                                                                         | Status of engine lights on J1939 vehicles.                                                                 |
| `diagnostic_trouble_codes`                                                                                 | List[[models.VehicleStatsFaultCodesJ1939TroubleCode](../models/vehiclestatsfaultcodesj1939troublecode.md)] | :heavy_minus_sign:                                                                                         | Diagnostic trouble codes for J1939 vehicles.                                                               |