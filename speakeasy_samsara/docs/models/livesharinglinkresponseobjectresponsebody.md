# LiveSharingLinkResponseObjectResponseBody

Live Sharing Link response object.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `live_sharing_url`                                                           | *str*                                                                        | :heavy_check_mark:                                                           | The shareable URL of the vehicle's location.                                 | https://cloud.samsara.com/o/123456/fleet/viewer/address/gEAitEnnOwcv92cuPzcU |
| `name`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | Name of the Live Sharing Link.                                               | Name                                                                         |
| `expires_at_time`                                                            | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Date that this link expires, in RFC 3339 format.                             | 2020-01-27T07:06:25Z                                                         |