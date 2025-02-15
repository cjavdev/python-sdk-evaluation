# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .driver_eld_rulesets import DriverEldRulesets
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class DriverEldSettings(UniversalBaseModel):
    """
    The driver's ELD settings.
    """

    rulesets: typing.Optional[DriverEldRulesets] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
