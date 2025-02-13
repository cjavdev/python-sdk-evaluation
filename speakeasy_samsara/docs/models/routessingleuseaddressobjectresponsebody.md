# RoutesSingleUseAddressObjectResponseBody

This field is used to indicate stops along the route for which an address has not been persisted. This field is mutually exclusive with addressId.


## Fields

| Field                         | Type                          | Required                      | Description                   | Example                       |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `latitude`                    | *float*                       | :heavy_check_mark:            | The latitude of the location  | 123.456                       |
| `longitude`                   | *float*                       | :heavy_check_mark:            | The longitude of the location | 37.459                        |
| `address`                     | *Optional[str]*               | :heavy_minus_sign:            | Address of the stop.          | 1234 Main St, San Jose, CA    |