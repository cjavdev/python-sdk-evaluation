"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .documentsgetdocumentsbadrequesterrorresponsebody import (
    DocumentsGetDocumentsBadRequestErrorResponseBody,
    DocumentsGetDocumentsBadRequestErrorResponseBodyTypedDict,
)
from .documentsgetdocumentsresponsebody import (
    DocumentsGetDocumentsResponseBody,
    DocumentsGetDocumentsResponseBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, QueryParamMetadata
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class GetDocumentsRequestTypedDict(TypedDict):
    start_time: str
    r"""A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""
    end_time: str
    r"""An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""
    after: NotRequired[str]
    r"""If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results."""
    document_type_id: NotRequired[str]
    r"""ID of the document template type."""
    query_by: NotRequired[str]
    r"""Query by document creation time (`created`) or updated time (`updated`). Defaults to `created`."""


class GetDocumentsRequest(BaseModel):
    start_time: Annotated[
        str,
        pydantic.Field(alias="startTime"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""

    end_time: Annotated[
        str,
        pydantic.Field(alias="endTime"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""

    after: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results."""

    document_type_id: Annotated[
        Optional[str],
        pydantic.Field(alias="documentTypeId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""ID of the document template type."""

    query_by: Annotated[
        Optional[str],
        pydantic.Field(alias="queryBy"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Query by document creation time (`created`) or updated time (`updated`). Defaults to `created`."""


GetDocumentsResponseTypedDict = TypeAliasType(
    "GetDocumentsResponseTypedDict",
    Union[
        DocumentsGetDocumentsResponseBodyTypedDict,
        DocumentsGetDocumentsBadRequestErrorResponseBodyTypedDict,
    ],
)


GetDocumentsResponse = TypeAliasType(
    "GetDocumentsResponse",
    Union[
        DocumentsGetDocumentsResponseBody,
        DocumentsGetDocumentsBadRequestErrorResponseBody,
    ],
)
