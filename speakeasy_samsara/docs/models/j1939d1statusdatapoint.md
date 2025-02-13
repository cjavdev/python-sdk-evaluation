# J1939D1StatusDataPoint

Active J1939D1 statuses of a device.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          | Example                                                                              |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `time`                                                                               | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.                   | 2020-01-27T07:06:25Z                                                                 |
| `value`                                                                              | List[[models.J1939D1StatusDataPointValue](../models/j1939d1statusdatapointvalue.md)] | :heavy_minus_sign:                                                                   | List of active statuses.                                                             |                                                                                      |