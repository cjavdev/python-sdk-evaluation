# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["EngineImmobilizerGetEngineImmobilizerStatesResponseBody", "Data", "DataRelayState", "Pagination"]


class DataRelayState(BaseModel):
    id: Literal["relay1", "relay2"]
    """The ID of the relay Valid values: `relay1`, `relay2`"""

    is_open: bool = FieldInfo(alias="isOpen")
    """Whether the relay is open."""


class Data(BaseModel):
    happened_at_time: str = FieldInfo(alias="happenedAtTime")
    """A UTC time in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    is_connected_to_vehicle: bool = FieldInfo(alias="isConnectedToVehicle")
    """Whether the engine immobilizer is connected the vehicle."""

    relay_states: List[DataRelayState] = FieldInfo(alias="relayStates")
    """A list of states for each relay"""

    vehicle_id: str = FieldInfo(alias="vehicleId")
    """The ID of the vehicle that the engine immobilizer is connected to."""


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


class EngineImmobilizerGetEngineImmobilizerStatesResponseBody(BaseModel):
    data: List[Data]
    """A list of engine immobilizer states in ascending order of happenedAtTime."""

    pagination: Pagination
    """Pagination parameters."""
