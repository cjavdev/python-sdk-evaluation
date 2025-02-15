# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .post_job_objectjob_location_request_object_request_body import PostJobObjectjobLocationRequestObjectRequestBody
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class PostJobObjectRequestBody(UniversalBaseModel):
    """
    Job object to be created
    """

    address: typing.Optional[PostJobObjectjobLocationRequestObjectRequestBody] = None
    customer_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="customerName")] = (
        pydantic.Field(default=None)
    )
    """
    Customer name for job
    """

    end_date: typing_extensions.Annotated[str, FieldMetadata(alias="endDate")] = pydantic.Field()
    """
    End date of job in RFC 3339 format. Must be greater than or equal to the start date
    """

    fleet_device_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="fleetDeviceIds")
    ] = pydantic.Field(default=None)
    """
    Fleet devices to be added to this job (cannot have both industrial assets and fleet devices in the same job)
    """

    id: str = pydantic.Field()
    """
    Job Id
    """

    industrial_asset_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="industrialAssetIds")
    ] = pydantic.Field(default=None)
    """
    IndustrialAssets to be added to this job (cannot have both industrial assets and fleet devices in the same job)
    """

    name: str = pydantic.Field()
    """
    Job name
    """

    notes: typing.Optional[str] = pydantic.Field(default=None)
    """
    Notes for the upcoming job
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

    start_date: typing_extensions.Annotated[str, FieldMetadata(alias="startDate")] = pydantic.Field()
    """
    Start date of job in RFC 3339 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
