# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "ConfigurationUpdateParams",
    "Action",
    "ActionActionParams",
    "ActionActionParamsDriverAppNotification",
    "ActionActionParamsDriverAppNotificationInAppNotificationOptions",
    "ActionActionParamsDriverAppNotificationPushNotificationOptions",
    "ActionActionParamsRecipient",
    "ActionActionParamsWebhooks",
    "OperationalSettings",
    "OperationalSettingsTimeRange",
    "Scope",
    "ScopeAsset",
    "ScopeDriver",
    "ScopeTag",
    "ScopeWidget",
    "Trigger",
    "TriggerTriggerParams",
    "TriggerTriggerParamsAmbientTemperature",
    "TriggerTriggerParamsCellSignalLoss",
    "TriggerTriggerParamsDefLevel",
    "TriggerTriggerParamsDeviceMovement",
    "TriggerTriggerParamsDocumentSubmitted",
    "TriggerTriggerParamsDvirSubmittedDevice",
    "TriggerTriggerParamsEngineIdle",
    "TriggerTriggerParamsEngineOff",
    "TriggerTriggerParamsEngineOn",
    "TriggerTriggerParamsFuelLevel",
    "TriggerTriggerParamsGatewayDisconnected",
    "TriggerTriggerParamsGatewayUnplugged",
    "TriggerTriggerParamsGeofenceEntry",
    "TriggerTriggerParamsGeofenceEntryLocation",
    "TriggerTriggerParamsGeofenceEntryLocationCircle",
    "TriggerTriggerParamsGeofenceEntryLocationPolygon",
    "TriggerTriggerParamsGeofenceEntryLocationPolygonVertex",
    "TriggerTriggerParamsGeofenceExit",
    "TriggerTriggerParamsGeofenceExitLocation",
    "TriggerTriggerParamsGeofenceExitLocationCircle",
    "TriggerTriggerParamsGeofenceExitLocationPolygon",
    "TriggerTriggerParamsGeofenceExitLocationPolygonVertex",
    "TriggerTriggerParamsGpsSignalLoss",
    "TriggerTriggerParamsHarshEvent",
    "TriggerTriggerParamsHosViolation",
    "TriggerTriggerParamsInsideGeofence",
    "TriggerTriggerParamsInsideGeofenceLocation",
    "TriggerTriggerParamsInsideGeofenceLocationCircle",
    "TriggerTriggerParamsInsideGeofenceLocationPolygon",
    "TriggerTriggerParamsInsideGeofenceLocationPolygonVertex",
    "TriggerTriggerParamsOutOfRoute",
    "TriggerTriggerParamsOutsideGeofence",
    "TriggerTriggerParamsOutsideGeofenceLocation",
    "TriggerTriggerParamsOutsideGeofenceLocationCircle",
    "TriggerTriggerParamsOutsideGeofenceLocationPolygon",
    "TriggerTriggerParamsOutsideGeofenceLocationPolygonVertex",
    "TriggerTriggerParamsPanicButton",
    "TriggerTriggerParamsRouteStopEstimatedArrival",
    "TriggerTriggerParamsRouteStopEstimatedArrivalLocation",
    "TriggerTriggerParamsRouteStopEstimatedArrivalLocationCircle",
    "TriggerTriggerParamsRouteStopEstimatedArrivalLocationPolygon",
    "TriggerTriggerParamsRouteStopEstimatedArrivalLocationPolygonVertex",
    "TriggerTriggerParamsScheduledMaintenance",
    "TriggerTriggerParamsScheduledMaintenanceByEngineHours",
    "TriggerTriggerParamsScheduledMaintenanceOdometer",
    "TriggerTriggerParamsSpeed",
    "TriggerTriggerParamsTireFaultCode",
    "TriggerTriggerParamsUnassignedDriving",
    "TriggerTriggerParamsVehicleBatteryVoltage",
    "TriggerTriggerParamsVehicleFaultCode",
    "TriggerTriggerParamsVehicleFaultCodeSpecificFaultCode",
]


class ConfigurationUpdateParams(TypedDict, total=False):
    id: Required[str]
    """The unqiue Samsara id of the alert configuration."""

    actions: Iterable[Action]
    """An array of actions."""

    external_ids: Annotated[Dict[str, str], PropertyInfo(alias="externalIds")]
    """A map of external ids"""

    is_enabled: Annotated[bool, PropertyInfo(alias="isEnabled")]
    """Whether the alert is enabled or not."""

    name: str
    """The custom name of the configuration."""

    operational_settings: Annotated[OperationalSettings, PropertyInfo(alias="operationalSettings")]
    """Settings on when the alert should be operational."""

    scope: Scope
    """What the triggers are scoped to. These are the objects this alert applies to."""

    triggers: Iterable[Trigger]
    """An array of triggers."""


class ActionActionParamsDriverAppNotificationInAppNotificationOptions(TypedDict, total=False):
    is_enabled: Required[Annotated[bool, PropertyInfo(alias="isEnabled")]]
    """Whether in-app notifications are enabled."""

    can_dictate_alert_title: Annotated[bool, PropertyInfo(alias="canDictateAlertTitle")]
    """Whether the alert will dictate the title of the alert.

    Both canDictateAlertTitle and canPlayAlertSound should be enabled or disabled
    together.
    """

    can_play_alert_sound: Annotated[bool, PropertyInfo(alias="canPlayAlertSound")]
    """Whether the alert will play a sound.

    Both canDictateAlertTitle and canPlayAlertSound should be enabled or disabled
    together.
    """

    custom_text: Annotated[str, PropertyInfo(alias="customText")]
    """Custom text to display in the notification (320 character max)."""


class ActionActionParamsDriverAppNotificationPushNotificationOptions(TypedDict, total=False):
    is_enabled: Required[Annotated[bool, PropertyInfo(alias="isEnabled")]]
    """Whether push notifications are enabled."""


