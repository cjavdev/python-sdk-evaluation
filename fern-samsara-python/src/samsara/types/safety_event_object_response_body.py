# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .safety_event_behavior_labels_response_body import SafetyEventBehaviorLabelsResponseBody
from ..core.serialization import FieldMetadata
import pydantic
from .safety_event_driver_object_response_body import SafetyEventDriverObjectResponseBody
from .safety_event_vehicle_object_response_body import SafetyEventVehicleObjectResponseBody
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SafetyEventObjectResponseBody(UniversalBaseModel):
    """
    The safety event that was updated.
    """

    behavior_labels: typing_extensions.Annotated[
        typing.Optional[typing.List[SafetyEventBehaviorLabelsResponseBody]], FieldMetadata(alias="behaviorLabels")
    ] = pydantic.Field(default=None)
    """
    Behavior labels for a safety event.
    """

    driver: typing.Optional[SafetyEventDriverObjectResponseBody] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique Samsara ID of the safety event.
    """

    time: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time the safety event occurred in RFC 3339 milliseconds format.
    """

    vehicle: typing.Optional[SafetyEventVehicleObjectResponseBody] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
