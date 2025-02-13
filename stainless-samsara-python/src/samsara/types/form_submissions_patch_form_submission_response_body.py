# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "FormSubmissionsPatchFormSubmissionResponseBody",
    "Data",
    "DataField",
    "DataFieldAssetValue",
    "DataFieldAssetValueAsset",
    "DataFieldCheckBoxesValue",
    "DataFieldDateTimeValue",
    "DataFieldIssue",
    "DataFieldMediaList",
    "DataFieldMediaValue",
    "DataFieldMediaValueMediaList",
    "DataFieldMultipleChoiceValue",
    "DataFieldNumberValue",
    "DataFieldPersonValue",
    "DataFieldPersonValuePerson",
    "DataFieldPersonValuePersonPolymorphicUserID",
    "DataFieldSignatureValue",
    "DataFieldSignatureValueMedia",
    "DataFieldTableValue",
    "DataFieldTableValueColumn",
    "DataFieldTableValueRow",
    "DataFieldTableValueRowCell",
    "DataFieldTableValueRowCellCheckBoxesValue",
    "DataFieldTableValueRowCellDateTimeValue",
    "DataFieldTableValueRowCellMediaValue",
    "DataFieldTableValueRowCellMediaValueMediaList",
    "DataFieldTableValueRowCellMultipleChoiceValue",
    "DataFieldTableValueRowCellNumberValue",
    "DataFieldTableValueRowCellPersonValue",
    "DataFieldTableValueRowCellPersonValuePerson",
    "DataFieldTableValueRowCellPersonValuePersonPolymorphicUserID",
    "DataFieldTableValueRowCellSignatureValue",
    "DataFieldTableValueRowCellSignatureValueMedia",
    "DataFieldTableValueRowCellTextValue",
    "DataFieldTextValue",
    "DataFormTemplate",
    "DataSubmittedBy",
    "DataAsset",
    "DataAssignedTo",
    "DataLocation",
    "DataScore",
]


class DataFieldAssetValueAsset(BaseModel):
    entry_type: Literal["tracked", "untracked"] = FieldInfo(alias="entryType")
    """The type of entry for the asset. Valid values: `tracked`, `untracked`"""

    id: Optional[str] = None
    """ID of a tracked asset. Included if 'entryType' is 'tracked'."""

    name: Optional[str] = None
    """Name of an untracked (i.e. manually entered) asset."""


class DataFieldAssetValue(BaseModel):
    asset: DataFieldAssetValueAsset
    """Tracked or untracked (i.e. manually entered) asset object."""


class DataFieldCheckBoxesValue(BaseModel):
    value: List[str]
    """List of selected options."""


class DataFieldDateTimeValue(BaseModel):
    type: Literal["datetime", "date", "time"]
    """The type of datetime format. Valid values: `datetime`, `date`, `time`"""

    value: datetime
    """UTC timestamp in RFC 3339 format."""


