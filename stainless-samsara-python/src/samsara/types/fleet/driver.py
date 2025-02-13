# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "Driver",
    "Data",
    "DataAttribute",
    "DataCarrierSettings",
    "DataEldSettings",
    "DataEldSettingsRuleset",
    "DataPeerGroupTag",
    "DataStaticAssignedVehicle",
    "DataTag",
    "DataUsDriverRulesetOverride",
    "DataVehicleGroupTag",
]


class DataAttribute(BaseModel):
    id: Optional[str] = None
    """The samsara id of the attribute object."""

    name: Optional[str] = None
    """Name of attribute."""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """Number values that are associated with this attribute."""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """String values that are associated with this attribute."""


class DataCarrierSettings(BaseModel):
    carrier_name: Optional[str] = FieldInfo(alias="carrierName", default=None)
    """Carrier for a given driver."""

    dot_number: Optional[int] = FieldInfo(alias="dotNumber", default=None)
    """Carrier US DOT Number.

    If this differs from the general organization's settings, the override value is
    used. Updating this value only updates the override setting for this driver.
    """

    home_terminal_address: Optional[str] = FieldInfo(alias="homeTerminalAddress", default=None)
    """Address of the place of business at which a driver ordinarily reports for work."""

    home_terminal_name: Optional[str] = FieldInfo(alias="homeTerminalName", default=None)
    """Name of the place of business at which a driver ordinarily reports for work."""

    main_office_address: Optional[str] = FieldInfo(alias="mainOfficeAddress", default=None)
    """Main office address for a given driver.

    If this differs from the general organization's settings, the override value is
    used.
    """


class DataEldSettingsRuleset(BaseModel):
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
    `Canada North Cycle 2 (120 hour / 14 day)`.
    """

    jurisdiction: Optional[str] = None
    """The jurisdiction of the ELD ruleset applied to this driver.

    These are specified by either `CS` or `CN` for Canada South and Canada North,
    respectively, or the ISO 3166-2 postal code for the supported state or
    territory.
    """

    restart: Optional[Literal["None", "34-hour Restart", "24-hour Restart", "36-hour Restart", "72-hour Restart"]] = (
        None
    )
    """The restart of the ELD ruleset applied to this driver.

    Valid values: `None`, `34-hour Restart`, `24-hour Restart`, `36-hour Restart`,
    `72-hour Restart`.
    """

    shift: Optional[Literal["US Interstate Property", "US Interstate Passenger", "Texas Intrastate"]] = None
    """The shift of the ELD ruleset applied to this driver.

    Valid values: `US Interstate Property`, `US Interstate Passenger`,
    `Texas Intrastate`.
    """


class DataEldSettings(BaseModel):
    rulesets: Optional[List[DataEldSettingsRuleset]] = None
    """The driver's ELD rulesets and overrides.

    This is the full set of rulesets that may apply to the driver depending on their
    activity. If you wish to interface with the specific US driver override, use the
    usDriverRulesetOverride field.
    """


class DataPeerGroupTag(BaseModel):
    id: Optional[str] = None
    """ID of the tag."""

    name: Optional[str] = None
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataStaticAssignedVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle."""

    name: Optional[str] = None
    """Name of the vehicle."""


