# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TrainingLearnerObjectResponseBody(UniversalBaseModel):
    """
    Learner that is associated with the training assignment. Only driver learners are supported currently.
    """

    id: str = pydantic.Field()
    """
    ID of the polymorphic user.
    """

    type: typing.Literal["driver"] = pydantic.Field(default="driver")
    """
    The type of the polymorphic user.  Valid values: `driver`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
