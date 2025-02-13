# EquipmentStatsResponse

The most recent equipment stats and pagination information


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `data`                                                                             | List[[models.EquipmentStatsResponseData](../models/equipmentstatsresponsedata.md)] | :heavy_check_mark:                                                                 | List of the most recent stats for the specified units of equipment and stat types. |
| `pagination`                                                                       | [models.PaginationResponse](../models/paginationresponse.md)                       | :heavy_check_mark:                                                                 | Pagination parameters.                                                             |