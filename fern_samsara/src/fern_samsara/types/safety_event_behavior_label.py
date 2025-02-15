# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .safety_event_behavior_label_type import SafetyEventBehaviorLabelType
import typing
from .safety_event_behavior_label_name import SafetyEventBehaviorLabelName
from .safety_event_behavior_label_source import SafetyEventBehaviorLabelSource
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class SafetyEventBehaviorLabel(UniversalBaseModel):
    """
    The label and source of the label associated with the safety event.
    """

    label: SafetyEventBehaviorLabelType
    name: typing.Optional[SafetyEventBehaviorLabelName] = None
    source: SafetyEventBehaviorLabelSource

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
