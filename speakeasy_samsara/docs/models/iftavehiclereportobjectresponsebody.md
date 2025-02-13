# IftaVehicleReportObjectResponseBody

A summary of this vehicle's IFTA data.


## Fields

| Field                                                                                                            | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `jurisdictions`                                                                                                  | List[[models.IftaJurisdictionSummaryObjectResponseBody](../models/iftajurisdictionsummaryobjectresponsebody.md)] | :heavy_check_mark:                                                                                               | List of jurisdiction summaries.                                                                                  |
| `vehicle`                                                                                                        | [models.GoaVehicleTinyResponseResponseBody](../models/goavehicletinyresponseresponsebody.md)                     | :heavy_check_mark:                                                                                               | A minified vehicle object. This object is only returned if the route is assigned to the vehicle.                 |