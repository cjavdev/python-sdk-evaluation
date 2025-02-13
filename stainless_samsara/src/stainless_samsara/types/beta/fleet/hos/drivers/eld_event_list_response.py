# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ......_models import BaseModel

__all__ = [
    "EldEventListResponse",
    "Data",
    "DataEldEvent",
    "DataEldEventLocation",
    "DataEldEventRemark",
    "DataEldEventVehicle",
    "Pagination",
]


class DataEldEventLocation(BaseModel):
    city: Optional[str] = None
    """The best effort city for the latitude and longitude."""

    eld_location: Optional[str] = FieldInfo(alias="eldLocation", default=None)
    """
    Relative location to the city, village, or town with population of 5,000 or
    greater.
    """

    latitude: Optional[float] = None
    """The latitude of the location."""

    longitude: Optional[float] = None
    """The longitude of the location."""

    state: Optional[str] = None
    """The best effort state for the latitude and longitude."""


class DataEldEventRemark(BaseModel):
    comment: str
    """The content of the remark."""

    location_description: str = FieldInfo(alias="locationDescription")
    """The location description entered by the user"""

    time: str
    """The time in RFC 3339 format at which the remark was created."""


class DataEldEventVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the vehicle"""


class DataEldEvent(BaseModel):
    eld_event_code: int = FieldInfo(alias="eldEventCode")
    """
    A dependent attribute on `eldEventType` that specifies the nature of the event,
    as defined in the ELD Mandate
    [section 7.20](https://www.ecfr.gov/cgi-bin/retrieveECFR?gp=1&ty=HTML&h=L&mc=true&=PART&n=pt49.5.395#ap49.5.395_138.a).
    Valid values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`
    """

    eld_event_type: int = FieldInfo(alias="eldEventType")
    """
    An attribute specifying the type of ELD event, as defined in the ELD Mandate
    [section 7.25](https://www.ecfr.gov/cgi-bin/retrieveECFR?gp=1&ty=HTML&h=L&mc=true&=PART&n=pt49.5.395#ap49.5.395_138.a).
    Valid values: `1`, `2`, `3`, `4`, `5`, `6`, `7`
    """

    time: str
    """A time in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    accumulated_vehicle_meters: Optional[int] = FieldInfo(alias="accumulatedVehicleMeters", default=None)
    """The accumulated meters in the given ignition power on cycle."""

    elapsed_engine_hours: Optional[float] = FieldInfo(alias="elapsedEngineHours", default=None)
    """
    The elapsed time in the engine's operation in the given ignition power on cycle.
    """

    eld_event_record_origin: Optional[int] = FieldInfo(alias="eldEventRecordOrigin", default=None)
    """
    An attribute for the event record indicating whether it is automatically
    recorded, or edited, entered or accepted by the driver, requested by another
    authenticated user, or assumed from unidentified driver profile, as defined in
    the ELD Mandate
    [section 7.22](https://www.ecfr.gov/cgi-bin/retrieveECFR?gp=1&ty=HTML&h=L&mc=true&=PART&n=pt49.5.395#ap49.5.395_138.a).
    Valid values: `1`, `2`, `3`, `4`
    """

    eld_event_record_status: Optional[int] = FieldInfo(alias="eldEventRecordStatus", default=None)
    """
    An attribute for the event record indicating whether an event is active or
    inactive and further, if inactive, whether it is due to a change or lack of
    confirmation by the driver or due to a driver's rejection of change request, as
    defined in the ELD Mandate
    [section 7.23](https://www.ecfr.gov/cgi-bin/retrieveECFR?gp=1&ty=HTML&h=L&mc=true&=PART&n=pt49.5.395#ap49.5.395_138.a).
    Valid values: `1`, `2`, `3`, `4`
    """

    location: Optional[DataEldEventLocation] = None

    malfunction_diagnostic_code: Optional[Literal["P", "E", "T", "L", "R", "S", "O", "1", "2", "3", "4", "5", "6"]] = (
        FieldInfo(alias="malfunctionDiagnosticCode", default=None)
    )
    """
    A code that further specifies the underlying malfunction or data diagnostic
    event, as defined in the ELD Mandate
    [section 7.34](https://www.ecfr.gov/cgi-bin/retrieveECFR?gp=1&ty=HTML&h=L&mc=true&=PART&n=pt49.5.395#ap49.5.395_138.a).
    Valid values: `P`, `E`, `T`, `L`, `R`, `S`, `O`, `1`, `2`, `3`, `4`, `5`, `6`
    """

    remark: Optional[DataEldEventRemark] = None

    total_engine_hours: Optional[float] = FieldInfo(alias="totalEngineHours", default=None)
    """The aggregated time of a vehicle's engine's operation since its inception."""

    total_vehicle_meters: Optional[int] = FieldInfo(alias="totalVehicleMeters", default=None)
    """The total meters recorded for the vehicle."""

    vehicle: Optional[DataEldEventVehicle] = None
    """A minified vehicle object.

    This object is only returned if the route is assigned to the vehicle.
    """


class Data(BaseModel):
    id: str
    """ID of the driver."""

    driver_activation_status: Literal["active", "deactivated"] = FieldInfo(alias="driverActivationStatus")
    """A value indicating whether the driver is active or deactivated.

    Valid values: `active`, `deactivated`
    """

    eld_events: List[DataEldEvent] = FieldInfo(alias="eldEvents")
    """List of ELD event objects."""

    name: str
    """Name of the driver."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""


class Pagination(BaseModel):
    end_cursor: str = FieldInfo(alias="endCursor")
    """Cursor identifier representing the last element in the response.

    This value should be used in conjunction with a subsequent request's 'after'
    query parameter. This may be an empty string if there are no more pages left to
    view.
    """

    has_next_page: bool = FieldInfo(alias="hasNextPage")
    """
    True if there are more pages of results immediately available after this
    endCursor.
    """


class EldEventListResponse(BaseModel):
    data: List[Data]
    """List of drivers and their ELD event objects data."""

    pagination: Optional[Pagination] = None
    """Pagination parameters."""
