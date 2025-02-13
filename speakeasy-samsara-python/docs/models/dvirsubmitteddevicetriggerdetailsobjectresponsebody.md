# DVIRSubmittedDeviceTriggerDetailsObjectResponseBody

Details specific to DVIR Submitted by Device


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              | Example                                                                                  |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `dvir_min_duration_milliseconds`                                                         | *Optional[int]*                                                                          | :heavy_minus_sign:                                                                       | The trigger will only fire if the selected DVIR types are submitted within the duration. | 600000                                                                                   |
| `dvir_submission_types`                                                                  | List[[models.DvirSubmissionTypes](../models/dvirsubmissiontypes.md)]                     | :heavy_minus_sign:                                                                       | Filter to these types of DVIR submissions.                                               | [<br/>"SAFE_NO_DEFECTS",<br/>"SAFE_NO_DEFECTS",<br/>"UNSAFE",<br/>"UNSAFE"<br/>]         |