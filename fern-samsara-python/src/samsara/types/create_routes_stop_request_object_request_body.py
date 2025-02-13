# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
import datetime as dt
from .routes_single_use_address_object_request_body import RoutesSingleUseAddressObjectRequestBody
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CreateRoutesStopRequestObjectRequestBody(UniversalBaseModel):
    address_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="addressId")] = pydantic.Field(
        default=None
    )
    """
    ID of the address. An address [externalId](https://developers.samsara.com/docs/external-ids#using-external-ids) can also be used interchangeably here.
    """

    external_ids: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="externalIds")
    ] = pydantic.Field(default=None)
    """
    A map of external ids
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the stop
    """

    notes: typing.Optional[str] = pydantic.Field(default=None)
    """
    Notes for the stop
    """

    ontime_window_after_arrival_ms: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ontimeWindowAfterArrivalMs")
    ] = pydantic.Field(default=None)
    """
    Specifies the time window (in milliseconds) after a stop's scheduled arrival time during which the stop is considered 'on-time'.
    """

    ontime_window_before_arrival_ms: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ontimeWindowBeforeArrivalMs")
    ] = pydantic.Field(default=None)
    """
    Specifies the time window (in milliseconds) before a stop's scheduled arrival time during which the stop is considered 'on-time'.
    """

    scheduled_arrival_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="scheduledArrivalTime")
    ] = pydantic.Field(default=None)
    """
    This is a required field for all stops EXCEPT the start and end, based on route start and stop settings selected.
    """

    scheduled_departure_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="scheduledDepartureTime")
    ] = pydantic.Field(default=None)
    """
    This is a required field for all stops EXCEPT the start and end, based on route start and stop settings selected.
    """

    single_use_location: typing_extensions.Annotated[
        typing.Optional[RoutesSingleUseAddressObjectRequestBody], FieldMetadata(alias="singleUseLocation")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
