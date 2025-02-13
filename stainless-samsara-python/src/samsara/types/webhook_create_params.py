# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebhookCreateParams", "CustomHeader"]


class WebhookCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the webhook.

    This will appear in both Samsara’s cloud dashboard and the API. It can be set or
    updated through the Samsara Dashboard or through the API at any time.
    """

    url: Required[str]
    """The url of the webhook.

    This will appear in both Samsara’s cloud dashboard and the API. It can be set or
    updated through the Samsara Dashboard or through the API at any time.
    """

    custom_headers: Annotated[Iterable[CustomHeader], PropertyInfo(alias="customHeaders")]
    """The list of custom headers that users can include with their request"""

    event_types: Annotated[
        List[
            Literal[
                "AddressCreated",
                "AddressDeleted",
                "AddressUpdated",
                "AlertIncident",
                "AlertObjectEvent",
                "DocumentSubmitted",
                "DriverCreated",
                "DriverUpdated",
                "DvirSubmitted",
                "EngineFaultOff",
                "EngineFaultOn",
                "FormSubmitted",
                "GatewayUnplugged",
                "GeofenceEntry",
                "GeofenceExit",
                "IssueCreated",
                "PredictiveMaintenanceAlert",
                "RouteStopArrival",
                "RouteStopDeparture",
                "RouteStopResequence",
                "SevereSpeedingEnded",
                "SevereSpeedingStarted",
                "VehicleCreated",
                "VehicleUpdated",
            ]
        ],
        PropertyInfo(alias="eventTypes"),
    ]
    """[beta] The list of event types associated with a particular event type"""

    version: Literal["2018-01-01", "2021-06-09", "2022-09-13", "2024-02-27"]
    """The version of the webhook.

    Valid values: `2018-01-01`, `2021-06-09`, `2022-09-13`, `2024-02-27`
    """


class CustomHeader(TypedDict, total=False):
    key: Required[str]
    """The alphanumeric key of the custom header."""

    value: Required[str]
    """The value of the custom header.

    The default maximum length of the value is 100 characters.
    """
