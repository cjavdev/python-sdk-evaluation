# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class TrainingCourseLabelObjectResponseBody(UniversalBaseModel):
    """
    Label of the training course.
    """

    name: str = pydantic.Field()
    """
    Name of the course label. Valid values: “safety”.
    """

    type: str = pydantic.Field()
    """
    Type of the course label. Valid values when course.label.name is ‘safety’: accel, braking, crashSharpTurn, rolloverProtection, yawControl, speeding, rolledStopSign, tileRollingRailroad, seatbeltPolicy, nearCollision, phonePolicy, drowsy, defensiveDriving, driverObstructionPolicy, didNotYield, distractedDriving, tailgating, laneDeparture, lateResponse, ranRedLight, forwardCollisionWarning, foodDrinkPolicy, smokingPolicy, maskPolicy, maxSpeed, severeSpeeding, drinkPolicy, foodPolicy, unknown.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
