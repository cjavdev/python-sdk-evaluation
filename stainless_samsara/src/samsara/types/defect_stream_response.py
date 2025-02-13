# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DefectStreamResponse", "Data", "DataResolvedBy", "DataTrailer", "DataVehicle", "Pagination"]


class DataResolvedBy(BaseModel):
    id: str
    """ID of the entity that resolved this defect.

    If the defect was resolved by a driver, this will be a Samsara Driver ID. If the
    defect was resolved by a mechanic, this will be the Samsara Dashboard User ID of
    the mechanic.
    """

    name: str
    """Name of the person who resolved this defect."""

    type: Literal["driver", "mechanic"]
    """Indicates whether this defect was resolved by a driver or a mechanic.

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
    """The unique ID of the DVIR defect."""

    comment: str
    """Comment on the defect."""

    dvir_id: str = FieldInfo(alias="dvirId")
    """The unique ID of the defect's DVIR."""

    is_resolved: bool = FieldInfo(alias="isResolved")
    """Signifies if this defect is resolved."""

    created_at_time: Optional[str] = FieldInfo(alias="createdAtTime", default=None)
    """Time when defect was created in RFC 3339 format."""

    defect_type_id: Optional[str] = FieldInfo(alias="defectTypeId", default=None)
    """The unique ID of the defect type."""

    mechanic_notes: Optional[str] = FieldInfo(alias="mechanicNotes", default=None)
    """The mechanics notes on the defect."""

    resolved_at_time: Optional[str] = FieldInfo(alias="resolvedAtTime", default=None)
    """Time when this defect was resolved in RFC 3339 format.

    Will not be returned if the defect is unresolved.
    """

    resolved_by: Optional[DataResolvedBy] = FieldInfo(alias="resolvedBy", default=None)
    """The person who resolved this defect."""

    trailer: Optional[DataTrailer] = None
    """Defect's trailer object"""

    updated_at_time: Optional[str] = FieldInfo(alias="updatedAtTime", default=None)
    """Time when defect was last updated in RFC 3339 format."""

    vehicle: Optional[DataVehicle] = None
    """Defect's vehicle object"""


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


class DefectStreamResponse(BaseModel):
    data: List[Data]
    """List of DVIR defects."""

    pagination: Pagination
    """Pagination parameters."""
