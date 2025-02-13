# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DriverUpdateParams", "Attribute", "CarrierSettings", "HosSetting", "UsDriverRulesetOverride"]


class DriverUpdateParams(TypedDict, total=False):
    attributes: Iterable[Attribute]

    carrier_settings: Annotated[CarrierSettings, PropertyInfo(alias="carrierSettings")]
    """Carrier for a given driver.

    If the driver's carrier differs from the general organization's carrier
    settings, the override value is used. Updating this value only updates the
    override setting for this driver.
    """

    current_id_card_code: Annotated[str, PropertyInfo(alias="currentIdCardCode")]
    """The ID Card Code on the back of the physical card assigned to the driver.

    Contact Samsara if you would like to enable this feature.
    """

    deactivated_at_time: Annotated[str, PropertyInfo(alias="deactivatedAtTime")]
    """
    The date and time this driver is considered to be deactivated in RFC 3339
    format.
    """

    driver_activation_status: Annotated[Literal["active", "deactivated"], PropertyInfo(alias="driverActivationStatus")]
    """A value indicating whether the driver is active or deactivated.

    Valid values: `active`, `deactivated`.
    """

    eld_adverse_weather_exemption_enabled: Annotated[bool, PropertyInfo(alias="eldAdverseWeatherExemptionEnabled")]
    """Flag indicating this driver may use Adverse Weather exemptions in ELD logs."""

    eld_big_day_exemption_enabled: Annotated[bool, PropertyInfo(alias="eldBigDayExemptionEnabled")]
    """Flag indicating this driver may use Big Day exemption in ELD logs."""

    eld_day_start_hour: Annotated[int, PropertyInfo(alias="eldDayStartHour")]
    """
    `0` indicating midnight-to-midnight ELD driving hours, `12` to indicate
    noon-to-noon driving hours.
    """

    eld_exempt: Annotated[bool, PropertyInfo(alias="eldExempt")]
    """Flag indicating this driver is exempt from the Electronic Logging Mandate."""

    eld_exempt_reason: Annotated[str, PropertyInfo(alias="eldExemptReason")]
    """
    Reason that this driver is exempt from the Electronic Logging Mandate (see
    eldExempt).
    """

    eld_pc_enabled: Annotated[bool, PropertyInfo(alias="eldPcEnabled")]
    """
    Flag indicating this driver may select the Personal Conveyance duty status in
    ELD logs.
    """

    eld_ym_enabled: Annotated[bool, PropertyInfo(alias="eldYmEnabled")]
    """Flag indicating this driver may select the Yard Move duty status in ELD logs."""

    external_ids: Annotated[Dict[str, str], PropertyInfo(alias="externalIds")]
    """
    The [external IDs](https://developers.samsara.com/docs/external-ids) for the
    given object.
    """

    has_driving_features_hidden: Annotated[bool, PropertyInfo(alias="hasDrivingFeaturesHidden")]
    """
    A boolean indicating whether the driver has driving-related features hidden in
    the Driver App, including Vehicle selection, HOS, Routing, Team Driving,
    Documents, and Trip Logs. Default value is false if omitted. Note: only
    available to customers of Connected Forms.
    """

    hos_setting: Annotated[HosSetting, PropertyInfo(alias="hosSetting")]
    """Hos settings for a driver."""

    license_number: Annotated[str, PropertyInfo(alias="licenseNumber")]
    """Driver's state issued license number.

    The combination of this number and `licenseState` must be unique.
    """

    license_state: Annotated[str, PropertyInfo(alias="licenseState")]
    """
    Abbreviation of US state, Canadian province, or US territory that issued
    driver's license.
    """

    locale: Literal["us", "at", "be", "ca", "gb", "fr", "de", "ie", "it", "lu", "mx", "nl", "es", "ch", "pr"]
    """Locale override (uncommon).

    These are specified by ISO 3166-2 country codes for supported locales. Valid
    values: `us`, `at`, `be`, `ca`, `gb`, `fr`, `de`, `ie`, `it`, `lu`, `mx`, `nl`,
    `es`, `ch`, `pr`.
    """

    name: str
    """Driver's name."""

    notes: str
    """Notes about the driver."""

    password: str
    """Password that the driver can use to login to the Samsara driver app."""

    peer_group_tag_id: Annotated[str, PropertyInfo(alias="peerGroupTagId")]
    """
    The peer group tag id this driver belong to, leave blank to be in group with
    everyone, used for gamification.
    """

    phone: str
    """Phone number of the driver."""

    static_assigned_vehicle_id: Annotated[str, PropertyInfo(alias="staticAssignedVehicleId")]
    """ID of vehicle that the driver is permanently assigned to. (uncommon)."""

    tachograph_card_number: Annotated[str, PropertyInfo(alias="tachographCardNumber")]
    """Driver's assigned tachograph card number (Europe specific)"""

    tag_ids: Annotated[List[str], PropertyInfo(alias="tagIds")]
    """IDs of tags the driver is associated with.

    If your access to the API is scoped by one or more tags, this field is required
    to pass in.
    """

    timezone: str
    """
    Home terminal timezone, in order to indicate what time zone should be used to
    calculate the ELD logs. Driver timezones use
    [IANA timezone database](https://www.iana.org/time-zones) keys (e.g.
    `America/Los_Angeles`, `America/New_York`, `Europe/London`, etc.). You can find
    a mapping of common timezone formats to IANA timezone keys
    [here](https://unicode.org/cldr/charts/latest/supplemental/zone_tzid.html).
    """

    us_driver_ruleset_override: Annotated[UsDriverRulesetOverride, PropertyInfo(alias="usDriverRulesetOverride")]
    """US Driver Ruleset override for a given driver.

    If the driver is operating under a ruleset different from the organization
    default, the override is used. Updating this value only updates the override
    setting for this driver. Explicitly setting this field to `null` will delete
    driver's ruleset override. If the driver does not have an override ruleset set,
    the response will not include any usDriverRulesetOverride information.
    """

    username: str
    """Driver's login username into the driver app.

    The username may not contain spaces or the '@' symbol. The username must be
    unique.
    """

    vehicle_group_tag_id: Annotated[str, PropertyInfo(alias="vehicleGroupTagId")]
    """
    Tag ID which determines which vehicles a driver will see when selecting
    vehicles.
    """

    waiting_time_duty_status_enabled: Annotated[bool, PropertyInfo(alias="waitingTimeDutyStatusEnabled")]
    """Flag indicating this driver may select waiting time duty status in ELD logs"""


