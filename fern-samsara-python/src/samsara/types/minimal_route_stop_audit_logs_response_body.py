# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
import datetime as dt
from ..core.serialization import FieldMetadata
import pydantic
from .minimal_route_stop_audit_logs_response_body_state import MinimalRouteStopAuditLogsResponseBodyState
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class MinimalRouteStopAuditLogsResponseBody(UniversalBaseModel):
    """
    A single route stop for a route.
    """

    actual_arrival_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="actualArrivalTime")
    ] = pydantic.Field(default=None)
    """
    Actual arrival time, if it exists, for the route stop in RFC 3339 format.
    """

    actual_departure_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="actualDepartureTime")
    ] = pydantic.Field(default=None)
    """
    Actual departure time, if it exists, for the route stop in RFC 3339 format.
    """

    en_route_time: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="enRouteTime")] = (
        pydantic.Field(default=None)
    )
    """
    The time the stop became en-route, in RFC 3339 format.
    """

    eta: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Estimated time of arrival, if this stop is currently en-route, in RFC 3339 format.
    """

    external_ids: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="externalIds")
    ] = pydantic.Field(default=None)
    """
    A map of external ids
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the route stop.
    """

    live_sharing_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="liveSharingUrl")] = (
        pydantic.Field(default=None)
    )
    """
    The shareable url of the stop's current status.
    """

    scheduled_arrival_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="scheduledArrivalTime")
    ] = pydantic.Field(default=None)
    """
    Scheduled arrival time, if it exists, for the stop in RFC 3339 format. If it does not exist, and this field was changed in the update, it will be an empty string.
    """

    scheduled_departure_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="scheduledDepartureTime")
    ] = pydantic.Field(default=None)
    """
    Scheduled departure time, if it exists, for the stop in RFC 3339 format. If it does not exist, and this field was changed in the update, it will be an empty string.
    """

    skipped_time: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="skippedTime")] = (
        pydantic.Field(default=None)
    )
    """
    Skipped time, if it exists, for the route stop in RFC 3339 format.
    """

    state: typing.Optional[MinimalRouteStopAuditLogsResponseBodyState] = pydantic.Field(default=None)
    """
    The current state of the route stop.  Valid values: `unassigned`, `scheduled`, `en route`, `skipped`, `arrived`, `departed`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
