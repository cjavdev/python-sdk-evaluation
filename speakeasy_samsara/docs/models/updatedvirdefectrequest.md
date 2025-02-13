# UpdateDvirDefectRequest


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `id`                                                     | *str*                                                    | :heavy_check_mark:                                       | ID of the defect.                                        |
| `defect_patch`                                           | [Optional[models.DefectPatch]](../models/defectpatch.md) | :heavy_minus_sign:                                       | The DVIR defect fields to update.                        |