"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .tachographvehiclefile import TachographVehicleFile, TachographVehicleFileTypedDict
from .vehicletinyresponse import VehicleTinyResponse, VehicleTinyResponseTypedDict
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class TachographVehicleFileListWrapperTypedDict(TypedDict):
    files: NotRequired[List[TachographVehicleFileTypedDict]]
    r"""List of all tachograph vehicle files in a specified time range."""
    vehicle: NotRequired[VehicleTinyResponseTypedDict]
    r"""A minified vehicle object."""


class TachographVehicleFileListWrapper(BaseModel):
    files: Optional[List[TachographVehicleFile]] = None
    r"""List of all tachograph vehicle files in a specified time range."""

    vehicle: Optional[VehicleTinyResponse] = None
    r"""A minified vehicle object."""
