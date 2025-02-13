# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "DocumentTypeListResponse",
    "Data",
    "DataConditionalFieldSection",
    "DataFieldType",
    "DataFieldTypeMultipleChoiceFieldTypeMetaData",
    "DataFieldTypeNumberFieldTypeMetaData",
    "DataFieldTypeSignatureFieldTypeMetaData",
    "Pagination",
]


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


class DataFieldTypeMultipleChoiceFieldTypeMetaData(BaseModel):
    label: Optional[str] = None
    """The option choice label."""


class DataFieldTypeNumberFieldTypeMetaData(BaseModel):
    number_of_decimal_places: Optional[int] = FieldInfo(alias="numberOfDecimalPlaces", default=None)
    """The number of decimal places allowed for the field."""


class DataFieldTypeSignatureFieldTypeMetaData(BaseModel):
    legal_text: Optional[str] = FieldInfo(alias="legalText", default=None)
    """The signature field legal text."""


class DataFieldType(BaseModel):
    field_type: Literal[
        "photo", "string", "number", "multipleChoice", "signature", "dateTime", "scannedDocument", "barcode"
    ] = FieldInfo(alias="fieldType")
    """The type of value this field can have.

    Valid values: `photo`, `string`, `number`, `multipleChoice`, `signature`,
    `dateTime`, `scannedDocument`, `barcode`
    """

    label: str
    """The name of the field type."""

    required_field: bool = FieldInfo(alias="requiredField")
    """The indicator that states if the field is required."""

    multiple_choice_field_type_meta_data: Optional[List[DataFieldTypeMultipleChoiceFieldTypeMetaData]] = FieldInfo(
        alias="multipleChoiceFieldTypeMetaData", default=None
    )
    """A list of the multiple choice field option labels."""

    number_field_type_meta_data: Optional[DataFieldTypeNumberFieldTypeMetaData] = FieldInfo(
        alias="numberFieldTypeMetaData", default=None
    )
    """The number field metadata."""

    signature_field_type_meta_data: Optional[DataFieldTypeSignatureFieldTypeMetaData] = FieldInfo(
        alias="signatureFieldTypeMetaData", default=None
    )
    """The signature field metadata."""


class Data(BaseModel):
    id: Optional[str] = None
    """Universally unique identifier for the document type.

    This value can be passed in as the documentTypeId when creating a document.
    """

    conditional_field_sections: Optional[List[DataConditionalFieldSection]] = FieldInfo(
        alias="conditionalFieldSections", default=None
    )
    """List of the document type conditional field sections."""

    field_types: Optional[List[DataFieldType]] = FieldInfo(alias="fieldTypes", default=None)
    """The fields associated with this document type."""

    name: Optional[str] = None
    """Name of the document type."""

    org_id: Optional[int] = FieldInfo(alias="orgId", default=None)
    """ID for the organization this document type belongs to."""


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


class DocumentTypeListResponse(BaseModel):
    data: List[Data]
    """List of all document types for the organization"""

    pagination: Pagination
    """Pagination parameters."""
