# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "DvirStreamResponse",
    "Data",
    "DataAuthorSignature",
    "DataAuthorSignatureSignatoryUser",
    "DataSecondSignature",
    "DataSecondSignatureSignatoryUser",
    "DataThirdSignature",
    "DataThirdSignatureSignatoryUser",
    "DataTrailer",
    "DataVehicle",
    "Pagination",
]


class DataAuthorSignatureSignatoryUser(BaseModel):
    id: str
    """ID of the user."""


class DataAuthorSignature(BaseModel):
    signatory_user: DataAuthorSignatureSignatoryUser = FieldInfo(alias="signatoryUser")
    """The user who signed the DVIR."""

    signed_at_time: str = FieldInfo(alias="signedAtTime")
    """The time when the DVIR was signed. UTC timestamp in RFC 3339 format."""

    type: Literal["driver", "mechanic"]
    """Whether the DVIR was submitted by a driver or mechanic.

    Valid values: `driver`, `mechanic`
    """


class DataSecondSignatureSignatoryUser(BaseModel):
    id: str
    """ID of the user."""


class DataSecondSignature(BaseModel):
    signatory_user: DataSecondSignatureSignatoryUser = FieldInfo(alias="signatoryUser")
    """The user who signed the DVIR."""

    signed_at_time: str = FieldInfo(alias="signedAtTime")
    """The time when the DVIR was signed. UTC timestamp in RFC 3339 format."""

    type: Literal["driver", "mechanic"]
    """Whether the DVIR was submitted by a driver or mechanic.

    Valid values: `driver`, `mechanic`
    """


class DataThirdSignatureSignatoryUser(BaseModel):
    id: str
    """ID of the user."""


class DataThirdSignature(BaseModel):
    signatory_user: DataThirdSignatureSignatoryUser = FieldInfo(alias="signatoryUser")
    """The user who signed the DVIR."""

    signed_at_time: str = FieldInfo(alias="signedAtTime")
    """The time when the DVIR was signed. UTC timestamp in RFC 3339 format."""

    type: Literal["driver", "mechanic"]
    """Whether the DVIR was submitted by a driver or mechanic.

    Valid values: `driver`, `mechanic`
    """


class DataTrailer(BaseModel):
    id: Optional[str] = None
    """ID of the trailer"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""


class DataVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""


class Data(BaseModel):
    id: str
    """The unique id of the DVIR"""

    author_signature: DataAuthorSignature = FieldInfo(alias="authorSignature")
    """An author signature for DVIRs with a signed time."""

    dvir_submission_begin_time: str = FieldInfo(alias="dvirSubmissionBeginTime")
    """Time when driver created DVIR. UTC timestamp in RFC 3339 format."""

    dvir_submission_time: str = FieldInfo(alias="dvirSubmissionTime")
    """Time when driver submitted the DVIR. UTC timestamp in RFC 3339 format."""

    type: Literal["preTrip", "postTrip", "mechanic", "unspecified"]
    """Inspection type of the DVIR.

    Valid values: `preTrip`, `postTrip`, `mechanic`, `unspecified`
    """

    updated_at_time: str = FieldInfo(alias="updatedAtTime")
    """Time of any DVIR updates. UTC timestamp in RFC 3339 format."""

    defect_ids: Optional[List[str]] = FieldInfo(alias="defectIds", default=None)
    """IDs of defects registered for the DVIR."""

    formatted_address: Optional[str] = FieldInfo(alias="formattedAddress", default=None)

    mechanic_notes: Optional[str] = FieldInfo(alias="mechanicNotes", default=None)
    """The mechanics notes on the DVIR."""

    odometer_meters: Optional[int] = FieldInfo(alias="odometerMeters", default=None)
    """The odometer reading in meters."""

    safety_status: Optional[Literal["unknown", "safe", "unsafe", "resolved"]] = FieldInfo(
        alias="safetyStatus", default=None
    )
    """The condition of vehicle on which DVIR was done.

    Valid values: `unknown`, `safe`, `unsafe`, `resolved`
    """

    second_signature: Optional[DataSecondSignature] = FieldInfo(alias="secondSignature", default=None)
    """An author signature for DVIRs with a signed time."""

    third_signature: Optional[DataThirdSignature] = FieldInfo(alias="thirdSignature", default=None)
    """An author signature for DVIRs with a signed time."""

    trailer: Optional[DataTrailer] = None
    """A trailer object"""

    vehicle: Optional[DataVehicle] = None
    """A vehicle object"""


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


class DvirStreamResponse(BaseModel):
    data: List[Data]

    pagination: Pagination
    """Pagination parameters."""