class ActionActionParamsDriverAppNotification(TypedDict, total=False):
    in_app_notification_options: Annotated[
        ActionActionParamsDriverAppNotificationInAppNotificationOptions, PropertyInfo(alias="inAppNotificationOptions")
    ]
    """Options for in-app notifications"""

    push_notification_options: Annotated[
        ActionActionParamsDriverAppNotificationPushNotificationOptions, PropertyInfo(alias="pushNotificationOptions")
    ]
    """Options for push notifications"""


class ActionActionParamsRecipient(TypedDict, total=False):
    type: Required[Literal["user", "contact", "role"]]
    """The type of recipients Valid values: `user`, `contact`, `role`"""

    contact_id: Annotated[str, PropertyInfo(alias="contactId")]
    """The ID of the contact."""

    notification_types: Annotated[List[Literal["push", "sms", "email"]], PropertyInfo(alias="notificationTypes")]
    """How the user/contact/role should be notified."""

    role_id: Annotated[str, PropertyInfo(alias="roleId")]
    """The ID of the role."""

    user_id: Annotated[str, PropertyInfo(alias="userId")]
    """The ID of the user."""


class ActionActionParamsWebhooks(TypedDict, total=False):
    webhook_ids: Required[Annotated[List[str], PropertyInfo(alias="webhookIds")]]
    """The webhook IDs."""

    payload_type: Annotated[Literal["legacy", "enriched"], PropertyInfo(alias="payloadType")]
    """This determines the alert webhook payload type to use.

    Learn more: https://developers.samsara.com/docs/webhook-reference. Valid values:
    `legacy`, `enriched`
    """


class ActionActionParams(TypedDict, total=False):
    driver_app_notification: Annotated[
        ActionActionParamsDriverAppNotification, PropertyInfo(alias="driverAppNotification")
    ]
    """Driver app notification settings"""

    recipients: Iterable[ActionActionParamsRecipient]
    """Recipient of the action."""

    webhooks: ActionActionParamsWebhooks
    """The webhook configuration for an Action."""


class Action(TypedDict, total=False):
    action_type_id: Required[Annotated[int, PropertyInfo(alias="actionTypeId")]]
    """The id of the of the action type.

    Reference the following list for the ids: The following action types are in
    Beta: Driver App Push = 5 The following action types are Stable: Notification
    (Email, Text, Samsara Fleet Push) = 1 Dashboard Notification = 3 Webhook = 4
    Slack = 6
    """

    action_params: Annotated[ActionActionParams, PropertyInfo(alias="actionParams")]
    """The action type specific details.

    Set webhookIds for Slack or Webhook actions. Set recipients for Notifications.
    Set driverAppNotification for Driver App Push. Other action types don't need to
    set a param.
    """


class OperationalSettingsTimeRange(TypedDict, total=False):
    days_of_week: Required[
        Annotated[
            List[Literal["FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"]],
            PropertyInfo(alias="daysOfWeek"),
        ]
    ]
    """Which days this timezone applies to."""

    end_time: Required[Annotated[str, PropertyInfo(alias="endTime")]]
    """The time of day at which the time range starts.

    In 24 hour kitchen clock format.
    """

    start_time: Required[Annotated[str, PropertyInfo(alias="startTime")]]
    """The time of day at which the time range starts.

    In 24 hour kitchen clock format.
    """

    timezone: Required[str]
    """
    The timezone of the time range uses
    [IANA timezone database](https://www.iana.org/time-zones) keys (e.g.
    `America/Los_Angeles`, `America/New_York`, `Europe/London`, etc.). You can find
    a mapping of common timezone formats to IANA timezone keys
    [here](https://unicode.org/cldr/charts/latest/supplemental/zone_tzid.html).
    """


class OperationalSettings(TypedDict, total=False):
    time_ranges: Required[Annotated[Iterable[OperationalSettingsTimeRange], PropertyInfo(alias="timeRanges")]]
    """The time ranges this alert applies to."""

    time_range_type: Required[
        Annotated[Literal["activeBetween", "inactiveBetween"], PropertyInfo(alias="timeRangeType")]
    ]
    """The type of time ranges. Valid values: `activeBetween`, `inactiveBetween`"""


class ScopeAsset(TypedDict, total=False):
    asset_id: Required[Annotated[str, PropertyInfo(alias="assetId")]]
    """ID of the asset."""

    asset_type: Required[
        Annotated[
            Literal["uncategorized", "trailer", "equipment", "unpowered", "vehicle"], PropertyInfo(alias="assetType")
        ]
    ]
    """The operational context in which the asset interacts with the Samsara system.

    Examples: Vehicle (eg: truck, bus...), Trailer (eg: dry van, reefer,
    flatbed...), Powered Equipment (eg: dozer, crane...), Unpowered Equipment (eg:
    container, dumpster...), or Uncategorized. Valid values: `uncategorized`,
    `trailer`, `equipment`, `unpowered`, `vehicle`
    """


class ScopeDriver(TypedDict, total=False):
    driver_id: Required[Annotated[str, PropertyInfo(alias="driverId")]]
    """ID of the driver."""


class ScopeTag(TypedDict, total=False):
    id: Required[str]
    """ID of the tag"""

    name: Required[str]
    """Name of the tag."""

    parent_tag_id: Annotated[str, PropertyInfo(alias="parentTagId")]
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class ScopeWidget(TypedDict, total=False):
    widget_id: Required[Annotated[str, PropertyInfo(alias="widgetId")]]
    """ID of the widget."""


class Scope(TypedDict, total=False):
    all: Required[bool]
    """Whether it applies to all applicable objects."""

    assets: Iterable[ScopeAsset]
    """The assets these triggers are scoped to."""

    drivers: Iterable[ScopeDriver]
    """The drivers these triggers are scoped to."""

    tags: Iterable[ScopeTag]
    """The tags these triggers are scoped to."""

    widgets: Iterable[ScopeWidget]
    """The widgets these triggers are scoped to."""


