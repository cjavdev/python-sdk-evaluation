# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class PanicButtonDetailsObjectRequestBody(UniversalBaseModel):
    """
    Details specific to Panic Button
    """

    is_filtering_out_power_loss: typing_extensions.Annotated[bool, FieldMetadata(alias="isFilteringOutPowerLoss")] = (
        pydantic.Field()
    )
    """
    If true, only receive alerts when the panic button is pressed, otherwise receive alerts when the panic button is pressed or looses connection.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
