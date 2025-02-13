# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DriverVehicleAssignmentCreateResponse", "Data"]


class Data(BaseModel):
    message: Optional[str] = None
    """A description of the outcome from submitting Driver Assignment information"""


class DriverVehicleAssignmentCreateResponse(BaseModel):
    data: Data
    """Response after successfully submitting a Driver Assignment"""
