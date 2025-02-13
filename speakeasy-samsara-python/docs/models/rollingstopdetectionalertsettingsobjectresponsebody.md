# RollingStopDetectionAlertSettingsObjectResponseBody

AI event detection settings for the rolling stop behavior. Detection is available in vehicles with compatible dash cams.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `is_enabled`                                                         | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Indicates whether AI event detection for rolling stops is turned on. | true                                                                 |
| `speeding_threshold_mph`                                             | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Alert when speed is over this many miles per hour.                   | 0                                                                    |