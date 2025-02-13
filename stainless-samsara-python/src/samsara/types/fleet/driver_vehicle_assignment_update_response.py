# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DriverVehicleAssignmentUpdateResponse", "Data"]


class Data(BaseModel):
    message: Optional[str] = None
    """A description of the outcome from updating Driver Assignment information"""


class DriverVehicleAssignmentUpdateResponse(BaseModel):
    data: Data
    """Response after successfully updating a Driver Assignment"""
