# This file was auto-generated by Fern from our API Definition.

from .v_1_dispatch_route_without_eta_all_of import V1DispatchRouteWithoutEtaAllOf
from .v_1_dispatch_route_base import V1DispatchRouteBase
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class V1DispatchRouteWithoutEta(V1DispatchRouteWithoutEtaAllOf, V1DispatchRouteBase):
    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
