# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1VisionCamerasResponse", "V1VisionCamerasResponseItem"]


class V1VisionCamerasResponseItem(BaseModel):
    camera_id: Optional[int] = FieldInfo(alias="cameraId", default=None)

    camera_name: Optional[str] = FieldInfo(alias="cameraName", default=None)

    ethernet_ip: Optional[str] = FieldInfo(alias="ethernetIp", default=None)

    wifi_ip: Optional[str] = FieldInfo(alias="wifiIp", default=None)


V1VisionCamerasResponse: TypeAlias = List[V1VisionCamerasResponseItem]
