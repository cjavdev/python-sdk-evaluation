# V1Asset

Basic information of an asset


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `id`                                                       | *int*                                                      | :heavy_check_mark:                                         | Asset ID                                                   | 1                                                          |
| `asset_serial_number`                                      | *Optional[str]*                                            | :heavy_minus_sign:                                         | Serial number of the host asset                            | SNTEST123                                                  |
| `cable`                                                    | [Optional[models.V1AssetCable]](../models/v1assetcable.md) | :heavy_minus_sign:                                         | The cable connected to the asset                           |                                                            |
| `engine_hours`                                             | *Optional[int]*                                            | :heavy_minus_sign:                                         | Engine hours                                               | 104                                                        |
| `name`                                                     | *Optional[str]*                                            | :heavy_minus_sign:                                         | Asset name                                                 | Trailer 123                                                |
| `vehicle_id`                                               | *Optional[int]*                                            | :heavy_minus_sign:                                         | The ID of the Vehicle associated to the Asset (if present) | 2                                                          |