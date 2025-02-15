"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .minimalrouteauditlogsresponsebody import (
    MinimalRouteAuditLogsResponseBody,
    MinimalRouteAuditLogsResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing_extensions import TypedDict


class RouteChangesResponseBodyTypedDict(TypedDict):
    r"""A diff of the changes for a route update."""

    after: MinimalRouteAuditLogsResponseBodyTypedDict
    r"""A single route. Only the fields that have changed are present in the response. All other fields, including the route id, will not be present in the response. For now, only routeStops are included since only Route Tracking updates are supported."""
    before: MinimalRouteAuditLogsResponseBodyTypedDict
    r"""A single route. Only the fields that have changed are present in the response. All other fields, including the route id, will not be present in the response. For now, only routeStops are included since only Route Tracking updates are supported."""


class RouteChangesResponseBody(BaseModel):
    r"""A diff of the changes for a route update."""

    after: MinimalRouteAuditLogsResponseBody
    r"""A single route. Only the fields that have changed are present in the response. All other fields, including the route id, will not be present in the response. For now, only routeStops are included since only Route Tracking updates are supported."""

    before: MinimalRouteAuditLogsResponseBody
    r"""A single route. Only the fields that have changed are present in the response. All other fields, including the route id, will not be present in the response. For now, only routeStops are included since only Route Tracking updates are supported."""
