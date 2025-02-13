# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["MediaRetrievalListUploadedMediaResponseBody", "Data", "DataMedia", "DataMediaURLInfo", "Pagination"]


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
    available_at_time: str = FieldInfo(alias="availableAtTime")
    """Timestamp, in RFC 3339 format, at which the media item was made available.

    Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
    2015-09-15T14:00:12-04:00
    """

    end_time: str = FieldInfo(alias="endTime")
    """An end time in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    input: Literal["dashcamForwardFacing", "dashcamInwardFacing", "dashcamRearFacing"]
    """Input type for this media.

    Examples: dashcamForwardFacing Valid values: `dashcamForwardFacing`,
    `dashcamInwardFacing`, `dashcamRearFacing`
    """

    media_type: Literal["image"] = FieldInfo(alias="mediaType")
    """Type of media. Examples: image Valid values: `image`"""

    start_time: str = FieldInfo(alias="startTime")
    """A start time in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    trigger_reason: Literal[
        "api", "panicButton", "periodicStill", "tripEndStill", "tripStartStill", "videoRetrieval"
    ] = FieldInfo(alias="triggerReason")
    """Trigger reason for this media capture.

    Examples: api Valid values: `api`, `panicButton`, `periodicStill`,
    `tripEndStill`, `tripStartStill`, `videoRetrieval`
    """

    vehicle_id: str = FieldInfo(alias="vehicleId")
    """Vehicle ID for which this media was captured. Examples: 1234"""

    url_info: Optional[DataMediaURLInfo] = FieldInfo(alias="urlInfo", default=None)
    """URL info for this piece of media.

    This field is only populated when the 'status' response field is 'available'
    """


class Data(BaseModel):
    media: List[DataMedia]
    """List of media retrieval objects."""


class Pagination(BaseModel):
    end_cursor: str = FieldInfo(alias="endCursor")
    """Cursor identifier representing the last element in the response.

    This value should be used in conjunction with a subsequent request's 'after'
    query parameter. This may be an empty string if there are no more pages left to
    view.
    """

    has_next_page: bool = FieldInfo(alias="hasNextPage")
    """
    True if there are more pages of results immediately available after this
    endCursor.
    """


class MediaRetrievalListUploadedMediaResponseBody(BaseModel):
    data: Data

    pagination: Pagination
    """Pagination parameters."""
