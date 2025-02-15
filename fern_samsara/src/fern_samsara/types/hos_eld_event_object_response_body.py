# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from .hos_eld_event_location_object_response_body import HosEldEventLocationObjectResponseBody
from .hos_eld_event_object_response_body_malfunction_diagnostic_code import (
    HosEldEventObjectResponseBodyMalfunctionDiagnosticCode,
)
from .hos_eld_event_remark_object_response_body import HosEldEventRemarkObjectResponseBody
from .goa_vehicle_tiny_response_response_body import GoaVehicleTinyResponseResponseBody
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class HosEldEventObjectResponseBody(UniversalBaseModel):
    """
    An event that refers to a discrete instance in time with various data elements. Depending on the type of event, not every field will be populated. For more information, see the ELD Mandate [section 3.1.2](https://www.ecfr.gov/cgi-bin/retrieveECFR?gp=1&ty=HTML&h=L&mc=true&=PART&n=pt49.5.395#ap49.5.395_138.a).
    """

    accumulated_vehicle_meters: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="accumulatedVehicleMeters")
    ] = pydantic.Field(default=None)
    """
    The accumulated meters in the given ignition power on cycle.
    """

    elapsed_engine_hours: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="elapsedEngineHours")
    ] = pydantic.Field(default=None)
    """
    The elapsed time in the engine's operation in the given ignition power on cycle.
    """

    eld_event_code: typing_extensions.Annotated[int, FieldMetadata(alias="eldEventCode")] = pydantic.Field()
    """
    A dependent attribute on `eldEventType` that specifies the nature of the event, as defined in the ELD Mandate [section 7.20](https://www.ecfr.gov/cgi-bin/retrieveECFR?gp=1&ty=HTML&h=L&mc=true&=PART&n=pt49.5.395#ap49.5.395_138.a).  Valid values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`
    """

    eld_event_record_origin: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="eldEventRecordOrigin")
    ] = pydantic.Field(default=None)
    """
    An attribute for the event record indicating whether it is automatically recorded, or edited, entered or accepted by the driver, requested by another authenticated user, or assumed from unidentified driver profile, as defined in the ELD Mandate [section 7.22](https://www.ecfr.gov/cgi-bin/retrieveECFR?gp=1&ty=HTML&h=L&mc=true&=PART&n=pt49.5.395#ap49.5.395_138.a).  Valid values: `1`, `2`, `3`, `4`
    """

    eld_event_record_status: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="eldEventRecordStatus")
    ] = pydantic.Field(default=None)
    """
    An attribute for the event record indicating whether an event is active or inactive and further, if inactive, whether it is due to a change or lack of confirmation by the driver or due to a driver's rejection of change request, as defined in the ELD Mandate [section 7.23](https://www.ecfr.gov/cgi-bin/retrieveECFR?gp=1&ty=HTML&h=L&mc=true&=PART&n=pt49.5.395#ap49.5.395_138.a).  Valid values: `1`, `2`, `3`, `4`
    """

    eld_event_type: typing_extensions.Annotated[int, FieldMetadata(alias="eldEventType")] = pydantic.Field()
    """
    An attribute specifying the type of ELD event, as defined in the ELD Mandate [section 7.25](https://www.ecfr.gov/cgi-bin/retrieveECFR?gp=1&ty=HTML&h=L&mc=true&=PART&n=pt49.5.395#ap49.5.395_138.a).  Valid values: `1`, `2`, `3`, `4`, `5`, `6`, `7`
    """

    location: typing.Optional[HosEldEventLocationObjectResponseBody] = None
    malfunction_diagnostic_code: typing_extensions.Annotated[
        typing.Optional[HosEldEventObjectResponseBodyMalfunctionDiagnosticCode],
        FieldMetadata(alias="malfunctionDiagnosticCode"),
    ] = pydantic.Field(default=None)
    """
    A code that further specifies the underlying malfunction or data diagnostic event, as defined in the ELD Mandate [section 7.34](https://www.ecfr.gov/cgi-bin/retrieveECFR?gp=1&ty=HTML&h=L&mc=true&=PART&n=pt49.5.395#ap49.5.395_138.a).  Valid values: `P`, `E`, `T`, `L`, `R`, `S`, `O`, `1`, `2`, `3`, `4`, `5`, `6`
    """

    remark: typing.Optional[HosEldEventRemarkObjectResponseBody] = None
    time: str = pydantic.Field()
    """
    A time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    total_engine_hours: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="totalEngineHours")] = (
        pydantic.Field(default=None)
    )
    """
    The aggregated time of a vehicle's engine's operation since its inception.
    """

    total_vehicle_meters: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalVehicleMeters")
    ] = pydantic.Field(default=None)
    """
    The total meters recorded for the vehicle.
    """

    vehicle: typing.Optional[GoaVehicleTinyResponseResponseBody] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
