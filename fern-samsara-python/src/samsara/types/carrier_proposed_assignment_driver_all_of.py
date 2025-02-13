# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .carrier_proposed_assignment_driver_all_of_2_external_ids import CarrierProposedAssignmentDriverAllOf2ExternalIds
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class CarrierProposedAssignmentDriverAllOf(UniversalBaseModel):
    external_ids: typing_extensions.Annotated[
        typing.Optional[CarrierProposedAssignmentDriverAllOf2ExternalIds], FieldMetadata(alias="externalIds")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
