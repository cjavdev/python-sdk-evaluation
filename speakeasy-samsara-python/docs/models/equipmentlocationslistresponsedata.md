# EquipmentLocationsListResponseData

A unit of equipment and its time-series of location events.


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       | Example                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `id`                                                              | *str*                                                             | :heavy_check_mark:                                                | Unique Samsara ID for the equipment.                              | 112                                                               |
| `locations`                                                       | List[[models.EquipmentLocation](../models/equipmentlocation.md)]  | :heavy_check_mark:                                                | A time-series of location events for the given unit of equipment. |                                                                   |
| `name`                                                            | *str*                                                             | :heavy_check_mark:                                                | Name of the equipment.                                            | Crane A7                                                          |