# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "DailyLogListResponse",
    "Data",
    "DataDriver",
    "DataDriverEldSettings",
    "DataDriverEldSettingsRuleset",
    "DataDistanceTraveled",
    "DataDutyStatusDurations",
    "DataLogMetaData",
    "DataLogMetaDataVehicle",
    "DataPendingDutyStatusDurations",
    "Pagination",
]


class DataDriverEldSettingsRuleset(BaseModel):
    break_: Optional[Literal["Property (off-duty/sleeper)", "Explosives/HazMat (on-duty)"]] = FieldInfo(
        alias="break", default=None
    )
    """The rest break required setting of the ELD ruleset applied to this driver.

    Valid values: `Property (off-duty/sleeper)`, `Explosives/HazMat (on-duty)`
    """

    cycle: Optional[
        Literal[
            "USA 60 hour / 7 day",
            "USA 70 hour / 8 day",
            "AK 80 hour / 8 day",
            "AK 70 hour / 7 day",
            "CA 80 hour / 8 day",
            "CA 112 hour / 8 day",
            "FL 80 hour / 8 day",
            "FL 70 hour / 7 day",
            "NE 80 hour / 8 day",
            "NE 70 hour / 7 day",
            "NC 80 hour / 8 day",
            "NC 70 hour / 7 day",
            "OK 70 hour / 8 day",
            "OK 60 hour / 7 day",
            "OR 80 hour / 8 day",
            "OR 70 hour / 7 day",
            "SC 80 hour / 8 day",
            "SC 70 hour / 7 day",
            "TX 70 hour / 7 day",
            "WI 80 hour / 8 day",
            "WI 70 hour / 7 day",
            "Canada South Cycle 1 (70 hour / 7 day)",
            "Canada South Cycle 2 (120 hour / 14 day)",
            "Canada North Cycle 1 (80 hour / 7 day)",
            "Canada North Cycle 2 (120 hour / 14 day)",
        ]
    ] = None
    """The cycle of the ELD ruleset applied to this driver.

    Valid values: `USA 60 hour / 7 day`, `USA 70 hour / 8 day`,
    `AK 80 hour / 8 day`, `AK 70 hour / 7 day`, `CA 80 hour / 8 day`,
    `CA 112 hour / 8 day`, `FL 80 hour / 8 day`, `FL 70 hour / 7 day`,
    `NE 80 hour / 8 day`, `NE 70 hour / 7 day`, `NC 80 hour / 8 day`,
    `NC 70 hour / 7 day`, `OK 70 hour / 8 day`, `OK 60 hour / 7 day`,
    `OR 80 hour / 8 day`, `OR 70 hour / 7 day`, `SC 80 hour / 8 day`,
    `SC 70 hour / 7 day`, `TX 70 hour / 7 day`, `WI 80 hour / 8 day`,
    `WI 70 hour / 7 day`, `Canada South Cycle 1 (70 hour / 7 day)`,
    `Canada South Cycle 2 (120 hour / 14 day)`,
    `Canada North Cycle 1 (80 hour / 7 day)`,
    `Canada North Cycle 2 (120 hour / 14 day)`
    """

    jurisdiction: Optional[str] = None
    """The jurisdiction of the ELD ruleset applied to this driver.

    These are specified by either `CS` or `CN` for Canada South and Canada North,
    respectively, or the ISO 3166-2 postal code for the supported state or
    territory.
    """

    restart: Optional[Literal["34-hour Restart", "24-hour Restart", "36-hour Restart", "72-hour Restart"]] = None
    """The restart of the ELD ruleset applied to this driver.

    Valid values: `34-hour Restart`, `24-hour Restart`, `36-hour Restart`,
    `72-hour Restart`
    """

    shift: Optional[Literal["US Interstate Property", "US Interstate Passenger"]] = None
    """The shift of the ELD ruleset applied to this driver.

    Valid values: `US Interstate Property`, `US Interstate Passenger`
    """


class DataDriverEldSettings(BaseModel):
    rulesets: Optional[List[DataDriverEldSettingsRuleset]] = None
    """The driver's ELD rulesets and overrides."""


