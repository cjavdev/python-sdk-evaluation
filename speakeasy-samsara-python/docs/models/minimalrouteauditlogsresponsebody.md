# MinimalRouteAuditLogsResponseBody

A single route. Only the fields that have changed are present in the response. All other fields, including the route id, will not be present in the response. For now, only routeStops are included since only Route Tracking updates are supported.


## Fields

| Field                                                                                                    | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `stops`                                                                                                  | List[[models.MinimalRouteStopAuditLogsResponseBody](../models/minimalroutestopauditlogsresponsebody.md)] | :heavy_minus_sign:                                                                                       | The route stops in the route. Only stops that have been updated will be included in the response.        |