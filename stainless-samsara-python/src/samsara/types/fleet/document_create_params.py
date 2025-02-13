# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "DocumentCreateParams",
    "Field",
    "FieldValue",
    "FieldValueBarcodeValue",
    "FieldValueDateTimeValue",
    "FieldValueMultipleChoiceValue",
    "FieldValuePhotoValue",
    "FieldValueScannedDocumentValue",
    "FieldValueSignatureValue",
]


class DocumentCreateParams(TypedDict, total=False):
    document_type_id: Required[Annotated[str, PropertyInfo(alias="documentTypeId")]]
    """ID for the document type."""

    driver_id: Required[Annotated[str, PropertyInfo(alias="driverId")]]
    """ID of the driver.

    Can be either unique Samsara ID or an
    [external ID](https://developers.samsara.com/docs/external-ids) for the driver.
    """

    fields: Iterable[Field]
    """The fields associated with this document."""

    name: str
    """Name of the document."""

    notes: str
    """Notes on the document."""

    route_stop_id: Annotated[str, PropertyInfo(alias="routeStopId")]
    """ID of the route stop.

    Can be either unique Samsara ID or an
    [external ID](https://developers.samsara.com/docs/external-ids) for the route
    stop.
    """

    state: Literal["submitted", "required"]
    """The condition of the document created for the driver.

    Can be either `required` or `submitted`, if no value is specified, `state`
    defaults to `required`. `required` documents are pre-populated documents for the
    Driver to fill out in the Driver App. Valid values: `submitted`, `required`
    """

    vehicle_id: Annotated[str, PropertyInfo(alias="vehicleId")]
    """ID of the vehicle.

    Can be either unique Samsara ID or an
    [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.
    """


class FieldValueBarcodeValue(TypedDict, total=False):
    barcode_type: Annotated[str, PropertyInfo(alias="barcodeType")]
    """The barcode type that was scanned."""

    barcode_value: Annotated[str, PropertyInfo(alias="barcodeValue")]
    """The captured barcode value."""


class FieldValueDateTimeValue(TypedDict, total=False):
    date_time: Annotated[Union[str, datetime], PropertyInfo(alias="dateTime", format="iso8601")]
    """Date time value inin RFC 3339 format."""


class FieldValueMultipleChoiceValue(TypedDict, total=False):
    selected: bool
    """Boolean representing if the choice has been selected."""

    value: str
    """Description of the choice."""


class FieldValuePhotoValue(TypedDict, total=False):
    id: str
    """Id of the photo."""

    url: str
    """Url of the photo."""


class FieldValueScannedDocumentValue(TypedDict, total=False):
    id: str
    """Id of the scanned document."""

    url: str
    """Url of the scanned document."""


class FieldValueSignatureValue(TypedDict, total=False):
    id: str
    """Id of the signature field."""

    name: str
    """Name of the signee for a signature field."""

    signed_at_time: Annotated[Union[str, datetime], PropertyInfo(alias="signedAtTime", format="iso8601")]
    """Time the signature was captured in RFC 3339 format."""

    url: str
    """Url of a signature field's PNG signature image."""


class FieldValue(TypedDict, total=False):
    barcode_value: Annotated[Iterable[FieldValueBarcodeValue], PropertyInfo(alias="barcodeValue")]
    """The value of a barcode scanning field.

    Only present for barcode scanning fields.
    """

    date_time_value: Annotated[FieldValueDateTimeValue, PropertyInfo(alias="dateTimeValue")]
    """The value of a date time field. Only present for date time fields."""

    multiple_choice_value: Annotated[Iterable[FieldValueMultipleChoiceValue], PropertyInfo(alias="multipleChoiceValue")]
    """The value of a multiple choice field. Only present for multiple choice fields."""

    number_value: Annotated[float, PropertyInfo(alias="numberValue")]
    """The value of a number field. Only present for number fields."""

    photo_value: Annotated[Iterable[FieldValuePhotoValue], PropertyInfo(alias="photoValue")]
    """The value of a photo field. Only present for photo fields."""

    scanned_document_value: Annotated[
        Iterable[FieldValueScannedDocumentValue], PropertyInfo(alias="scannedDocumentValue")
    ]
    """The value of a scanned document field.

    Only present for scanned document fields.
    """

    signature_value: Annotated[FieldValueSignatureValue, PropertyInfo(alias="signatureValue")]
    """The value of a signature field. Only present for signature fields."""

    string_value: Annotated[str, PropertyInfo(alias="stringValue")]
    """The value of a string field. Only present for string fields."""


class Field(TypedDict, total=False):
    label: Required[str]
    """The name of the field."""

    type: Required[
        Literal["photo", "string", "number", "multipleChoice", "signature", "dateTime", "scannedDocument", "barcode"]
    ]
    """The type of field.

    Valid values: `photo`, `string`, `number`, `multipleChoice`, `signature`,
    `dateTime`, `scannedDocument`, `barcode`
    """

    value: FieldValue
    """The value of the document field. The shape of value depends on the type."""
