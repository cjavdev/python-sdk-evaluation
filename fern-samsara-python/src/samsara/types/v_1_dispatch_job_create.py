# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .v_1_dispatch_route_job_external_ids import V1DispatchRouteJobExternalIds
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class V1DispatchJobCreate(UniversalBaseModel):
    destination_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The address of the job destination, as it would be recognized if provided to maps.google.com. Optional if a valid destination address ID is provided.
    """

    destination_address_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    ID of the job destination associated with an address book entry. Optional if valid values are provided for destination address and latitude/longitude. If a valid destination address ID is provided, address/latitude/longitude will be used from the address book entry. Name of the address book entry will only be used if the destination name is not provided.
    """

    destination_lat: typing.Optional[float] = pydantic.Field(default=None)
    """
    Latitude of the destination in decimal degrees. Optional if a valid destination address ID is provided.
    """

    destination_lng: typing.Optional[float] = pydantic.Field(default=None)
    """
    Longitude of the destination in decimal degrees. Optional if a valid destination address ID is provided.
    """

    destination_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the job destination. If provided, it will take precedence over the name of the address book entry.
    """

    external_ids: typing.Optional[V1DispatchRouteJobExternalIds] = None
    notes: typing.Optional[str] = pydantic.Field(default=None)
    """
    Notes regarding the details of this job, maximum of 2000 characters; newline characters ('\n')can be used for formatting.
    """

    scheduled_arrival_time_ms: int = pydantic.Field()
    """
    The time at which the assigned driver is scheduled to arrive at the job destination.
    """

    scheduled_departure_time_ms: typing.Optional[int] = pydantic.Field(default=None)
    """
    The time at which the assigned driver is scheduled to depart from the job destination.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
