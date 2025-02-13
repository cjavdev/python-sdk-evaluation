# VehicleLocationsResponse

Most recent vehicle locations and pagination info.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `data`                                                                                 | List[[models.VehicleLocationsResponseData](../models/vehiclelocationsresponsedata.md)] | :heavy_check_mark:                                                                     | List of the most recent locations for the specified vehicles.                          |
| `pagination`                                                                           | [models.PaginationResponse](../models/paginationresponse.md)                           | :heavy_check_mark:                                                                     | Pagination parameters.                                                                 |