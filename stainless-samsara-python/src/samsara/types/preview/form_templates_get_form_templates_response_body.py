# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "FormTemplatesGetFormTemplatesResponseBody",
    "Data",
    "DataCreatedBy",
    "DataField",
    "DataFieldOption",
    "DataSection",
    "DataUpdatedBy",
    "DataApprovalConfig",
    "DataApprovalConfigSingleApprovalConfig",
    "DataApprovalConfigSingleApprovalConfigRequirements",
    "Pagination",
]


class DataCreatedBy(BaseModel):
    id: str
    """ID of the polymorphic user."""

    type: Literal["driver", "user"]
    """The type of the polymorphic user. Valid values: `driver`, `user`"""


class DataFieldOption(BaseModel):
    id: str
    """Identifier of the option."""

    label: str
    """Label of the option."""

    ignore_question_from_score_if_selected: Optional[bool] = FieldInfo(
        alias="ignoreQuestionFromScoreIfSelected", default=None
    )
    """
    Indicates whether the question should be ignored from the total score if this
    option is selected. Returns true if a score weight was not given to this option.
    Only present when the select form field has scoring.
    """

    option_score_weight: Optional[int] = FieldInfo(alias="optionScoreWeight", default=None)
    """
    Score weight of the option, indicates number of score points received if this
    option is selected. Only present if the select form field has scoring.
    """


class DataField(BaseModel):
    id: str
    """Identifier of the field."""

    is_required: bool = FieldInfo(alias="isRequired")
    """Indicates whether the form field is required to be filled out by the user."""

    label: str
    """Label of the field."""

    type: Literal[
        "number",
        "text",
        "multiple_choice",
        "check_boxes",
        "media",
        "datetime",
        "signature",
        "asset",
        "person",
        "geofence",
        "instruction",
        "media_instruction",
    ]
    """Type of the field.

    Valid values: `number`, `text`, `multiple_choice`, `check_boxes`, `media`,
    `datetime`, `signature`, `asset`, `person`, `geofence`, `instruction`,
    `media_instruction`
    """

    allowed_asset_types: Optional[List[Literal["Vehicle", "Trailer", "Equipment", "UnpoweredAsset"]]] = FieldInfo(
        alias="allowedAssetTypes", default=None
    )
    """List of allowed asset types that can be selected for this field.

    Only present for asset fields.
    """

    allowed_date_time_value_type: Optional[Literal["datetime", "date", "time"]] = FieldInfo(
        alias="allowedDateTimeValueType", default=None
    )
    """Type of date/time entry allowed for this question.

    Only present for datetime fields. Valid values: `datetime`, `date`, `time`
    """

    allow_manual_entry: Optional[bool] = FieldInfo(alias="allowManualEntry", default=None)
    """Indicates whether the field allows manual entry of a person.

    Only present for person fields.
    """

    filter_by_current_driver_tags: Optional[bool] = FieldInfo(alias="filterByCurrentDriverTags", default=None)
    """
    Indicates whether the person search filters by the current logged in worker's
    tags. Only present for person fields.
    """

    filter_by_role_ids: Optional[List[str]] = FieldInfo(alias="filterByRoleIds", default=None)
    """
    List of role IDs to filter org users by, representing which roles are selectable
    people for this field. Only present for person fields.
    """

    include_drivers: Optional[bool] = FieldInfo(alias="includeDrivers", default=None)
    """Indicates whether the field includes drivers as selectable people.

    Only present for person fields.
    """

    include_users: Optional[bool] = FieldInfo(alias="includeUsers", default=None)
    """Indicates whether the field includes users as selectable people.

    Only present for person fields.
    """

    legal_text: Optional[str] = FieldInfo(alias="legalText", default=None)
    """Legal text for the field. Only present for signature fields."""

    num_decimal_places: Optional[int] = FieldInfo(alias="numDecimalPlaces", default=None)
    """Number of decimal places allowed. Only present for number fields."""

    options: Optional[List[DataFieldOption]] = None
    """List of select options for checkboxes or multiple choice fields."""

    question_weight: Optional[int] = FieldInfo(alias="questionWeight", default=None)
    """The maximum possible score weight for this field.

    For multiple choice fields, this number is the highest option score weight of
    the given options. For checkboxes fields, this number is the sum of the score
    weights for all scored options. Only present for multiple choice or checkboxes
    fields that have scoring.
    """


class DataSection(BaseModel):
    field_index_first_inclusive: int = FieldInfo(alias="fieldIndexFirstInclusive")
    """The index of the first field from the fields array that is in this section.

    Index 0 represents the first field definition of the fields array.
    """

    field_index_last_inclusive: int = FieldInfo(alias="fieldIndexLastInclusive")
    """The index of the last field from the fields array that is in this section."""

    label: str
    """Label of the section."""


class DataUpdatedBy(BaseModel):
    id: str
    """ID of the polymorphic user."""

    type: Literal["driver", "user"]
    """The type of the polymorphic user. Valid values: `driver`, `user`"""


class DataApprovalConfigSingleApprovalConfigRequirements(BaseModel):
    role_ids: List[str] = FieldInfo(alias="roleIds")
    """List of role IDs representing which user roles can be approvers."""


class DataApprovalConfigSingleApprovalConfig(BaseModel):
    allow_manual_approver_selection: bool = FieldInfo(alias="allowManualApproverSelection")
    """Indicates whether approver can be manually selected. True by default."""

    requirements: DataApprovalConfigSingleApprovalConfigRequirements
    """Single approval requirements object."""


class DataApprovalConfig(BaseModel):
    type: Literal["singleApproval"]
    """Type of approval. Valid values: `singleApproval`"""

    single_approval_config: Optional[DataApprovalConfigSingleApprovalConfig] = FieldInfo(
        alias="singleApprovalConfig", default=None
    )
    """Single approval configuration object."""


class Data(BaseModel):
    id: str
    """Unique identifier of the form template."""

    created_at_time: datetime = FieldInfo(alias="createdAtTime")
    """Creation time of the form template. UTC timestamp in RFC 3339 format."""

    created_by: DataCreatedBy = FieldInfo(alias="createdBy")
    """User or driver object."""

    description: str
    """Description of the form template."""

    fields: List[DataField]
    """List of fields in the form template."""

    revision_id: str = FieldInfo(alias="revisionId")
    """Unique identifier of the form template revision."""

    sections: List[DataSection]
    """List of sections in the form template."""

    title: str
    """Title of the form template."""

    updated_at_time: datetime = FieldInfo(alias="updatedAtTime")
    """Update time of the form template. UTC timestamp in RFC 3339 format."""

    updated_by: DataUpdatedBy = FieldInfo(alias="updatedBy")
    """User or driver object."""

    approval_config: Optional[DataApprovalConfig] = FieldInfo(alias="approvalConfig", default=None)
    """Form Template approval configuration object."""


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


class FormTemplatesGetFormTemplatesResponseBody(BaseModel):
    data: List[Data]
    """List of form templates."""

    pagination: Pagination
    """Pagination parameters."""
