# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InlineResponse200_1", "Asset", "AssetCable"]


class AssetCable(BaseModel):
    asset_type: Optional[str] = FieldInfo(alias="assetType", default=None)
    """Asset type"""


class Asset(BaseModel):
    id: int
    """Asset ID"""

    asset_serial_number: Optional[str] = FieldInfo(alias="assetSerialNumber", default=None)
    """Serial number of the host asset"""

    cable: Optional[AssetCable] = None
    """The cable connected to the asset"""

    engine_hours: Optional[int] = FieldInfo(alias="engineHours", default=None)
    """Engine hours"""

    name: Optional[str] = None
    """Asset name"""

    vehicle_id: Optional[int] = FieldInfo(alias="vehicleId", default=None)
    """The ID of the Vehicle associated to the Asset (if present)"""


class InlineResponse200_1(BaseModel):
    assets: Optional[List[Asset]] = None
