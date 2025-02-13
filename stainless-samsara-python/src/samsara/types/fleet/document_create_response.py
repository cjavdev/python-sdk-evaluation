# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "DocumentCreateResponse",
    "Data",
    "DataDocumentType",
    "DataDriver",
    "DataField",
    "DataFieldValue",
    "DataFieldValueBarcodeValue",
    "DataFieldValueDateTimeValue",
    "DataFieldValueMultipleChoiceValue",
    "DataFieldValuePhotoValue",
    "DataFieldValueScannedDocumentValue",
    "DataFieldValueSignatureValue",
    "DataConditionalFieldSection",
    "DataRoute",
    "DataRouteStop",
    "DataVehicle",
]


class DataDocumentType(BaseModel):
    id: Optional[str] = None
    """ID of the document type."""

    name: Optional[str] = None
    """Name of the document type."""


class DataDriver(BaseModel):
    id: str
    """ID of the driver"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the driver"""


class DataFieldValueBarcodeValue(BaseModel):
    barcode_type: Optional[str] = FieldInfo(alias="barcodeType", default=None)
    """The barcode type that was scanned."""

    barcode_value: Optional[str] = FieldInfo(alias="barcodeValue", default=None)
    """The captured barcode value."""


class DataFieldValueDateTimeValue(BaseModel):
    date_time: Optional[datetime] = FieldInfo(alias="dateTime", default=None)
    """Date time value inin RFC 3339 format."""


class DataFieldValueMultipleChoiceValue(BaseModel):
    selected: Optional[bool] = None
    """Boolean representing if the choice has been selected."""

    value: Optional[str] = None
    """Description of the choice."""


class DataFieldValuePhotoValue(BaseModel):
    id: Optional[str] = None
    """Id of the photo."""

    url: Optional[str] = None
    """Url of the photo."""


class DataFieldValueScannedDocumentValue(BaseModel):
    id: Optional[str] = None
    """Id of the scanned document."""

    url: Optional[str] = None
    """Url of the scanned document."""


class DataFieldValueSignatureValue(BaseModel):
    id: Optional[str] = None
    """Id of the signature field."""

    name: Optional[str] = None
    """Name of the signee for a signature field."""

    signed_at_time: Optional[datetime] = FieldInfo(alias="signedAtTime", default=None)
    """Time the signature was captured in RFC 3339 format."""

    url: Optional[str] = None
    """Url of a signature field's PNG signature image."""


class DataFieldValue(BaseModel):
    barcode_value: Optional[List[DataFieldValueBarcodeValue]] = FieldInfo(alias="barcodeValue", default=None)
    """The value of a barcode scanning field.

    Only present for barcode scanning fields.
    """

    date_time_value: Optional[DataFieldValueDateTimeValue] = FieldInfo(alias="dateTimeValue", default=None)
    """The value of a date time field. Only present for date time fields."""

    multiple_choice_value: Optional[List[DataFieldValueMultipleChoiceValue]] = FieldInfo(
        alias="multipleChoiceValue", default=None
    )
    """The value of a multiple choice field. Only present for multiple choice fields."""

    number_value: Optional[float] = FieldInfo(alias="numberValue", default=None)
    """The value of a number field. Only present for number fields."""

    photo_value: Optional[List[DataFieldValuePhotoValue]] = FieldInfo(alias="photoValue", default=None)
    """The value of a photo field. Only present for photo fields."""

    scanned_document_value: Optional[List[DataFieldValueScannedDocumentValue]] = FieldInfo(
        alias="scannedDocumentValue", default=None
    )
    """The value of a scanned document field.

    Only present for scanned document fields.
    """

    signature_value: Optional[DataFieldValueSignatureValue] = FieldInfo(alias="signatureValue", default=None)
    """The value of a signature field. Only present for signature fields."""

    string_value: Optional[str] = FieldInfo(alias="stringValue", default=None)
    """The value of a string field. Only present for string fields."""


class DataField(BaseModel):
    label: str
    """The name of the field."""

    type: Literal["photo", "string", "number", "multipleChoice", "signature", "dateTime", "scannedDocument", "barcode"]
    """The type of field.

    Valid values: `photo`, `string`, `number`, `multipleChoice`, `signature`,
    `dateTime`, `scannedDocument`, `barcode`
    """

    value: DataFieldValue
    """The value of the document field. The shape of value depends on the type."""


class DataConditionalFieldSection(BaseModel):
    conditional_field_first_index: Optional[int] = FieldInfo(alias="conditionalFieldFirstIndex", default=None)
    """
    The index of the first conditional field associated with the
    triggeringFieldValue in the fieldTypes list.
    """

    conditional_field_last_index: Optional[int] = FieldInfo(alias="conditionalFieldLastIndex", default=None)
    """
    The index of the last conditional field associated with the triggeringFieldValue
    in the fieldTypes list.
    """

    triggering_field_index: Optional[int] = FieldInfo(alias="triggeringFieldIndex", default=None)
    """
    The index of the multiple choice field in the fieldTypes list that triggers one
    or more conditional fields.
    """

    triggering_field_value: Optional[str] = FieldInfo(alias="triggeringFieldValue", default=None)
    """The multiple choice option value that triggers the conditional fields."""


class DataRoute(BaseModel):
    id: str
    """Unique identifier for the route."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the route."""


class DataRouteStop(BaseModel):
    id: Optional[str] = None
    """Id of the route stop"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the route stop"""


class DataVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the vehicle"""


class Data(BaseModel):
    id: str
    """Universally unique identifier for the document."""

    created_at_time: datetime = FieldInfo(alias="createdAtTime")
    """Time the document was created in RFC 3339 format."""

    document_type: DataDocumentType = FieldInfo(alias="documentType")
    """A minified document type object"""

    driver: DataDriver
    """A minified driver object.

    This object is only returned if the route is assigned to the driver.
    """

    fields: List[DataField]
    """The fields associated with this document."""

    state: Literal["submitted", "required", "archived"]
    """The condition of the document created for the driver.

    Can be either Required or Submitted. Required documents are pre-populated
    documents for the Driver to fill out in the Driver App and have not yet been
    submitted. Submitted documents have been submitted by the driver in the Driver
    App. Archived documents have been archived by the admin in the cloud dashboard.
    Valid values: `submitted`, `required`, `archived`
    """

    conditional_field_sections: Optional[List[DataConditionalFieldSection]] = FieldInfo(
        alias="conditionalFieldSections", default=None
    )
    """List of the document conditional field sections."""

    name: Optional[str] = None
    """Name of the document."""

    notes: Optional[str] = None
    """Notes on the document."""

    route: Optional[DataRoute] = None
    """A minified representation of a single route."""

    route_stop: Optional[DataRouteStop] = FieldInfo(alias="routeStop", default=None)
    """A minified route stop object"""

    updated_at_time: Optional[datetime] = FieldInfo(alias="updatedAtTime", default=None)
    """Time the document was updated in RFC 3339 format."""

    vehicle: Optional[DataVehicle] = None
    """A minified vehicle object.

    This object is only returned if the route is assigned to the vehicle.
    """


class DocumentCreateResponse(BaseModel):
    data: Optional[Data] = None
    """A single document."""
