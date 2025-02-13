# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .forms_asset_object_response_body import FormsAssetObjectResponseBody
import typing_extensions
from .forms_polymorphic_user_object_response_body import FormsPolymorphicUserObjectResponseBody
from ..core.serialization import FieldMetadata
import datetime as dt
import pydantic
from .issue_source_object_response_body import IssueSourceObjectResponseBody
from .forms_media_record_object_response_body import FormsMediaRecordObjectResponseBody
from .issue_response_object_response_body_priority import IssueResponseObjectResponseBodyPriority
from .issue_response_object_response_body_status import IssueResponseObjectResponseBodyStatus
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class IssueResponseObjectResponseBody(UniversalBaseModel):
    """
    Issue response object.
    """

    asset: typing.Optional[FormsAssetObjectResponseBody] = None
    assigned_to: typing_extensions.Annotated[
        typing.Optional[FormsPolymorphicUserObjectResponseBody], FieldMetadata(alias="assignedTo")
    ] = None
    created_at_time: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAtTime")] = pydantic.Field()
    """
    Creation time of the issue. UTC timestamp in RFC 3339 format.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the issue. Included if the issue was given a description.
    """

    due_date: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="dueDate")] = (
        pydantic.Field(default=None)
    )
    """
    Due date of the issue. UTC timestamp in RFC 3339 format. Included if the issue was assigned a due date.
    """

    external_ids: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="externalIds")
    ] = pydantic.Field(default=None)
    """
    A map of external ids
    """

    id: str = pydantic.Field()
    """
    ID of the issue.
    """

    issue_source: typing_extensions.Annotated[IssueSourceObjectResponseBody, FieldMetadata(alias="issueSource")]
    media_list: typing_extensions.Annotated[
        typing.Optional[typing.List[FormsMediaRecordObjectResponseBody]], FieldMetadata(alias="mediaList")
    ] = pydantic.Field(default=None)
    """
    List of media objects for the issue. Included if the issue has media.
    """

    priority: typing.Optional[IssueResponseObjectResponseBodyPriority] = pydantic.Field(default=None)
    """
    Priority of the issue. Included if the issue was assigned a priority.  Valid values: `low`, `medium`, `high`
    """

    status: IssueResponseObjectResponseBodyStatus = pydantic.Field()
    """
    Status of the issue.  Valid values: `open`, `inProgress`, `resolved`, `dismissed`
    """

    submitted_at_time: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="submittedAtTime")] = (
        pydantic.Field()
    )
    """
    Submission time of the issue. UTC timestamp in RFC 3339 format.
    """

    submitted_by: typing_extensions.Annotated[
        FormsPolymorphicUserObjectResponseBody, FieldMetadata(alias="submittedBy")
    ]
    title: str = pydantic.Field()
    """
    Title of the issue.
    """

    updated_at_time: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAtTime")] = pydantic.Field()
    """
    Update time of the issue. UTC timestamp in RFC 3339 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
