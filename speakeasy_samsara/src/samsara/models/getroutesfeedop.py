"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .routesgetroutesfeedbadrequesterrorresponsebody import (
    RoutesGetRoutesFeedBadRequestErrorResponseBody,
    RoutesGetRoutesFeedBadRequestErrorResponseBodyTypedDict,
)
from .routesgetroutesfeedresponsebody import (
    RoutesGetRoutesFeedResponseBody,
    RoutesGetRoutesFeedResponseBodyTypedDict,
)
from enum import Enum
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, QueryParamMetadata
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class QueryParamExpand(str, Enum):
    r"""Expands the specified value(s) in the response object. Expansion populates additional fields in an object, if supported. Unsupported fields are ignored. To expand multiple fields, input a comma-separated list.

    Valid value: `route`  Valid values: `route`
    """

    ROUTE = "route"


class GetRoutesFeedRequestTypedDict(TypedDict):
    after: NotRequired[str]
    r"""If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results."""
    expand: NotRequired[QueryParamExpand]
    r"""Expands the specified value(s) in the response object. Expansion populates additional fields in an object, if supported. Unsupported fields are ignored. To expand multiple fields, input a comma-separated list.

    Valid value: `route`  Valid values: `route`
    """


class GetRoutesFeedRequest(BaseModel):
    after: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results."""

    expand: Annotated[
        Optional[QueryParamExpand],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Expands the specified value(s) in the response object. Expansion populates additional fields in an object, if supported. Unsupported fields are ignored. To expand multiple fields, input a comma-separated list.

    Valid value: `route`  Valid values: `route`
    """


GetRoutesFeedResponseTypedDict = TypeAliasType(
    "GetRoutesFeedResponseTypedDict",
    Union[
        RoutesGetRoutesFeedResponseBodyTypedDict,
        RoutesGetRoutesFeedBadRequestErrorResponseBodyTypedDict,
    ],
)


GetRoutesFeedResponse = TypeAliasType(
    "GetRoutesFeedResponse",
    Union[
        RoutesGetRoutesFeedResponseBody, RoutesGetRoutesFeedBadRequestErrorResponseBody
    ],
)
