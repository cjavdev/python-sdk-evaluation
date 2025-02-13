# VehicleStatsObdEngineSeconds

Vehicle OBD engine seconds reading.


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               | Example                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `time`                                                                                    | *str*                                                                                     | :heavy_check_mark:                                                                        | UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.                        | 2020-01-27T07:06:25Z                                                                      |
| `value`                                                                                   | *int*                                                                                     | :heavy_check_mark:                                                                        | Number of seconds the vehicle's engine has been on according to the on-board diagnostics. | 9723103                                                                                   |