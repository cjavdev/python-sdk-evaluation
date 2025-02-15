# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .settings_compliance_response_object_response_body import SettingsComplianceResponseObjectResponseBody
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class SettingsPatchComplianceSettingsResponseBody(UniversalBaseModel):
    data: SettingsComplianceResponseObjectResponseBody

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