class DataFieldIssue(BaseModel):
    id: str
    """ID of the issue created from this form input field input object."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""


class DataFieldMediaList(BaseModel):
    id: str
    """ID of the media record."""

    processing_status: Literal["unknown", "processing", "finished"] = FieldInfo(alias="processingStatus")
    """Status of the media record. Valid values: `unknown`, `processing`, `finished`"""

    url: Optional[str] = None
    """URL containing a link to associated media content.

    Included if 'processingStatus' is 'finished'.
    """

    url_expires_at: Optional[datetime] = FieldInfo(alias="urlExpiresAt", default=None)
    """Expiration time of the media record 'url'. UTC timestamp in RFC 3339 format."""


class DataFieldMediaValueMediaList(BaseModel):
    id: str
    """ID of the media record."""

    processing_status: Literal["unknown", "processing", "finished"] = FieldInfo(alias="processingStatus")
    """Status of the media record. Valid values: `unknown`, `processing`, `finished`"""

    url: Optional[str] = None
    """URL containing a link to associated media content.

    Included if 'processingStatus' is 'finished'.
    """

    url_expires_at: Optional[datetime] = FieldInfo(alias="urlExpiresAt", default=None)
    """Expiration time of the media record 'url'. UTC timestamp in RFC 3339 format."""


class DataFieldMediaValue(BaseModel):
    media_list: List[DataFieldMediaValueMediaList] = FieldInfo(alias="mediaList")
    """List of forms media record objects."""


class DataFieldMultipleChoiceValue(BaseModel):
    value: str
    """Selected choice."""


class DataFieldNumberValue(BaseModel):
    value: float
    """Number value."""


class DataFieldPersonValuePersonPolymorphicUserID(BaseModel):
    id: str
    """ID of the polymorphic user."""

    type: Literal["driver", "user"]
    """The type of the polymorphic user. Valid values: `driver`, `user`"""


class DataFieldPersonValuePerson(BaseModel):
    entry_type: Literal["tracked", "untracked"] = FieldInfo(alias="entryType")
    """The type of entry for the person. Valid values: `tracked`, `untracked`"""

    name: Optional[str] = None
    """Name of an untracked (i.e. manually entered) person."""

    polymorphic_user_id: Optional[DataFieldPersonValuePersonPolymorphicUserID] = FieldInfo(
        alias="polymorphicUserId", default=None
    )
    """User or driver object."""


class DataFieldPersonValue(BaseModel):
    person: DataFieldPersonValuePerson
    """Tracked or untracked (i.e. manually entered) person object."""


class DataFieldSignatureValueMedia(BaseModel):
    id: str
    """ID of the media record."""

    processing_status: Literal["unknown", "processing", "finished"] = FieldInfo(alias="processingStatus")
    """Status of the media record. Valid values: `unknown`, `processing`, `finished`"""

    url: Optional[str] = None
    """URL containing a link to associated media content.

    Included if 'processingStatus' is 'finished'.
    """

    url_expires_at: Optional[datetime] = FieldInfo(alias="urlExpiresAt", default=None)
    """Expiration time of the media record 'url'. UTC timestamp in RFC 3339 format."""


class DataFieldSignatureValue(BaseModel):
    media: DataFieldSignatureValueMedia
    """Forms media record object."""


class DataFieldTableValueColumn(BaseModel):
    id: str
    """Unique identifier for the column."""

    label: str
    """Label of the column."""

    type: Literal["text, number, datetime, check_boxes, multiple_choice, signature, media, person"]
    """Type of the column field.

    Valid values:
    `text, number, datetime, check_boxes, multiple_choice, signature, media, person`
    """


class DataFieldTableValueRowCellCheckBoxesValue(BaseModel):
    value: List[str]
    """List of selected options."""


class DataFieldTableValueRowCellDateTimeValue(BaseModel):
    type: Literal["datetime", "date", "time"]
    """The type of datetime format. Valid values: `datetime`, `date`, `time`"""

    value: datetime
    """UTC timestamp in RFC 3339 format."""


class DataFieldTableValueRowCellMediaValueMediaList(BaseModel):
    id: str
    """ID of the media record."""

    processing_status: Literal["unknown", "processing", "finished"] = FieldInfo(alias="processingStatus")
    """Status of the media record. Valid values: `unknown`, `processing`, `finished`"""

    url: Optional[str] = None
    """URL containing a link to associated media content.

    Included if 'processingStatus' is 'finished'.
    """

    url_expires_at: Optional[datetime] = FieldInfo(alias="urlExpiresAt", default=None)
    """Expiration time of the media record 'url'. UTC timestamp in RFC 3339 format."""


class DataFieldTableValueRowCellMediaValue(BaseModel):
    media_list: List[DataFieldTableValueRowCellMediaValueMediaList] = FieldInfo(alias="mediaList")
    """List of forms media record objects."""


class DataFieldTableValueRowCellMultipleChoiceValue(BaseModel):
    value: str
    """Selected choice."""


class DataFieldTableValueRowCellNumberValue(BaseModel):
    value: float
    """Number value."""


class DataFieldTableValueRowCellPersonValuePersonPolymorphicUserID(BaseModel):
    id: str
    """ID of the polymorphic user."""

    type: Literal["driver", "user"]
    """The type of the polymorphic user. Valid values: `driver`, `user`"""


class DataFieldTableValueRowCellPersonValuePerson(BaseModel):
    entry_type: Literal["tracked", "untracked"] = FieldInfo(alias="entryType")
    """The type of entry for the person. Valid values: `tracked`, `untracked`"""

    name: Optional[str] = None
    """Name of an untracked (i.e. manually entered) person."""

    polymorphic_user_id: Optional[DataFieldTableValueRowCellPersonValuePersonPolymorphicUserID] = FieldInfo(
        alias="polymorphicUserId", default=None
    )
    """User or driver object."""


class DataFieldTableValueRowCellPersonValue(BaseModel):
    person: DataFieldTableValueRowCellPersonValuePerson
    """Tracked or untracked (i.e. manually entered) person object."""


class DataFieldTableValueRowCellSignatureValueMedia(BaseModel):
    id: str
    """ID of the media record."""

    processing_status: Literal["unknown", "processing", "finished"] = FieldInfo(alias="processingStatus")
    """Status of the media record. Valid values: `unknown`, `processing`, `finished`"""

    url: Optional[str] = None
    """URL containing a link to associated media content.

    Included if 'processingStatus' is 'finished'.
    """

    url_expires_at: Optional[datetime] = FieldInfo(alias="urlExpiresAt", default=None)
    """Expiration time of the media record 'url'. UTC timestamp in RFC 3339 format."""


class DataFieldTableValueRowCellSignatureValue(BaseModel):
    media: DataFieldTableValueRowCellSignatureValueMedia
    """Forms media record object."""


class DataFieldTableValueRowCellTextValue(BaseModel):
    value: str
    """Text value."""


class DataFieldTableValueRowCell(BaseModel):
    id: str
    """Unique identifier for the cell."""

    type: Literal["number, text, multiple_choice, check_boxes, datetime, signature, media, person"]
    """Type of the cell field.

    Valid values:
    `number, text, multiple_choice, check_boxes, datetime, signature, media, person`
    """

    check_boxes_value: Optional[DataFieldTableValueRowCellCheckBoxesValue] = FieldInfo(
        alias="checkBoxesValue", default=None
    )
    """The value of a check boxes form input field."""

    date_time_value: Optional[DataFieldTableValueRowCellDateTimeValue] = FieldInfo(alias="dateTimeValue", default=None)
    """The value of a datetime form input field."""

    media_value: Optional[DataFieldTableValueRowCellMediaValue] = FieldInfo(alias="mediaValue", default=None)
    """The value of a media form input field."""

    multiple_choice_value: Optional[DataFieldTableValueRowCellMultipleChoiceValue] = FieldInfo(
        alias="multipleChoiceValue", default=None
    )
    """The value of a multiple choice form input field."""

    number_value: Optional[DataFieldTableValueRowCellNumberValue] = FieldInfo(alias="numberValue", default=None)
    """The value of a number form input field."""

    person_value: Optional[DataFieldTableValueRowCellPersonValue] = FieldInfo(alias="personValue", default=None)
    """The value of a person form input field."""

    signature_value: Optional[DataFieldTableValueRowCellSignatureValue] = FieldInfo(
        alias="signatureValue", default=None
    )
    """The value of a signature form input field."""

    text_value: Optional[DataFieldTableValueRowCellTextValue] = FieldInfo(alias="textValue", default=None)
    """The value of a text form input field."""


class DataFieldTableValueRow(BaseModel):
    id: str
    """Unique identifier for the row."""

    cells: List[DataFieldTableValueRowCell]
    """List of cells in the row."""


class DataFieldTableValue(BaseModel):
    columns: List[DataFieldTableValueColumn]
    """List of table columns."""

    rows: List[DataFieldTableValueRow]
    """List of table rows."""


class DataFieldTextValue(BaseModel):
    value: str
    """Text value."""


class DataField(BaseModel):
    id: str
    """ID of the forms input field object."""

    type: Literal["number, text, multiple_choice, check_boxes, datetime, signature, media, asset, table"]
    """Type of the field.

    Valid values:
    `number, text, multiple_choice, check_boxes, datetime, signature, media, asset, table`
    """

    asset_value: Optional[DataFieldAssetValue] = FieldInfo(alias="assetValue", default=None)
    """The value of an asset form input field."""

    check_boxes_value: Optional[DataFieldCheckBoxesValue] = FieldInfo(alias="checkBoxesValue", default=None)
    """The value of a check boxes form input field."""

    date_time_value: Optional[DataFieldDateTimeValue] = FieldInfo(alias="dateTimeValue", default=None)
    """The value of a datetime form input field."""

    issue: Optional[DataFieldIssue] = None
    """Issue created from this form input field input object."""

    label: Optional[str] = None
    """Forms input field label."""

    media_list: Optional[List[DataFieldMediaList]] = FieldInfo(alias="mediaList", default=None)
    """List of forms media record objects."""

    media_value: Optional[DataFieldMediaValue] = FieldInfo(alias="mediaValue", default=None)
    """The value of a media form input field."""

    multiple_choice_value: Optional[DataFieldMultipleChoiceValue] = FieldInfo(alias="multipleChoiceValue", default=None)
    """The value of a multiple choice form input field."""

    note: Optional[str] = None
    """A note attached to the field input."""

    number_value: Optional[DataFieldNumberValue] = FieldInfo(alias="numberValue", default=None)
    """The value of a number form input field."""

    person_value: Optional[DataFieldPersonValue] = FieldInfo(alias="personValue", default=None)
    """The value of a person form input field."""

    signature_value: Optional[DataFieldSignatureValue] = FieldInfo(alias="signatureValue", default=None)
    """The value of a signature form input field."""

    table_value: Optional[DataFieldTableValue] = FieldInfo(alias="tableValue", default=None)
    """The value of a table form input field."""

    text_value: Optional[DataFieldTextValue] = FieldInfo(alias="textValue", default=None)
    """The value of a text form input field."""


class DataFormTemplate(BaseModel):
    id: str
    """ID of the form template."""

    revision_id: str = FieldInfo(alias="revisionId")
    """ID of the form template revision."""


class DataSubmittedBy(BaseModel):
    id: str
    """ID of the polymorphic user."""

    type: Literal["driver", "user"]
    """The type of the polymorphic user. Valid values: `driver`, `user`"""


class DataAsset(BaseModel):
    entry_type: Literal["tracked", "untracked"] = FieldInfo(alias="entryType")
    """The type of entry for the asset. Valid values: `tracked`, `untracked`"""

    id: Optional[str] = None
    """ID of a tracked asset. Included if 'entryType' is 'tracked'."""

    name: Optional[str] = None
    """Name of an untracked (i.e. manually entered) asset."""


class DataAssignedTo(BaseModel):
    id: str
    """ID of the polymorphic user."""

    type: Literal["driver", "user"]
    """The type of the polymorphic user. Valid values: `driver`, `user`"""


class DataLocation(BaseModel):
    latitude: float
    """Latitude of a location."""

    longitude: float
    """Longitude of a location."""


class DataScore(BaseModel):
    max_points: float = FieldInfo(alias="maxPoints")
    """Total possible points of the form submission."""

    score_percent: float = FieldInfo(alias="scorePercent")
    """Percentage score of the form submission, calculated as scorePoints / maxPoints."""

    score_points: float = FieldInfo(alias="scorePoints")
    """Score, in points, of the form submission."""


class Data(BaseModel):
    id: str
    """ID of the form submission."""

    created_at_time: datetime = FieldInfo(alias="createdAtTime")
    """Creation time of the form submission. UTC timestamp in RFC 3339 format."""

    fields: List[DataField]
    """List of field inputs in a form submission."""

    form_template: DataFormTemplate = FieldInfo(alias="formTemplate")
    """Form template reference object."""

    status: Literal["toDo", "submitted", "dismissed"]
    """State for the Form Submission.

    Always returned. Valid values: `toDo`, `submitted`, `dismissed`
    """

    submitted_at_time: datetime = FieldInfo(alias="submittedAtTime")
    """Submission time of the form submission. UTC timestamp in RFC 3339 format."""

    submitted_by: DataSubmittedBy = FieldInfo(alias="submittedBy")
    """User or driver object."""

    updated_at_time: datetime = FieldInfo(alias="updatedAtTime")
    """Update time of the form submission. UTC timestamp in RFC 3339 format."""

    asset: Optional[DataAsset] = None
    """Tracked or untracked (i.e. manually entered) asset object."""

    assigned_at_time: Optional[datetime] = FieldInfo(alias="assignedAtTime", default=None)
    """Assignment time of the form submission.

    Sometimes returned if the submission was assigned to a user or driver. UTC
    timestamp in RFC 3339 format.
    """

    assigned_to: Optional[DataAssignedTo] = FieldInfo(alias="assignedTo", default=None)
    """User or driver object."""

    due_at_time: Optional[datetime] = FieldInfo(alias="dueAtTime", default=None)
    """Time of when the submission is due.

    Sometimes returned, if the submission has a due date. UTC timestamp in RFC 3339
    format.
    """

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    is_required: Optional[bool] = FieldInfo(alias="isRequired", default=None)
    """Indicates whether the worker is required to complete this form or not.

    Sometimes returned if the submission was assigned to a user or driver.
    """

    location: Optional[DataLocation] = None
    """Form template location object."""

    score: Optional[DataScore] = None
    """Forms score object."""

    title: Optional[str] = None
    """Title of the form submission. Sometimes returned if the submission has a title."""


class FormSubmissionsPatchFormSubmissionResponseBody(BaseModel):
    data: Data
    """Form Submission response object."""
