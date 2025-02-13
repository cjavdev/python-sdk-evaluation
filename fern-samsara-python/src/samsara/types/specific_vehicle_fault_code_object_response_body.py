# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
from .specific_vehicle_fault_code_object_response_body_type import SpecificVehicleFaultCodeObjectResponseBodyType
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class SpecificVehicleFaultCodeObjectResponseBody(UniversalBaseModel):
    """
    A specific vehicle fault code.
    """

    fault_code: typing_extensions.Annotated[str, FieldMetadata(alias="faultCode")] = pydantic.Field()
    """
    The specific fault code name.
    """

    type: SpecificVehicleFaultCodeObjectResponseBodyType = pydantic.Field()
    """
    The specific fault code type.  Valid values: `INVALID_FAULT_CODE_TYPE`, `J1939_DTC`, `J1939_SPN`, `PASSENGER_DTC`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
