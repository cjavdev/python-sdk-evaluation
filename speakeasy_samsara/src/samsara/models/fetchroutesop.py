"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .routesfetchroutesbadrequesterrorresponsebody import (
    RoutesFetchRoutesBadRequestErrorResponseBody,
    RoutesFetchRoutesBadRequestErrorResponseBodyTypedDict,
)
from .routesfetchroutesresponsebody import (
    RoutesFetchRoutesResponseBody,
    RoutesFetchRoutesResponseBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, QueryParamMetadata
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class FetchRoutesRequestTypedDict(TypedDict):
    start_time: str
    r"""A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""
    end_time: str
    r"""An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""
    limit: NotRequired[int]
    r"""The limit for how many objects will be in the response. Default and max for this value is 512 objects."""
    after: NotRequired[str]
    r"""If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results."""


class FetchRoutesRequest(BaseModel):
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

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 512
    r"""The limit for how many objects will be in the response. Default and max for this value is 512 objects."""

    after: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results."""


FetchRoutesResponseTypedDict = TypeAliasType(
    "FetchRoutesResponseTypedDict",
    Union[
        RoutesFetchRoutesResponseBodyTypedDict,
        RoutesFetchRoutesBadRequestErrorResponseBodyTypedDict,
    ],
)


FetchRoutesResponse = TypeAliasType(
    "FetchRoutesResponse",
    Union[RoutesFetchRoutesResponseBody, RoutesFetchRoutesBadRequestErrorResponseBody],
)
