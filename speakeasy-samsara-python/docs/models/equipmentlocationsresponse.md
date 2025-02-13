# EquipmentLocationsResponse

The most recent equipment locations and pagination information


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `data`                                                                                     | List[[models.EquipmentLocationsResponseData](../models/equipmentlocationsresponsedata.md)] | :heavy_check_mark:                                                                         | List of the most recent locations for the specified units of equipment.                    |
| `pagination`                                                                               | [models.PaginationResponse](../models/paginationresponse.md)                               | :heavy_check_mark:                                                                         | Pagination parameters.                                                                     |