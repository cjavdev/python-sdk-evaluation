# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
import typing
from .v_1_document_base_state import V1DocumentBaseState
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class V1DocumentBase(UniversalBaseModel):
    dispatch_job_id: typing_extensions.Annotated[int, FieldMetadata(alias="dispatchJobId")] = pydantic.Field()
    """
    ID of the Samsara dispatch job for which the document is submitted.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Custom name of the document. If no custom name is given to the document, the admin dashboard and driver app will display the template name as the default document name.
    """

    notes: str = pydantic.Field()
    """
    Notes submitted with this document.
    """

    state: typing.Optional[V1DocumentBaseState] = pydantic.Field(default=None)
    """
    The condition of the document created for the driver. Can be either `Required` or `Submitted`. If no value is specified, `state` defaults to `Required`. `Required` documents are pre-populated documents for the Driver to fill out in the Driver App and have not yet been submitted. `Submitted` documents have been submitted by the driver in the Driver App. `Archived` documents have been archived by the admin in the cloud dashboard.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
