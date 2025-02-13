# V1SensorHistoryResponseResults


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      | Example                                                          |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `series`                                                         | List[*int*]                                                      | :heavy_minus_sign:                                               | List of datapoints, one for each requested (sensor, field) pair. |                                                                  |
| `time_ms`                                                        | *Optional[int]*                                                  | :heavy_minus_sign:                                               | Timestamp in UNIX milliseconds.                                  | 1453449599999                                                    |