class DataTag(BaseModel):
    id: Optional[str] = None
    """ID of the tag."""

    name: Optional[str] = None
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataUsDriverRulesetOverride(BaseModel):
    cycle: Literal[
        "USA Property (8/70)",
        "USA Property (7/60)",
        "USA Passenger (8/70)",
        "USA Passenger (7/60)",
        "Alaska Property (8/80)",
        "Alaska Property (7/70)",
        "Alaska Passenger (8/80)",
        "Alaska Passenger (7/70)",
        "California School/FLV (8/80)",
        "California Farm (8/112)",
        "California Property (8/80)",
        "California Flammable Liquid (8/80)",
        "California Passenger (8/80)",
        "California Motion Picture (8/80)",
        "Florida (8/80)",
        "Florida (7/70)",
        "Nebraska (8/80)",
        "Nebraska (7/70)",
        "North Carolina (8/80)",
        "North Carolina (7/70)",
        "Oklahoma (8/70)",
        "Oklahoma (7/60)",
        "Oregon (8/80)",
        "Oregon (7/70)",
        "South Carolina (8/80)",
        "South Carolina (7/70)",
        "Texas (7/70)",
        "Wisconsin (8/80)",
        "Wisconsin (7/70)",
    ]
    """The driver's working cycle.

    Valid values: `USA Property (8/70)`, `USA Property (7/60)`,
    `USA Passenger (8/70)`, `USA Passenger (7/60)`, `Alaska Property (8/80)`,
    `Alaska Property (7/70)`, `Alaska Passenger (8/80)`, `Alaska Passenger (7/70)`,
    `California School/FLV (8/80)`, `California Farm (8/112)`,
    `California Property (8/80)`, `California Flammable Liquid (8/80)`,
    `California Passenger (8/80)`, `California Motion Picture (8/80)`,
    `Florida (8/80)`, `Florida (7/70)`, `Nebraska (8/80)`, `Nebraska (7/70)`,
    `North Carolina (8/80)`, `North Carolina (7/70)`, `Oklahoma (8/70)`,
    `Oklahoma (7/60)`, `Oregon (8/80)`, `Oregon (7/70)`, `South Carolina (8/80)`,
    `South Carolina (7/70)`, `Texas (7/70)`, `Wisconsin (8/80)`, `Wisconsin (7/70)`
    """

    restart: Literal["34-hour Restart", "24-hour Restart", "36-hour Restart", "72-hour Restart", "None"]
    """
    Amount of time necessary for the driver to be resting in order to restart their
    cycle. Valid values: `34-hour Restart`, `24-hour Restart`, `36-hour Restart`,
    `72-hour Restart`, `None`.
    """

    restbreak: Literal["Property (off-duty/sleeper)", "California Mealbreak (off-duty/sleeper)", "None"]
    """The restbreak required for this driver.

    Valid values: `Property (off-duty/sleeper)`,
    `California Mealbreak (off-duty/sleeper)`, `None`.
    """

    us_state_to_override: Literal["", "AK", "CA", "FL", "NE", "NC", "OK", "OR", "SC", "TX", "WI"] = FieldInfo(
        alias="usStateToOverride"
    )
    """The jurisdiction of the ruleset applied to this driver.

    These are specified by either the ISO 3166-2 postal code for the supported US
    states, or empty string '' for US Federal Ruleset jurisdiction. Valid values:
    ``, `AK`, `CA`, `FL`, `NE`, `NC`, `OK`, `OR`, `SC`, `TX`, `WI`.
    """


