# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "DvirCreateResponse",
    "Data",
    "DataAuthorSignature",
    "DataAuthorSignatureSignatoryUser",
    "DataSecondSignature",
    "DataSecondSignatureSignatoryUser",
    "DataThirdSignature",
    "DataThirdSignatureSignatoryUser",
    "DataTrailer",
    "DataTrailerDefect",
    "DataTrailerDefectResolvedBy",
    "DataTrailerDefectTrailer",
    "DataTrailerDefectVehicle",
    "DataVehicle",
    "DataVehicleDefect",
    "DataVehicleDefectResolvedBy",
    "DataVehicleDefectTrailer",
    "DataVehicleDefectVehicle",
]


class DataAuthorSignatureSignatoryUser(BaseModel):
    id: Optional[str] = None
    """ID of the user."""

    name: Optional[str] = None
    """Name of the user."""


class DataAuthorSignature(BaseModel):
    signatory_user: Optional[DataAuthorSignatureSignatoryUser] = FieldInfo(alias="signatoryUser", default=None)

    signed_at_time: Optional[str] = FieldInfo(alias="signedAtTime", default=None)
    """The time when the DVIR was signed.

    UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.
    """

    type: Optional[Literal["driver", "mechanic"]] = None
    """Whether the DVIR was submitted by a `driver` or `mechanic`.

    Valid values: `driver`, `mechanic`.
    """


class DataSecondSignatureSignatoryUser(BaseModel):
    id: Optional[str] = None
    """ID of the user."""

    name: Optional[str] = None
    """Name of the user."""


class DataSecondSignature(BaseModel):
    signatory_user: Optional[DataSecondSignatureSignatoryUser] = FieldInfo(alias="signatoryUser", default=None)

    signed_at_time: Optional[str] = FieldInfo(alias="signedAtTime", default=None)
    """The time when the DVIR was signed.

    UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.
    """

    type: Optional[Literal["driver", "mechanic"]] = None
    """Whether the DVIR was submitted by a `driver` or `mechanic`.

    Valid values: `driver`, `mechanic`.
    """


class DataThirdSignatureSignatoryUser(BaseModel):
    id: Optional[str] = None
    """ID of the user."""

    name: Optional[str] = None
    """Name of the user."""


class DataThirdSignature(BaseModel):
    signatory_user: Optional[DataThirdSignatureSignatoryUser] = FieldInfo(alias="signatoryUser", default=None)

    signed_at_time: Optional[str] = FieldInfo(alias="signedAtTime", default=None)
    """The time when the DVIR was signed.

    UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.
    """

    type: Optional[Literal["driver", "mechanic"]] = None
    """Whether the DVIR was submitted by a `driver` or `mechanic`.

    Valid values: `driver`, `mechanic`.
    """


class DataTrailer(BaseModel):
    id: Optional[str] = None
    """ID of the trailer."""

    name: Optional[str] = None
    """Name of the trailer."""


class DataTrailerDefectResolvedBy(BaseModel):
    id: Optional[str] = None
    """ID of the entity that resolved this defect.

    If the defect was resolved by a driver, this will be a Samsara Driver ID. If the
    defect was resolved by a mechanic, this will be the Samsara Dashboard User ID of
    the mechanic.
    """

    name: Optional[str] = None
    """Name of the person who resolved this defect."""

    type: Optional[Literal["driver", "mechanic"]] = None
    """Indicates whether this defect was resolved by a `driver` or a `mechanic`."""


class DataTrailerDefectTrailer(BaseModel):
    id: Optional[str] = None
    """ID of the trailer."""

    name: Optional[str] = None
    """Name of the trailer."""


class DataTrailerDefectVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="ExternalIds", default=None)
    """
    The [external IDs](https://developers.samsara.com/docs/external-ids) for the
    given object.
    """

    name: Optional[str] = None
    """Name of the vehicle."""


class DataTrailerDefect(BaseModel):
    id: str
    """ID of the defect."""

    is_resolved: bool = FieldInfo(alias="isResolved")
    """Signifies if this defect is resolved."""

    comment: Optional[str] = None
    """Comment on the defect."""

    created_at_time: Optional[str] = FieldInfo(alias="createdAtTime", default=None)
    """Time when the defect was created.

    UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.
    """

    defect_type: Optional[str] = FieldInfo(alias="defectType", default=None)
    """The type of DVIR defect."""

    mechanic_notes: Optional[str] = FieldInfo(alias="mechanicNotes", default=None)
    """The mechanics notes on the defect."""

    mechanic_notes_updated_at_time: Optional[str] = FieldInfo(alias="mechanicNotesUpdatedAtTime", default=None)
    """Time when mechanic notes were last updated.

    UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.
    """

    resolved_at_time: Optional[str] = FieldInfo(alias="resolvedAtTime", default=None)
    """Time when this defect was resolved.

    Will not be returned if the defect is unresolved. UTC timestamp in RFC 3339
    format. Example: `2020-01-27T07:06:25Z`.
    """

    resolved_by: Optional[DataTrailerDefectResolvedBy] = FieldInfo(alias="resolvedBy", default=None)
    """The person who resolved this defect.

    Will not be returned if the defect is unresolved.
    """

    trailer: Optional[DataTrailerDefectTrailer] = None

    vehicle: Optional[DataTrailerDefectVehicle] = None


class DataVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="ExternalIds", default=None)
    """
    The [external IDs](https://developers.samsara.com/docs/external-ids) for the
    given object.
    """

    name: Optional[str] = None
    """Name of the vehicle."""


class DataVehicleDefectResolvedBy(BaseModel):
    id: Optional[str] = None
    """ID of the entity that resolved this defect.

    If the defect was resolved by a driver, this will be a Samsara Driver ID. If the
    defect was resolved by a mechanic, this will be the Samsara Dashboard User ID of
    the mechanic.
    """

    name: Optional[str] = None
    """Name of the person who resolved this defect."""

    type: Optional[Literal["driver", "mechanic"]] = None
    """Indicates whether this defect was resolved by a `driver` or a `mechanic`."""


class DataVehicleDefectTrailer(BaseModel):
    id: Optional[str] = None
    """ID of the trailer."""

    name: Optional[str] = None
    """Name of the trailer."""


class DataVehicleDefectVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="ExternalIds", default=None)
    """
    The [external IDs](https://developers.samsara.com/docs/external-ids) for the
    given object.
    """

    name: Optional[str] = None
    """Name of the vehicle."""


class DataVehicleDefect(BaseModel):
    id: str
    """ID of the defect."""

    is_resolved: bool = FieldInfo(alias="isResolved")
    """Signifies if this defect is resolved."""

    comment: Optional[str] = None
    """Comment on the defect."""

    created_at_time: Optional[str] = FieldInfo(alias="createdAtTime", default=None)
    """Time when the defect was created.

    UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.
    """

    defect_type: Optional[str] = FieldInfo(alias="defectType", default=None)
    """The type of DVIR defect."""

    mechanic_notes: Optional[str] = FieldInfo(alias="mechanicNotes", default=None)
    """The mechanics notes on the defect."""

    mechanic_notes_updated_at_time: Optional[str] = FieldInfo(alias="mechanicNotesUpdatedAtTime", default=None)
    """Time when mechanic notes were last updated.

    UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.
    """

    resolved_at_time: Optional[str] = FieldInfo(alias="resolvedAtTime", default=None)
    """Time when this defect was resolved.

    Will not be returned if the defect is unresolved. UTC timestamp in RFC 3339
    format. Example: `2020-01-27T07:06:25Z`.
    """

    resolved_by: Optional[DataVehicleDefectResolvedBy] = FieldInfo(alias="resolvedBy", default=None)
    """The person who resolved this defect.

    Will not be returned if the defect is unresolved.
    """

    trailer: Optional[DataVehicleDefectTrailer] = None

    vehicle: Optional[DataVehicleDefectVehicle] = None


class Data(BaseModel):
    id: str
    """Unique Samsara ID for the DVIR."""

    author_signature: Optional[DataAuthorSignature] = FieldInfo(alias="authorSignature", default=None)

    end_time: Optional[str] = FieldInfo(alias="endTime", default=None)
    """Time when driver signed and completed this DVIR.

    UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.
    """

    license_plate: Optional[str] = FieldInfo(alias="licensePlate", default=None)
    """The license plate of this vehicle."""

    location: Optional[str] = None
    """Optional string if your jurisdiction requires a location of the DVIR."""

    mechanic_notes: Optional[str] = FieldInfo(alias="mechanicNotes", default=None)
    """The mechanics notes on the DVIR."""

    odometer_meters: Optional[int] = FieldInfo(alias="odometerMeters", default=None)
    """The odometer reading in meters."""

    safety_status: Optional[Literal["safe", "unsafe", "resolved"]] = FieldInfo(alias="safetyStatus", default=None)
    """The condition of vehicle on which DVIR was done.

    Valid values: `safe`, `unsafe`, `resolved`.
    """

    second_signature: Optional[DataSecondSignature] = FieldInfo(alias="secondSignature", default=None)

    start_time: Optional[str] = FieldInfo(alias="startTime", default=None)
    """Time when driver began filling out this DVIR.

    UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.
    """

    third_signature: Optional[DataThirdSignature] = FieldInfo(alias="thirdSignature", default=None)

    trailer: Optional[DataTrailer] = None

    trailer_defects: Optional[List[DataTrailerDefect]] = FieldInfo(alias="trailerDefects", default=None)
    """Defects registered for the trailer which was part of the DVIR."""

    trailer_name: Optional[str] = FieldInfo(alias="trailerName", default=None)
    """The name of the trailer the DVIR was submitted for.

    Only included for tractor+trailer DVIRs.
    """

    type: Optional[Literal["preTrip", "postTrip", "mechanic", "unspecified"]] = None
    """Inspection type of the DVIR.

    Valid values: `preTrip`, `postTrip`, `mechanic`, `unspecified`.
    """

    vehicle: Optional[DataVehicle] = None

    vehicle_defects: Optional[List[DataVehicleDefect]] = FieldInfo(alias="vehicleDefects", default=None)
    """Defects registered for the vehicle which was part of the DVIR."""


class DvirCreateResponse(BaseModel):
    data: Optional[Data] = None
    """Information about a DVIR."""
