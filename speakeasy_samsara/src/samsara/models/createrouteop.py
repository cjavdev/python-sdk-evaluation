"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .routescreateroutebadrequesterrorresponsebody import (
    RoutesCreateRouteBadRequestErrorResponseBody,
    RoutesCreateRouteBadRequestErrorResponseBodyTypedDict,
)
from .routescreaterouteresponsebody import (
    RoutesCreateRouteResponseBody,
    RoutesCreateRouteResponseBodyTypedDict,
)
from typing import Union
from typing_extensions import TypeAliasType


CreateRouteResponseTypedDict = TypeAliasType(
    "CreateRouteResponseTypedDict",
    Union[
        RoutesCreateRouteResponseBodyTypedDict,
        RoutesCreateRouteBadRequestErrorResponseBodyTypedDict,
    ],
)


CreateRouteResponse = TypeAliasType(
    "CreateRouteResponse",
    Union[RoutesCreateRouteResponseBody, RoutesCreateRouteBadRequestErrorResponseBody],
)
