# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DefectUpdateResponse", "Data", "DataResolvedBy", "DataTrailer", "DataVehicle"]


class DataResolvedBy(BaseModel):
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


class DataTrailer(BaseModel):
    id: Optional[str] = None
    """ID of the trailer."""

    name: Optional[str] = None
    """Name of the trailer."""


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


class Data(BaseModel):
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

    resolved_by: Optional[DataResolvedBy] = FieldInfo(alias="resolvedBy", default=None)
    """The person who resolved this defect.

    Will not be returned if the defect is unresolved.
    """

    trailer: Optional[DataTrailer] = None

    vehicle: Optional[DataVehicle] = None


class DefectUpdateResponse(BaseModel):
    data: Optional[Data] = None