class TriggerTriggerParamsAmbientTemperature(TypedDict, total=False):
    min_duration_milliseconds: Required[Annotated[int, PropertyInfo(alias="minDurationMilliseconds")]]
    """The number of milliseconds the trigger needs to stay active before alerting."""

    operation: Required[Literal["GREATER", "INSIDE_RANGE", "LESS", "OUTSIDE_RANGE"]]
    """How to evaluate the threshold.

    Valid values: `GREATER`, `INSIDE_RANGE`, `LESS`, `OUTSIDE_RANGE`
    """

    temperature_celcius: Required[Annotated[int, PropertyInfo(alias="temperatureCelcius")]]
    """The temperature in Celcius threshold value."""

    cargo_is_full: Annotated[bool, PropertyInfo(alias="cargoIsFull")]
    """Whether the cargo is full."""

    doors_are_closed: Annotated[bool, PropertyInfo(alias="doorsAreClosed")]
    """Whether the doors are closed."""


class TriggerTriggerParamsCellSignalLoss(TypedDict, total=False):
    min_duration_milliseconds: Required[Annotated[int, PropertyInfo(alias="minDurationMilliseconds")]]
    """The number of milliseconds the trigger needs to stay active before alerting."""


class TriggerTriggerParamsDefLevel(TypedDict, total=False):
    def_level_percent: Required[Annotated[int, PropertyInfo(alias="defLevelPercent")]]
    """The DEF percentage threshold value."""

    min_duration_milliseconds: Required[Annotated[int, PropertyInfo(alias="minDurationMilliseconds")]]
    """The number of milliseconds the trigger needs to stay active before alerting."""

    operation: Required[Literal["GREATER", "LESS"]]
    """How to evaluate the threshold. Valid values: `GREATER`, `LESS`"""


class TriggerTriggerParamsDeviceMovement(TypedDict, total=False):
    min_duration_milliseconds: Required[Annotated[int, PropertyInfo(alias="minDurationMilliseconds")]]
    """The number of milliseconds the trigger needs to stay active before alerting."""


class TriggerTriggerParamsDocumentSubmitted(TypedDict, total=False):
    template_ids: Required[Annotated[List[str], PropertyInfo(alias="templateIds")]]
    """Specific template IDs to be alerted on."""


class TriggerTriggerParamsDvirSubmittedDevice(TypedDict, total=False):
    dvir_min_duration_milliseconds: Annotated[int, PropertyInfo(alias="dvirMinDurationMilliseconds")]
    """
    The trigger will only fire if the selected DVIR types are submitted within the
    duration.
    """

    dvir_submission_types: Annotated[
        List[Literal["SAFE_NO_DEFECTS", "SAFE_WITH_DEFECTS", "UNSAFE"]], PropertyInfo(alias="dvirSubmissionTypes")
    ]
    """Filter to these types of DVIR submissions."""


class TriggerTriggerParamsEngineIdle(TypedDict, total=False):
    min_duration_milliseconds: Required[Annotated[int, PropertyInfo(alias="minDurationMilliseconds")]]
    """The number of milliseconds the trigger needs to stay active before alerting."""


class TriggerTriggerParamsEngineOff(TypedDict, total=False):
    min_duration_milliseconds: Required[Annotated[int, PropertyInfo(alias="minDurationMilliseconds")]]
    """The number of milliseconds the trigger needs to stay active before alerting."""


class TriggerTriggerParamsEngineOn(TypedDict, total=False):
    min_duration_milliseconds: Required[Annotated[int, PropertyInfo(alias="minDurationMilliseconds")]]
    """The number of milliseconds the trigger needs to stay active before alerting."""


class TriggerTriggerParamsFuelLevel(TypedDict, total=False):
    fuel_level_percent: Required[Annotated[int, PropertyInfo(alias="fuelLevelPercent")]]
    """The fuel level percentage threshold value."""

    min_duration_milliseconds: Required[Annotated[int, PropertyInfo(alias="minDurationMilliseconds")]]
    """The number of milliseconds the trigger needs to stay active before alerting."""

    operation: Required[Literal["LESS"]]
    """How to evaluate the threshold. Valid values: `LESS`"""


class TriggerTriggerParamsGatewayDisconnected(TypedDict, total=False):
    min_duration_milliseconds: Required[Annotated[int, PropertyInfo(alias="minDurationMilliseconds")]]
    """The number of milliseconds the trigger needs to stay active before alerting.

    Can only be either 900000 (15 minutes) or 3600000 (60 min).
    """


class TriggerTriggerParamsGatewayUnplugged(TypedDict, total=False):
    min_duration_milliseconds: Required[Annotated[int, PropertyInfo(alias="minDurationMilliseconds")]]
    """The number of milliseconds the trigger needs to stay active before alerting."""


class TriggerTriggerParamsGeofenceEntryLocationCircle(TypedDict, total=False):
    name: Required[str]
    """The name of the cirlce."""

    radius_meters: Required[Annotated[int, PropertyInfo(alias="radiusMeters")]]
    """The radius of the circular geofence in meters."""

    latitude: float
    """Latitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """

    longitude: float
    """Longitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """


class TriggerTriggerParamsGeofenceEntryLocationPolygonVertex(TypedDict, total=False):
    latitude: Required[float]
    """The latitude of a geofence vertex in decimal degrees."""

    longitude: Required[float]
    """The longitude of a geofence vertex in decimal degrees."""


class TriggerTriggerParamsGeofenceEntryLocationPolygon(TypedDict, total=False):
    name: Required[str]
    """The name of the polygon."""

    vertices: Iterable[TriggerTriggerParamsGeofenceEntryLocationPolygonVertex]
    """The vertices of the polygon geofence.

    These geofence vertices describe the perimeter of the polygon, and must consist
    of at least 3 vertices and less than 40.
    """


