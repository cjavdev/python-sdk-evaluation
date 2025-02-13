# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .minimal_route_stop_audit_logs_response_body import MinimalRouteStopAuditLogsResponseBody
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class MinimalRouteAuditLogsResponseBody(UniversalBaseModel):
    """
    A single route. Only the fields that have changed are present in the response. All other fields, including the route id, will not be present in the response. For now, only routeStops are included since only Route Tracking updates are supported.
    """

    stops: typing.Optional[typing.List[MinimalRouteStopAuditLogsResponseBody]] = pydantic.Field(default=None)
    """
    The route stops in the route. Only stops that have been updated will be included in the response.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
