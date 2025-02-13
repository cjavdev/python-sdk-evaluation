# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebhookListResponse", "Data", "DataCustomHeader", "Pagination"]


class DataCustomHeader(BaseModel):
    key: str
    """The alphanumeric key of the custom header."""

    value: str
    """The value of the custom header.

    The default maximum length of the value is 100 characters.
    """


class Data(BaseModel):
    id: str
    """The ID of the webhook.

    This will appear in both Samsara’s cloud dashboard and the API. This is the id
    of the webhook. This is system generated.
    """

    name: str
    """The name of the webhook.

    This will appear in both Samsara’s cloud dashboard and the API. It can be set or
    updated through the Samsara Dashboard or through the API at any time.
    """

    secret_key: str = FieldInfo(alias="secretKey")
    """The secret key of the webhook.

    This will appear in both Samsara’s cloud dashboard and the API.
    """

    url: str
    """The url of the webhook.

    This will appear in both Samsara’s cloud dashboard and the API. It can be set or
    updated through the Samsara Dashboard or through the API at any time.
    """

    version: Literal["2018-01-01", "2021-06-09"]
    """The version of the webhook. Valid values: `2018-01-01`, `2021-06-09`"""

    custom_headers: Optional[List[DataCustomHeader]] = FieldInfo(alias="customHeaders", default=None)
    """The list of custom headers that users can include with their request"""

    event_types: Optional[
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
        ]
    ] = FieldInfo(alias="eventTypes", default=None)
    """The list of event types associated with a particular webhook."""


class Pagination(BaseModel):
    end_cursor: str = FieldInfo(alias="endCursor")
    """Cursor identifier representing the last element in the response.

    This value should be used in conjunction with a subsequent request's 'after'
    query parameter. This may be an empty string if there are no more pages left to
    view.
    """

    has_next_page: bool = FieldInfo(alias="hasNextPage")
    """
    True if there are more pages of results immediately available after this
    endCursor.
    """


class WebhookListResponse(BaseModel):
    data: List[Data]
    """This is a list of Webhooks."""

    pagination: Pagination
    """Pagination parameters."""