class TriggerTriggerParamsGeofenceEntryLocation(TypedDict, total=False):
    address_ids: Annotated[List[str], PropertyInfo(alias="addressIds")]
    """All locations with selected address IDs will trigger."""

    address_types: Annotated[
        List[Literal["alertsOnly", "industrialSite", "riskZone", "shortHaul", "undefined", "workforceSite", "yard"]],
        PropertyInfo(alias="addressTypes"),
    ]
    """All locations with the selected address types will trigger."""

    circle: TriggerTriggerParamsGeofenceEntryLocationCircle
    """Information about a circular geofence.

    This field is only needed if the geofence is a circle.
    """

    polygon: TriggerTriggerParamsGeofenceEntryLocationPolygon
    """Information about a polygon geofence.

    This field is only needed if the geofence is a polygon.
    """

    tag_ids: Annotated[List[str], PropertyInfo(alias="tagIds")]
    """All locations with selected tag will trigger."""


class TriggerTriggerParamsGeofenceEntry(TypedDict, total=False):
    location: Required[TriggerTriggerParamsGeofenceEntryLocation]
    """A location.

    Polygon and Circle is deprecated, but may be set for old Alerts. At least one
    location must be selected.
    """


class TriggerTriggerParamsGeofenceExitLocationCircle(TypedDict, total=False):
    name: Required[str]
    """The name of the cirlce."""

    radius_meters: Required[Annotated[int, PropertyInfo(alias="radiusMeters")]]
    """The radius of the circular geofence in meters."""

    latitude: float
    """Latitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """

    longitude: float
    """Longitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """


class TriggerTriggerParamsGeofenceExitLocationPolygonVertex(TypedDict, total=False):
    latitude: Required[float]
    """The latitude of a geofence vertex in decimal degrees."""

    longitude: Required[float]
    """The longitude of a geofence vertex in decimal degrees."""


class TriggerTriggerParamsGeofenceExitLocationPolygon(TypedDict, total=False):
    name: Required[str]
    """The name of the polygon."""

    vertices: Iterable[TriggerTriggerParamsGeofenceExitLocationPolygonVertex]
    """The vertices of the polygon geofence.

    These geofence vertices describe the perimeter of the polygon, and must consist
    of at least 3 vertices and less than 40.
    """


class TriggerTriggerParamsGeofenceExitLocation(TypedDict, total=False):
    address_ids: Annotated[List[str], PropertyInfo(alias="addressIds")]
    """All locations with selected address IDs will trigger."""

    address_types: Annotated[
        List[Literal["alertsOnly", "industrialSite", "riskZone", "shortHaul", "undefined", "workforceSite", "yard"]],
        PropertyInfo(alias="addressTypes"),
    ]
    """All locations with the selected address types will trigger."""

    circle: TriggerTriggerParamsGeofenceExitLocationCircle
    """Information about a circular geofence.

    This field is only needed if the geofence is a circle.
    """

    polygon: TriggerTriggerParamsGeofenceExitLocationPolygon
    """Information about a polygon geofence.

    This field is only needed if the geofence is a polygon.
    """

    tag_ids: Annotated[List[str], PropertyInfo(alias="tagIds")]
    """All locations with selected tag will trigger."""


class TriggerTriggerParamsGeofenceExit(TypedDict, total=False):
    location: Required[TriggerTriggerParamsGeofenceExitLocation]
    """A location.

    Polygon and Circle is deprecated, but may be set for old Alerts. At least one
    location must be selected.
    """


class TriggerTriggerParamsGpsSignalLoss(TypedDict, total=False):
    min_duration_milliseconds: Required[Annotated[int, PropertyInfo(alias="minDurationMilliseconds")]]
    """The number of milliseconds the trigger needs to stay active before alerting."""


class TriggerTriggerParamsHarshEvent(TypedDict, total=False):
    types: Required[
        List[
            Literal[
                "haAccel",
                "haBraking",
                "haCameraMisaligned",
                "haCrash",
                "haDistractedDriving",
                "haDistractedDrivingCalibration",
                "haDrinkPolicy",
                "haDriverObstructionPolicy",
                "haDrowsinessDetection",
                "haEvent",
                "haFalsePositive",
                "haFoodPolicy",
                "haInvalid",
                "haLaneDeparture",
                "haMaskPolicy",
                "haNearCollision",
                "haOutwardObstructionPolicy",
                "haPassengerPolicy",
                "haPhonePolicy",
                "haPolicyDetector",
                "haRearCollisionWarning",
                "haRolledStopSign",
                "haRollover",
                "haRolloverProtectionBrakeControlActivated",
                "haRolloverProtectionEngineControlActivated",
                "haSeatbeltPolicy",
                "haSharpTurn",
                "haSignDetection",
                "haSmokingPolicy",
                "haSpeeding",
                "haTailgating",
                "haTileRollingRailroadCrossing",
                "haTileRollingStopSign",
                "haVulnerableRoadUserCollisionWarning",
                "haYawControlBrakeControlActivated",
                "haYawControlEngineControlActivated",
            ]
        ]
    ]
    """On which harsh events to trigger on."""


class TriggerTriggerParamsHosViolation(TypedDict, total=False):
    max_until_violation_milliseconds: Required[Annotated[int, PropertyInfo(alias="maxUntilViolationMilliseconds")]]
    """Alert if driver has this specified time until driving causes an HOS violation."""

    violation: Required[
        Literal[
            "CaliforniaMealbreakMissed",
            "CycleHoursOn",
            "DailyDrivingHours",
            "DailyOnDutyHours",
            "Invalid",
            "RestbreakMissed",
            "ShiftDrivingHours",
            "ShiftHours",
            "ShiftOnDutyHours",
            "UnsubmittedLogs",
        ]
    ]
    """The type of HOS violation.

    Valid values: `CaliforniaMealbreakMissed`, `CycleHoursOn`, `DailyDrivingHours`,
    `DailyOnDutyHours`, `Invalid`, `RestbreakMissed`, `ShiftDrivingHours`,
    `ShiftHours`, `ShiftOnDutyHours`, `UnsubmittedLogs`
    """


