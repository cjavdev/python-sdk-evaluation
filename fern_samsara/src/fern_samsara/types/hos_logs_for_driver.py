# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .driver_tiny_response import DriverTinyResponse
import typing_extensions
from .hos_logs_list import HosLogsList
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class HosLogsForDriver(UniversalBaseModel):
    """
    List of HOS logs for a driver.
    """

    driver: typing.Optional[DriverTinyResponse] = None
    hos_logs: typing_extensions.Annotated[typing.Optional[HosLogsList], FieldMetadata(alias="hosLogs")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
