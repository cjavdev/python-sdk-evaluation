# TachographDriverFileListWrapper


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `driver`                                                               | [Optional[models.DriverTinyResponse]](../models/drivertinyresponse.md) | :heavy_minus_sign:                                                     | A minified driver object.                                              |
| `files`                                                                | List[[models.TachographDriverFile](../models/tachographdriverfile.md)] | :heavy_minus_sign:                                                     | List of all tachograph driver files in a specified time range.         |