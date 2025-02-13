# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "RouteCreateResponse",
    "Data",
    "DataDriver",
    "DataRecurringRouteLiveSharingLink",
    "DataSettings",
    "DataStop",
    "DataStopAddress",
    "DataStopDocument",
    "DataStopLocationLiveSharingLink",
    "DataStopSingleUseLocation",
    "DataVehicle",
]


class DataDriver(BaseModel):
    id: str
    """ID of the driver"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the driver"""


class DataRecurringRouteLiveSharingLink(BaseModel):
    live_sharing_url: str = FieldInfo(alias="liveSharingUrl")
    """The shareable URL of the vehicle's location."""

    name: str
    """Name of the Live Sharing Link."""

    expires_at_time: Optional[str] = FieldInfo(alias="expiresAtTime", default=None)
    """Date that this link expires, in RFC 3339 format."""


class DataSettings(BaseModel):
    route_completion_condition: Optional[Literal["arriveLastStop", "departLastStop"]] = FieldInfo(
        alias="routeCompletionCondition", default=None
    )
    """
    Defaults to 'arriveLastStop' which ends the route upon arriving at the final
    stop. The condition 'departLastStop' ends the route upon departing the last
    stop. If 'arriveLastStop' is set, then the departure time of the final stop
    should not be set. Valid values: `arriveLastStop`, `departLastStop`
    """

    route_starting_condition: Optional[Literal["departFirstStop", "arriveFirstStop"]] = FieldInfo(
        alias="routeStartingCondition", default=None
    )
    """
    Defaults to 'departFirstStop' which starts the route upon departing the first
    stop in the route. The condition 'arriveFirstStop' starts the route upon
    arriving at the first stop in the route. If 'departFirstStop' is set, the
    arrival time of the first stop should not be set. Valid values:
    `departFirstStop`, `arriveFirstStop`
    """


class DataStopAddress(BaseModel):
    id: str
    """Id of the address"""

    name: str
    """Name of the address"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""


class DataStopDocument(BaseModel):
    id: str
    """Id of the document"""

    name: Optional[str] = None
    """Name of the document"""


class DataStopLocationLiveSharingLink(BaseModel):
    live_sharing_url: str = FieldInfo(alias="liveSharingUrl")
    """The shareable URL of the vehicle's location."""

    name: str
    """Name of the Live Sharing Link."""

    expires_at_time: Optional[str] = FieldInfo(alias="expiresAtTime", default=None)
    """Date that this link expires, in RFC 3339 format."""


class DataStopSingleUseLocation(BaseModel):
    latitude: float
    """The latitude of the location"""

    longitude: float
    """The longitude of the location"""

    address: Optional[str] = None
    """Address of the stop."""


class DataStop(BaseModel):
    id: str
    """Id of the stop"""

    name: str
    """Name of the stop"""

    state: Literal["unassigned", "scheduled", "en route", "skipped", "arrived", "departed"]
    """The current state of the route stop.

    Valid values: `unassigned`, `scheduled`, `en route`, `skipped`, `arrived`,
    `departed`
    """

    actual_arrival_time: Optional[datetime] = FieldInfo(alias="actualArrivalTime", default=None)
    """Actual arrival time, if it exists, for the route stop in RFC 3339 format."""

    actual_departure_time: Optional[datetime] = FieldInfo(alias="actualDepartureTime", default=None)
    """Actual departure time, if it exists, for the route stop in RFC 3339 format."""

    address: Optional[DataStopAddress] = None
    """A minified Address object"""

    documents: Optional[List[DataStopDocument]] = None
    """List of documents associated with the stop."""

    en_route_time: Optional[datetime] = FieldInfo(alias="enRouteTime", default=None)
    """The time the stop became en-route, in RFC 3339 format."""

    eta: Optional[datetime] = None
    """
    Estimated time of arrival, if this stop is currently en-route, in RFC 3339
    format.
    """

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    live_sharing_url: Optional[str] = FieldInfo(alias="liveSharingUrl", default=None)
    """The shareable url of the stop's current status."""

    location_live_sharing_links: Optional[List[DataStopLocationLiveSharingLink]] = FieldInfo(
        alias="locationLiveSharingLinks", default=None
    )
    """List of shareable, non-expired 'By Location' Live Sharing Links."""

    notes: Optional[str] = None
    """Notes for the stop"""

    ontime_window_after_arrival_ms: Optional[int] = FieldInfo(alias="ontimeWindowAfterArrivalMs", default=None)
    """
    Specifies the time window (in milliseconds) after a stop's scheduled arrival
    time during which the stop is considered 'on-time'.
    """

    ontime_window_before_arrival_ms: Optional[int] = FieldInfo(alias="ontimeWindowBeforeArrivalMs", default=None)
    """
    Specifies the time window (in milliseconds) before a stop's scheduled arrival
    time during which the stop is considered 'on-time'.
    """

    scheduled_arrival_time: Optional[datetime] = FieldInfo(alias="scheduledArrivalTime", default=None)
    """Scheduled arrival time, if it exists, for the stop in RFC 3339 format."""

    scheduled_departure_time: Optional[datetime] = FieldInfo(alias="scheduledDepartureTime", default=None)
    """Scheduled departure time, if it exists, for the stop in RFC 3339 format."""

    single_use_location: Optional[DataStopSingleUseLocation] = FieldInfo(alias="singleUseLocation", default=None)
    """
    This field is used to indicate stops along the route for which an address has
    not been persisted. This field is mutually exclusive with addressId.
    """

    skipped_time: Optional[datetime] = FieldInfo(alias="skippedTime", default=None)
    """Skipped time, if it exists, for the route stop in RFC 3339 format."""


class DataVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the vehicle"""


class Data(BaseModel):
    id: str
    """ID of the route"""

    actual_route_end_time: Optional[datetime] = FieldInfo(alias="actualRouteEndTime", default=None)
    """Actual end time, if it exists, for the route in RFC 3339 format."""

    actual_route_start_time: Optional[datetime] = FieldInfo(alias="actualRouteStartTime", default=None)
    """Actual start time, if it exists, for the route in RFC 3339 format."""

    driver: Optional[DataDriver] = None
    """A minified driver object.

    This object is only returned if the route is assigned to the driver.
    """

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Route name"""

    notes: Optional[str] = None
    """Notes for the route"""

    recurring_route_live_sharing_links: Optional[List[DataRecurringRouteLiveSharingLink]] = FieldInfo(
        alias="recurringRouteLiveSharingLinks", default=None
    )
    """List of shareable, non-expired 'By recurring Route' Live Sharing Links."""

    scheduled_route_end_time: Optional[datetime] = FieldInfo(alias="scheduledRouteEndTime", default=None)
    """Scheduled end time, if it exists, for the route in RFC 3339 format."""

    scheduled_route_start_time: Optional[datetime] = FieldInfo(alias="scheduledRouteStartTime", default=None)
    """Scheduled start time, if it exists, for the route in RFC 3339 format."""

    settings: Optional[DataSettings] = None
    """
    An optional dictionary, only necessary to override the defaults for route start
    and end conditions.
    """

    stops: Optional[List[DataStop]] = None
    """List of stops along the route"""

    vehicle: Optional[DataVehicle] = None
    """A minified vehicle object.

    This object is only returned if the route is assigned to the vehicle.
    """


class RouteCreateResponse(BaseModel):
    data: Optional[Data] = None
