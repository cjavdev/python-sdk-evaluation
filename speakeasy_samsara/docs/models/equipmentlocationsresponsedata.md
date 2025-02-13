# EquipmentLocationsResponseData

A unit of equipment and its most recent location.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `id`                                                       | *str*                                                      | :heavy_check_mark:                                         | Unique Samsara ID for the equipment.                       | 112                                                        |
| `location`                                                 | [models.EquipmentLocation](../models/equipmentlocation.md) | :heavy_check_mark:                                         | Location reading.                                          |                                                            |
| `name`                                                     | *str*                                                      | :heavy_check_mark:                                         | Name of the equipment.                                     | Crane A7                                                   |