# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1VehicleHarshEventResponse", "Location"]


class Location(BaseModel):
    address: Optional[str] = None
    """Address of location where the harsh event occurred"""

    latitude: Optional[float] = None
    """Latitude of location where the harsh event occurred"""

    longitude: Optional[float] = None
    """Longitude of location where the harsh event occurred"""


class V1VehicleHarshEventResponse(BaseModel):
    harsh_event_type: str = FieldInfo(alias="harshEventType")
    """Type of the harsh event.

    One of: [Crash, Harsh Acceleration, Harsh Braking, Harsh Turn, ROP Engine, ROP
    Brake, YC Engine, YC Brake, Harsh Event]
    """

    incident_report_url: str = FieldInfo(alias="incidentReportUrl")
    """URL of the associated incident report page"""

    download_forward_video_url: Optional[str] = FieldInfo(alias="downloadForwardVideoUrl", default=None)
    """URL for downloading the forward facing video"""

    download_inward_video_url: Optional[str] = FieldInfo(alias="downloadInwardVideoUrl", default=None)
    """URL for downloading the inward facing video"""

    download_tracked_inward_video_url: Optional[str] = FieldInfo(alias="downloadTrackedInwardVideoUrl", default=None)
    """URL for downloading the tracked inward facing video"""

    is_distracted: Optional[bool] = FieldInfo(alias="isDistracted", default=None)
    """Whether the driver was deemed distracted during this harsh event"""

    location: Optional[Location] = None
