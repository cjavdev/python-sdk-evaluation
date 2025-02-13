# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .forms_asset_object_response_body import FormsAssetObjectResponseBody
import typing_extensions
import datetime as dt
from ..core.serialization import FieldMetadata
import pydantic
from .forms_polymorphic_user_object_response_body import FormsPolymorphicUserObjectResponseBody
from .forms_field_input_object_response_body import FormsFieldInputObjectResponseBody
from .form_template_reference_object_response_body import FormTemplateReferenceObjectResponseBody
from .forms_location_object_response_body import FormsLocationObjectResponseBody
from .forms_score_object_response_body import FormsScoreObjectResponseBody
from .form_submission_response_object_response_body_status import FormSubmissionResponseObjectResponseBodyStatus
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class FormSubmissionResponseObjectResponseBody(UniversalBaseModel):
    """
    Form Submission response object.
    """

    asset: typing.Optional[FormsAssetObjectResponseBody] = None
    assigned_at_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="assignedAtTime")
    ] = pydantic.Field(default=None)
    """
    Assignment time of the form submission. Sometimes returned if the submission was assigned to a user or driver. UTC timestamp in RFC 3339 format.
    """

    assigned_to: typing_extensions.Annotated[
        typing.Optional[FormsPolymorphicUserObjectResponseBody], FieldMetadata(alias="assignedTo")
    ] = None
    created_at_time: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAtTime")] = pydantic.Field()
    """
    Creation time of the form submission. UTC timestamp in RFC 3339 format.
    """

    due_at_time: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="dueAtTime")] = (
        pydantic.Field(default=None)
    )
    """
    Time of when the submission is due. Sometimes returned, if the submission has a due date. UTC timestamp in RFC 3339 format.
    """

    external_ids: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="externalIds")
    ] = pydantic.Field(default=None)
    """
    A map of external ids
    """

    fields: typing.List[FormsFieldInputObjectResponseBody] = pydantic.Field()
    """
    List of field inputs in a form submission.
    """

    form_template: typing_extensions.Annotated[
        FormTemplateReferenceObjectResponseBody, FieldMetadata(alias="formTemplate")
    ]
    id: str = pydantic.Field()
    """
    ID of the form submission.
    """

    is_required: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isRequired")] = pydantic.Field(
        default=None
    )
    """
    Indicates whether the worker is required to complete this form or not. Sometimes returned if the submission was assigned to a worker or route stop.
    """

    location: typing.Optional[FormsLocationObjectResponseBody] = None
    route_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="routeId")] = pydantic.Field(
        default=None
    )
    """
    ID of the route. Sometimes returned if the submission was assigned to a route stop.
    """

    route_stop_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="routeStopId")] = (
        pydantic.Field(default=None)
    )
    """
    ID of the route stop. Sometimes returned if the submission was assigned to a route stop.
    """

    score: typing.Optional[FormsScoreObjectResponseBody] = None
    status: FormSubmissionResponseObjectResponseBodyStatus = pydantic.Field()
    """
    State for the Form Submission. Always returned.  Valid values: `toDo`, `submitted`, `dismissed`
    """

    submitted_at_time: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="submittedAtTime")] = (
        pydantic.Field()
    )
    """
    Submission time of the form submission. UTC timestamp in RFC 3339 format.
    """

    submitted_by: typing_extensions.Annotated[
        FormsPolymorphicUserObjectResponseBody, FieldMetadata(alias="submittedBy")
    ]
    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Title of the form submission. Sometimes returned if the submission has a title.
    """

    updated_at_time: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAtTime")] = pydantic.Field()
    """
    Update time of the form submission. UTC timestamp in RFC 3339 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
