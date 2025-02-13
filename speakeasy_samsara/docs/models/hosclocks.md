# HosClocks

Remaining durations and start times (where applicable) for various HOS rules. See [this page](https://www.samsara.com/fleet/eld-compliance/hours-of-service) for more information on HOS rules.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `break_`                                                             | [Optional[models.HosBreak]](../models/hosbreak.md)                   | :heavy_minus_sign:                                                   | Remaining durations for the HOS rest break requirement.              |
| `cycle`                                                              | [Optional[models.HosCycle]](../models/hoscycle.md)                   | :heavy_minus_sign:                                                   | Remaining durations and start time for the HOS driving cycle.        |
| `drive`                                                              | [Optional[models.HosDrive]](../models/hosdrive.md)                   | :heavy_minus_sign:                                                   | Remaining durations for the HOS driving shift limits.                |
| `shift`                                                              | [Optional[models.HosShift]](../models/hosshift.md)                   | :heavy_minus_sign:                                                   | Remaining durations and start time for the HOS on duty shift limits. |