class TriggerTriggerParamsInsideGeofenceLocationCircle(TypedDict, total=False):
    name: Required[str]
    """The name of the cirlce."""

    radius_meters: Required[Annotated[int, PropertyInfo(alias="radiusMeters")]]
    """The radius of the circular geofence in meters."""

    latitude: float
    """Latitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """

    longitude: float
    """Longitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """


class TriggerTriggerParamsInsideGeofenceLocationPolygonVertex(TypedDict, total=False):
    latitude: Required[float]
    """The latitude of a geofence vertex in decimal degrees."""

    longitude: Required[float]
    """The longitude of a geofence vertex in decimal degrees."""


class TriggerTriggerParamsInsideGeofenceLocationPolygon(TypedDict, total=False):
    name: Required[str]
    """The name of the polygon."""

    vertices: Iterable[TriggerTriggerParamsInsideGeofenceLocationPolygonVertex]
    """The vertices of the polygon geofence.

    These geofence vertices describe the perimeter of the polygon, and must consist
    of at least 3 vertices and less than 40.
    """


class TriggerTriggerParamsInsideGeofenceLocation(TypedDict, total=False):
    address_ids: Annotated[List[str], PropertyInfo(alias="addressIds")]
    """All locations with selected address IDs will trigger."""

    address_types: Annotated[
        List[Literal["alertsOnly", "industrialSite", "riskZone", "shortHaul", "undefined", "workforceSite", "yard"]],
        PropertyInfo(alias="addressTypes"),
    ]
    """All locations with the selected address types will trigger."""

    circle: TriggerTriggerParamsInsideGeofenceLocationCircle
    """Information about a circular geofence.

    This field is only needed if the geofence is a circle.
    """

    polygon: TriggerTriggerParamsInsideGeofenceLocationPolygon
    """Information about a polygon geofence.

    This field is only needed if the geofence is a polygon.
    """

    tag_ids: Annotated[List[str], PropertyInfo(alias="tagIds")]
    """All locations with selected tag will trigger."""


class TriggerTriggerParamsInsideGeofence(TypedDict, total=False):
    location: Required[TriggerTriggerParamsInsideGeofenceLocation]
    """A location.

    Polygon and Circle is deprecated, but may be set for old Alerts. At least one
    location must be selected.
    """

    min_duration_milliseconds: Required[Annotated[int, PropertyInfo(alias="minDurationMilliseconds")]]
    """The number of milliseconds the trigger needs to stay active before alerting."""


class TriggerTriggerParamsOutOfRoute(TypedDict, total=False):
    max_off_route_meters: Required[Annotated[int, PropertyInfo(alias="maxOffRouteMeters")]]
    """
    The minimum distance in meters a vehicle has to be from its active route path to
    be considered out of its route.
    """

    min_duration_milliseconds: Required[Annotated[int, PropertyInfo(alias="minDurationMilliseconds")]]
    """The number of milliseconds the trigger needs to stay active before alerting."""


class TriggerTriggerParamsOutsideGeofenceLocationCircle(TypedDict, total=False):
    name: Required[str]
    """The name of the cirlce."""

    radius_meters: Required[Annotated[int, PropertyInfo(alias="radiusMeters")]]
    """The radius of the circular geofence in meters."""

    latitude: float
    """Latitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """

    longitude: float
    """Longitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """


class TriggerTriggerParamsOutsideGeofenceLocationPolygonVertex(TypedDict, total=False):
    latitude: Required[float]
    """The latitude of a geofence vertex in decimal degrees."""

    longitude: Required[float]
    """The longitude of a geofence vertex in decimal degrees."""


class TriggerTriggerParamsOutsideGeofenceLocationPolygon(TypedDict, total=False):
    name: Required[str]
    """The name of the polygon."""

    vertices: Iterable[TriggerTriggerParamsOutsideGeofenceLocationPolygonVertex]
    """The vertices of the polygon geofence.

    These geofence vertices describe the perimeter of the polygon, and must consist
    of at least 3 vertices and less than 40.
    """


class TriggerTriggerParamsOutsideGeofenceLocation(TypedDict, total=False):
    address_ids: Annotated[List[str], PropertyInfo(alias="addressIds")]
    """All locations with selected address IDs will trigger."""

    address_types: Annotated[
        List[Literal["alertsOnly", "industrialSite", "riskZone", "shortHaul", "undefined", "workforceSite", "yard"]],
        PropertyInfo(alias="addressTypes"),
    ]
    """All locations with the selected address types will trigger."""

    circle: TriggerTriggerParamsOutsideGeofenceLocationCircle
    """Information about a circular geofence.

    This field is only needed if the geofence is a circle.
    """

    polygon: TriggerTriggerParamsOutsideGeofenceLocationPolygon
    """Information about a polygon geofence.

    This field is only needed if the geofence is a polygon.
    """

    tag_ids: Annotated[List[str], PropertyInfo(alias="tagIds")]
    """All locations with selected tag will trigger."""


class TriggerTriggerParamsOutsideGeofence(TypedDict, total=False):
    location: Required[TriggerTriggerParamsOutsideGeofenceLocation]
    """A location.

    Polygon and Circle is deprecated, but may be set for old Alerts. At least one
    location must be selected.
    """

    min_duration_milliseconds: Required[Annotated[int, PropertyInfo(alias="minDurationMilliseconds")]]
    """The number of milliseconds the trigger needs to stay active before alerting."""


class TriggerTriggerParamsPanicButton(TypedDict, total=False):
    is_filtering_out_power_loss: Required[Annotated[bool, PropertyInfo(alias="isFilteringOutPowerLoss")]]
    """
    If true, only receive alerts when the panic button is pressed, otherwise receive
    alerts when the panic button is pressed or looses connection.
    """


