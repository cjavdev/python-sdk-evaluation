# FormsScoreObjectResponseBody

Forms score object.


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     | Example                                                                         |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `max_points`                                                                    | *float*                                                                         | :heavy_check_mark:                                                              | Total possible points of the form submission.                                   | 80                                                                              |
| `score_percent`                                                                 | *float*                                                                         | :heavy_check_mark:                                                              | Percentage score of the form submission, calculated as scorePoints / maxPoints. | 75                                                                              |
| `score_points`                                                                  | *float*                                                                         | :heavy_check_mark:                                                              | Score, in points, of the form submission.                                       | 60                                                                              |