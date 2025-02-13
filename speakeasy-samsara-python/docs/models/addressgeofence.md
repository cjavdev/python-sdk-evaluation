# AddressGeofence

The geofence that defines this address and its bounds. This can either be a circle or a polygon, but not both.


## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `circle`                                                                                      | [Optional[models.AddressGeofenceCircle]](../models/addressgeofencecircle.md)                  | :heavy_minus_sign:                                                                            | Information about a circular geofence. This field is only needed if the geofence is a circle. |
| `polygon`                                                                                     | [Optional[models.AddressGeofencePolygon]](../models/addressgeofencepolygon.md)                | :heavy_minus_sign:                                                                            | Information about a polygon geofence. This field is only needed if the geofence is a polygon. |
| `settings`                                                                                    | [Optional[models.AddressGeofenceSettings]](../models/addressgeofencesettings.md)              | :heavy_minus_sign:                                                                            | Information about a geofence's settings.                                                      |