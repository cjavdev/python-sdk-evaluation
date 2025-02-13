# TachographActivityListWrapper


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `activity`                                                             | List[[models.TachographActivity](../models/tachographactivity.md)]     | :heavy_minus_sign:                                                     | List of all driver tachograph activities in a specified time range.    |
| `driver`                                                               | [Optional[models.DriverTinyResponse]](../models/drivertinyresponse.md) | :heavy_minus_sign:                                                     | A minified driver object.                                              |