# FormsAssetObjectResponseBody

Tracked or untracked (i.e. manually entered) asset object.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `entry_type`                                                           | [models.EntryType](../models/entrytype.md)                             | :heavy_check_mark:                                                     | The type of entry for the asset.  Valid values: `tracked`, `untracked` | tracked                                                                |
| `id`                                                                   | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | ID of a tracked asset. Included if 'entryType' is 'tracked'.           | 281474982859091                                                        |
| `name`                                                                 | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Name of an untracked (i.e. manually entered) asset.                    | trailer 123                                                            |