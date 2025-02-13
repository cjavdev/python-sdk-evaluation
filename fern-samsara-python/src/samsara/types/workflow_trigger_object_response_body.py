# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .trigger_params_object_response_body import TriggerParamsObjectResponseBody
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class WorkflowTriggerObjectResponseBody(UniversalBaseModel):
    """
    The trigger of an alert.
    """

    trigger_params: typing_extensions.Annotated[
        typing.Optional[TriggerParamsObjectResponseBody], FieldMetadata(alias="triggerParams")
    ] = None
    trigger_type_id: typing_extensions.Annotated[int, FieldMetadata(alias="triggerTypeId")] = pydantic.Field()
    """
    The id of the trigger type. Reference the following list for the ids:
    
    Ambient Temperature = 1003
    DVIR Submitted for Asset = 5005
    Driver Recorded = 5027
    Vehicle Speed = 1000
    Fuel Level (Percentage) = 1005
    Vehicle DEF Level (Percentage) = 1006
    Vehicle Battery = 1007
    Gateway Unplugged = 1009
    Dashcam Disconnected = 1012
    Camera Connector Disconnected = 1046
    Asset starts moving = 1013
    Inside Geofence = 1014
    Outside Geofence = 1020
    Unassigned Driving = 1016
    Driver HOS Violation = 1018
    Vehicle Engine Idle = 1019
    Asset Engine On = 1021
    Asset Engine Off = 1022
    Harsh Event = 1023
    Scheduled Maintenance = 1024
    Scheduled Maintenance by Odometer = 1025
    Scheduled Maintenance by Engine Hours = 1026
    Out of Route = 1027
    GPS Signal Loss = 1032
    Cell Signal Loss = 1033
    Fault Code = 1029
    Tire Faults = 1043
    Gateway Disconnected = 1030
    Panic Button = 1034
    Tampering Detected = 1045
    If vehicle is severely speeding (as defined by your organization) = 5022
    Driver Document Submitted = 5009
    Driver App Sign In = 5012
    Driver App Sign Out = 5013
    Geofence Entry = 5016
    Geofence Exit = 5017
    Route Stop ETA Alert = 5018
    Scheduled Date And Time = 8001
    
    The following trigger types are in Preview:
    Training Assignment Due Soon = 8003
    Training Assignment Past Due = 8004
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
