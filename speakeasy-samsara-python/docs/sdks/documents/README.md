# Documents
(*documents*)

## Overview

### Available Operations

* [get_document_types](#get_document_types) - Fetch document types
* [get_documents](#get_documents) - Fetch all documents
* [post_document](#post_document) - Create document
* [generate_document_pdf](#generate_document_pdf) - Create a document PDF
* [get_document_pdf](#get_document_pdf) - Query a document PDF
* [delete_document](#delete_document) - Delete document
* [get_document](#get_document) - Fetch document

## get_document_types

Returns a list of the organization document types. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/getDriverDocumentTypesByOrgId).

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Documents** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.documents.get_document_types()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                       | Type                                                                                                                                                                                                            | Required                                                                                                                                                                                                        | Description                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `after`                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              |  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. |
| `retries`                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                             |

### Response

**[models.GetDocumentTypesResponse](../../models/getdocumenttypesresponse.md)**

### Errors

| Error Type                                                              | Status Code                                                             | Content Type                                                            |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| models.DocumentTypesGetDocumentTypesUnauthorizedErrorResponseBody       | 401                                                                     | application/json                                                        |
| models.DocumentTypesGetDocumentTypesNotFoundErrorResponseBody           | 404                                                                     | application/json                                                        |
| models.DocumentTypesGetDocumentTypesMethodNotAllowedErrorResponseBody   | 405                                                                     | application/json                                                        |
| models.DocumentTypesGetDocumentTypesTooManyRequestsErrorResponseBody    | 429                                                                     | application/json                                                        |
| models.DocumentTypesGetDocumentTypesInternalServerErrorResponseBody     | 500                                                                     | application/json                                                        |
| models.DocumentTypesGetDocumentTypesNotImplementedErrorResponseBody     | 501                                                                     | application/json                                                        |
| models.DocumentTypesGetDocumentTypesBadGatewayErrorResponseBody         | 502                                                                     | application/json                                                        |
| models.DocumentTypesGetDocumentTypesServiceUnavailableErrorResponseBody | 503                                                                     | application/json                                                        |
| models.DocumentTypesGetDocumentTypesGatewayTimeoutErrorResponseBody     | 504                                                                     | application/json                                                        |
| models.APIError                                                         | 4XX, 5XX                                                                | \*/\*                                                                   |

## get_documents

Get all documents for the given time range. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/getDriverDocumentsByOrgId).

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Documents** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.documents.get_documents(start_time="<value>", end_time="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                       | Type                                                                                                                                                                                                            | Required                                                                                                                                                                                                        | Description                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                                                                                                    | *str*                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                              |  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). |
| `end_time`                                                                                                                                                                                                      | *str*                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                              |  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).  |
| `after`                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              |  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. |
| `document_type_id`                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              | ID of the document template type.                                                                                                                                                                               |
| `query_by`                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              | Query by document creation time (`created`) or updated time (`updated`). Defaults to `created`.                                                                                                                 |
| `retries`                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                             |

### Response

**[models.GetDocumentsResponse](../../models/getdocumentsresponse.md)**

### Errors

| Error Type                                                      | Status Code                                                     | Content Type                                                    |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| models.DocumentsGetDocumentsUnauthorizedErrorResponseBody       | 401                                                             | application/json                                                |
| models.DocumentsGetDocumentsNotFoundErrorResponseBody           | 404                                                             | application/json                                                |
| models.DocumentsGetDocumentsMethodNotAllowedErrorResponseBody   | 405                                                             | application/json                                                |
| models.DocumentsGetDocumentsTooManyRequestsErrorResponseBody    | 429                                                             | application/json                                                |
| models.DocumentsGetDocumentsInternalServerErrorResponseBody     | 500                                                             | application/json                                                |
| models.DocumentsGetDocumentsNotImplementedErrorResponseBody     | 501                                                             | application/json                                                |
| models.DocumentsGetDocumentsBadGatewayErrorResponseBody         | 502                                                             | application/json                                                |
| models.DocumentsGetDocumentsServiceUnavailableErrorResponseBody | 503                                                             | application/json                                                |
| models.DocumentsGetDocumentsGatewayTimeoutErrorResponseBody     | 504                                                             | application/json                                                |
| models.APIError                                                 | 4XX, 5XX                                                        | \*/\*                                                           |

## post_document

Creates a single document. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/createDriverDocument).

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Documents** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import dateutil.parser
import os
import samsara
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.documents.post_document(document_type_id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7", driver_id="45646", fields=[
        {
            "label": "Load weight",
            "type": samsara.FieldObjectPostRequestBodyType.PHOTO,
            "value": {
                "barcode_value": [
                    {
                        "barcode_type": "org.gs1.EAN-13",
                        "barcode_value": "0853883003114",
                    },
                    {
                        "barcode_type": "org.gs1.EAN-13",
                        "barcode_value": "0853883003114",
                    },
                ],
                "date_time_value": {
                    "date_time": dateutil.parser.isoparse("1996-02-22T20:14:42Z"),
                },
                "multiple_choice_value": [
                    {
                        "selected": False,
                        "value": "Yes",
                    },
                    {
                        "selected": False,
                        "value": "Yes",
                    },
                ],
                "number_value": 123.456,
                "photo_value": [
                    {
                        "id": "f5271458-21f9-4a9f-a290-780c6d8840ff",
                        "url": "https://samsara-driver-media-upload.s3.us-west-2.amazonaws.com/123456",
                    },
                    {
                        "id": "f5271458-21f9-4a9f-a290-780c6d8840ff",
                        "url": "https://samsara-driver-media-upload.s3.us-west-2.amazonaws.com/123456",
                    },
                ],
                "scanned_document_value": [
                    {
                        "id": "f5271458-21f9-4a9f-a290-780c6d8840ff",
                        "url": "https://samsara-driver-media-upload.s3.us-west-2.amazonaws.com/123456",
                    },
                    {
                        "id": "f5271458-21f9-4a9f-a290-780c6d8840ff",
                        "url": "https://samsara-driver-media-upload.s3.us-west-2.amazonaws.com/123456",
                    },
                ],
                "signature_value": {
                    "id": "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                    "name": "John Smith",
                    "signed_at_time": dateutil.parser.isoparse("2010-07-18T06:13:42Z"),
                    "url": "https://samsara-driver-media-upload.s3.us-west-2.amazonaws.com/123456",
                },
                "string_value": "Red Truck",
            },
        },
    ], name="Dropoff Slip 123", notes="Missing a crate", route_stop_id="45646", vehicle_id="45646")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                    | Example                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `document_type_id`                                                                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                                             | ID for the document type.                                                                                                                                                                                                                                                                      | 9814a1fa-f0c6-408b-bf85-51dc3bc71ac7                                                                                                                                                                                                                                                           |
| `driver_id`                                                                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                                             | ID of the driver. Can be either unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the driver.                                                                                                                                                        | 45646                                                                                                                                                                                                                                                                                          |
| `fields`                                                                                                                                                                                                                                                                                       | List[[models.FieldObjectPostRequestBody](../../models/fieldobjectpostrequestbody.md)]                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | The fields associated with this document.                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                |
| `name`                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Name of the document.                                                                                                                                                                                                                                                                          | Dropoff Slip 123                                                                                                                                                                                                                                                                               |
| `notes`                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Notes on the document.                                                                                                                                                                                                                                                                         | Missing a crate                                                                                                                                                                                                                                                                                |
| `route_stop_id`                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | ID of the route stop. Can be either unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the route stop.                                                                                                                                                | 45646                                                                                                                                                                                                                                                                                          |
| `state`                                                                                                                                                                                                                                                                                        | [Optional[models.DocumentsPostDocumentRequestBodyState]](../../models/documentspostdocumentrequestbodystate.md)                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | The condition of the document created for the driver. Can be either `required` or `submitted`, if no value is specified, `state` defaults to `required`. `required` documents are pre-populated documents for the Driver to fill out in the Driver App.  Valid values: `submitted`, `required` | submitted                                                                                                                                                                                                                                                                                      |
| `vehicle_id`                                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | ID of the vehicle. Can be either unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.                                                                                                                                                      | 45646                                                                                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                |

### Response

**[models.PostDocumentResponse](../../models/postdocumentresponse.md)**

### Errors

| Error Type                                                      | Status Code                                                     | Content Type                                                    |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| models.DocumentsPostDocumentUnauthorizedErrorResponseBody       | 401                                                             | application/json                                                |
| models.DocumentsPostDocumentNotFoundErrorResponseBody           | 404                                                             | application/json                                                |
| models.DocumentsPostDocumentMethodNotAllowedErrorResponseBody   | 405                                                             | application/json                                                |
| models.DocumentsPostDocumentTooManyRequestsErrorResponseBody    | 429                                                             | application/json                                                |
| models.DocumentsPostDocumentInternalServerErrorResponseBody     | 500                                                             | application/json                                                |
| models.DocumentsPostDocumentNotImplementedErrorResponseBody     | 501                                                             | application/json                                                |
| models.DocumentsPostDocumentBadGatewayErrorResponseBody         | 502                                                             | application/json                                                |
| models.DocumentsPostDocumentServiceUnavailableErrorResponseBody | 503                                                             | application/json                                                |
| models.DocumentsPostDocumentGatewayTimeoutErrorResponseBody     | 504                                                             | application/json                                                |
| models.APIError                                                 | 4XX, 5XX                                                        | \*/\*                                                           |

## generate_document_pdf

Request creation of a document PDF. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Documents** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.documents.generate_document_pdf(request={
        "document_id": "6c8c0c01-206a-41a4-9d21-15b9978d04cb",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.DocumentPdfGenerationRequest](../../models/documentpdfgenerationrequest.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.GenerateDocumentPdfResponse](../../models/generatedocumentpdfresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_document_pdf

Returns generation job status and download URL for a PDF. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Documents** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.documents.get_document_pdf(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | ID of the pdf.                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetDocumentPdfResponse](../../models/getdocumentpdfresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_document

Deletes a single document. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/deleteDriverDocumentByIdAndDriverId).

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Documents** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.documents.delete_document(id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | ID of the document to delete                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DocumentsDeleteDocumentBadRequestErrorResponseBody](../../models/documentsdeletedocumentbadrequesterrorresponsebody.md)**

### Errors

| Error Type                                                        | Status Code                                                       | Content Type                                                      |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| models.DocumentsDeleteDocumentUnauthorizedErrorResponseBody       | 401                                                               | application/json                                                  |
| models.DocumentsDeleteDocumentNotFoundErrorResponseBody           | 404                                                               | application/json                                                  |
| models.DocumentsDeleteDocumentMethodNotAllowedErrorResponseBody   | 405                                                               | application/json                                                  |
| models.DocumentsDeleteDocumentTooManyRequestsErrorResponseBody    | 429                                                               | application/json                                                  |
| models.DocumentsDeleteDocumentInternalServerErrorResponseBody     | 500                                                               | application/json                                                  |
| models.DocumentsDeleteDocumentNotImplementedErrorResponseBody     | 501                                                               | application/json                                                  |
| models.DocumentsDeleteDocumentBadGatewayErrorResponseBody         | 502                                                               | application/json                                                  |
| models.DocumentsDeleteDocumentServiceUnavailableErrorResponseBody | 503                                                               | application/json                                                  |
| models.DocumentsDeleteDocumentGatewayTimeoutErrorResponseBody     | 504                                                               | application/json                                                  |
| models.APIError                                                   | 4XX, 5XX                                                          | \*/\*                                                             |

## get_document

Returns a single document. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/getDriverDocumentByIdAndDriverId).

 <b>Rate limit:</b> 25 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Documents** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.documents.get_document(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | ID of the document                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetDocumentResponse](../../models/getdocumentresponse.md)**

### Errors

| Error Type                                                     | Status Code                                                    | Content Type                                                   |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| models.DocumentsGetDocumentUnauthorizedErrorResponseBody       | 401                                                            | application/json                                               |
| models.DocumentsGetDocumentNotFoundErrorResponseBody           | 404                                                            | application/json                                               |
| models.DocumentsGetDocumentMethodNotAllowedErrorResponseBody   | 405                                                            | application/json                                               |
| models.DocumentsGetDocumentTooManyRequestsErrorResponseBody    | 429                                                            | application/json                                               |
| models.DocumentsGetDocumentInternalServerErrorResponseBody     | 500                                                            | application/json                                               |
| models.DocumentsGetDocumentNotImplementedErrorResponseBody     | 501                                                            | application/json                                               |
| models.DocumentsGetDocumentBadGatewayErrorResponseBody         | 502                                                            | application/json                                               |
| models.DocumentsGetDocumentServiceUnavailableErrorResponseBody | 503                                                            | application/json                                               |
| models.DocumentsGetDocumentGatewayTimeoutErrorResponseBody     | 504                                                            | application/json                                               |
| models.APIError                                                | 4XX, 5XX                                                       | \*/\*                                                          |