class TriggerTriggerParamsRouteStopEstimatedArrivalLocationCircle(TypedDict, total=False):
    name: Required[str]
    """The name of the cirlce."""

    radius_meters: Required[Annotated[int, PropertyInfo(alias="radiusMeters")]]
    """The radius of the circular geofence in meters."""

    latitude: float
    """Latitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """

    longitude: float
    """Longitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """


class TriggerTriggerParamsRouteStopEstimatedArrivalLocationPolygonVertex(TypedDict, total=False):
    latitude: Required[float]
    """The latitude of a geofence vertex in decimal degrees."""

    longitude: Required[float]
    """The longitude of a geofence vertex in decimal degrees."""


class TriggerTriggerParamsRouteStopEstimatedArrivalLocationPolygon(TypedDict, total=False):
    name: Required[str]
    """The name of the polygon."""

    vertices: Iterable[TriggerTriggerParamsRouteStopEstimatedArrivalLocationPolygonVertex]
    """The vertices of the polygon geofence.

    These geofence vertices describe the perimeter of the polygon, and must consist
    of at least 3 vertices and less than 40.
    """


class TriggerTriggerParamsRouteStopEstimatedArrivalLocation(TypedDict, total=False):
    address_ids: Annotated[List[str], PropertyInfo(alias="addressIds")]
    """All locations with selected address IDs will trigger."""

    address_types: Annotated[
        List[Literal["alertsOnly", "industrialSite", "riskZone", "shortHaul", "undefined", "workforceSite", "yard"]],
        PropertyInfo(alias="addressTypes"),
    ]
    """All locations with the selected address types will trigger."""

    circle: TriggerTriggerParamsRouteStopEstimatedArrivalLocationCircle
    """Information about a circular geofence.

    This field is only needed if the geofence is a circle.
    """

    polygon: TriggerTriggerParamsRouteStopEstimatedArrivalLocationPolygon
    """Information about a polygon geofence.

    This field is only needed if the geofence is a polygon.
    """

    tag_ids: Annotated[List[str], PropertyInfo(alias="tagIds")]
    """All locations with selected tag will trigger."""


class TriggerTriggerParamsRouteStopEstimatedArrival(TypedDict, total=False):
    alert_before_arrival_milliseconds: Required[Annotated[int, PropertyInfo(alias="alertBeforeArrivalMilliseconds")]]
    """Time threshold for when to send an alert.

    Sends an alert when the ETA is less than the threshold.
    """

    location: Required[TriggerTriggerParamsRouteStopEstimatedArrivalLocation]
    """A location.

    Polygon and Circle is deprecated, but may be set for old Alerts. At least one
    location must be selected.
    """

    has_live_share_link: Annotated[bool, PropertyInfo(alias="hasLiveShareLink")]
    """If true, will include a live sharing link in the alert. Defaults to false."""

    is_alert_on_route_stop_only: Annotated[bool, PropertyInfo(alias="isAlertOnRouteStopOnly")]
    """If true, will only alert if the vehicle is en-route to the stop.

    Defaults to false.
    """


class TriggerTriggerParamsScheduledMaintenance(TypedDict, total=False):
    due_in_days: Required[Annotated[int, PropertyInfo(alias="dueInDays")]]
    """Alert when maintenance is due in the specified number of days."""

    schedule_id: Required[Annotated[str, PropertyInfo(alias="scheduleId")]]
    """The id of the maintenance schedule."""


class TriggerTriggerParamsScheduledMaintenanceByEngineHours(TypedDict, total=False):
    due_in_hours: Required[Annotated[int, PropertyInfo(alias="dueInHours")]]
    """Alert when maintenance is due in the specified number of hours."""

    schedule_id: Required[Annotated[str, PropertyInfo(alias="scheduleId")]]
    """The id of the maintenance schedule."""


class TriggerTriggerParamsScheduledMaintenanceOdometer(TypedDict, total=False):
    due_in_meters: Required[Annotated[int, PropertyInfo(alias="dueInMeters")]]
    """Alert when vehicle odometer has this many meters left until maintenance is due."""

    schedule_id: Required[Annotated[str, PropertyInfo(alias="scheduleId")]]
    """The id of the maintenance schedule."""


class TriggerTriggerParamsSpeed(TypedDict, total=False):
    min_duration_milliseconds: Required[Annotated[int, PropertyInfo(alias="minDurationMilliseconds")]]
    """The number of milliseconds the trigger needs to stay active before alerting."""

    operation: Required[Literal["GREATER", "LESS"]]
    """How to evaluate the threshold. Valid values: `GREATER`, `LESS`"""

    speed_kilometers_per_hour: Required[Annotated[int, PropertyInfo(alias="speedKilometersPerHour")]]
    """The speed threshold value."""


