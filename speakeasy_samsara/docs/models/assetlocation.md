# AssetLocation

For locationType "point", latitude and longitude are required. For "address", formattedAddress must be provided, and lat/long can be optionally included for displaying a dot on the assets map. For "dataInput", this object should not be passed in.


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    | Example                                        |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `formatted_address`                            | *Optional[str]*                                | :heavy_minus_sign:                             | Formatted address of the location              | 350 Rhode Island St, San Francisco CA, 94103   |
| `latitude`                                     | *Optional[float]*                              | :heavy_minus_sign:                             | The latitude of the asset in decimal degrees.  | 37.765363                                      |
| `longitude`                                    | *Optional[float]*                              | :heavy_minus_sign:                             | The longitude of the asset in decimal degrees. | -122.403098                                    |