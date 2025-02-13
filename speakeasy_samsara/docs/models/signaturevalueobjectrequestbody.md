# SignatureValueObjectRequestBody

The value of a signature field. Only present for signature fields.


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `id`                                                                  | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Id of the signature field.                                            | 9814a1fa-f0c6-408b-bf85-51dc3bc71ac7                                  |
| `name`                                                                | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Name of the signee for a signature field.                             | John Smith                                                            |
| `signed_at_time`                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)  | :heavy_minus_sign:                                                    | Time the signature was captured in RFC 3339 format.                   | 2010-07-18T06:13:42Z                                                  |
| `url`                                                                 | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Url of a signature field's PNG signature image.                       | https://samsara-driver-media-upload.s3.us-west-2.amazonaws.com/123456 |