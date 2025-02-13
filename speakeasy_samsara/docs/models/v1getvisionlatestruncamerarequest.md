# V1getVisionLatestRunCameraRequest


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `camera_id`                                                           | *int*                                                                 | :heavy_check_mark:                                                    | The camera_id should be valid for the given accessToken.              |
| `program_id`                                                          | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | The configured program's ID on the camera.                            |
| `started_at_ms`                                                       | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | EndMs is an optional param. It will default to the current time.      |
| `include`                                                             | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Include is a filter parameter. Accepts 'pass', 'reject' or 'no_read'. |
| `limit`                                                               | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | Limit is an integer value from 1 to 1,000.                            |