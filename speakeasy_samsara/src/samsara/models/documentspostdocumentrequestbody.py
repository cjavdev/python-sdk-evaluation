"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .fieldobjectpostrequestbody import (
    FieldObjectPostRequestBody,
    FieldObjectPostRequestBodyTypedDict,
)
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DocumentsPostDocumentRequestBodyState(str, Enum):
    r"""The condition of the document created for the driver. Can be either `required` or `submitted`, if no value is specified, `state` defaults to `required`. `required` documents are pre-populated documents for the Driver to fill out in the Driver App.  Valid values: `submitted`, `required`"""

    SUBMITTED = "submitted"
    REQUIRED = "required"


class DocumentsPostDocumentRequestBodyTypedDict(TypedDict):
    document_type_id: str
    r"""ID for the document type."""
    driver_id: str
    r"""ID of the driver. Can be either unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the driver."""
    fields: NotRequired[List[FieldObjectPostRequestBodyTypedDict]]
    r"""The fields associated with this document."""
    name: NotRequired[str]
    r"""Name of the document."""
    notes: NotRequired[str]
    r"""Notes on the document."""
    route_stop_id: NotRequired[str]
    r"""ID of the route stop. Can be either unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the route stop."""
    state: NotRequired[DocumentsPostDocumentRequestBodyState]
    r"""The condition of the document created for the driver. Can be either `required` or `submitted`, if no value is specified, `state` defaults to `required`. `required` documents are pre-populated documents for the Driver to fill out in the Driver App.  Valid values: `submitted`, `required`"""
    vehicle_id: NotRequired[str]
    r"""ID of the vehicle. Can be either unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle."""


class DocumentsPostDocumentRequestBody(BaseModel):
    document_type_id: Annotated[str, pydantic.Field(alias="documentTypeId")]
    r"""ID for the document type."""

    driver_id: Annotated[str, pydantic.Field(alias="driverId")]
    r"""ID of the driver. Can be either unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the driver."""

    fields: Optional[List[FieldObjectPostRequestBody]] = None
    r"""The fields associated with this document."""

    name: Optional[str] = None
    r"""Name of the document."""

    notes: Optional[str] = None
    r"""Notes on the document."""

    route_stop_id: Annotated[Optional[str], pydantic.Field(alias="routeStopId")] = None
    r"""ID of the route stop. Can be either unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the route stop."""

    state: Optional[DocumentsPostDocumentRequestBodyState] = (
        DocumentsPostDocumentRequestBodyState.REQUIRED
    )
    r"""The condition of the document created for the driver. Can be either `required` or `submitted`, if no value is specified, `state` defaults to `required`. `required` documents are pre-populated documents for the Driver to fill out in the Driver App.  Valid values: `submitted`, `required`"""

    vehicle_id: Annotated[Optional[str], pydantic.Field(alias="vehicleId")] = None
    r"""ID of the vehicle. Can be either unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle."""
