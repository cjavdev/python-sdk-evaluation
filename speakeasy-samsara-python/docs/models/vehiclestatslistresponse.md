# VehicleStatsListResponse

List of vehicle stat events and pagination info.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `data`                                                                                 | List[[models.VehicleStatsListResponseData](../models/vehiclestatslistresponsedata.md)] | :heavy_check_mark:                                                                     | A list of vehicles and an array of stat events for each vehicle.                       |
| `pagination`                                                                           | [models.PaginationResponse](../models/paginationresponse.md)                           | :heavy_check_mark:                                                                     | Pagination parameters.                                                                 |