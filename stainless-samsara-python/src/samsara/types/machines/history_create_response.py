# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["HistoryCreateResponse", "Machine", "MachineVibration"]


class MachineVibration(BaseModel):
    time: Optional[int] = None

    x: Optional[float] = FieldInfo(alias="X", default=None)

    y: Optional[float] = FieldInfo(alias="Y", default=None)

    z: Optional[float] = FieldInfo(alias="Z", default=None)


class Machine(BaseModel):
    id: Optional[int] = None
    """Machine ID"""

    name: Optional[str] = None
    """Machine name"""

    vibrations: Optional[List[MachineVibration]] = None
    """
    List of vibration datapoints, with timestamp and vibration measurement for x/y/z
    axis in mm/s
    """


class HistoryCreateResponse(BaseModel):
    machines: Optional[List[Machine]] = None
