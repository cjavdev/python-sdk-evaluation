"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v1tripresponse_endaddress import (
    V1TripResponseEndAddress,
    V1TripResponseEndAddressTypedDict,
)
from .v1tripresponse_endcoordinates import (
    V1TripResponseEndCoordinates,
    V1TripResponseEndCoordinatesTypedDict,
)
from .v1tripresponse_startaddress import (
    V1TripResponseStartAddress,
    V1TripResponseStartAddressTypedDict,
)
from .v1tripresponse_startcoordinates import (
    V1TripResponseStartCoordinates,
    V1TripResponseStartCoordinatesTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V1TripResponseTripsTypedDict(TypedDict):
    asset_ids: NotRequired[List[int]]
    r"""List of associated asset IDs"""
    codriver_ids: NotRequired[List[int]]
    r"""List of codriver IDs"""
    distance_meters: NotRequired[int]
    r"""Length of the trip in meters. This value is calculated from the GPS data collected by the Samsara Vehicle Gateway."""
    driver_id: NotRequired[int]
    r"""ID of the driver."""
    end_address: NotRequired[V1TripResponseEndAddressTypedDict]
    r"""Text representation of nearest identifiable location to the end (latitude, longitude) coordinates."""
    end_coordinates: NotRequired[V1TripResponseEndCoordinatesTypedDict]
    r"""End (latitude, longitude) in decimal degrees."""
    end_location: NotRequired[str]
    r"""Geocoded street address of start (latitude, longitude) coordinates."""
    end_ms: NotRequired[int]
    r"""End of the trip in UNIX milliseconds. Ongoing trips are indicated by an endMs value of 9223372036854775807."""
    end_odometer: NotRequired[int]
    r"""Odometer reading (in meters) at the end of the trip. This is read from the vehicle's on-board diagnostics. If Samsara cannot read the vehicle's odometer values from on-board diagnostics, this value will be 0."""
    fuel_consumed_ml: NotRequired[int]
    r"""Amount in milliliters of fuel consumed on this trip."""
    start_address: NotRequired[V1TripResponseStartAddressTypedDict]
    r"""Text representation of nearest identifiable location to the start (latitude, longitude) coordinates."""
    start_coordinates: NotRequired[V1TripResponseStartCoordinatesTypedDict]
    r"""Start (latitude, longitude) in decimal degrees."""
    start_location: NotRequired[str]
    r"""Geocoded street address of start (latitude, longitude) coordinates."""
    start_ms: NotRequired[int]
    r"""Beginning of the trip in UNIX milliseconds."""
    start_odometer: NotRequired[int]
    r"""Odometer reading (in meters) at the beginning of the trip. This is read from the vehicle's on-board diagnostics. If Samsara cannot read the vehicle's odometer values from on-board diagnostics, this value will be 0."""
    toll_meters: NotRequired[int]
    r"""Length in meters trip spent on toll roads."""


class V1TripResponseTrips(BaseModel):
    asset_ids: Annotated[Optional[List[int]], pydantic.Field(alias="assetIds")] = None
    r"""List of associated asset IDs"""

    codriver_ids: Annotated[
        Optional[List[int]], pydantic.Field(alias="codriverIds")
    ] = None
    r"""List of codriver IDs"""

    distance_meters: Annotated[
        Optional[int], pydantic.Field(alias="distanceMeters")
    ] = None
    r"""Length of the trip in meters. This value is calculated from the GPS data collected by the Samsara Vehicle Gateway."""

    driver_id: Annotated[Optional[int], pydantic.Field(alias="driverId")] = None
    r"""ID of the driver."""

    end_address: Annotated[
        Optional[V1TripResponseEndAddress], pydantic.Field(alias="endAddress")
    ] = None
    r"""Text representation of nearest identifiable location to the end (latitude, longitude) coordinates."""

    end_coordinates: Annotated[
        Optional[V1TripResponseEndCoordinates], pydantic.Field(alias="endCoordinates")
    ] = None
    r"""End (latitude, longitude) in decimal degrees."""

    end_location: Annotated[Optional[str], pydantic.Field(alias="endLocation")] = None
    r"""Geocoded street address of start (latitude, longitude) coordinates."""

    end_ms: Annotated[Optional[int], pydantic.Field(alias="endMs")] = None
    r"""End of the trip in UNIX milliseconds. Ongoing trips are indicated by an endMs value of 9223372036854775807."""

    end_odometer: Annotated[Optional[int], pydantic.Field(alias="endOdometer")] = None
    r"""Odometer reading (in meters) at the end of the trip. This is read from the vehicle's on-board diagnostics. If Samsara cannot read the vehicle's odometer values from on-board diagnostics, this value will be 0."""

    fuel_consumed_ml: Annotated[
        Optional[int], pydantic.Field(alias="fuelConsumedMl")
    ] = None
    r"""Amount in milliliters of fuel consumed on this trip."""

    start_address: Annotated[
        Optional[V1TripResponseStartAddress], pydantic.Field(alias="startAddress")
    ] = None
    r"""Text representation of nearest identifiable location to the start (latitude, longitude) coordinates."""

    start_coordinates: Annotated[
        Optional[V1TripResponseStartCoordinates],
        pydantic.Field(alias="startCoordinates"),
    ] = None
    r"""Start (latitude, longitude) in decimal degrees."""

    start_location: Annotated[Optional[str], pydantic.Field(alias="startLocation")] = (
        None
    )
    r"""Geocoded street address of start (latitude, longitude) coordinates."""

    start_ms: Annotated[Optional[int], pydantic.Field(alias="startMs")] = None
    r"""Beginning of the trip in UNIX milliseconds."""

    start_odometer: Annotated[Optional[int], pydantic.Field(alias="startOdometer")] = (
        None
    )
    r"""Odometer reading (in meters) at the beginning of the trip. This is read from the vehicle's on-board diagnostics. If Samsara cannot read the vehicle's odometer values from on-board diagnostics, this value will be 0."""

    toll_meters: Annotated[Optional[int], pydantic.Field(alias="tollMeters")] = None
    r"""Length in meters trip spent on toll roads."""
