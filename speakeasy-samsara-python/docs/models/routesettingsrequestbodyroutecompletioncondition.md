# RouteSettingsRequestBodyRouteCompletionCondition

Defaults to 'arriveLastStop' which ends the route upon arriving at the final stop. The condition 'departLastStop' 
ends the route upon departing the last stop. If 'arriveLastStop' is set, then the departure time of the final stop should not be set.  Valid values: `arriveLastStop`, `departLastStop`


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `ARRIVE_LAST_STOP` | arriveLastStop     |
| `DEPART_LAST_STOP` | departLastStop     |