class DataVehicleGroupTag(BaseModel):
    id: Optional[str] = None
    """ID of the tag."""

    name: Optional[str] = None
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class Data(BaseModel):
    id: Optional[str] = None
    """Samsara ID for the driver."""

    attributes: Optional[List[DataAttribute]] = None
    """A minified attribute"""

    carrier_settings: Optional[DataCarrierSettings] = FieldInfo(alias="carrierSettings", default=None)
    """Carrier for a given driver.

    If the driver's carrier differs from the general organization's carrier
    settings, the override value is used. Updating this value only updates the
    override setting for this driver.
    """

    created_at_time: Optional[str] = FieldInfo(alias="createdAtTime", default=None)
    """The date and time this driver was created in RFC 3339 format."""

    current_id_card_code: Optional[str] = FieldInfo(alias="currentIdCardCode", default=None)
    """The ID Card Code on the back of the physical card assigned to the driver.

    Contact Samsara if you would like to enable this feature.
    """

    driver_activation_status: Optional[Literal["active", "deactivated"]] = FieldInfo(
        alias="driverActivationStatus", default=None
    )
    """A value indicating whether the driver is active or deactivated.

    Valid values: `active`, `deactivated`.
    """

    eld_adverse_weather_exemption_enabled: Optional[bool] = FieldInfo(
        alias="eldAdverseWeatherExemptionEnabled", default=None
    )
    """Flag indicating this driver may use Adverse Weather exemptions in ELD logs."""

    eld_big_day_exemption_enabled: Optional[bool] = FieldInfo(alias="eldBigDayExemptionEnabled", default=None)
    """Flag indicating this driver may use Big Day exemption in ELD logs."""

    eld_day_start_hour: Optional[int] = FieldInfo(alias="eldDayStartHour", default=None)
    """
    `0` indicating midnight-to-midnight ELD driving hours, `12` to indicate
    noon-to-noon driving hours.
    """

    eld_exempt: Optional[bool] = FieldInfo(alias="eldExempt", default=None)
    """Flag indicating this driver is exempt from the Electronic Logging Mandate."""

    eld_exempt_reason: Optional[str] = FieldInfo(alias="eldExemptReason", default=None)
    """
    Reason that this driver is exempt from the Electronic Logging Mandate (see
    eldExempt).
    """

    eld_pc_enabled: Optional[bool] = FieldInfo(alias="eldPcEnabled", default=None)
    """
    Flag indicating this driver may select the Personal Conveyance duty status in
    ELD logs.
    """

    eld_settings: Optional[DataEldSettings] = FieldInfo(alias="eldSettings", default=None)
    """The driver's ELD settings."""

    eld_ym_enabled: Optional[bool] = FieldInfo(alias="eldYmEnabled", default=None)
    """Flag indicating this driver may select the Yard Move duty status in ELD logs."""

    external_ids: Optional[object] = FieldInfo(alias="externalIds", default=None)
    """
    The [external IDs](https://developers.samsara.com/docs/external-ids) for the
    given object.
    """

    has_driving_features_hidden: Optional[bool] = FieldInfo(alias="hasDrivingFeaturesHidden", default=None)
    """
    A boolean indicating whether the driver has driving-related features hidden in
    the Driver App, including Vehicle selection, HOS, Routing, Team Driving,
    Documents, and Trip Logs. Default value is false if omitted. Note: only
    available to customers of Connected Forms.
    """

    is_deactivated: Optional[bool] = FieldInfo(alias="isDeactivated", default=None)
    """[DEPRECATED] A boolean indicating whether or not the driver is deactivated.

    Use `driverActivationStatus` instead.
    """

    license_number: Optional[str] = FieldInfo(alias="licenseNumber", default=None)
    """Driver's state issued license number.

    The combination of this number and `licenseState` must be unique.
    """

    license_state: Optional[str] = FieldInfo(alias="licenseState", default=None)
    """
    Abbreviation of US state, Canadian province, or US territory that issued
    driver's license.
    """

    locale: Optional[
        Literal["us", "at", "be", "ca", "gb", "fr", "de", "ie", "it", "lu", "mx", "nl", "es", "ch", "pr"]
    ] = None
    """Locale override (uncommon).

    These are specified by ISO 3166-2 country codes for supported locales. Valid
    values: `us`, `at`, `be`, `ca`, `gb`, `fr`, `de`, `ie`, `it`, `lu`, `mx`, `nl`,
    `es`, `ch`, `pr`.
    """

    name: Optional[str] = None
    """Driver's name."""

    notes: Optional[str] = None
    """Notes about the driver."""

    peer_group_tag: Optional[DataPeerGroupTag] = FieldInfo(alias="peerGroupTag", default=None)
    """A minified tag object"""

    phone: Optional[str] = None
    """Phone number of the driver."""

    static_assigned_vehicle: Optional[DataStaticAssignedVehicle] = FieldInfo(
        alias="staticAssignedVehicle", default=None
    )
    """Vehicle assigned to the driver for static vehicle assignments. (uncommon)."""

    tachograph_card_number: Optional[str] = FieldInfo(alias="tachographCardNumber", default=None)
    """Driver's assigned tachograph card number (Europe specific)"""

    tags: Optional[List[DataTag]] = None
    """The tags this driver belongs to."""

    timezone: Optional[str] = None
    """
    Home terminal timezone, in order to indicate what time zone should be used to
    calculate the ELD logs. Driver timezones use
    [IANA timezone database](https://www.iana.org/time-zones) keys (e.g.
    `America/Los_Angeles`, `America/New_York`, `Europe/London`, etc.). You can find
    a mapping of common timezone formats to IANA timezone keys
    [here](https://unicode.org/cldr/charts/latest/supplemental/zone_tzid.html).
    """

    updated_at_time: Optional[str] = FieldInfo(alias="updatedAtTime", default=None)
    """The date and time this driver was last updated in RFC 3339 format."""

    us_driver_ruleset_override: Optional[DataUsDriverRulesetOverride] = FieldInfo(
        alias="usDriverRulesetOverride", default=None
    )
    """US Driver Ruleset override for a given driver.

    If the driver is operating under a ruleset different from the organization
    default, the override is used. Updating this value only updates the override
    setting for this driver. Explicitly setting this field to `null` will delete
    driver's ruleset override. If the driver does not have an override ruleset set,
    the response will not include any usDriverRulesetOverride information.
    """

    username: Optional[str] = None
    """Driver's login username into the driver app.

    The username may not contain spaces or the '@' symbol. The username must be
    unique.
    """

    vehicle_group_tag: Optional[DataVehicleGroupTag] = FieldInfo(alias="vehicleGroupTag", default=None)
    """Tag which determines which vehicles a driver will see when selecting vehicles."""

    waiting_time_duty_status_enabled: Optional[bool] = FieldInfo(alias="waitingTimeDutyStatusEnabled", default=None)
    """Flag indicating this driver may select waiting time duty status in ELD logs."""


class Driver(BaseModel):
    data: Optional[Data] = None
    """A driver object"""