class Attribute(TypedDict, total=False):
    id: str
    """The samsara id of the attribute object."""

    name: str
    """Name of attribute."""

    number_values: Annotated[Iterable[float], PropertyInfo(alias="numberValues")]
    """Number values that are associated with this attribute."""

    string_values: Annotated[List[str], PropertyInfo(alias="stringValues")]
    """String values that are associated with this attribute."""


class CarrierSettings(TypedDict, total=False):
    carrier_name: Annotated[str, PropertyInfo(alias="carrierName")]
    """Carrier for a given driver."""

    dot_number: Annotated[int, PropertyInfo(alias="dotNumber")]
    """Carrier US DOT Number.

    If this differs from the general organization's settings, the override value is
    used. Updating this value only updates the override setting for this driver.
    """

    home_terminal_address: Annotated[str, PropertyInfo(alias="homeTerminalAddress")]
    """Address of the place of business at which a driver ordinarily reports for work."""

    home_terminal_name: Annotated[str, PropertyInfo(alias="homeTerminalName")]
    """Name of the place of business at which a driver ordinarily reports for work."""

    main_office_address: Annotated[str, PropertyInfo(alias="mainOfficeAddress")]
    """Main office address for a given driver.

    If this differs from the general organization's settings, the override value is
    used.
    """


class HosSetting(TypedDict, total=False):
    heavy_haul_exemption_toggle_enabled: Annotated[bool, PropertyInfo(alias="heavyHaulExemptionToggleEnabled")]
    """Flag indicating this driver may use the Heavy Haul exemption in ELD logs."""


class UsDriverRulesetOverride(TypedDict, total=False):
    cycle: Required[
        Literal[
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

    restart: Required[Literal["34-hour Restart", "24-hour Restart", "36-hour Restart", "72-hour Restart", "None"]]
    """
    Amount of time necessary for the driver to be resting in order to restart their
    cycle. Valid values: `34-hour Restart`, `24-hour Restart`, `36-hour Restart`,
    `72-hour Restart`, `None`.
    """

    restbreak: Required[Literal["Property (off-duty/sleeper)", "California Mealbreak (off-duty/sleeper)", "None"]]
    """The restbreak required for this driver.

    Valid values: `Property (off-duty/sleeper)`,
    `California Mealbreak (off-duty/sleeper)`, `None`.
    """

    us_state_to_override: Required[
        Annotated[
            Literal["", "AK", "CA", "FL", "NE", "NC", "OK", "OR", "SC", "TX", "WI"],
            PropertyInfo(alias="usStateToOverride"),
        ]
    ]
    """The jurisdiction of the ruleset applied to this driver.

    These are specified by either the ISO 3166-2 postal code for the supported US
    states, or empty string '' for US Federal Ruleset jurisdiction. Valid values:
    ``, `AK`, `CA`, `FL`, `NE`, `NC`, `OK`, `OR`, `SC`, `TX`, `WI`.
    """
