"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing import Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AssetsCreateAssetRequestBodyRegulationMode(str, Enum):
    r"""Whether or not the asset is regulated, unregulated (non-CMV), or a mixed use unregulated asset. Primarily used with vehicles.  Valid values: `mixed`, `regulated`, `unregulated`"""

    MIXED = "mixed"
    REGULATED = "regulated"
    UNREGULATED = "unregulated"


class AssetsCreateAssetRequestBodyType(str, Enum):
    r"""The operational context in which the asset interacts with the Samsara system. Examples: Vehicle (eg: truck, bus...), Trailer (eg: dry van, reefer, flatbed...), Powered Equipment (eg: dozer, crane...), Unpowered Equipment (eg: container, dumpster...), or Uncategorized.  Valid values: `uncategorized`, `trailer`, `equipment`, `unpowered`, `vehicle`"""

    UNCATEGORIZED = "uncategorized"
    TRAILER = "trailer"
    EQUIPMENT = "equipment"
    UNPOWERED = "unpowered"
    VEHICLE = "vehicle"


class AssetsCreateAssetRequestBodyTypedDict(TypedDict):
    r"""Representation of a vehicle trailer or other equipment to be tracked."""

    external_ids: NotRequired[Dict[str, str]]
    r"""A map of external ids"""
    license_plate: NotRequired[str]
    r"""The license plate of the asset."""
    make: NotRequired[str]
    r"""The manufacturer of the asset. (If a VIN is entered and the system detects it is registered to a different manufacturer than provided an error will be returned)."""
    model: NotRequired[str]
    r"""The manufacturer model of the asset. (If a VIN is entered and the system detects it is registered to a different model than provided an error will be returned)."""
    name: NotRequired[str]
    r"""The human-readable name of the asset. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. By default, this name is the serial number of the Samsara Asset Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time."""
    notes: NotRequired[str]
    r"""These are generic notes about the asset. Can be set or updated through the Samsara Dashboard or the API at any time."""
    regulation_mode: NotRequired[AssetsCreateAssetRequestBodyRegulationMode]
    r"""Whether or not the asset is regulated, unregulated (non-CMV), or a mixed use unregulated asset. Primarily used with vehicles.  Valid values: `mixed`, `regulated`, `unregulated`"""
    serial_number: NotRequired[str]
    r"""The serial number of the asset."""
    type: NotRequired[AssetsCreateAssetRequestBodyType]
    r"""The operational context in which the asset interacts with the Samsara system. Examples: Vehicle (eg: truck, bus...), Trailer (eg: dry van, reefer, flatbed...), Powered Equipment (eg: dozer, crane...), Unpowered Equipment (eg: container, dumpster...), or Uncategorized.  Valid values: `uncategorized`, `trailer`, `equipment`, `unpowered`, `vehicle`"""
    vin: NotRequired[str]
    r"""The vehicle identification number of the asset."""
    year: NotRequired[int]
    r"""The year of manufacture of the asset.  (If a VIN is entered and the system detects it is registered to a different year than provided an error will be returned)."""


class AssetsCreateAssetRequestBody(BaseModel):
    r"""Representation of a vehicle trailer or other equipment to be tracked."""

    external_ids: Annotated[
        Optional[Dict[str, str]], pydantic.Field(alias="externalIds")
    ] = None
    r"""A map of external ids"""

    license_plate: Annotated[Optional[str], pydantic.Field(alias="licensePlate")] = None
    r"""The license plate of the asset."""

    make: Optional[str] = None
    r"""The manufacturer of the asset. (If a VIN is entered and the system detects it is registered to a different manufacturer than provided an error will be returned)."""

    model: Optional[str] = None
    r"""The manufacturer model of the asset. (If a VIN is entered and the system detects it is registered to a different model than provided an error will be returned)."""

    name: Optional[str] = None
    r"""The human-readable name of the asset. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. By default, this name is the serial number of the Samsara Asset Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time."""

    notes: Optional[str] = None
    r"""These are generic notes about the asset. Can be set or updated through the Samsara Dashboard or the API at any time."""

    regulation_mode: Annotated[
        Optional[AssetsCreateAssetRequestBodyRegulationMode],
        pydantic.Field(alias="regulationMode"),
    ] = None
    r"""Whether or not the asset is regulated, unregulated (non-CMV), or a mixed use unregulated asset. Primarily used with vehicles.  Valid values: `mixed`, `regulated`, `unregulated`"""

    serial_number: Annotated[Optional[str], pydantic.Field(alias="serialNumber")] = None
    r"""The serial number of the asset."""

    type: Optional[AssetsCreateAssetRequestBodyType] = (
        AssetsCreateAssetRequestBodyType.UNCATEGORIZED
    )
    r"""The operational context in which the asset interacts with the Samsara system. Examples: Vehicle (eg: truck, bus...), Trailer (eg: dry van, reefer, flatbed...), Powered Equipment (eg: dozer, crane...), Unpowered Equipment (eg: container, dumpster...), or Uncategorized.  Valid values: `uncategorized`, `trailer`, `equipment`, `unpowered`, `vehicle`"""

    vin: Optional[str] = None
    r"""The vehicle identification number of the asset."""

    year: Optional[int] = None
    r"""The year of manufacture of the asset.  (If a VIN is entered and the system detects it is registered to a different year than provided an error will be returned)."""
