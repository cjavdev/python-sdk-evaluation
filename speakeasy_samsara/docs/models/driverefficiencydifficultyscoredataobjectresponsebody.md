# DriverEfficiencyDifficultyScoreDataObjectResponseBody

Difficulty score won't be available if there is no data to compute it against.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              | Example                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `overall_score`                                                          | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | Represents the overall difficulty score. It has scores from 1 to 5.      | 4                                                                        |
| `topography_score`                                                       | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | Represents the topography difficulty score. It has scores from 1 to 5.   | 5                                                                        |
| `vehicle_weight_score`                                                   | *Optional[str]*                                                          | :heavy_minus_sign:                                                       |  Represents the average vehicle weight score. It has scores from 1 to 5. | 4                                                                        |