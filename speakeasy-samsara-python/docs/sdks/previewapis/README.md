# PreviewAPIs
(*preview_ap_is*)

## Overview

### Available Operations

* [list_uploaded_media](#list_uploaded_media) - [preview] List uploaded media by time range.
* [get_custom_report_configs](#get_custom_report_configs) - [preview] Get custom report configs
* [get_custom_report_runs](#get_custom_report_runs) - [preview] Get custom report runs
* [post_custom_report_run](#post_custom_report_run) - [preview] Create a custom report run
* [get_custom_report_run_data](#get_custom_report_run_data) - [preview] Get custom report run data
* [get_driver_efficiency_by_drivers](#get_driver_efficiency_by_drivers) - [preview] Get Driver efficiency data grouped by drivers.
* [get_driver_efficiency_by_vehicles](#get_driver_efficiency_by_vehicles) - [preview] Get Driver efficiency data grouped by vehicles.
* [get_form_templates](#get_form_templates) - [preview] Get a list of form templates.
* [delete_training_assignments](#delete_training_assignments) - [preview] Delete training assignments.
* [patch_training_assignments](#patch_training_assignments) - [preview] Update training assignments.
* [get_training_courses](#get_training_courses) - [preview] Get a list of filtered training courses.

## list_uploaded_media

This endpoint returns a list of all uploaded media (video and still images) matching query parameters. Additional media can be retrieved with the [Create a media retrieval request](https://developers.samsara.com/reference/postmediaretrieval) endpoint, and they will be included in the list after they are uploaded. Urls provided by this endpoint expire in 8 hours.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Preview** under the  category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.preview_ap_is.list_uploaded_media(start_time="<value>", end_time="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                        | Type                                                                                                                                                                                                                                                                             | Required                                                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                               | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).                                                                                                    |
| `end_time`                                                                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                               | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).                                                                                                     |
| `vehicle_ids`                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                               |  A filter on the data based on this comma-separated list of vehicle IDs and externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`                                                                                                                           |
| `inputs`                                                                                                                                                                                                                                                                         | List[[models.QueryParamInputs](../../models/queryparaminputs.md)]                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                               | A list of desired camera inputs for which to return captured media. If empty, media for all available inputs will be returned.                                                                                                                                                   |
| `media_types`                                                                                                                                                                                                                                                                    | List[[models.MediaTypes](../../models/mediatypes.md)]                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                               | A list of desired media types for which to return captured media. If empty, media for all available media types will be returned.                                                                                                                                                |
| `trigger_reasons`                                                                                                                                                                                                                                                                | List[[models.TriggerReasons](../../models/triggerreasons.md)]                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                               | A list of desired trigger reasons for which to return captured media. If empty, media for all available trigger reasons will be returned.                                                                                                                                        |
| `tag_ids`                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                               |  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`                                                                                                                                                                                 |
| `parent_tag_ids`                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                               |  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`                                         |
| `available_after_time`                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                               | A timestamp in RFC 3339 format that can act as a cursor to track which media has previously been retrieved; only media whose availableAtTime comes after this parameter will be returned. Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00 |
| `after`                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                               |  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.                                                                  |
| `retries`                                                                                                                                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                              |

### Response

**[models.ListUploadedMediaResponse](../../models/listuploadedmediaresponse.md)**

### Errors

| Error Type                                                                | Status Code                                                               | Content Type                                                              |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| models.MediaRetrievalListUploadedMediaUnauthorizedErrorResponseBody       | 401                                                                       | application/json                                                          |
| models.MediaRetrievalListUploadedMediaNotFoundErrorResponseBody           | 404                                                                       | application/json                                                          |
| models.MediaRetrievalListUploadedMediaMethodNotAllowedErrorResponseBody   | 405                                                                       | application/json                                                          |
| models.MediaRetrievalListUploadedMediaTooManyRequestsErrorResponseBody    | 429                                                                       | application/json                                                          |
| models.MediaRetrievalListUploadedMediaInternalServerErrorResponseBody     | 500                                                                       | application/json                                                          |
| models.MediaRetrievalListUploadedMediaNotImplementedErrorResponseBody     | 501                                                                       | application/json                                                          |
| models.MediaRetrievalListUploadedMediaBadGatewayErrorResponseBody         | 502                                                                       | application/json                                                          |
| models.MediaRetrievalListUploadedMediaServiceUnavailableErrorResponseBody | 503                                                                       | application/json                                                          |
| models.MediaRetrievalListUploadedMediaGatewayTimeoutErrorResponseBody     | 504                                                                       | application/json                                                          |
| models.APIError                                                           | 4XX, 5XX                                                                  | \*/\*                                                                     |

## get_custom_report_configs

Get paginated custom report configs created in the organization.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Custom Reports** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.preview_ap_is.get_custom_report_configs()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                       | Type                                                                                                                                                                                                            | Required                                                                                                                                                                                                        | Description                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `after`                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              |  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. |
| `limit`                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              | The limit for how many reports will be in the response. Default and max for this value is 100 objects.                                                                                                          |
| `retries`                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                             |

### Response

**[models.GetCustomReportConfigsResponse](../../models/getcustomreportconfigsresponse.md)**

### Errors

| Error Type                                                                    | Status Code                                                                   | Content Type                                                                  |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| models.CustomReportsGetCustomReportConfigsUnauthorizedErrorResponseBody       | 401                                                                           | application/json                                                              |
| models.CustomReportsGetCustomReportConfigsNotFoundErrorResponseBody           | 404                                                                           | application/json                                                              |
| models.CustomReportsGetCustomReportConfigsMethodNotAllowedErrorResponseBody   | 405                                                                           | application/json                                                              |
| models.CustomReportsGetCustomReportConfigsTooManyRequestsErrorResponseBody    | 429                                                                           | application/json                                                              |
| models.CustomReportsGetCustomReportConfigsInternalServerErrorResponseBody     | 500                                                                           | application/json                                                              |
| models.CustomReportsGetCustomReportConfigsNotImplementedErrorResponseBody     | 501                                                                           | application/json                                                              |
| models.CustomReportsGetCustomReportConfigsBadGatewayErrorResponseBody         | 502                                                                           | application/json                                                              |
| models.CustomReportsGetCustomReportConfigsServiceUnavailableErrorResponseBody | 503                                                                           | application/json                                                              |
| models.CustomReportsGetCustomReportConfigsGatewayTimeoutErrorResponseBody     | 504                                                                           | application/json                                                              |
| models.APIError                                                               | 4XX, 5XX                                                                      | \*/\*                                                                         |

## get_custom_report_runs

Get all custom report runs with the provided IDs or customReportIds.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Custom Reports** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.preview_ap_is.get_custom_report_runs()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                       | Type                                                                                                                                                                                                            | Required                                                                                                                                                                                                        | Description                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `custom_report_ids`                                                                                                                                                                                             | List[*str*]                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                              | Required array of custom report IDs for the custom report runs wanted. Only one of customReportIds or ids is allowed.                                                                                           |
| `ids`                                                                                                                                                                                                           | List[*str*]                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                              | Required array of custom report run IDs to fetch. Only one of ids or customReportIds is allowed.                                                                                                                |
| `after`                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              |  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. |
| `retries`                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                             |

### Response

**[models.GetCustomReportRunsResponse](../../models/getcustomreportrunsresponse.md)**

### Errors

| Error Type                                                                 | Status Code                                                                | Content Type                                                               |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| models.CustomReportsGetCustomReportRunsUnauthorizedErrorResponseBody       | 401                                                                        | application/json                                                           |
| models.CustomReportsGetCustomReportRunsNotFoundErrorResponseBody           | 404                                                                        | application/json                                                           |
| models.CustomReportsGetCustomReportRunsMethodNotAllowedErrorResponseBody   | 405                                                                        | application/json                                                           |
| models.CustomReportsGetCustomReportRunsTooManyRequestsErrorResponseBody    | 429                                                                        | application/json                                                           |
| models.CustomReportsGetCustomReportRunsInternalServerErrorResponseBody     | 500                                                                        | application/json                                                           |
| models.CustomReportsGetCustomReportRunsNotImplementedErrorResponseBody     | 501                                                                        | application/json                                                           |
| models.CustomReportsGetCustomReportRunsBadGatewayErrorResponseBody         | 502                                                                        | application/json                                                           |
| models.CustomReportsGetCustomReportRunsServiceUnavailableErrorResponseBody | 503                                                                        | application/json                                                           |
| models.CustomReportsGetCustomReportRunsGatewayTimeoutErrorResponseBody     | 504                                                                        | application/json                                                           |
| models.APIError                                                            | 4XX, 5XX                                                                   | \*/\*                                                                      |

## post_custom_report_run

Create a custom report run which then gets queued up to generate custom report data for the report run.

 <b>Rate limit:</b> 240 requests/day (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Custom Reports** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import dateutil.parser
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.preview_ap_is.post_custom_report_run(custom_report_id="4f71fd67-54f0-41de-991c-ee1e031134d1", end_time=dateutil.parser.isoparse("2019-06-13T21:08:25Z"), start_time=dateutil.parser.isoparse("2019-06-13T19:08:25Z"), attribute_value_ids=[
        "Aspernatur cumque voluptatibus nihil magni facere.",
    ], tag_ids=[
        2677784051113612000,
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        | Example                                                                            |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `custom_report_id`                                                                 | *str*                                                                              | :heavy_check_mark:                                                                 | Required unique ID for the custom report linked to this run.                       | 4f71fd67-54f0-41de-991c-ee1e031134d1                                               |
| `end_time`                                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects)               | :heavy_check_mark:                                                                 | The end time of the custom report run in RFC 3339 format.                          | 2019-06-13T21:08:25Z                                                               |
| `start_time`                                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects)               | :heavy_check_mark:                                                                 | The start time of the custom report run in RFC 3339 format.                        | 2019-06-13T19:08:25Z                                                               |
| `attribute_value_ids`                                                              | List[*str*]                                                                        | :heavy_minus_sign:                                                                 | The optional array of attribute value ids to filter the custom report run by.      | [<br/>"19abdecf-54f0-41de-991c-ee1e031134d1",<br/>"ab83dfce-54f0-41de-991c-ee1e031134d2"<br/>] |
| `tag_ids`                                                                          | List[*int*]                                                                        | :heavy_minus_sign:                                                                 | The optional array of tag ids to filter the custom report run by.                  | [<br/>48923049,<br/>198349<br/>]                                                   |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |                                                                                    |

### Response

**[models.PostCustomReportRunResponse](../../models/postcustomreportrunresponse.md)**

### Errors

| Error Type                                                                 | Status Code                                                                | Content Type                                                               |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| models.CustomReportsPostCustomReportRunUnauthorizedErrorResponseBody       | 401                                                                        | application/json                                                           |
| models.CustomReportsPostCustomReportRunNotFoundErrorResponseBody           | 404                                                                        | application/json                                                           |
| models.CustomReportsPostCustomReportRunMethodNotAllowedErrorResponseBody   | 405                                                                        | application/json                                                           |
| models.CustomReportsPostCustomReportRunTooManyRequestsErrorResponseBody    | 429                                                                        | application/json                                                           |
| models.CustomReportsPostCustomReportRunInternalServerErrorResponseBody     | 500                                                                        | application/json                                                           |
| models.CustomReportsPostCustomReportRunNotImplementedErrorResponseBody     | 501                                                                        | application/json                                                           |
| models.CustomReportsPostCustomReportRunBadGatewayErrorResponseBody         | 502                                                                        | application/json                                                           |
| models.CustomReportsPostCustomReportRunServiceUnavailableErrorResponseBody | 503                                                                        | application/json                                                           |
| models.CustomReportsPostCustomReportRunGatewayTimeoutErrorResponseBody     | 504                                                                        | application/json                                                           |
| models.APIError                                                            | 4XX, 5XX                                                                   | \*/\*                                                                      |

## get_custom_report_run_data

This endpoint will return the custom report data for a given custom report run ID. For more information regarding custom report columns, please see our [KB article section on Custom Report Fields](https://kb.samsara.com/hc/en-us/articles/360052711232-Manage-Custom-Reports).

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Custom Reports** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.preview_ap_is.get_custom_report_run_data()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                       | Type                                                                                                                                                                                                            | Required                                                                                                                                                                                                        | Description                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              | The ID of the specified run for the requested custom report.                                                                                                                                                    |
| `after`                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              |  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. |
| `retries`                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                             |

### Response

**[models.GetCustomReportRunDataResponse](../../models/getcustomreportrundataresponse.md)**

### Errors

| Error Type                                                                    | Status Code                                                                   | Content Type                                                                  |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| models.CustomReportsGetCustomReportRunDataUnauthorizedErrorResponseBody       | 401                                                                           | application/json                                                              |
| models.CustomReportsGetCustomReportRunDataNotFoundErrorResponseBody           | 404                                                                           | application/json                                                              |
| models.CustomReportsGetCustomReportRunDataMethodNotAllowedErrorResponseBody   | 405                                                                           | application/json                                                              |
| models.CustomReportsGetCustomReportRunDataTooManyRequestsErrorResponseBody    | 429                                                                           | application/json                                                              |
| models.CustomReportsGetCustomReportRunDataInternalServerErrorResponseBody     | 500                                                                           | application/json                                                              |
| models.CustomReportsGetCustomReportRunDataNotImplementedErrorResponseBody     | 501                                                                           | application/json                                                              |
| models.CustomReportsGetCustomReportRunDataBadGatewayErrorResponseBody         | 502                                                                           | application/json                                                              |
| models.CustomReportsGetCustomReportRunDataServiceUnavailableErrorResponseBody | 503                                                                           | application/json                                                              |
| models.CustomReportsGetCustomReportRunDataGatewayTimeoutErrorResponseBody     | 504                                                                           | application/json                                                              |
| models.APIError                                                               | 4XX, 5XX                                                                      | \*/\*                                                                         |

## get_driver_efficiency_by_drivers

This endpoint will return driver efficiency data that has been collected for your organization and grouped by drivers based on the time parameters passed in. Results are paginated.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Driver Efficiency** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.preview_ap_is.get_driver_efficiency_by_drivers(start_time="<value>", end_time="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                    | A start time in RFC 3339 format. Must be in multiple of hours and at least 1 day before endTime. Timezones are supported. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. (Examples: 2019-06-11T19:00:00Z, 2015-09-12T14:00:00-04:00).                |
| `end_time`                                                                                                                                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                    | An end time in RFC 3339 format. Must be in multiple of hours and no later than 3 hours before the current time. Timezones are supported. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. (Examples: 2019-06-13T19:00:00Z, 2015-09-15T14:00:00-04:00). |
| `driver_ids`                                                                                                                                                                                                                                                                                                                                                                          | List[*str*]                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                    |  A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`                                                                                                                                                                                                                                                   |
| `data_formats`                                                                                                                                                                                                                                                                                                                                                                        | List[*str*]                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                    | A comma-separated list of data formats you want to fetch. Valid values: `score`, `raw` and `percentage`. The default data format is `score`. Example: `dataFormats=raw,score`                                                                                                                                                                                                         |
| `tag_ids`                                                                                                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                    |  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`                                                                                                                                                                                                                                                                                      |
| `parent_tag_ids`                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                    |  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`                                                                                                                                              |
| `after`                                                                                                                                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                    |  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.                                                                                                                                                                       |
| `retries`                                                                                                                                                                                                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                   |

### Response

**[models.GetDriverEfficiencyByDriversResponse](../../models/getdriverefficiencybydriversresponse.md)**

### Errors

| Error Type                                                                             | Status Code                                                                            | Content Type                                                                           |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| models.DriverEfficiencyGetDriverEfficiencyByDriversUnauthorizedErrorResponseBody       | 401                                                                                    | application/json                                                                       |
| models.DriverEfficiencyGetDriverEfficiencyByDriversNotFoundErrorResponseBody           | 404                                                                                    | application/json                                                                       |
| models.DriverEfficiencyGetDriverEfficiencyByDriversMethodNotAllowedErrorResponseBody   | 405                                                                                    | application/json                                                                       |
| models.DriverEfficiencyGetDriverEfficiencyByDriversTooManyRequestsErrorResponseBody    | 429                                                                                    | application/json                                                                       |
| models.DriverEfficiencyGetDriverEfficiencyByDriversInternalServerErrorResponseBody     | 500                                                                                    | application/json                                                                       |
| models.DriverEfficiencyGetDriverEfficiencyByDriversNotImplementedErrorResponseBody     | 501                                                                                    | application/json                                                                       |
| models.DriverEfficiencyGetDriverEfficiencyByDriversBadGatewayErrorResponseBody         | 502                                                                                    | application/json                                                                       |
| models.DriverEfficiencyGetDriverEfficiencyByDriversServiceUnavailableErrorResponseBody | 503                                                                                    | application/json                                                                       |
| models.DriverEfficiencyGetDriverEfficiencyByDriversGatewayTimeoutErrorResponseBody     | 504                                                                                    | application/json                                                                       |
| models.APIError                                                                        | 4XX, 5XX                                                                               | \*/\*                                                                                  |

## get_driver_efficiency_by_vehicles

This endpoint will return driver efficiency data that has been collected for your organization and grouped by vehicle drivers used based on the time parameters passed in. Results are paginated.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Driver Efficiency** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.preview_ap_is.get_driver_efficiency_by_vehicles(start_time="<value>", end_time="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                    | A start time in RFC 3339 format. Must be in multiple of hours and at least 1 day before endTime. Timezones are supported. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. (Examples: 2019-06-11T19:00:00Z, 2015-09-12T14:00:00-04:00).                |
| `end_time`                                                                                                                                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                    | An end time in RFC 3339 format. Must be in multiple of hours and no later than 3 hours before the current time. Timezones are supported. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. (Examples: 2019-06-13T19:00:00Z, 2015-09-15T14:00:00-04:00). |
| `vehicle_ids`                                                                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                    |  A filter on the data based on this comma-separated list of vehicle IDs and externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`                                                                                                                                                                                                                                |
| `data_formats`                                                                                                                                                                                                                                                                                                                                                                        | List[*str*]                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                    | A comma-separated list of data formats you want to fetch. Valid values: `score`, `raw` and `percentage`. The default data format is `score`. Example: `dataFormats=raw,score`                                                                                                                                                                                                         |
| `tag_ids`                                                                                                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                    |  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`                                                                                                                                                                                                                                                                                      |
| `parent_tag_ids`                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                    |  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`                                                                                                                                              |
| `after`                                                                                                                                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                    |  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.                                                                                                                                                                       |
| `retries`                                                                                                                                                                                                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                   |

### Response

**[models.GetDriverEfficiencyByVehiclesResponse](../../models/getdriverefficiencybyvehiclesresponse.md)**

### Errors

| Error Type                                                                              | Status Code                                                                             | Content Type                                                                            |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| models.DriverEfficiencyGetDriverEfficiencyByVehiclesUnauthorizedErrorResponseBody       | 401                                                                                     | application/json                                                                        |
| models.DriverEfficiencyGetDriverEfficiencyByVehiclesNotFoundErrorResponseBody           | 404                                                                                     | application/json                                                                        |
| models.DriverEfficiencyGetDriverEfficiencyByVehiclesMethodNotAllowedErrorResponseBody   | 405                                                                                     | application/json                                                                        |
| models.DriverEfficiencyGetDriverEfficiencyByVehiclesTooManyRequestsErrorResponseBody    | 429                                                                                     | application/json                                                                        |
| models.DriverEfficiencyGetDriverEfficiencyByVehiclesInternalServerErrorResponseBody     | 500                                                                                     | application/json                                                                        |
| models.DriverEfficiencyGetDriverEfficiencyByVehiclesNotImplementedErrorResponseBody     | 501                                                                                     | application/json                                                                        |
| models.DriverEfficiencyGetDriverEfficiencyByVehiclesBadGatewayErrorResponseBody         | 502                                                                                     | application/json                                                                        |
| models.DriverEfficiencyGetDriverEfficiencyByVehiclesServiceUnavailableErrorResponseBody | 503                                                                                     | application/json                                                                        |
| models.DriverEfficiencyGetDriverEfficiencyByVehiclesGatewayTimeoutErrorResponseBody     | 504                                                                                     | application/json                                                                        |
| models.APIError                                                                         | 4XX, 5XX                                                                                | \*/\*                                                                                   |

## get_form_templates

Returns a list of the organization's form templates.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Preview** under the  category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.preview_ap_is.get_form_templates()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                       | Type                                                                                                                                                                                                            | Required                                                                                                                                                                                                        | Description                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ids`                                                                                                                                                                                                           | List[*str*]                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                              | A comma-separated list containing up to 100 template IDs to filter on.                                                                                                                                          |
| `after`                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              |  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. |
| `retries`                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                             |

### Response

**[models.GetFormTemplatesResponse](../../models/getformtemplatesresponse.md)**

### Errors

| Error Type                                                              | Status Code                                                             | Content Type                                                            |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| models.FormTemplatesGetFormTemplatesUnauthorizedErrorResponseBody       | 401                                                                     | application/json                                                        |
| models.FormTemplatesGetFormTemplatesNotFoundErrorResponseBody           | 404                                                                     | application/json                                                        |
| models.FormTemplatesGetFormTemplatesMethodNotAllowedErrorResponseBody   | 405                                                                     | application/json                                                        |
| models.FormTemplatesGetFormTemplatesTooManyRequestsErrorResponseBody    | 429                                                                     | application/json                                                        |
| models.FormTemplatesGetFormTemplatesInternalServerErrorResponseBody     | 500                                                                     | application/json                                                        |
| models.FormTemplatesGetFormTemplatesNotImplementedErrorResponseBody     | 501                                                                     | application/json                                                        |
| models.FormTemplatesGetFormTemplatesBadGatewayErrorResponseBody         | 502                                                                     | application/json                                                        |
| models.FormTemplatesGetFormTemplatesServiceUnavailableErrorResponseBody | 503                                                                     | application/json                                                        |
| models.FormTemplatesGetFormTemplatesGatewayTimeoutErrorResponseBody     | 504                                                                     | application/json                                                        |
| models.APIError                                                         | 4XX, 5XX                                                                | \*/\*                                                                   |

## delete_training_assignments

This endpoint supports batch deletion operations. The response does not indicate which specific deletions, if any, have failed. On a successful deletion or partial failure, a ‘204 No Content’ status is returned.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Training Assignments** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.preview_ap_is.delete_training_assignments(ids=[
        "<value>",
        "<value>",
    ])

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ids`                                                                                                                                                                        | List[*str*]                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                           | String of comma separated assignments IDs. Max value for this value is 100 objects .Example: `ids=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075` |
| `retries`                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                          |

### Response

**[models.TrainingAssignmentsDeleteTrainingAssignmentsBadRequestErrorResponseBody](../../models/trainingassignmentsdeletetrainingassignmentsbadrequesterrorresponsebody.md)**

### Errors

| Error Type                                                                             | Status Code                                                                            | Content Type                                                                           |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| models.TrainingAssignmentsDeleteTrainingAssignmentsUnauthorizedErrorResponseBody       | 401                                                                                    | application/json                                                                       |
| models.TrainingAssignmentsDeleteTrainingAssignmentsNotFoundErrorResponseBody           | 404                                                                                    | application/json                                                                       |
| models.TrainingAssignmentsDeleteTrainingAssignmentsMethodNotAllowedErrorResponseBody   | 405                                                                                    | application/json                                                                       |
| models.TrainingAssignmentsDeleteTrainingAssignmentsTooManyRequestsErrorResponseBody    | 429                                                                                    | application/json                                                                       |
| models.TrainingAssignmentsDeleteTrainingAssignmentsInternalServerErrorResponseBody     | 500                                                                                    | application/json                                                                       |
| models.TrainingAssignmentsDeleteTrainingAssignmentsNotImplementedErrorResponseBody     | 501                                                                                    | application/json                                                                       |
| models.TrainingAssignmentsDeleteTrainingAssignmentsBadGatewayErrorResponseBody         | 502                                                                                    | application/json                                                                       |
| models.TrainingAssignmentsDeleteTrainingAssignmentsServiceUnavailableErrorResponseBody | 503                                                                                    | application/json                                                                       |
| models.TrainingAssignmentsDeleteTrainingAssignmentsGatewayTimeoutErrorResponseBody     | 504                                                                                    | application/json                                                                       |
| models.APIError                                                                        | 4XX, 5XX                                                                               | \*/\*                                                                                  |

## patch_training_assignments

**Preview:** This endpoint is in preview and is likely to change before being broadly available. Reach out to your Samsara Representative to have Training APIs enabled for your organization.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Training Assignments** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.preview_ap_is.patch_training_assignments(ids=[
        "<value>",
    ], due_at_time="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ids`                                                                                                                                                                        | List[*str*]                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                           | String of comma separated assignments IDs. Max value for this value is 100 objects .Example: `ids=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075` |
| `due_at_time`                                                                                                                                                                | *str*                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                           | Due date of the training assignment in RFC 3339 format. Millisecond precision and timezones are supported.                                                                   |
| `retries`                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                          |

### Response

**[models.PatchTrainingAssignmentsResponse](../../models/patchtrainingassignmentsresponse.md)**

### Errors

| Error Type                                                                            | Status Code                                                                           | Content Type                                                                          |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| models.TrainingAssignmentsPatchTrainingAssignmentsUnauthorizedErrorResponseBody       | 401                                                                                   | application/json                                                                      |
| models.TrainingAssignmentsPatchTrainingAssignmentsNotFoundErrorResponseBody           | 404                                                                                   | application/json                                                                      |
| models.TrainingAssignmentsPatchTrainingAssignmentsMethodNotAllowedErrorResponseBody   | 405                                                                                   | application/json                                                                      |
| models.TrainingAssignmentsPatchTrainingAssignmentsTooManyRequestsErrorResponseBody    | 429                                                                                   | application/json                                                                      |
| models.TrainingAssignmentsPatchTrainingAssignmentsInternalServerErrorResponseBody     | 500                                                                                   | application/json                                                                      |
| models.TrainingAssignmentsPatchTrainingAssignmentsNotImplementedErrorResponseBody     | 501                                                                                   | application/json                                                                      |
| models.TrainingAssignmentsPatchTrainingAssignmentsBadGatewayErrorResponseBody         | 502                                                                                   | application/json                                                                      |
| models.TrainingAssignmentsPatchTrainingAssignmentsServiceUnavailableErrorResponseBody | 503                                                                                   | application/json                                                                      |
| models.TrainingAssignmentsPatchTrainingAssignmentsGatewayTimeoutErrorResponseBody     | 504                                                                                   | application/json                                                                      |
| models.APIError                                                                       | 4XX, 5XX                                                                              | \*/\*                                                                                 |

## get_training_courses

Returns all training courses data. Results are paginated. 
 Courses in the ‘draft’ status are excluded from the data returned by this endpoint.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Preview** under the  category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.preview_ap_is.get_training_courses()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                     | Type                                                                                                                                                                                                                                                                                                                                          | Required                                                                                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `after`                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                            |  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.                                                                                                                               |
| `course_ids`                                                                                                                                                                                                                                                                                                                                  | List[*str*]                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                            | Optional string of comma separated course IDs. If course ID is present, training assignments for the specified course ID(s) will be returned. Max value for this value is 100 objects. Defaults to returning all courses. Example: `courseIds=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`                      |
| `category_ids`                                                                                                                                                                                                                                                                                                                                | List[*str*]                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                            | Optional string of comma separated course category IDs. If courseCategoryId is present, training courses for the specified course category(s) will be returned. Max value for this value is 100 objects. Defaults to returning all courses.  Example: `categoryIds=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075` |
| `status`                                                                                                                                                                                                                                                                                                                                      | List[*str*]                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                            | Optional string of comma separated values. If status is present, training courses with the specified status(s) will be returned. Valid values: “published”, “deleted”, “archived”. Defaults to returning all courses.                                                                                                                         |
| `retries`                                                                                                                                                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                           |

### Response

**[models.GetTrainingCoursesResponse](../../models/gettrainingcoursesresponse.md)**

### Errors

| Error Type                                                                  | Status Code                                                                 | Content Type                                                                |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| models.TrainingCoursesGetTrainingCoursesUnauthorizedErrorResponseBody       | 401                                                                         | application/json                                                            |
| models.TrainingCoursesGetTrainingCoursesNotFoundErrorResponseBody           | 404                                                                         | application/json                                                            |
| models.TrainingCoursesGetTrainingCoursesMethodNotAllowedErrorResponseBody   | 405                                                                         | application/json                                                            |
| models.TrainingCoursesGetTrainingCoursesTooManyRequestsErrorResponseBody    | 429                                                                         | application/json                                                            |
| models.TrainingCoursesGetTrainingCoursesInternalServerErrorResponseBody     | 500                                                                         | application/json                                                            |
| models.TrainingCoursesGetTrainingCoursesNotImplementedErrorResponseBody     | 501                                                                         | application/json                                                            |
| models.TrainingCoursesGetTrainingCoursesBadGatewayErrorResponseBody         | 502                                                                         | application/json                                                            |
| models.TrainingCoursesGetTrainingCoursesServiceUnavailableErrorResponseBody | 503                                                                         | application/json                                                            |
| models.TrainingCoursesGetTrainingCoursesGatewayTimeoutErrorResponseBody     | 504                                                                         | application/json                                                            |
| models.APIError                                                             | 4XX, 5XX                                                                    | \*/\*                                                                       |