# VertexResponseBody

The vertex of the polygon geofence. These geofence vertices describe the perimeter of the polygon, and must consist of at least 3 vertices and less than 40.


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            | Example                                                |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `latitude`                                             | *float*                                                | :heavy_check_mark:                                     | The latitude of a geofence vertex in decimal degrees.  | 37.7749                                                |
| `longitude`                                            | *float*                                                | :heavy_check_mark:                                     | The longitude of a geofence vertex in decimal degrees. | 137.7749                                               |