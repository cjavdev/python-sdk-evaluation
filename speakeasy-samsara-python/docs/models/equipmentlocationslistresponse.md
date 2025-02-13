# EquipmentLocationsListResponse

A time-series of equipment locations and pagination information


## Fields

| Field                                                                                              | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `data`                                                                                             | List[[models.EquipmentLocationsListResponseData](../models/equipmentlocationslistresponsedata.md)] | :heavy_check_mark:                                                                                 | Time-series of locations for the specified units of equipment.                                     |
| `pagination`                                                                                       | [models.PaginationResponse](../models/paginationresponse.md)                                       | :heavy_check_mark:                                                                                 | Pagination parameters.                                                                             |