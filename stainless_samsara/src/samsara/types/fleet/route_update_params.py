# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RouteUpdateParams", "Settings", "Stop", "StopSingleUseLocation"]


class RouteUpdateParams(TypedDict, total=False):
    driver_id: Annotated[str, PropertyInfo(alias="driverId")]
    """ID of the driver.

    Can be either a unique Samsara ID or an
    [external ID](https://developers.samsara.com/docs/external-ids) for the driver.
    """

    external_ids: Annotated[Dict[str, str], PropertyInfo(alias="externalIds")]
    """A map of external ids"""

    name: str
    """Name for the route"""

    notes: str
    """Notes about the route."""

    settings: Settings
    """
    An optional dictionary, only necessary to override the defaults for route start
    and end conditions.
    """

    stops: Iterable[Stop]
    """List of stops along the route.

    If a valid `id` of a stop is provided, that stop will be updated. If no `id` is
    provided for a passed in stop, that stop will be created. If `id` value are
    passed in for some stops and not for others, those with `id` value specified
    will be retained and updated in the original route, those without `id` value
    specified in the body will be created, and those without `id` value specified
    that already existed on the route will be deleted. For each new stop, exactly
    one of `addressId` and `singleUseLocation` are required. Depending on the
    `settings` on your route, either a `scheduledArrivalTime` or
    `scheduledDepartureTime` must be specified for the first job, if a new first job
    is being added.
    """

    vehicle_id: Annotated[str, PropertyInfo(alias="vehicleId")]
    """ID of the vehicle.

    Can be either a unique Samsara ID or an
    [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.
    """


class Settings(TypedDict, total=False):
    route_completion_condition: Annotated[
        Literal["arriveLastStop", "departLastStop"], PropertyInfo(alias="routeCompletionCondition")
    ]
    """
    Defaults to 'arriveLastStop' which ends the route upon arriving at the final
    stop. The condition 'departLastStop' ends the route upon departing the last
    stop. If 'arriveLastStop' is set, then the departure time of the final stop
    should not be set. Valid values: `arriveLastStop`, `departLastStop`
    """

    route_starting_condition: Annotated[
        Literal["departFirstStop", "arriveFirstStop"], PropertyInfo(alias="routeStartingCondition")
    ]
    """
    Defaults to 'departFirstStop' which starts the route upon departing the first
    stop in the route. The condition 'arriveFirstStop' starts the route upon
    arriving at the first stop in the route. If 'departFirstStop' is set, the
    arrival time of the first stop should not be set. Valid values:
    `departFirstStop`, `arriveFirstStop`
    """


class StopSingleUseLocation(TypedDict, total=False):
    latitude: Required[float]
    """The latitude of the location"""

    longitude: Required[float]
    """The longitude of the location"""

    address: str
    """Address of the stop."""


class Stop(TypedDict, total=False):
    id: str
    """ID of the stop"""

    address_id: Annotated[str, PropertyInfo(alias="addressId")]
    """ID of the address.

    An address
    [externalId](https://developers.samsara.com/docs/external-ids#using-external-ids)
    can also be used interchangeably here.
    """

    external_ids: Annotated[Dict[str, str], PropertyInfo(alias="externalIds")]
    """A map of external ids"""

    name: str
    """Name of the stop"""

    notes: str
    """Notes for the stop"""

    ontime_window_after_arrival_ms: Annotated[int, PropertyInfo(alias="ontimeWindowAfterArrivalMs")]
    """
    Specifies the time window (in milliseconds) after a stop's scheduled arrival
    time during which the stop is considered 'on-time'.
    """

    ontime_window_before_arrival_ms: Annotated[int, PropertyInfo(alias="ontimeWindowBeforeArrivalMs")]
    """
    Specifies the time window (in milliseconds) before a stop's scheduled arrival
    time during which the stop is considered 'on-time'.
    """

    scheduled_arrival_time: Annotated[
        Union[str, datetime], PropertyInfo(alias="scheduledArrivalTime", format="iso8601")
    ]
    """
    This is a required field for all stops EXCEPT the start and end, based on route
    start and stop settings selected.
    """

    scheduled_departure_time: Annotated[
        Union[str, datetime], PropertyInfo(alias="scheduledDepartureTime", format="iso8601")
    ]
    """
    This is a required field for all stops EXCEPT the start and end, based on route
    start and stop settings selected.
    """

    single_use_location: Annotated[StopSingleUseLocation, PropertyInfo(alias="singleUseLocation")]
    """
    This field is used to indicate stops along the route for which an address has
    not been persisted. This field is mutually exclusive with addressId.
    """