class TriggerTriggerParamsTireFaultCode(TypedDict, total=False):
    manufacturer: Required[
        Literal[
            "MANUFACTURER_BENDIX",
            "MANUFACTURER_CONTINENTAL",
            "MANUFACTURER_DORAN",
            "MANUFACTURER_HENDRICKSON",
            "MANUFACTURER_INVALID",
            "MANUFACTURER_PRESSURE_PRO",
            "MANUFACTURER_UNIVERSAL_J1939",
            "MANUFACTURER_UNIVERSAL_R141",
        ]
    ]
    """The tire manufacturer.

    Valid values: `MANUFACTURER_BENDIX`, `MANUFACTURER_CONTINENTAL`,
    `MANUFACTURER_DORAN`, `MANUFACTURER_HENDRICKSON`, `MANUFACTURER_INVALID`,
    `MANUFACTURER_PRESSURE_PRO`, `MANUFACTURER_UNIVERSAL_J1939`,
    `MANUFACTURER_UNIVERSAL_R141`
    """

    has_cautionary_tire_fault_codes: Annotated[bool, PropertyInfo(alias="hasCautionaryTireFaultCodes")]
    """
    If true then alert over pressure, under pressure, across axle fault, or leak
    detected fault codes. Defaults to false.
    """

    has_critical_tire_fault_codes: Annotated[bool, PropertyInfo(alias="hasCriticalTireFaultCodes")]
    """
    If true then alert over temperature or extreme pressure over or under fault
    codes. Defaults to false.
    """

    specific_tire_fault_codes: Annotated[
        List[
            Literal[
                "TIRE_ALERT_ACROSS_AXLE_FAULT",
                "TIRE_ALERT_EXTREME_OVER_PRESSURE",
                "TIRE_ALERT_EXTREME_UNDER_PRESSURE",
                "TIRE_ALERT_INVALID",
                "TIRE_ALERT_LEAK_DETECTED",
                "TIRE_ALERT_OVER_PRESSURE",
                "TIRE_ALERT_OVER_TEMPERATURE",
                "TIRE_ALERT_UNDER_PRESSURE",
            ]
        ],
        PropertyInfo(alias="specificTireFaultCodes"),
    ]
    """The list of specific tire fault codes to be alerted on."""


class TriggerTriggerParamsUnassignedDriving(TypedDict, total=False):
    min_duration_milliseconds: Required[Annotated[int, PropertyInfo(alias="minDurationMilliseconds")]]
    """The number of milliseconds the trigger needs to stay active before alerting."""


class TriggerTriggerParamsVehicleBatteryVoltage(TypedDict, total=False):
    battery_volts: Required[Annotated[int, PropertyInfo(alias="batteryVolts")]]
    """The battery volt threshold value."""

    min_duration_milliseconds: Required[Annotated[int, PropertyInfo(alias="minDurationMilliseconds")]]
    """The number of milliseconds the trigger needs to stay active before alerting."""

    operation: Required[Literal["GREATER", "LESS"]]
    """How to evaluate the threshold. Valid values: `GREATER`, `LESS`"""


class TriggerTriggerParamsVehicleFaultCodeSpecificFaultCode(TypedDict, total=False):
    fault_code: Required[Annotated[str, PropertyInfo(alias="faultCode")]]
    """The specific fault code name."""

    type: Required[Literal["INVALID_FAULT_CODE_TYPE", "J1939_DTC", "J1939_SPN", "PASSENGER_DTC"]]
    """The specific fault code type.

    Valid values: `INVALID_FAULT_CODE_TYPE`, `J1939_DTC`, `J1939_SPN`,
    `PASSENGER_DTC`
    """


class TriggerTriggerParamsVehicleFaultCode(TypedDict, total=False):
    has_any_amber_warning_lamp_codes: Annotated[bool, PropertyInfo(alias="hasAnyAmberWarningLampCodes")]
    """If true then alert on codes for less serious errors that do not warrant
    stopping.

    Defaults to false.
    """

    has_any_fault_codes: Annotated[bool, PropertyInfo(alias="hasAnyFaultCodes")]
    """If true this means that any code is alertable. Defaults to false."""

    has_any_malfunction_indicator_lamp_codes: Annotated[bool, PropertyInfo(alias="hasAnyMalfunctionIndicatorLampCodes")]
    """If true then alert on emission-related codes. Defaults to false."""

    has_any_protection_lamp_codes: Annotated[bool, PropertyInfo(alias="hasAnyProtectionLampCodes")]
    """If true then alert on codes for non-electric vehicle parts. Defaults to false."""

    has_any_red_stop_lamp_codes: Annotated[bool, PropertyInfo(alias="hasAnyRedStopLampCodes")]
    """If true then alert when the vehicle warrants stopping. Defaults to false."""

    has_any_trailer_abs_lamp_codes: Annotated[bool, PropertyInfo(alias="hasAnyTrailerAbsLampCodes")]
    """If true then alert when the ABS light is on. Defaults to false."""

    specific_fault_codes: Annotated[
        Iterable[TriggerTriggerParamsVehicleFaultCodeSpecificFaultCode], PropertyInfo(alias="specificFaultCodes")
    ]
    """The list of specific fault codes to be alerted on."""


