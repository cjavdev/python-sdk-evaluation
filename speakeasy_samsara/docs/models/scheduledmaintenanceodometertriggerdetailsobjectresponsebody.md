# ScheduledMaintenanceOdometerTriggerDetailsObjectResponseBody

Details specific to Scheduled Maintenance by Odometer


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     | Example                                                                         |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `due_in_meters`                                                                 | *int*                                                                           | :heavy_check_mark:                                                              | Alert when vehicle odometer has this many meters left until maintenance is due. | 5000                                                                            |
| `schedule_id`                                                                   | *str*                                                                           | :heavy_check_mark:                                                              | The id of the maintenance schedule.                                             | 123                                                                             |