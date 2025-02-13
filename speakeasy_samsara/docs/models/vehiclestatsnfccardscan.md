# VehicleStatsNfcCardScan

Data for the nfc card and the time that it was scanned.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    | Example                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `card`                                                                         | [models.VehicleStatsNfcCardScanCard](../models/vehiclestatsnfccardscancard.md) | :heavy_check_mark:                                                             | The card that was scanned.                                                     |                                                                                |
| `time`                                                                         | *str*                                                                          | :heavy_check_mark:                                                             | UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.             | 2020-01-27T07:06:25Z                                                           |