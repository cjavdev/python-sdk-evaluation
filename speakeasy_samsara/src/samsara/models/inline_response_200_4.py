"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v1vehiclemaintenance import V1VehicleMaintenance, V1VehicleMaintenanceTypedDict
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class InlineResponse2004TypedDict(TypedDict):
    vehicles: NotRequired[List[V1VehicleMaintenanceTypedDict]]


class InlineResponse2004(BaseModel):
    vehicles: Optional[List[V1VehicleMaintenance]] = None
