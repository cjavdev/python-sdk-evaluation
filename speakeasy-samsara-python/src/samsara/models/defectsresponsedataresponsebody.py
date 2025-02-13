"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .defectphotoresponseresponsebody import (
    DefectPhotoResponseResponseBody,
    DefectPhotoResponseResponseBodyTypedDict,
)
from .defecttrailerresponseresponsebody import (
    DefectTrailerResponseResponseBody,
    DefectTrailerResponseResponseBodyTypedDict,
)
from .defectvehicleresponseresponsebody import (
    DefectVehicleResponseResponseBody,
    DefectVehicleResponseResponseBodyTypedDict,
)
from .dvirresolvedbyobjectresponsebody import (
    DvirResolvedByObjectResponseBody,
    DvirResolvedByObjectResponseBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DefectsResponseDataResponseBodyTypedDict(TypedDict):
    r"""DVIR defects data."""

    comment: str
    r"""Comment on the defect."""
    dvir_id: str
    r"""The unique ID of the defect's DVIR."""
    id: str
    r"""The unique ID of the DVIR defect."""
    is_resolved: bool
    r"""Signifies if this defect is resolved."""
    created_at_time: NotRequired[str]
    r"""Time when defect was created in RFC 3339 format."""
    defect_photos: NotRequired[List[DefectPhotoResponseResponseBodyTypedDict]]
    r"""List of DVIR defect's photos"""
    defect_type_id: NotRequired[str]
    r"""The unique ID of the defect type."""
    mechanic_notes: NotRequired[str]
    r"""The mechanics notes on the defect."""
    resolved_at_time: NotRequired[str]
    r"""Time when this defect was resolved in RFC 3339 format. Will not be returned if the defect is unresolved."""
    resolved_by: NotRequired[DvirResolvedByObjectResponseBodyTypedDict]
    r"""The person who resolved this defect."""
    trailer: NotRequired[DefectTrailerResponseResponseBodyTypedDict]
    r"""Defect's trailer object"""
    updated_at_time: NotRequired[str]
    r"""Time when defect was last updated in RFC 3339 format."""
    vehicle: NotRequired[DefectVehicleResponseResponseBodyTypedDict]
    r"""Defect's vehicle object"""


class DefectsResponseDataResponseBody(BaseModel):
    r"""DVIR defects data."""

    comment: str
    r"""Comment on the defect."""

    dvir_id: Annotated[str, pydantic.Field(alias="dvirId")]
    r"""The unique ID of the defect's DVIR."""

    id: str
    r"""The unique ID of the DVIR defect."""

    is_resolved: Annotated[bool, pydantic.Field(alias="isResolved")]
    r"""Signifies if this defect is resolved."""

    created_at_time: Annotated[Optional[str], pydantic.Field(alias="createdAtTime")] = (
        None
    )
    r"""Time when defect was created in RFC 3339 format."""

    defect_photos: Annotated[
        Optional[List[DefectPhotoResponseResponseBody]],
        pydantic.Field(alias="defectPhotos"),
    ] = None
    r"""List of DVIR defect's photos"""

    defect_type_id: Annotated[Optional[str], pydantic.Field(alias="defectTypeId")] = (
        None
    )
    r"""The unique ID of the defect type."""

    mechanic_notes: Annotated[Optional[str], pydantic.Field(alias="mechanicNotes")] = (
        None
    )
    r"""The mechanics notes on the defect."""

    resolved_at_time: Annotated[
        Optional[str], pydantic.Field(alias="resolvedAtTime")
    ] = None
    r"""Time when this defect was resolved in RFC 3339 format. Will not be returned if the defect is unresolved."""

    resolved_by: Annotated[
        Optional[DvirResolvedByObjectResponseBody], pydantic.Field(alias="resolvedBy")
    ] = None
    r"""The person who resolved this defect."""

    trailer: Optional[DefectTrailerResponseResponseBody] = None
    r"""Defect's trailer object"""

    updated_at_time: Annotated[Optional[str], pydantic.Field(alias="updatedAtTime")] = (
        None
    )
    r"""Time when defect was last updated in RFC 3339 format."""

    vehicle: Optional[DefectVehicleResponseResponseBody] = None
    r"""Defect's vehicle object"""
