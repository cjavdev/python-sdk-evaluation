# HosLogsForDriver

List of HOS logs for a driver.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `driver`                                                               | [Optional[models.DriverTinyResponse]](../models/drivertinyresponse.md) | :heavy_minus_sign:                                                     | A minified driver object.                                              |
| `hos_logs`                                                             | List[[models.HosLogEntry](../models/hoslogentry.md)]                   | :heavy_minus_sign:                                                     | List of HOS log entries.                                               |