"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customheadersobjectresponsebody import (
    CustomHeadersObjectResponseBody,
    CustomHeadersObjectResponseBodyTypedDict,
)
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class WebhooksPatchWebhookResponseBodyEventTypes(str, Enum):
    r"""This is the name of the event type.  Valid values: `AddressCreated`, `AddressDeleted`, `AddressUpdated`, `AlertIncident`, `AlertObjectEvent`, `DocumentSubmitted`, `DriverCreated`, `DriverUpdated`, `DvirSubmitted`, `EngineFaultOff`, `EngineFaultOn`, `FormSubmitted`, `GatewayUnplugged`, `GeofenceEntry`, `GeofenceExit`, `IssueCreated`, `PredictiveMaintenanceAlert`, `RouteStopArrival`, `RouteStopDeparture`, `RouteStopResequence`, `SevereSpeedingEnded`, `SevereSpeedingStarted`, `VehicleCreated`, `VehicleUpdated`"""

    ADDRESS_CREATED = "AddressCreated"
    ADDRESS_DELETED = "AddressDeleted"
    ADDRESS_UPDATED = "AddressUpdated"
    ALERT_INCIDENT = "AlertIncident"
    ALERT_OBJECT_EVENT = "AlertObjectEvent"
    DOCUMENT_SUBMITTED = "DocumentSubmitted"
    DRIVER_CREATED = "DriverCreated"
    DRIVER_UPDATED = "DriverUpdated"
    DVIR_SUBMITTED = "DvirSubmitted"
    ENGINE_FAULT_OFF = "EngineFaultOff"
    ENGINE_FAULT_ON = "EngineFaultOn"
    FORM_SUBMITTED = "FormSubmitted"
    GATEWAY_UNPLUGGED = "GatewayUnplugged"
    GEOFENCE_ENTRY = "GeofenceEntry"
    GEOFENCE_EXIT = "GeofenceExit"
    ISSUE_CREATED = "IssueCreated"
    PREDICTIVE_MAINTENANCE_ALERT = "PredictiveMaintenanceAlert"
    ROUTE_STOP_ARRIVAL = "RouteStopArrival"
    ROUTE_STOP_DEPARTURE = "RouteStopDeparture"
    ROUTE_STOP_RESEQUENCE = "RouteStopResequence"
    SEVERE_SPEEDING_ENDED = "SevereSpeedingEnded"
    SEVERE_SPEEDING_STARTED = "SevereSpeedingStarted"
    VEHICLE_CREATED = "VehicleCreated"
    VEHICLE_UPDATED = "VehicleUpdated"


class WebhooksPatchWebhookResponseBodyVersion(str, Enum):
    r"""The version of the webhook.  Valid values: `2018-01-01`, `2021-06-09`"""

    TWO_THOUSAND_AND_EIGHTEEN_01_01 = "2018-01-01"
    TWO_THOUSAND_AND_TWENTY_ONE_06_09 = "2021-06-09"


class WebhooksPatchWebhookResponseBodyTypedDict(TypedDict):
    id: str
    r"""The ID of the webhook. This will appear in both Samsara’s cloud dashboard and the API. This is the id of the webhook. This is system generated."""
    name: str
    r"""The name of the webhook. This will appear in both Samsara’s cloud dashboard and the API. It can be set or updated through the Samsara Dashboard or through the API at any time."""
    secret_key: str
    r"""The secret key of the webhook. This will appear in both Samsara’s cloud dashboard and the API."""
    url: str
    r"""The url of the webhook. This will appear in both Samsara’s cloud dashboard and the API. It can be set or updated through the Samsara Dashboard or through the API at any time."""
    version: WebhooksPatchWebhookResponseBodyVersion
    r"""The version of the webhook.  Valid values: `2018-01-01`, `2021-06-09`"""
    custom_headers: NotRequired[List[CustomHeadersObjectResponseBodyTypedDict]]
    r"""The list of custom headers that users can include with their request"""
    event_types: NotRequired[List[WebhooksPatchWebhookResponseBodyEventTypes]]
    r"""The list of event types associated with a particular webhook."""


class WebhooksPatchWebhookResponseBody(BaseModel):
    id: str
    r"""The ID of the webhook. This will appear in both Samsara’s cloud dashboard and the API. This is the id of the webhook. This is system generated."""

    name: str
    r"""The name of the webhook. This will appear in both Samsara’s cloud dashboard and the API. It can be set or updated through the Samsara Dashboard or through the API at any time."""

    secret_key: Annotated[str, pydantic.Field(alias="secretKey")]
    r"""The secret key of the webhook. This will appear in both Samsara’s cloud dashboard and the API."""

    url: str
    r"""The url of the webhook. This will appear in both Samsara’s cloud dashboard and the API. It can be set or updated through the Samsara Dashboard or through the API at any time."""

    version: WebhooksPatchWebhookResponseBodyVersion
    r"""The version of the webhook.  Valid values: `2018-01-01`, `2021-06-09`"""

    custom_headers: Annotated[
        Optional[List[CustomHeadersObjectResponseBody]],
        pydantic.Field(alias="customHeaders"),
    ] = None
    r"""The list of custom headers that users can include with their request"""

    event_types: Annotated[
        Optional[List[WebhooksPatchWebhookResponseBodyEventTypes]],
        pydantic.Field(alias="eventTypes"),
    ] = None
    r"""The list of event types associated with a particular webhook."""
