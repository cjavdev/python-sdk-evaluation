"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .routespatchroutebadrequesterrorresponsebody import (
    RoutesPatchRouteBadRequestErrorResponseBody,
    RoutesPatchRouteBadRequestErrorResponseBodyTypedDict,
)
from .routespatchrouterequestbody import (
    RoutesPatchRouteRequestBody,
    RoutesPatchRouteRequestBodyTypedDict,
)
from .routespatchrouteresponsebody import (
    RoutesPatchRouteResponseBody,
    RoutesPatchRouteResponseBodyTypedDict,
)
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


class PatchRouteRequestTypedDict(TypedDict):
    id: str
    r"""ID of the route. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`"""
    routes_patch_route_request_body: RoutesPatchRouteRequestBodyTypedDict


class PatchRouteRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the route. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`"""

    routes_patch_route_request_body: Annotated[
        RoutesPatchRouteRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


PatchRouteResponseTypedDict = TypeAliasType(
    "PatchRouteResponseTypedDict",
    Union[
        RoutesPatchRouteResponseBodyTypedDict,
        RoutesPatchRouteBadRequestErrorResponseBodyTypedDict,
    ],
)


PatchRouteResponse = TypeAliasType(
    "PatchRouteResponse",
    Union[RoutesPatchRouteResponseBody, RoutesPatchRouteBadRequestErrorResponseBody],
)
