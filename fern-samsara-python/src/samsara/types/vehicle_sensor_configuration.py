# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .vehicle_sensor_configuration_area import VehicleSensorConfigurationArea
from .vehicle_sensor_configuration_door import VehicleSensorConfigurationDoor
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class VehicleSensorConfiguration(UniversalBaseModel):
    """
    The sensors configured on a vehicle
    """

    areas: typing.Optional[typing.List[VehicleSensorConfigurationArea]] = None
    doors: typing.Optional[typing.List[VehicleSensorConfigurationDoor]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
