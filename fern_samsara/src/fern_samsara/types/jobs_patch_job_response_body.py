# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .job_response_object_response_body import JobResponseObjectResponseBody
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class JobsPatchJobResponseBody(UniversalBaseModel):
    data: JobResponseObjectResponseBody
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The job id of the failed request
    """

    uuid_: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="uuid")] = pydantic.Field(default=None)
    """
    The uuid of the failed request
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
