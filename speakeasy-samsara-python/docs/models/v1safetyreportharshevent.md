# V1SafetyReportHarshEvent

List of harsh events


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              | Example                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `harsh_event_type`                                                       | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | Sensor generated harsh event type.                                       | Harsh Braking                                                            |
| `timestamp_ms`                                                           | *Optional[int]*                                                          | :heavy_minus_sign:                                                       | Timestamp that the harsh event occurred in Unix milliseconds since epoch | 1535590776000                                                            |
| `vehicle_id`                                                             | *Optional[int]*                                                          | :heavy_minus_sign:                                                       | Vehicle associated with the harsh event                                  | 212014918086169                                                          |