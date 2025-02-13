# RouteSettingsRequestBodyRouteStartingCondition

Defaults to 'departFirstStop' which starts the route upon departing the first stop in the route.
 The condition 'arriveFirstStop' starts the route upon arriving at the first stop in the route. If 'departFirstStop' is set,
the arrival time of the first stop should not be set.  Valid values: `departFirstStop`, `arriveFirstStop`


## Values

| Name                | Value               |
| ------------------- | ------------------- |
| `DEPART_FIRST_STOP` | departFirstStop     |
| `ARRIVE_FIRST_STOP` | arriveFirstStop     |