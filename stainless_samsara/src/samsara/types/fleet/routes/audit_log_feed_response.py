# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "AuditLogFeedResponse",
    "Data",
    "DataChanges",
    "DataChangesAfter",
    "DataChangesAfterStop",
    "DataChangesBefore",
    "DataChangesBeforeStop",
    "DataRoute",
    "DataRouteDriver",
    "DataRouteRecurringRouteLiveSharingLink",
    "DataRouteSettings",
    "DataRouteStop",
    "DataRouteStopAddress",
    "DataRouteStopDocument",
    "DataRouteStopLocationLiveSharingLink",
    "DataRouteStopSingleUseLocation",
    "DataRouteVehicle",
    "Pagination",
]


class DataChangesAfterStop(BaseModel):
    id: str
    """Unique identifier for the route stop."""

    actual_arrival_time: Optional[datetime] = FieldInfo(alias="actualArrivalTime", default=None)
    """Actual arrival time, if it exists, for the route stop in RFC 3339 format."""

    actual_departure_time: Optional[datetime] = FieldInfo(alias="actualDepartureTime", default=None)
    """Actual departure time, if it exists, for the route stop in RFC 3339 format."""

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

    scheduled_arrival_time: Optional[datetime] = FieldInfo(alias="scheduledArrivalTime", default=None)
    """Scheduled arrival time, if it exists, for the stop in RFC 3339 format.

    If it does not exist, and this field was changed in the update, it will be an
    empty string.
    """

    scheduled_departure_time: Optional[datetime] = FieldInfo(alias="scheduledDepartureTime", default=None)
    """Scheduled departure time, if it exists, for the stop in RFC 3339 format.

    If it does not exist, and this field was changed in the update, it will be an
    empty string.
    """

    skipped_time: Optional[datetime] = FieldInfo(alias="skippedTime", default=None)
    """Skipped time, if it exists, for the route stop in RFC 3339 format."""

    state: Optional[Literal["unassigned", "scheduled", "en route", "skipped", "arrived", "departed"]] = None
    """The current state of the route stop.

    Valid values: `unassigned`, `scheduled`, `en route`, `skipped`, `arrived`,
    `departed`
    """


class DataChangesAfter(BaseModel):
    stops: Optional[List[DataChangesAfterStop]] = None
    """The route stops in the route.

    Only stops that have been updated will be included in the response.
    """


class DataChangesBeforeStop(BaseModel):
    id: str
    """Unique identifier for the route stop."""

    actual_arrival_time: Optional[datetime] = FieldInfo(alias="actualArrivalTime", default=None)
    """Actual arrival time, if it exists, for the route stop in RFC 3339 format."""

    actual_departure_time: Optional[datetime] = FieldInfo(alias="actualDepartureTime", default=None)
    """Actual departure time, if it exists, for the route stop in RFC 3339 format."""

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

    scheduled_arrival_time: Optional[datetime] = FieldInfo(alias="scheduledArrivalTime", default=None)
    """Scheduled arrival time, if it exists, for the stop in RFC 3339 format.

    If it does not exist, and this field was changed in the update, it will be an
    empty string.
    """

    scheduled_departure_time: Optional[datetime] = FieldInfo(alias="scheduledDepartureTime", default=None)
    """Scheduled departure time, if it exists, for the stop in RFC 3339 format.

    If it does not exist, and this field was changed in the update, it will be an
    empty string.
    """

    skipped_time: Optional[datetime] = FieldInfo(alias="skippedTime", default=None)
    """Skipped time, if it exists, for the route stop in RFC 3339 format."""

    state: Optional[Literal["unassigned", "scheduled", "en route", "skipped", "arrived", "departed"]] = None
    """The current state of the route stop.

    Valid values: `unassigned`, `scheduled`, `en route`, `skipped`, `arrived`,
    `departed`
    """


class DataChangesBefore(BaseModel):
    stops: Optional[List[DataChangesBeforeStop]] = None
    """The route stops in the route.

    Only stops that have been updated will be included in the response.
    """


class DataChanges(BaseModel):
    after: DataChangesAfter
    """A single route.

    Only the fields that have changed are present in the response. All other fields,
    including the route id, will not be present in the response. For now, only
    routeStops are included since only Route Tracking updates are supported.
    """

    before: DataChangesBefore
    """A single route.

    Only the fields that have changed are present in the response. All other fields,
    including the route id, will not be present in the response. For now, only
    routeStops are included since only Route Tracking updates are supported.
    """


class DataRouteDriver(BaseModel):
    id: str
    """ID of the driver"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the driver"""


class DataRouteRecurringRouteLiveSharingLink(BaseModel):
    live_sharing_url: str = FieldInfo(alias="liveSharingUrl")
    """The shareable URL of the vehicle's location."""

    name: str
    """Name of the Live Sharing Link."""

    expires_at_time: Optional[str] = FieldInfo(alias="expiresAtTime", default=None)
    """Date that this link expires, in RFC 3339 format."""


