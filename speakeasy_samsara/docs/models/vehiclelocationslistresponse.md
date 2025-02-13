# VehicleLocationsListResponse

List of vehicle location events and pagination info.


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `data`                                                                                         | List[[models.VehicleLocationsListResponseData](../models/vehiclelocationslistresponsedata.md)] | :heavy_check_mark:                                                                             | A list of vehicles and an array of location events for each vehicle.                           |
| `pagination`                                                                                   | [models.PaginationResponse](../models/paginationresponse.md)                                   | :heavy_check_mark:                                                                             | Pagination parameters.                                                                         |