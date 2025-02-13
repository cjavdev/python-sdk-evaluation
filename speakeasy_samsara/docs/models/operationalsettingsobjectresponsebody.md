# OperationalSettingsObjectResponseBody

Settings on when the alert should be operational.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          | Example                                                                              |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `time_range_type`                                                                    | [models.TimeRangeType](../models/timerangetype.md)                                   | :heavy_check_mark:                                                                   | The type of time ranges.  Valid values: `activeBetween`, `inactiveBetween`           | activeBetween                                                                        |
| `time_ranges`                                                                        | List[[models.TimeRangeObjectResponseBody](../models/timerangeobjectresponsebody.md)] | :heavy_check_mark:                                                                   | The time ranges this alert applies to.                                               |                                                                                      |