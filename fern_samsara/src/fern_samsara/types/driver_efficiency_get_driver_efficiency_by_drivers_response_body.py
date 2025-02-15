# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .single_driver_efficiency_by_driver_data_object_response_body import (
    SingleDriverEfficiencyByDriverDataObjectResponseBody,
)
import pydantic
from .goa_pagination_response_response_body import GoaPaginationResponseResponseBody
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class DriverEfficiencyGetDriverEfficiencyByDriversResponseBody(UniversalBaseModel):
    data: typing.List[SingleDriverEfficiencyByDriverDataObjectResponseBody] = pydantic.Field()
    """
    List of driver efficiency data associated with drivers.
    """

    pagination: GoaPaginationResponseResponseBody

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