class DataRouteSettings(BaseModel):
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


class DataRouteStopAddress(BaseModel):
    id: str
    """Id of the address"""

    name: str
    """Name of the address"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""


class DataRouteStopDocument(BaseModel):
    id: str
    """Id of the document"""

    name: Optional[str] = None
    """Name of the document"""


class DataRouteStopLocationLiveSharingLink(BaseModel):
    live_sharing_url: str = FieldInfo(alias="liveSharingUrl")
    """The shareable URL of the vehicle's location."""

    name: str
    """Name of the Live Sharing Link."""

    expires_at_time: Optional[str] = FieldInfo(alias="expiresAtTime", default=None)
    """Date that this link expires, in RFC 3339 format."""


class DataRouteStopSingleUseLocation(BaseModel):
    latitude: float
    """The latitude of the location"""

    longitude: float
    """The longitude of the location"""

    address: Optional[str] = None
    """Address of the stop."""


class DataRouteStop(BaseModel):
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

    address: Optional[DataRouteStopAddress] = None
    """A minified Address object"""

    documents: Optional[List[DataRouteStopDocument]] = None
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

    location_live_sharing_links: Optional[List[DataRouteStopLocationLiveSharingLink]] = FieldInfo(
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

    single_use_location: Optional[DataRouteStopSingleUseLocation] = FieldInfo(alias="singleUseLocation", default=None)
    """
    This field is used to indicate stops along the route for which an address has
    not been persisted. This field is mutually exclusive with addressId.
    """

    skipped_time: Optional[datetime] = FieldInfo(alias="skippedTime", default=None)
    """Skipped time, if it exists, for the route stop in RFC 3339 format."""


class DataRouteVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the vehicle"""


class DataRoute(BaseModel):
    id: str
    """ID of the route"""

    actual_route_end_time: Optional[datetime] = FieldInfo(alias="actualRouteEndTime", default=None)
    """Actual end time, if it exists, for the route in RFC 3339 format."""

    actual_route_start_time: Optional[datetime] = FieldInfo(alias="actualRouteStartTime", default=None)
    """Actual start time, if it exists, for the route in RFC 3339 format."""

    driver: Optional[DataRouteDriver] = None
    """A minified driver object.

    This object is only returned if the route is assigned to the driver.
    """

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Route name"""

    notes: Optional[str] = None
    """Notes for the route"""

    recurring_route_live_sharing_links: Optional[List[DataRouteRecurringRouteLiveSharingLink]] = FieldInfo(
        alias="recurringRouteLiveSharingLinks", default=None
    )
    """List of shareable, non-expired 'By recurring Route' Live Sharing Links."""

    scheduled_route_end_time: Optional[datetime] = FieldInfo(alias="scheduledRouteEndTime", default=None)
    """Scheduled end time, if it exists, for the route in RFC 3339 format."""

    scheduled_route_start_time: Optional[datetime] = FieldInfo(alias="scheduledRouteStartTime", default=None)
    """Scheduled start time, if it exists, for the route in RFC 3339 format."""

    settings: Optional[DataRouteSettings] = None
    """
    An optional dictionary, only necessary to override the defaults for route start
    and end conditions.
    """

    stops: Optional[List[DataRouteStop]] = None
    """List of stops along the route"""

    vehicle: Optional[DataRouteVehicle] = None
    """A minified vehicle object.

    This object is only returned if the route is assigned to the vehicle.
    """


class Data(BaseModel):
    changes: DataChanges
    """A diff of the changes for a route update."""

    route: DataRoute

    source: Literal["automatic", "driver", "admin"]
    """The source of this route update.

    Updates that are triggered by time or by the route being completed are
    'automatic'. Valid values: `automatic`, `driver`, `admin`
    """

    time: datetime
    """The timestamp of the route in RFC 3339 format."""

    type: Literal["route tracking"]
    """The type of route update.

    The route tracking updates occur as a route is completed and stops transition
    from one state to another. Currently only Route Tracking updates are supported,
    but this will change in the future when additional types are added. Valid
    values: `route tracking`
    """

    operation: Optional[
        Literal[
            "stop scheduled",
            "stop en route",
            "stop skipped",
            "stop arrived",
            "stop departed",
            "stop ETA updated",
            "stop arrival time updated",
            "stop completion time updated",
            "stop order changed",
            "stop arrival prevented",
        ]
    ] = None
    """The operation that was performed as part of this route update.

    Valid values: `stop scheduled`, `stop en route`, `stop skipped`, `stop arrived`,
    `stop departed`, `stop ETA updated`, `stop arrival time updated`,
    `stop completion time updated`, `stop order changed`, `stop arrival prevented`
    """


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


class AuditLogFeedResponse(BaseModel):
    data: List[Data]
    """Route feed response."""

    pagination: Pagination
    """Pagination parameters."""
