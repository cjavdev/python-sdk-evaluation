"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .goadrivertinyresponseresponsebody import (
    GoaDriverTinyResponseResponseBody,
    GoaDriverTinyResponseResponseBodyTypedDict,
)
from .minimalroutestopresponsebody import (
    MinimalRouteStopResponseBody,
    MinimalRouteStopResponseBodyTypedDict,
)
from .vehiclewithgatewaytinyresponseresponsebody import (
    VehicleWithGatewayTinyResponseResponseBody,
    VehicleWithGatewayTinyResponseResponseBodyTypedDict,
)
from .webhookrouteresponseobjectresponsebody import (
    WebhookRouteResponseObjectResponseBody,
    WebhookRouteResponseObjectResponseBodyTypedDict,
)
from datetime import datetime
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class RouteStopDetailsObjectResponseBodyOperation(str, Enum):
    r"""The operation that was performed as part of this route update.  Valid values: `stop arrived`, `stop departed`"""

    STOP_ARRIVED = "stop arrived"
    STOP_DEPARTED = "stop departed"


class RouteStopDetailsObjectResponseBodyType(str, Enum):
    r"""The type of route update. The route tracking updates occur as a route is completed and stops transition from one state to another. Currently only Route Tracking updates are supported, but this will change in the future when additional types are added.  Valid values: `route tracking`"""

    ROUTE_TRACKING = "route tracking"


class RouteStopDetailsObjectResponseBodyTypedDict(TypedDict):
    route: WebhookRouteResponseObjectResponseBodyTypedDict
    route_stop_details: MinimalRouteStopResponseBodyTypedDict
    r"""A single route stop for a route."""
    time: datetime
    r"""The timestamp of the route in RFC 3339 format."""
    type: RouteStopDetailsObjectResponseBodyType
    r"""The type of route update. The route tracking updates occur as a route is completed and stops transition from one state to another. Currently only Route Tracking updates are supported, but this will change in the future when additional types are added.  Valid values: `route tracking`"""
    driver: NotRequired[GoaDriverTinyResponseResponseBodyTypedDict]
    r"""A minified driver object. This object is only returned if the route is assigned to the driver."""
    operation: NotRequired[RouteStopDetailsObjectResponseBodyOperation]
    r"""The operation that was performed as part of this route update.  Valid values: `stop arrived`, `stop departed`"""
    vehicle: NotRequired[VehicleWithGatewayTinyResponseResponseBodyTypedDict]
    r"""A minified vehicle object. This object is only returned if the route is assigned to the vehicle."""


class RouteStopDetailsObjectResponseBody(BaseModel):
    route: WebhookRouteResponseObjectResponseBody

    route_stop_details: Annotated[
        MinimalRouteStopResponseBody, pydantic.Field(alias="routeStopDetails")
    ]
    r"""A single route stop for a route."""

    time: datetime
    r"""The timestamp of the route in RFC 3339 format."""

    type: RouteStopDetailsObjectResponseBodyType
    r"""The type of route update. The route tracking updates occur as a route is completed and stops transition from one state to another. Currently only Route Tracking updates are supported, but this will change in the future when additional types are added.  Valid values: `route tracking`"""

    driver: Optional[GoaDriverTinyResponseResponseBody] = None
    r"""A minified driver object. This object is only returned if the route is assigned to the driver."""

    operation: Optional[RouteStopDetailsObjectResponseBodyOperation] = None
    r"""The operation that was performed as part of this route update.  Valid values: `stop arrived`, `stop departed`"""

    vehicle: Optional[VehicleWithGatewayTinyResponseResponseBody] = None
    r"""A minified vehicle object. This object is only returned if the route is assigned to the vehicle."""
