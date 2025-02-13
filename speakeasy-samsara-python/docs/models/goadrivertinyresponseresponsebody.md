# GoaDriverTinyResponseResponseBody

A minified driver object. This object is only returned if the route is assigned to the driver.


## Fields

| Field                 | Type                  | Required              | Description           | Example               |
| --------------------- | --------------------- | --------------------- | --------------------- | --------------------- |
| `id`                  | *str*                 | :heavy_check_mark:    | ID of the driver      | 45646                 |
| `external_ids`        | Dict[str, *str*]      | :heavy_minus_sign:    | A map of external ids |                       |
| `name`                | *Optional[str]*       | :heavy_minus_sign:    | Name of the driver    | Driver Bob            |