# LocationDataPoint

A single location data point of a data input.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                | Example                                                                                    |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `gps_location`                                                                             | [Optional[models.LocationDataPointGpsLocation]](../models/locationdatapointgpslocation.md) | :heavy_minus_sign:                                                                         | GPS location information of the data input's datapoint.                                    |                                                                                            |
| `time`                                                                                     | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.                         | 2020-01-27T07:06:25Z                                                                       |