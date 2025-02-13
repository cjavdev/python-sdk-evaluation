# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "FormSubmissionCreateParams",
    "FormTemplate",
    "AssignedTo",
    "Field",
    "FieldAssetValue",
    "FieldAssetValueAsset",
    "FieldCheckBoxesValue",
    "FieldDateTimeValue",
    "FieldMultipleChoiceValue",
    "FieldNumberValue",
    "FieldPersonValue",
    "FieldPersonValuePerson",
    "FieldTableValue",
    "FieldTableValueRow",
    "FieldTableValueRowCell",
    "FieldTableValueRowCellCheckBoxesValue",
    "FieldTableValueRowCellDateTimeValue",
    "FieldTableValueRowCellMultipleChoiceValue",
    "FieldTableValueRowCellNumberValue",
    "FieldTableValueRowCellPersonValue",
    "FieldTableValueRowCellPersonValuePerson",
    "FieldTableValueRowCellTextValue",
    "FieldTextValue",
]


class FormSubmissionCreateParams(TypedDict, total=False):
    form_template: Required[Annotated[FormTemplate, PropertyInfo(alias="formTemplate")]]
    """Form template reference object."""

    status: Required[Literal["toDo"]]
    """Status of the form submission. Valid values: `toDo`"""

    assigned_to: Annotated[AssignedTo, PropertyInfo(alias="assignedTo")]
    """Form submission assignee update object"""

    due_at_time: Annotated[Union[str, datetime], PropertyInfo(alias="dueAtTime", format="iso8601")]
    """Due date of the form submission. UTC timestamp in RFC 3339 format."""

    fields: Iterable[Field]
    """List of field inputs in a form submission."""

    title: str
    """Title of the form submission."""


class FormTemplate(TypedDict, total=False):
    id: Required[str]
    """ID of the form template."""

    revision_id: Required[Annotated[str, PropertyInfo(alias="revisionId")]]
    """ID of the form template revision."""


class AssignedTo(TypedDict, total=False):
    id: Required[str]
    """ID of the form submission assignee."""

    type: Required[Literal["driver"]]
    """Type of the form submission assignee. Valid values: `driver`"""


class FieldAssetValueAsset(TypedDict, total=False):
    id: Required[str]
    """Samsara ID of the asset."""


class FieldAssetValue(TypedDict, total=False):
    asset: Required[FieldAssetValueAsset]
    """Asset object."""


class FieldCheckBoxesValue(TypedDict, total=False):
    value_ids: Required[Annotated[List[str], PropertyInfo(alias="valueIds")]]


class FieldDateTimeValue(TypedDict, total=False):
    value: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The value of the user generated date/time field response.

    UTC timestamp in RFC 3339 format.
    """


class FieldMultipleChoiceValue(TypedDict, total=False):
    value_id: Required[Annotated[str, PropertyInfo(alias="valueId")]]


class FieldNumberValue(TypedDict, total=False):
    value: Required[float]


class FieldPersonValuePerson(TypedDict, total=False):
    polymorphic_user_id: Required[Annotated[str, PropertyInfo(alias="polymorphicUserId")]]
    """Samsara polymorphicUserID of the person."""


class FieldPersonValue(TypedDict, total=False):
    person: Required[FieldPersonValuePerson]
    """Person object."""


class FieldTableValueRowCellCheckBoxesValue(TypedDict, total=False):
    value_ids: Required[Annotated[List[str], PropertyInfo(alias="valueIds")]]


class FieldTableValueRowCellDateTimeValue(TypedDict, total=False):
    value: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The value of the user generated date/time field response.

    UTC timestamp in RFC 3339 format.
    """


class FieldTableValueRowCellMultipleChoiceValue(TypedDict, total=False):
    value_id: Required[Annotated[str, PropertyInfo(alias="valueId")]]


class FieldTableValueRowCellNumberValue(TypedDict, total=False):
    value: Required[float]


class FieldTableValueRowCellPersonValuePerson(TypedDict, total=False):
    polymorphic_user_id: Required[Annotated[str, PropertyInfo(alias="polymorphicUserId")]]
    """Samsara polymorphicUserID of the person."""


