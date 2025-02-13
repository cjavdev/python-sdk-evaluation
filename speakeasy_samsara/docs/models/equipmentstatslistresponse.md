# EquipmentStatsListResponse

A time-series of equipment stats and pagination information


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `data`                                                                                     | List[[models.EquipmentStatsListResponseData](../models/equipmentstatslistresponsedata.md)] | :heavy_check_mark:                                                                         | Time-series of stats for the specified units of equipment and stat types.                  |
| `pagination`                                                                               | [models.PaginationResponse](../models/paginationresponse.md)                               | :heavy_check_mark:                                                                         | Pagination parameters.                                                                     |