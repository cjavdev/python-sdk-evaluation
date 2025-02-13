# MobileUsageDetectionAlertSettingsObjectResponseBody

Enables AI detection of mobile usage events.


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `has_in_cab_audio_alerts_enabled`                                     | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | Indicates whether in-cab audio alerts for mobile usage are turned on. | true                                                                  |
| `is_enabled`                                                          | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | Indicates whether AI event detection for mobile usage is turned on.   | true                                                                  |
| `speeding_threshold_mph`                                              | *Optional[float]*                                                     | :heavy_minus_sign:                                                    | Alert when speed is over this many miles per hour.                    | 5                                                                     |