class FieldTableValueRowCellPersonValue(TypedDict, total=False):
    person: Required[FieldTableValueRowCellPersonValuePerson]
    """Person object."""


class FieldTableValueRowCellTextValue(TypedDict, total=False):
    value: Required[str]


class FieldTableValueRowCell(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the cell."""

    type: Required[Literal["number", "text", "multiple_choice", "check_boxes", "datetime", "person"]]
    """Type of the cell field.

    Valid values: `number`, `text`, `multiple_choice`, `check_boxes`, `datetime`,
    `person`
    """

    check_boxes_value: Annotated[FieldTableValueRowCellCheckBoxesValue, PropertyInfo(alias="checkBoxesValue")]
    """The value of a check boxes form input field.

    Only valid for check boxes form input fields.
    """

    date_time_value: Annotated[FieldTableValueRowCellDateTimeValue, PropertyInfo(alias="dateTimeValue")]
    """The value of a datetime form input field.

    Only valid for datetime form input fields.
    """

    multiple_choice_value: Annotated[
        FieldTableValueRowCellMultipleChoiceValue, PropertyInfo(alias="multipleChoiceValue")
    ]
    """The value of a multiple choice form input field.

    Only valid for multiple choice form input fields.
    """

    number_value: Annotated[FieldTableValueRowCellNumberValue, PropertyInfo(alias="numberValue")]
    """The value of a number form input field.

    Only valid for number form input fields.
    """

    person_value: Annotated[FieldTableValueRowCellPersonValue, PropertyInfo(alias="personValue")]
    """The value of an person form input field.

    Only valid for person form input fields.
    """

    text_value: Annotated[FieldTableValueRowCellTextValue, PropertyInfo(alias="textValue")]
    """The value of a text form input field. Only valid for text form input fields."""


class FieldTableValueRow(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the row."""

    cells: Required[Iterable[FieldTableValueRowCell]]
    """List of cells in the row."""


class FieldTableValue(TypedDict, total=False):
    rows: Required[Iterable[FieldTableValueRow]]
    """List of rows in the table."""


class FieldTextValue(TypedDict, total=False):
    value: Required[str]


class Field(TypedDict, total=False):
    id: Required[str]
    """ID of the forms input field object."""

    type: Required[Literal["number", "text", "multiple_choice", "check_boxes", "datetime", "asset", "person", "table"]]
    """Type of the field.

    Valid values: `number`, `text`, `multiple_choice`, `check_boxes`, `datetime`,
    `asset`, `person`, `table`
    """

    asset_value: Annotated[FieldAssetValue, PropertyInfo(alias="assetValue")]
    """The value of an asset form input field. Only valid for asset form input fields."""

    check_boxes_value: Annotated[FieldCheckBoxesValue, PropertyInfo(alias="checkBoxesValue")]
    """The value of a check boxes form input field.

    Only valid for check boxes form input fields.
    """

    date_time_value: Annotated[FieldDateTimeValue, PropertyInfo(alias="dateTimeValue")]
    """The value of a datetime form input field.

    Only valid for datetime form input fields.
    """

    multiple_choice_value: Annotated[FieldMultipleChoiceValue, PropertyInfo(alias="multipleChoiceValue")]
    """The value of a multiple choice form input field.

    Only valid for multiple choice form input fields.
    """

    number_value: Annotated[FieldNumberValue, PropertyInfo(alias="numberValue")]
    """The value of a number form input field.

    Only valid for number form input fields.
    """

    person_value: Annotated[FieldPersonValue, PropertyInfo(alias="personValue")]
    """The value of an person form input field.

    Only valid for person form input fields.
    """

    table_value: Annotated[FieldTableValue, PropertyInfo(alias="tableValue")]
    """The value of a table form input field. Only valid for table form input fields."""

    text_value: Annotated[FieldTextValue, PropertyInfo(alias="textValue")]
    """The value of a text form input field. Only valid for text form input fields."""
