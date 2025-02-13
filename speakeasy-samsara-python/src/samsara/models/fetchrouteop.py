"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .routesfetchroutebadrequesterrorresponsebody import (
    RoutesFetchRouteBadRequestErrorResponseBody,
    RoutesFetchRouteBadRequestErrorResponseBodyTypedDict,
)
from .routesfetchrouteresponsebody import (
    RoutesFetchRouteResponseBody,
    RoutesFetchRouteResponseBodyTypedDict,
)
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, PathParamMetadata
from typing import Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


class FetchRouteRequestTypedDict(TypedDict):
    id: str
    r"""ID of the route. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`"""


class FetchRouteRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the route. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`"""


FetchRouteResponseTypedDict = TypeAliasType(
    "FetchRouteResponseTypedDict",
    Union[
        RoutesFetchRouteResponseBodyTypedDict,
        RoutesFetchRouteBadRequestErrorResponseBodyTypedDict,
    ],
)


FetchRouteResponse = TypeAliasType(
    "FetchRouteResponse",
    Union[RoutesFetchRouteResponseBody, RoutesFetchRouteBadRequestErrorResponseBody],
)
