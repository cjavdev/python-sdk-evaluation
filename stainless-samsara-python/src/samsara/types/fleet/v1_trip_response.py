# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1TripResponse", "Trip", "TripEndAddress", "TripEndCoordinates", "TripStartAddress", "TripStartCoordinates"]


class TripEndAddress(BaseModel):
    id: Optional[float] = None
    """The ID of the address"""

    address: Optional[str] = None
    """The formatted address"""

    name: Optional[str] = None
    """The name of the address"""


class TripEndCoordinates(BaseModel):
    latitude: Optional[float] = None

    longitude: Optional[float] = None


class TripStartAddress(BaseModel):
    id: Optional[float] = None
    """The ID of the address"""

    address: Optional[str] = None
    """The formatted address"""

    name: Optional[str] = None
    """The name of the address"""


class TripStartCoordinates(BaseModel):
    latitude: Optional[float] = None

    longitude: Optional[float] = None


class Trip(BaseModel):
    asset_ids: Optional[List[int]] = FieldInfo(alias="assetIds", default=None)
    """List of associated asset IDs"""

    codriver_ids: Optional[List[int]] = FieldInfo(alias="codriverIds", default=None)
    """List of codriver IDs"""

    distance_meters: Optional[int] = FieldInfo(alias="distanceMeters", default=None)
    """Length of the trip in meters.

    This value is calculated from the GPS data collected by the Samsara Vehicle
    Gateway.
    """

    driver_id: Optional[int] = FieldInfo(alias="driverId", default=None)
    """ID of the driver."""

    end_address: Optional[TripEndAddress] = FieldInfo(alias="endAddress", default=None)
    """
    Text representation of nearest identifiable location to the end (latitude,
    longitude) coordinates.
    """

    end_coordinates: Optional[TripEndCoordinates] = FieldInfo(alias="endCoordinates", default=None)
    """End (latitude, longitude) in decimal degrees."""

    end_location: Optional[str] = FieldInfo(alias="endLocation", default=None)
    """Geocoded street address of start (latitude, longitude) coordinates."""

    end_ms: Optional[int] = FieldInfo(alias="endMs", default=None)
    """End of the trip in UNIX milliseconds.

    Ongoing trips are indicated by an endMs value of 9223372036854775807.
    """

    end_odometer: Optional[int] = FieldInfo(alias="endOdometer", default=None)
    """Odometer reading (in meters) at the end of the trip.

    This is read from the vehicle's on-board diagnostics. If Samsara cannot read the
    vehicle's odometer values from on-board diagnostics, this value will be 0.
    """

    fuel_consumed_ml: Optional[int] = FieldInfo(alias="fuelConsumedMl", default=None)
    """Amount in milliliters of fuel consumed on this trip."""

    start_address: Optional[TripStartAddress] = FieldInfo(alias="startAddress", default=None)
    """
    Text representation of nearest identifiable location to the start (latitude,
    longitude) coordinates.
    """

    start_coordinates: Optional[TripStartCoordinates] = FieldInfo(alias="startCoordinates", default=None)
    """Start (latitude, longitude) in decimal degrees."""

    start_location: Optional[str] = FieldInfo(alias="startLocation", default=None)
    """Geocoded street address of start (latitude, longitude) coordinates."""

    start_ms: Optional[int] = FieldInfo(alias="startMs", default=None)
    """Beginning of the trip in UNIX milliseconds."""

    start_odometer: Optional[int] = FieldInfo(alias="startOdometer", default=None)
    """Odometer reading (in meters) at the beginning of the trip.

    This is read from the vehicle's on-board diagnostics. If Samsara cannot read the
    vehicle's odometer values from on-board diagnostics, this value will be 0.
    """

    toll_meters: Optional[int] = FieldInfo(alias="tollMeters", default=None)
    """Length in meters trip spent on toll roads."""


class V1TripResponse(BaseModel):
    trips: Optional[List[Trip]] = None
