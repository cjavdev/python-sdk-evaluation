# IftaJurisdictionSummaryObjectResponseBody

A summary of this jurisdiction's IFTA data.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `jurisdiction`                                                       | *str*                                                                | :heavy_check_mark:                                                   | Jurisdiction code.                                                   | GA                                                                   |
| `taxable_meters`                                                     | *float*                                                              | :heavy_check_mark:                                                   | Distance in meters traveled on public roads in an IFTA jurisdiction. | 2350                                                                 |
| `total_meters`                                                       | *float*                                                              | :heavy_check_mark:                                                   | Total meters driven in this jurisdiction, taxable and non-taxable.   | 2350                                                                 |
| `tax_paid_liters`                                                    | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Liters purchased for all qualified vehicles.                         | 25.5                                                                 |