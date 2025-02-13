# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["RetrievalRetrieveResponse", "Data", "DataMedia", "DataMediaURLInfo"]


class DataMediaURLInfo(BaseModel):
    url: str
    """Signed URL for this piece of media.

    Examples: https://sample.s3.url.com/image.jpeg
    """

    url_expiry_time: str = FieldInfo(alias="urlExpiryTime")
    """Timestamp, in RFC 3339 format, at which the URL expires.

    Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
    2015-09-15T14:00:12-04:00
    """


class DataMedia(BaseModel):
    end_time: str = FieldInfo(alias="endTime")
    """An end time in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    input: Literal["dashcamDriverFacing", "dashcamRoadFacing"]
    """Input type for this media.

    Examples: dashcamDriverFacing Valid values: `dashcamDriverFacing`,
    `dashcamRoadFacing`
    """

    media_type: Literal["image"] = FieldInfo(alias="mediaType")
    """Type of media. Examples: image Valid values: `image`"""

    start_time: str = FieldInfo(alias="startTime")
    """A start time in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    status: Literal["available", "invalid", "pending", "requested"]
    """Status of the media.

    Examples: invalid, pending, requested, available. Valid values: `available`,
    `invalid`, `pending`, `requested`
    """

    vehicle_id: str = FieldInfo(alias="vehicleId")
    """Vehicle ID for which this media was captured. Examples: 1234"""

    available_at_time: Optional[str] = FieldInfo(alias="availableAtTime", default=None)
    """Timestamp, in RFC 3339 format, at which the media item was made available.

    Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
    2015-09-15T14:00:12-04:00
    """

    url_info: Optional[DataMediaURLInfo] = FieldInfo(alias="urlInfo", default=None)
    """URL info for this piece of media.

    This field is only populated when the 'status' response field is 'available'
    """


class Data(BaseModel):
    media: List[DataMedia]
    """List of media retrieval objects."""


class RetrievalRetrieveResponse(BaseModel):
    data: Data
