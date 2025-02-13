# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .workflow_circle_response_body import WorkflowCircleResponseBody
from .workflow_polygon_response_body import WorkflowPolygonResponseBody
from .settings_response_body import SettingsResponseBody
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class WorkflowGeofenceResponseBody(UniversalBaseModel):
    """
    The geofence that defines this address and its bounds. This can either be a circle or a polygon, but not both.
    """

    circle: typing.Optional[WorkflowCircleResponseBody] = None
    polygon: typing.Optional[WorkflowPolygonResponseBody] = None
    settings: typing.Optional[SettingsResponseBody] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
