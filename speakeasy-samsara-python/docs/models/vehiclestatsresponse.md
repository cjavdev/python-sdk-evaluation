# VehicleStatsResponse

Vehicle stats snapshot and pagination info.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `data`                                                                         | List[[models.VehicleStatsResponseData](../models/vehiclestatsresponsedata.md)] | :heavy_check_mark:                                                             | List of vehicles and a snapshot of the request stats.                          |
| `pagination`                                                                   | [models.PaginationResponse](../models/paginationresponse.md)                   | :heavy_check_mark:                                                             | Pagination parameters.                                                         |