class DataDriver(BaseModel):
    id: str
    """ID of the driver"""

    name: str
    """Name of the driver"""

    eld_settings: Optional[DataDriverEldSettings] = FieldInfo(alias="eldSettings", default=None)
    """The driver's ELD settings."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    timezone: Optional[str] = None
    """
    Home terminal timezone, in order to indicate what time zone should be used to
    calculate the ELD logs. Driver timezones use
    [IANA timezone database](https://www.iana.org/time-zones) keys (e.g.
    `America/Los_Angeles`, `America/New_York`, `Europe/London`, etc.). You can find
    a mapping of common timezone formats to IANA timezone keys
    [here](https://unicode.org/cldr/charts/latest/supplemental/zone_tzid.html).
    """


class DataDistanceTraveled(BaseModel):
    drive_distance_meters: Optional[int] = FieldInfo(alias="driveDistanceMeters", default=None)
    """Distance driven in meters, rounded to two decimal places."""

    personal_conveyance_distance_meters: Optional[int] = FieldInfo(
        alias="personalConveyanceDistanceMeters", default=None
    )
    """Distance driven for personal conveyance, rounded to two decimal places."""

    yard_move_distance_meters: Optional[int] = FieldInfo(alias="yardMoveDistanceMeters", default=None)
    """Distance driven for yard moves, rounded to two decimal places."""


class DataDutyStatusDurations(BaseModel):
    active_duration_ms: Optional[int] = FieldInfo(alias="activeDurationMs", default=None)
    """Duration the driver was active for in the log period in milliseconds."""

    drive_duration_ms: Optional[int] = FieldInfo(alias="driveDurationMs", default=None)
    """Duration the driver was driving for in the log period in milliseconds."""

    off_duty_duration_ms: Optional[int] = FieldInfo(alias="offDutyDurationMs", default=None)
    """Duration the driver was off duty for in the log period in milliseconds."""

    on_duty_duration_ms: Optional[int] = FieldInfo(alias="onDutyDurationMs", default=None)
    """Duration the driver was on duty for in the log period in milliseconds."""

    personal_conveyance_duration_ms: Optional[int] = FieldInfo(alias="personalConveyanceDurationMs", default=None)
    """
    Duration the driver was driving for personal conveyance for in the log period in
    milliseconds.
    """

    sleeper_berth_duration_ms: Optional[int] = FieldInfo(alias="sleeperBerthDurationMs", default=None)
    """
    Duration the driver was in their sleeper berth for in the log period in
    milliseconds.
    """

    waiting_time_duration_ms: Optional[int] = FieldInfo(alias="waitingTimeDurationMs", default=None)
    """Duration the driver was waiting for in the log period in milliseconds."""

    yard_move_duration_ms: Optional[int] = FieldInfo(alias="yardMoveDurationMs", default=None)
    """
    Duration the driver was driving for yard moves for in the log period in
    milliseconds.
    """


class DataLogMetaDataVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle"""

    asset_type: Optional[Literal["uncategorized", "trailer", "equipment", "unpowered", "vehicle"]] = FieldInfo(
        alias="assetType", default=None
    )
    """The type of the asset.

    Valid values: `uncategorized`, `trailer`, `equipment`, `unpowered`, `vehicle`
    """

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    license_plate: Optional[str] = FieldInfo(alias="licensePlate", default=None)
    """The license plate of the vehicle."""

    name: Optional[str] = None
    """Name of the vehicle"""

    vehicle_vin: Optional[str] = FieldInfo(alias="vehicleVin", default=None)
    """The VIN of the vehicle."""


class DataLogMetaData(BaseModel):
    adverse_driving_claimed: Optional[bool] = FieldInfo(alias="adverseDrivingClaimed", default=None)
    """
    Whether the driver has claimed the
    [Adverse Driving Exemption](https://kb.samsara.com/hc/en-us/articles/360047336792-Adverse-Driving-Exemption)
    for this HOS day chart.
    """

    big_day_claimed: Optional[bool] = FieldInfo(alias="bigDayClaimed", default=None)
    """
    Whether the driver has claimed the
    [Big Day Exemption](https://kb.samsara.com/hc/en-us/articles/360057113891-16-Hour-Short-Haul-Exemption-Big-Day-)
    for this HOS day chart.
    """

    carrier_formatted_address: Optional[str] = FieldInfo(alias="carrierFormattedAddress", default=None)
    """The address of the carrier used for this HOS chart."""

    carrier_name: Optional[str] = FieldInfo(alias="carrierName", default=None)
    """The name of the carrier used for this HOS chart."""

    carrier_us_dot_number: Optional[int] = FieldInfo(alias="carrierUsDotNumber", default=None)
    """The US DOT number of the carrier used for this HOS chart."""

    certified_at_time: Optional[str] = FieldInfo(alias="certifiedAtTime", default=None)
    """The time this log was certified in RFC 3339 format."""

    home_terminal_formatted_address: Optional[str] = FieldInfo(alias="homeTerminalFormattedAddress", default=None)
    """The address of the Home Terminal used for this HOS chart."""

    home_terminal_name: Optional[str] = FieldInfo(alias="homeTerminalName", default=None)
    """The name of the Home Terminal used for this HOS chart."""

    is_certified: Optional[bool] = FieldInfo(alias="isCertified", default=None)
    """Whether this HOS day chart was certified by the driver."""

    is_us_short_haul_active: Optional[bool] = FieldInfo(alias="isUsShortHaulActive", default=None)
    """
    Whether the driver has the 150 air-mile Short Haul Exemption active for this HOS
    day chart.
    """

    shipping_docs: Optional[str] = FieldInfo(alias="shippingDocs", default=None)
    """List of shipping document names associated with the driver for the day.

    This field maps to Shipping ID in the dashboard.
    """

    trailer_names: Optional[List[str]] = FieldInfo(alias="trailerNames", default=None)
    """List of trailer names associated with the driver for the day.

    If a trailer was associated with a log through the driver app the trailer name
    will be the trailer ID.
    """

    vehicles: Optional[List[DataLogMetaDataVehicle]] = None
    """List of vehicles associated with the driver for the day."""


class DataPendingDutyStatusDurations(BaseModel):
    active_duration_ms: Optional[int] = FieldInfo(alias="activeDurationMs", default=None)
    """Duration the driver was active for in the log period in milliseconds."""

    drive_duration_ms: Optional[int] = FieldInfo(alias="driveDurationMs", default=None)
    """Duration the driver was driving for in the log period in milliseconds."""

    off_duty_duration_ms: Optional[int] = FieldInfo(alias="offDutyDurationMs", default=None)
    """Duration the driver was off duty for in the log period in milliseconds."""

    on_duty_duration_ms: Optional[int] = FieldInfo(alias="onDutyDurationMs", default=None)
    """Duration the driver was on duty for in the log period in milliseconds."""

    personal_conveyance_duration_ms: Optional[int] = FieldInfo(alias="personalConveyanceDurationMs", default=None)
    """
    Duration the driver was driving for personal conveyance for in the log period in
    milliseconds.
    """

    sleeper_berth_duration_ms: Optional[int] = FieldInfo(alias="sleeperBerthDurationMs", default=None)
    """
    Duration the driver was in their sleeper berth for in the log period in
    milliseconds.
    """

    waiting_time_duration_ms: Optional[int] = FieldInfo(alias="waitingTimeDurationMs", default=None)
    """Duration the driver was waiting for in the log period in milliseconds."""

    yard_move_duration_ms: Optional[int] = FieldInfo(alias="yardMoveDurationMs", default=None)
    """
    Duration the driver was driving for yard moves for in the log period in
    milliseconds.
    """


class Data(BaseModel):
    driver: DataDriver
    """The driver the log applies to."""

    end_time: str = FieldInfo(alias="endTime")
    """The end time of the daily log in RFC 3339 format.

    This will be calculated using timezone of the driver.
    """

    start_time: str = FieldInfo(alias="startTime")
    """The start time of the daily log in RFC 3339 format.

    This will be calculated using timezone of the driver.
    """

    distance_traveled: Optional[DataDistanceTraveled] = FieldInfo(alias="distanceTraveled", default=None)
    """The distance traveled information of the log."""

    duty_status_durations: Optional[DataDutyStatusDurations] = FieldInfo(alias="dutyStatusDurations", default=None)
    """The currently applied duty status durations on the driver's log."""

    log_meta_data: Optional[DataLogMetaData] = FieldInfo(alias="logMetaData", default=None)
    """The metadata of the log."""

    pending_duty_status_durations: Optional[DataPendingDutyStatusDurations] = FieldInfo(
        alias="pendingDutyStatusDurations", default=None
    )
    """
    What the duty status durations on the driver’s log would be if all pending
    carrier edits are accepted by the driver.
    """


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


class DailyLogListResponse(BaseModel):
    data: List[Data]
    """List of drivers and their HOS daily logs data."""

    pagination: Pagination
    """Pagination parameters."""
