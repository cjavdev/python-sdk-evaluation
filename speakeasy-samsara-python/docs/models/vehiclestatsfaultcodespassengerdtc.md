# VehicleStatsFaultCodesPassengerDtc

Passenger vehicle DTC information


## Fields

| Field                                      | Type                                       | Required                                   | Description                                | Example                                    |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `dtc_id`                                   | *int*                                      | :heavy_check_mark:                         | The DTC identifier.                        | 135                                        |
| `dtc_description`                          | *Optional[str]*                            | :heavy_minus_sign:                         | The DTC description, if available.         | Fuel Rail/System Pressure - Too Low Bank 1 |
| `dtc_short_code`                           | *Optional[str]*                            | :heavy_minus_sign:                         | The DTC short code, if available.          | P0087                                      |