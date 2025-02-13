# GeofenceEntryTriggerDetailsObjectRequestBody

Details specific to Geofence Entry


## Fields

| Field                                                                                                                | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `location`                                                                                                           | [models.LocationObjectRequestBody](../models/locationobjectrequestbody.md)                                           | :heavy_check_mark:                                                                                                   | A location. Polygon and Circle is deprecated, but may be set for old Alerts. At least one location must be selected. |