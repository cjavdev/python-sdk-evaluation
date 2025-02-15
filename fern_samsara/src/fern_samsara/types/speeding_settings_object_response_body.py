# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .speeding_severity_level_response_body import SpeedingSeverityLevelResponseBody
from ..core.serialization import FieldMetadata
import pydantic
from .speeding_settings_object_response_body_unit import SpeedingSettingsObjectResponseBodyUnit
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SpeedingSettingsObjectResponseBody(UniversalBaseModel):
    """
    Enables custom speeding levels.
    """

    severity_levels: typing_extensions.Annotated[
        typing.Optional[typing.List[SpeedingSeverityLevelResponseBody]], FieldMetadata(alias="severityLevels")
    ] = pydantic.Field(default=None)
    """
    The speeding severity levels for an organization.
    """

    unit: typing.Optional[SpeedingSettingsObjectResponseBodyUnit] = pydantic.Field(default=None)
    """
    The unit of measurement for speeding  Valid values: `milesPerHour`, `kilometersPerHour`, `percentage`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