class TriggerTriggerParams(TypedDict, total=False):
    ambient_temperature: Annotated[TriggerTriggerParamsAmbientTemperature, PropertyInfo(alias="ambientTemperature")]
    """Details specific to Ambient Temperature."""

    cell_signal_loss: Annotated[TriggerTriggerParamsCellSignalLoss, PropertyInfo(alias="cellSignalLoss")]
    """Details specific to Cell Signal Loss"""

    def_level: Annotated[TriggerTriggerParamsDefLevel, PropertyInfo(alias="defLevel")]
    """Details specific to DEF Level"""

    device_movement: Annotated[TriggerTriggerParamsDeviceMovement, PropertyInfo(alias="deviceMovement")]
    """Details specific to Device Movement"""

    document_submitted: Annotated[TriggerTriggerParamsDocumentSubmitted, PropertyInfo(alias="documentSubmitted")]
    """Details specific to Driver Document Submitted"""

    dvir_submitted_device: Annotated[TriggerTriggerParamsDvirSubmittedDevice, PropertyInfo(alias="dvirSubmittedDevice")]
    """Details specific to DVIR Submitted by Device"""

    engine_idle: Annotated[TriggerTriggerParamsEngineIdle, PropertyInfo(alias="engineIdle")]
    """Details specific to Engine Idle"""

    engine_off: Annotated[TriggerTriggerParamsEngineOff, PropertyInfo(alias="engineOff")]
    """Details specific to Engine Off"""

    engine_on: Annotated[TriggerTriggerParamsEngineOn, PropertyInfo(alias="engineOn")]
    """Details specific to Engine On"""

    fuel_level: Annotated[TriggerTriggerParamsFuelLevel, PropertyInfo(alias="fuelLevel")]
    """Details specific to Fuel Level Percentage"""

    gateway_disconnected: Annotated[TriggerTriggerParamsGatewayDisconnected, PropertyInfo(alias="gatewayDisconnected")]
    """Details specific to Gateway Disconnected"""

    gateway_unplugged: Annotated[TriggerTriggerParamsGatewayUnplugged, PropertyInfo(alias="gatewayUnplugged")]
    """Details specific to Gateway Unplugged"""

    geofence_entry: Annotated[TriggerTriggerParamsGeofenceEntry, PropertyInfo(alias="geofenceEntry")]
    """Details specific to Geofence Entry"""

    geofence_exit: Annotated[TriggerTriggerParamsGeofenceExit, PropertyInfo(alias="geofenceExit")]
    """Details specific to Geofence Exit"""

    gps_signal_loss: Annotated[TriggerTriggerParamsGpsSignalLoss, PropertyInfo(alias="gpsSignalLoss")]
    """Details specific to GPS Signal Loss"""

    harsh_event: Annotated[TriggerTriggerParamsHarshEvent, PropertyInfo(alias="harshEvent")]
    """Details specific to Harsh Events"""

    hos_violation: Annotated[TriggerTriggerParamsHosViolation, PropertyInfo(alias="hosViolation")]
    """Details specific to HOS Violation"""

    inside_geofence: Annotated[TriggerTriggerParamsInsideGeofence, PropertyInfo(alias="insideGeofence")]
    """Details specific to Inside Geofence"""

    out_of_route: Annotated[TriggerTriggerParamsOutOfRoute, PropertyInfo(alias="outOfRoute")]
    """Details specific to Out Of Route"""

    outside_geofence: Annotated[TriggerTriggerParamsOutsideGeofence, PropertyInfo(alias="outsideGeofence")]
    """Details specific to Outside Geofence"""

    panic_button: Annotated[TriggerTriggerParamsPanicButton, PropertyInfo(alias="panicButton")]
    """Details specific to Panic Button"""

    route_stop_estimated_arrival: Annotated[
        TriggerTriggerParamsRouteStopEstimatedArrival, PropertyInfo(alias="routeStopEstimatedArrival")
    ]
    """Details specific to Route Stop Estimated Arrival"""

    scheduled_maintenance: Annotated[
        TriggerTriggerParamsScheduledMaintenance, PropertyInfo(alias="scheduledMaintenance")
    ]
    """Details specific to Scheduled Maintenance by Date"""

    scheduled_maintenance_by_engine_hours: Annotated[
        TriggerTriggerParamsScheduledMaintenanceByEngineHours, PropertyInfo(alias="scheduledMaintenanceByEngineHours")
    ]
    """Details specific to Scheduled Maintenance By Engine Hours"""

    scheduled_maintenance_odometer: Annotated[
        TriggerTriggerParamsScheduledMaintenanceOdometer, PropertyInfo(alias="scheduledMaintenanceOdometer")
    ]
    """Details specific to Scheduled Maintenance by Odometer"""

    speed: TriggerTriggerParamsSpeed
    """Details specific to Speed"""

    tire_fault_code: Annotated[TriggerTriggerParamsTireFaultCode, PropertyInfo(alias="tireFaultCode")]
    """Details specific to Tire Fault Code.

    At least one fault code or fault code group must be selected.
    """

    unassigned_driving: Annotated[TriggerTriggerParamsUnassignedDriving, PropertyInfo(alias="unassignedDriving")]
    """Details specific to Unassigned Driving"""

    vehicle_battery_voltage: Annotated[
        TriggerTriggerParamsVehicleBatteryVoltage, PropertyInfo(alias="vehicleBatteryVoltage")
    ]
    """Details specific to Vehicle Battery Voltage"""

    vehicle_fault_code: Annotated[TriggerTriggerParamsVehicleFaultCode, PropertyInfo(alias="vehicleFaultCode")]
    """Details specific to Vehicle Fault Code.

    At least one fault code or fault code group must be selected.
    """


class Trigger(TypedDict, total=False):
    trigger_type_id: Required[Annotated[int, PropertyInfo(alias="triggerTypeId")]]
    """The id of the trigger type. Reference the following list for the ids:

    Ambient Temperature = 1003 DVIR Submitted for Asset = 5005 Driver Recorded =
    5027 Vehicle Speed = 1000 Fuel Level (Percentage) = 1005 Vehicle DEF Level
    (Percentage) = 1006 Vehicle Battery = 1007 Gateway Unplugged = 1009 Dashcam
    Disconnected = 1012 Camera Connector Disconnected = 1046 Asset starts moving =
    1013 Inside Geofence = 1014 Outside Geofence = 1020 Unassigned Driving = 1016
    Driver HOS Violation = 1018 Vehicle Engine Idle = 1019 Asset Engine On = 1021
    Asset Engine Off = 1022 Harsh Event = 1023 Scheduled Maintenance = 1024
    Scheduled Maintenance by Odometer = 1025 Scheduled Maintenance by Engine Hours =
    1026 Out of Route = 1027 GPS Signal Loss = 1032 Cell Signal Loss = 1033 Fault
    Code = 1029 Tire Faults = 1043 Gateway Disconnected = 1030 Panic Button = 1034
    Tampering Detected = 1045 If vehicle is severely speeding (as defined by your
    organization) = 5022 Driver Document Submitted = 5009 Driver App Sign In = 5012
    Driver App Sign Out = 5013 Geofence Entry = 5016 Geofence Exit = 5017 Route Stop
    ETA Alert = 5018 Scheduled Date And Time = 8001
    """

    trigger_params: Annotated[TriggerTriggerParams, PropertyInfo(alias="triggerParams")]
    """The trigger type specific details.

    Only the field that corresponds to the trigger type is filled in.
    """
