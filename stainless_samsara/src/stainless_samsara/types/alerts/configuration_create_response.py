# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ConfigurationCreateResponse",
    "Data",
    "DataAction",
    "DataActionActionParams",
    "DataActionActionParamsDriverAppNotification",
    "DataActionActionParamsDriverAppNotificationInAppNotificationOptions",
    "DataActionActionParamsDriverAppNotificationPushNotificationOptions",
    "DataActionActionParamsRecipient",
    "DataActionActionParamsWebhooks",
    "DataScope",
    "DataScopeAsset",
    "DataScopeDriver",
    "DataScopeTag",
    "DataScopeWidget",
    "DataTrigger",
    "DataTriggerTriggerParams",
    "DataTriggerTriggerParamsAmbientTemperature",
    "DataTriggerTriggerParamsCellSignalLoss",
    "DataTriggerTriggerParamsDefLevel",
    "DataTriggerTriggerParamsDeviceMovement",
    "DataTriggerTriggerParamsDocumentSubmitted",
    "DataTriggerTriggerParamsDvirSubmittedDevice",
    "DataTriggerTriggerParamsEngineIdle",
    "DataTriggerTriggerParamsEngineOff",
    "DataTriggerTriggerParamsEngineOn",
    "DataTriggerTriggerParamsFuelLevel",
    "DataTriggerTriggerParamsGatewayDisconnected",
    "DataTriggerTriggerParamsGatewayUnplugged",
    "DataTriggerTriggerParamsGeofenceEntry",
    "DataTriggerTriggerParamsGeofenceEntryLocation",
    "DataTriggerTriggerParamsGeofenceEntryLocationCircle",
    "DataTriggerTriggerParamsGeofenceEntryLocationPolygon",
    "DataTriggerTriggerParamsGeofenceEntryLocationPolygonVertex",
    "DataTriggerTriggerParamsGeofenceExit",
    "DataTriggerTriggerParamsGeofenceExitLocation",
    "DataTriggerTriggerParamsGeofenceExitLocationCircle",
    "DataTriggerTriggerParamsGeofenceExitLocationPolygon",
    "DataTriggerTriggerParamsGeofenceExitLocationPolygonVertex",
    "DataTriggerTriggerParamsGpsSignalLoss",
    "DataTriggerTriggerParamsHarshEvent",
    "DataTriggerTriggerParamsHosViolation",
    "DataTriggerTriggerParamsInsideGeofence",
    "DataTriggerTriggerParamsInsideGeofenceLocation",
    "DataTriggerTriggerParamsInsideGeofenceLocationCircle",
    "DataTriggerTriggerParamsInsideGeofenceLocationPolygon",
    "DataTriggerTriggerParamsInsideGeofenceLocationPolygonVertex",
    "DataTriggerTriggerParamsOutOfRoute",
    "DataTriggerTriggerParamsOutsideGeofence",
    "DataTriggerTriggerParamsOutsideGeofenceLocation",
    "DataTriggerTriggerParamsOutsideGeofenceLocationCircle",
    "DataTriggerTriggerParamsOutsideGeofenceLocationPolygon",
    "DataTriggerTriggerParamsOutsideGeofenceLocationPolygonVertex",
    "DataTriggerTriggerParamsPanicButton",
    "DataTriggerTriggerParamsRouteStopEstimatedArrival",
    "DataTriggerTriggerParamsRouteStopEstimatedArrivalLocation",
    "DataTriggerTriggerParamsRouteStopEstimatedArrivalLocationCircle",
    "DataTriggerTriggerParamsRouteStopEstimatedArrivalLocationPolygon",
    "DataTriggerTriggerParamsRouteStopEstimatedArrivalLocationPolygonVertex",
    "DataTriggerTriggerParamsScheduledMaintenance",
    "DataTriggerTriggerParamsScheduledMaintenanceByEngineHours",
    "DataTriggerTriggerParamsScheduledMaintenanceOdometer",
    "DataTriggerTriggerParamsSpeed",
    "DataTriggerTriggerParamsTireFaultCode",
    "DataTriggerTriggerParamsUnassignedDriving",
    "DataTriggerTriggerParamsVehicleBatteryVoltage",
    "DataTriggerTriggerParamsVehicleFaultCode",
    "DataTriggerTriggerParamsVehicleFaultCodeSpecificFaultCode",
    "DataOperationalSettings",
    "DataOperationalSettingsTimeRange",
]


class DataActionActionParamsDriverAppNotificationInAppNotificationOptions(BaseModel):
    is_enabled: bool = FieldInfo(alias="isEnabled")
    """Whether in-app notifications are enabled."""

    can_dictate_alert_title: Optional[bool] = FieldInfo(alias="canDictateAlertTitle", default=None)
    """Whether the alert will dictate the title of the alert.

    Both canDictateAlertTitle and canPlayAlertSound should be enabled or disabled
    together.
    """

    can_play_alert_sound: Optional[bool] = FieldInfo(alias="canPlayAlertSound", default=None)
    """Whether the alert will play a sound.

    Both canDictateAlertTitle and canPlayAlertSound should be enabled or disabled
    together.
    """

    custom_text: Optional[str] = FieldInfo(alias="customText", default=None)
    """Custom text to display in the notification (320 character max)."""


class DataActionActionParamsDriverAppNotificationPushNotificationOptions(BaseModel):
    is_enabled: bool = FieldInfo(alias="isEnabled")
    """Whether push notifications are enabled."""


class DataActionActionParamsDriverAppNotification(BaseModel):
    in_app_notification_options: Optional[DataActionActionParamsDriverAppNotificationInAppNotificationOptions] = (
        FieldInfo(alias="inAppNotificationOptions", default=None)
    )
    """Options for in-app notifications"""

    push_notification_options: Optional[DataActionActionParamsDriverAppNotificationPushNotificationOptions] = FieldInfo(
        alias="pushNotificationOptions", default=None
    )
    """Options for push notifications"""


class DataActionActionParamsRecipient(BaseModel):
    type: Literal["user", "contact", "role"]
    """The type of recipients Valid values: `user`, `contact`, `role`"""

    contact_id: Optional[str] = FieldInfo(alias="contactId", default=None)
    """The ID of the contact."""

    notification_types: Optional[List[Literal["push", "sms", "email"]]] = FieldInfo(
        alias="notificationTypes", default=None
    )
    """How the user/contact/role should be notified."""

    role_id: Optional[str] = FieldInfo(alias="roleId", default=None)
    """The ID of the role."""

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """The ID of the user."""


class DataActionActionParamsWebhooks(BaseModel):
    webhook_ids: List[str] = FieldInfo(alias="webhookIds")
    """The webhook IDs."""

    payload_type: Optional[Literal["legacy", "enriched"]] = FieldInfo(alias="payloadType", default=None)
    """This determines the alert webhook payload type to use.

    Learn more: https://developers.samsara.com/docs/webhook-reference. Valid values:
    `legacy`, `enriched`
    """


class DataActionActionParams(BaseModel):
    driver_app_notification: Optional[DataActionActionParamsDriverAppNotification] = FieldInfo(
        alias="driverAppNotification", default=None
    )
    """Driver app notification settings"""

    recipients: Optional[List[DataActionActionParamsRecipient]] = None
    """Recipient of the action."""

    webhooks: Optional[DataActionActionParamsWebhooks] = None
    """The webhook configuration for an Action."""


class DataAction(BaseModel):
    action_type_id: int = FieldInfo(alias="actionTypeId")
    """The id of the of the action type.

    Reference the following list for the ids: The following action types are in
    Beta: Driver App Push = 5 The following action types are Stable: Notification
    (Email, Text, Samsara Fleet Push) = 1 Dashboard Notification = 3 Webhook = 4
    Slack = 6
    """

    action_params: Optional[DataActionActionParams] = FieldInfo(alias="actionParams", default=None)
    """The action type specific details.

    Set webhookIds for Slack or Webhook actions. Set recipients for Notifications.
    Set driverAppNotification for Driver App Push. Other action types don't need to
    set a param.
    """


class DataScopeAsset(BaseModel):
    asset_id: str = FieldInfo(alias="assetId")
    """ID of the asset."""

    asset_type: Literal["uncategorized", "trailer", "equipment", "unpowered", "vehicle"] = FieldInfo(alias="assetType")
    """The operational context in which the asset interacts with the Samsara system.

    Examples: Vehicle (eg: truck, bus...), Trailer (eg: dry van, reefer,
    flatbed...), Powered Equipment (eg: dozer, crane...), Unpowered Equipment (eg:
    container, dumpster...), or Uncategorized. Valid values: `uncategorized`,
    `trailer`, `equipment`, `unpowered`, `vehicle`
    """


class DataScopeDriver(BaseModel):
    driver_id: str = FieldInfo(alias="driverId")
    """ID of the driver."""


class DataScopeTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataScopeWidget(BaseModel):
    widget_id: str = FieldInfo(alias="widgetId")
    """ID of the widget."""


class DataScope(BaseModel):
    all: bool
    """Whether it applies to all applicable objects."""

    assets: Optional[List[DataScopeAsset]] = None
    """The assets these triggers are scoped to."""

    drivers: Optional[List[DataScopeDriver]] = None
    """The drivers these triggers are scoped to."""

    tags: Optional[List[DataScopeTag]] = None
    """The tags these triggers are scoped to."""

    widgets: Optional[List[DataScopeWidget]] = None
    """The widgets these triggers are scoped to."""


class DataTriggerTriggerParamsAmbientTemperature(BaseModel):
    min_duration_milliseconds: int = FieldInfo(alias="minDurationMilliseconds")
    """The number of milliseconds the trigger needs to stay active before alerting."""

    operation: Literal["GREATER", "INSIDE_RANGE", "LESS", "OUTSIDE_RANGE"]
    """How to evaluate the threshold.

    Valid values: `GREATER`, `INSIDE_RANGE`, `LESS`, `OUTSIDE_RANGE`
    """

    temperature_celcius: int = FieldInfo(alias="temperatureCelcius")
    """The temperature in Celcius threshold value."""

    cargo_is_full: Optional[bool] = FieldInfo(alias="cargoIsFull", default=None)
    """Whether the cargo is full."""

    doors_are_closed: Optional[bool] = FieldInfo(alias="doorsAreClosed", default=None)
    """Whether the doors are closed."""


class DataTriggerTriggerParamsCellSignalLoss(BaseModel):
    min_duration_milliseconds: int = FieldInfo(alias="minDurationMilliseconds")
    """The number of milliseconds the trigger needs to stay active before alerting."""


class DataTriggerTriggerParamsDefLevel(BaseModel):
    def_level_percent: int = FieldInfo(alias="defLevelPercent")
    """The DEF percentage threshold value."""

    min_duration_milliseconds: int = FieldInfo(alias="minDurationMilliseconds")
    """The number of milliseconds the trigger needs to stay active before alerting."""

    operation: Literal["GREATER", "LESS"]
    """How to evaluate the threshold. Valid values: `GREATER`, `LESS`"""


class DataTriggerTriggerParamsDeviceMovement(BaseModel):
    min_duration_milliseconds: int = FieldInfo(alias="minDurationMilliseconds")
    """The number of milliseconds the trigger needs to stay active before alerting."""


class DataTriggerTriggerParamsDocumentSubmitted(BaseModel):
    template_ids: List[str] = FieldInfo(alias="templateIds")
    """Specific template IDs to be alerted on."""


class DataTriggerTriggerParamsDvirSubmittedDevice(BaseModel):
    dvir_min_duration_milliseconds: Optional[int] = FieldInfo(alias="dvirMinDurationMilliseconds", default=None)
    """
    The trigger will only fire if the selected DVIR types are submitted within the
    duration.
    """

    dvir_submission_types: Optional[List[Literal["SAFE_NO_DEFECTS", "SAFE_WITH_DEFECTS", "UNSAFE"]]] = FieldInfo(
        alias="dvirSubmissionTypes", default=None
    )
    """Filter to these types of DVIR submissions."""


class DataTriggerTriggerParamsEngineIdle(BaseModel):
    min_duration_milliseconds: int = FieldInfo(alias="minDurationMilliseconds")
    """The number of milliseconds the trigger needs to stay active before alerting."""


class DataTriggerTriggerParamsEngineOff(BaseModel):
    min_duration_milliseconds: int = FieldInfo(alias="minDurationMilliseconds")
    """The number of milliseconds the trigger needs to stay active before alerting."""


class DataTriggerTriggerParamsEngineOn(BaseModel):
    min_duration_milliseconds: int = FieldInfo(alias="minDurationMilliseconds")
    """The number of milliseconds the trigger needs to stay active before alerting."""


class DataTriggerTriggerParamsFuelLevel(BaseModel):
    fuel_level_percent: int = FieldInfo(alias="fuelLevelPercent")
    """The fuel level percentage threshold value."""

    min_duration_milliseconds: int = FieldInfo(alias="minDurationMilliseconds")
    """The number of milliseconds the trigger needs to stay active before alerting."""

    operation: Literal["LESS"]
    """How to evaluate the threshold. Valid values: `LESS`"""


class DataTriggerTriggerParamsGatewayDisconnected(BaseModel):
    min_duration_milliseconds: int = FieldInfo(alias="minDurationMilliseconds")
    """The number of milliseconds the trigger needs to stay active before alerting.

    Can only be either 900000 (15 minutes) or 3600000 (60 min).
    """


class DataTriggerTriggerParamsGatewayUnplugged(BaseModel):
    min_duration_milliseconds: int = FieldInfo(alias="minDurationMilliseconds")
    """The number of milliseconds the trigger needs to stay active before alerting."""


class DataTriggerTriggerParamsGeofenceEntryLocationCircle(BaseModel):
    name: str
    """The name of the cirlce."""

    radius_meters: int = FieldInfo(alias="radiusMeters")
    """The radius of the circular geofence in meters."""

    latitude: Optional[float] = None
    """Latitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """

    longitude: Optional[float] = None
    """Longitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """


class DataTriggerTriggerParamsGeofenceEntryLocationPolygonVertex(BaseModel):
    latitude: float
    """The latitude of a geofence vertex in decimal degrees."""

    longitude: float
    """The longitude of a geofence vertex in decimal degrees."""


class DataTriggerTriggerParamsGeofenceEntryLocationPolygon(BaseModel):
    name: str
    """The name of the polygon."""

    vertices: Optional[List[DataTriggerTriggerParamsGeofenceEntryLocationPolygonVertex]] = None
    """The vertices of the polygon geofence.

    These geofence vertices describe the perimeter of the polygon, and must consist
    of at least 3 vertices and less than 40.
    """


class DataTriggerTriggerParamsGeofenceEntryLocation(BaseModel):
    address_ids: Optional[List[str]] = FieldInfo(alias="addressIds", default=None)
    """All locations with selected address IDs will trigger."""

    address_types: Optional[
        List[Literal["alertsOnly", "industrialSite", "riskZone", "shortHaul", "undefined", "workforceSite", "yard"]]
    ] = FieldInfo(alias="addressTypes", default=None)
    """All locations with the selected address types will trigger."""

    circle: Optional[DataTriggerTriggerParamsGeofenceEntryLocationCircle] = None
    """Information about a circular geofence.

    This field is only needed if the geofence is a circle.
    """

    polygon: Optional[DataTriggerTriggerParamsGeofenceEntryLocationPolygon] = None
    """Information about a polygon geofence.

    This field is only needed if the geofence is a polygon.
    """

    tag_ids: Optional[List[str]] = FieldInfo(alias="tagIds", default=None)
    """All locations with selected tag will trigger."""


class DataTriggerTriggerParamsGeofenceEntry(BaseModel):
    location: DataTriggerTriggerParamsGeofenceEntryLocation
    """A location.

    Polygon and Circle is deprecated, but may be set for old Alerts. At least one
    location must be selected.
    """


class DataTriggerTriggerParamsGeofenceExitLocationCircle(BaseModel):
    name: str
    """The name of the cirlce."""

    radius_meters: int = FieldInfo(alias="radiusMeters")
    """The radius of the circular geofence in meters."""

    latitude: Optional[float] = None
    """Latitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """

    longitude: Optional[float] = None
    """Longitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """


class DataTriggerTriggerParamsGeofenceExitLocationPolygonVertex(BaseModel):
    latitude: float
    """The latitude of a geofence vertex in decimal degrees."""

    longitude: float
    """The longitude of a geofence vertex in decimal degrees."""


class DataTriggerTriggerParamsGeofenceExitLocationPolygon(BaseModel):
    name: str
    """The name of the polygon."""

    vertices: Optional[List[DataTriggerTriggerParamsGeofenceExitLocationPolygonVertex]] = None
    """The vertices of the polygon geofence.

    These geofence vertices describe the perimeter of the polygon, and must consist
    of at least 3 vertices and less than 40.
    """


class DataTriggerTriggerParamsGeofenceExitLocation(BaseModel):
    address_ids: Optional[List[str]] = FieldInfo(alias="addressIds", default=None)
    """All locations with selected address IDs will trigger."""

    address_types: Optional[
        List[Literal["alertsOnly", "industrialSite", "riskZone", "shortHaul", "undefined", "workforceSite", "yard"]]
    ] = FieldInfo(alias="addressTypes", default=None)
    """All locations with the selected address types will trigger."""

    circle: Optional[DataTriggerTriggerParamsGeofenceExitLocationCircle] = None
    """Information about a circular geofence.

    This field is only needed if the geofence is a circle.
    """

    polygon: Optional[DataTriggerTriggerParamsGeofenceExitLocationPolygon] = None
    """Information about a polygon geofence.

    This field is only needed if the geofence is a polygon.
    """

    tag_ids: Optional[List[str]] = FieldInfo(alias="tagIds", default=None)
    """All locations with selected tag will trigger."""


class DataTriggerTriggerParamsGeofenceExit(BaseModel):
    location: DataTriggerTriggerParamsGeofenceExitLocation
    """A location.

    Polygon and Circle is deprecated, but may be set for old Alerts. At least one
    location must be selected.
    """


class DataTriggerTriggerParamsGpsSignalLoss(BaseModel):
    min_duration_milliseconds: int = FieldInfo(alias="minDurationMilliseconds")
    """The number of milliseconds the trigger needs to stay active before alerting."""


class DataTriggerTriggerParamsHarshEvent(BaseModel):
    types: List[
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
    """On which harsh events to trigger on."""


class DataTriggerTriggerParamsHosViolation(BaseModel):
    max_until_violation_milliseconds: int = FieldInfo(alias="maxUntilViolationMilliseconds")
    """Alert if driver has this specified time until driving causes an HOS violation."""

    violation: Literal[
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
    """The type of HOS violation.

    Valid values: `CaliforniaMealbreakMissed`, `CycleHoursOn`, `DailyDrivingHours`,
    `DailyOnDutyHours`, `Invalid`, `RestbreakMissed`, `ShiftDrivingHours`,
    `ShiftHours`, `ShiftOnDutyHours`, `UnsubmittedLogs`
    """


class DataTriggerTriggerParamsInsideGeofenceLocationCircle(BaseModel):
    name: str
    """The name of the cirlce."""

    radius_meters: int = FieldInfo(alias="radiusMeters")
    """The radius of the circular geofence in meters."""

    latitude: Optional[float] = None
    """Latitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """

    longitude: Optional[float] = None
    """Longitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """


class DataTriggerTriggerParamsInsideGeofenceLocationPolygonVertex(BaseModel):
    latitude: float
    """The latitude of a geofence vertex in decimal degrees."""

    longitude: float
    """The longitude of a geofence vertex in decimal degrees."""


class DataTriggerTriggerParamsInsideGeofenceLocationPolygon(BaseModel):
    name: str
    """The name of the polygon."""

    vertices: Optional[List[DataTriggerTriggerParamsInsideGeofenceLocationPolygonVertex]] = None
    """The vertices of the polygon geofence.

    These geofence vertices describe the perimeter of the polygon, and must consist
    of at least 3 vertices and less than 40.
    """


class DataTriggerTriggerParamsInsideGeofenceLocation(BaseModel):
    address_ids: Optional[List[str]] = FieldInfo(alias="addressIds", default=None)
    """All locations with selected address IDs will trigger."""

    address_types: Optional[
        List[Literal["alertsOnly", "industrialSite", "riskZone", "shortHaul", "undefined", "workforceSite", "yard"]]
    ] = FieldInfo(alias="addressTypes", default=None)
    """All locations with the selected address types will trigger."""

    circle: Optional[DataTriggerTriggerParamsInsideGeofenceLocationCircle] = None
    """Information about a circular geofence.

    This field is only needed if the geofence is a circle.
    """

    polygon: Optional[DataTriggerTriggerParamsInsideGeofenceLocationPolygon] = None
    """Information about a polygon geofence.

    This field is only needed if the geofence is a polygon.
    """

    tag_ids: Optional[List[str]] = FieldInfo(alias="tagIds", default=None)
    """All locations with selected tag will trigger."""


class DataTriggerTriggerParamsInsideGeofence(BaseModel):
    location: DataTriggerTriggerParamsInsideGeofenceLocation
    """A location.

    Polygon and Circle is deprecated, but may be set for old Alerts. At least one
    location must be selected.
    """

    min_duration_milliseconds: int = FieldInfo(alias="minDurationMilliseconds")
    """The number of milliseconds the trigger needs to stay active before alerting."""


class DataTriggerTriggerParamsOutOfRoute(BaseModel):
    max_off_route_meters: int = FieldInfo(alias="maxOffRouteMeters")
    """
    The minimum distance in meters a vehicle has to be from its active route path to
    be considered out of its route.
    """

    min_duration_milliseconds: int = FieldInfo(alias="minDurationMilliseconds")
    """The number of milliseconds the trigger needs to stay active before alerting."""


class DataTriggerTriggerParamsOutsideGeofenceLocationCircle(BaseModel):
    name: str
    """The name of the cirlce."""

    radius_meters: int = FieldInfo(alias="radiusMeters")
    """The radius of the circular geofence in meters."""

    latitude: Optional[float] = None
    """Latitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """

    longitude: Optional[float] = None
    """Longitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """


class DataTriggerTriggerParamsOutsideGeofenceLocationPolygonVertex(BaseModel):
    latitude: float
    """The latitude of a geofence vertex in decimal degrees."""

    longitude: float
    """The longitude of a geofence vertex in decimal degrees."""


class DataTriggerTriggerParamsOutsideGeofenceLocationPolygon(BaseModel):
    name: str
    """The name of the polygon."""

    vertices: Optional[List[DataTriggerTriggerParamsOutsideGeofenceLocationPolygonVertex]] = None
    """The vertices of the polygon geofence.

    These geofence vertices describe the perimeter of the polygon, and must consist
    of at least 3 vertices and less than 40.
    """


class DataTriggerTriggerParamsOutsideGeofenceLocation(BaseModel):
    address_ids: Optional[List[str]] = FieldInfo(alias="addressIds", default=None)
    """All locations with selected address IDs will trigger."""

    address_types: Optional[
        List[Literal["alertsOnly", "industrialSite", "riskZone", "shortHaul", "undefined", "workforceSite", "yard"]]
    ] = FieldInfo(alias="addressTypes", default=None)
    """All locations with the selected address types will trigger."""

    circle: Optional[DataTriggerTriggerParamsOutsideGeofenceLocationCircle] = None
    """Information about a circular geofence.

    This field is only needed if the geofence is a circle.
    """

    polygon: Optional[DataTriggerTriggerParamsOutsideGeofenceLocationPolygon] = None
    """Information about a polygon geofence.

    This field is only needed if the geofence is a polygon.
    """

    tag_ids: Optional[List[str]] = FieldInfo(alias="tagIds", default=None)
    """All locations with selected tag will trigger."""


class DataTriggerTriggerParamsOutsideGeofence(BaseModel):
    location: DataTriggerTriggerParamsOutsideGeofenceLocation
    """A location.

    Polygon and Circle is deprecated, but may be set for old Alerts. At least one
    location must be selected.
    """

    min_duration_milliseconds: int = FieldInfo(alias="minDurationMilliseconds")
    """The number of milliseconds the trigger needs to stay active before alerting."""


class DataTriggerTriggerParamsPanicButton(BaseModel):
    is_filtering_out_power_loss: bool = FieldInfo(alias="isFilteringOutPowerLoss")
    """
    If true, only receive alerts when the panic button is pressed, otherwise receive
    alerts when the panic button is pressed or looses connection.
    """


class DataTriggerTriggerParamsRouteStopEstimatedArrivalLocationCircle(BaseModel):
    name: str
    """The name of the cirlce."""

    radius_meters: int = FieldInfo(alias="radiusMeters")
    """The radius of the circular geofence in meters."""

    latitude: Optional[float] = None
    """Latitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """

    longitude: Optional[float] = None
    """Longitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """


class DataTriggerTriggerParamsRouteStopEstimatedArrivalLocationPolygonVertex(BaseModel):
    latitude: float
    """The latitude of a geofence vertex in decimal degrees."""

    longitude: float
    """The longitude of a geofence vertex in decimal degrees."""


class DataTriggerTriggerParamsRouteStopEstimatedArrivalLocationPolygon(BaseModel):
    name: str
    """The name of the polygon."""

    vertices: Optional[List[DataTriggerTriggerParamsRouteStopEstimatedArrivalLocationPolygonVertex]] = None
    """The vertices of the polygon geofence.

    These geofence vertices describe the perimeter of the polygon, and must consist
    of at least 3 vertices and less than 40.
    """


class DataTriggerTriggerParamsRouteStopEstimatedArrivalLocation(BaseModel):
    address_ids: Optional[List[str]] = FieldInfo(alias="addressIds", default=None)
    """All locations with selected address IDs will trigger."""

    address_types: Optional[
        List[Literal["alertsOnly", "industrialSite", "riskZone", "shortHaul", "undefined", "workforceSite", "yard"]]
    ] = FieldInfo(alias="addressTypes", default=None)
    """All locations with the selected address types will trigger."""

    circle: Optional[DataTriggerTriggerParamsRouteStopEstimatedArrivalLocationCircle] = None
    """Information about a circular geofence.

    This field is only needed if the geofence is a circle.
    """

    polygon: Optional[DataTriggerTriggerParamsRouteStopEstimatedArrivalLocationPolygon] = None
    """Information about a polygon geofence.

    This field is only needed if the geofence is a polygon.
    """

    tag_ids: Optional[List[str]] = FieldInfo(alias="tagIds", default=None)
    """All locations with selected tag will trigger."""


class DataTriggerTriggerParamsRouteStopEstimatedArrival(BaseModel):
    alert_before_arrival_milliseconds: int = FieldInfo(alias="alertBeforeArrivalMilliseconds")
    """Time threshold for when to send an alert.

    Sends an alert when the ETA is less than the threshold.
    """

    location: DataTriggerTriggerParamsRouteStopEstimatedArrivalLocation
    """A location.

    Polygon and Circle is deprecated, but may be set for old Alerts. At least one
    location must be selected.
    """

    has_live_share_link: Optional[bool] = FieldInfo(alias="hasLiveShareLink", default=None)
    """If true, will include a live sharing link in the alert. Defaults to false."""

    is_alert_on_route_stop_only: Optional[bool] = FieldInfo(alias="isAlertOnRouteStopOnly", default=None)
    """If true, will only alert if the vehicle is en-route to the stop.

    Defaults to false.
    """


class DataTriggerTriggerParamsScheduledMaintenance(BaseModel):
    due_in_days: int = FieldInfo(alias="dueInDays")
    """Alert when maintenance is due in the specified number of days."""

    schedule_id: str = FieldInfo(alias="scheduleId")
    """The id of the maintenance schedule."""


class DataTriggerTriggerParamsScheduledMaintenanceByEngineHours(BaseModel):
    due_in_hours: int = FieldInfo(alias="dueInHours")
    """Alert when maintenance is due in the specified number of hours."""

    schedule_id: str = FieldInfo(alias="scheduleId")
    """The id of the maintenance schedule."""


class DataTriggerTriggerParamsScheduledMaintenanceOdometer(BaseModel):
    due_in_meters: int = FieldInfo(alias="dueInMeters")
    """Alert when vehicle odometer has this many meters left until maintenance is due."""

    schedule_id: str = FieldInfo(alias="scheduleId")
    """The id of the maintenance schedule."""


class DataTriggerTriggerParamsSpeed(BaseModel):
    min_duration_milliseconds: int = FieldInfo(alias="minDurationMilliseconds")
    """The number of milliseconds the trigger needs to stay active before alerting."""

    operation: Literal["GREATER", "LESS"]
    """How to evaluate the threshold. Valid values: `GREATER`, `LESS`"""

    speed_kilometers_per_hour: int = FieldInfo(alias="speedKilometersPerHour")
    """The speed threshold value."""


class DataTriggerTriggerParamsTireFaultCode(BaseModel):
    manufacturer: Literal[
        "MANUFACTURER_BENDIX",
        "MANUFACTURER_CONTINENTAL",
        "MANUFACTURER_DORAN",
        "MANUFACTURER_HENDRICKSON",
        "MANUFACTURER_INVALID",
        "MANUFACTURER_PRESSURE_PRO",
        "MANUFACTURER_UNIVERSAL_J1939",
        "MANUFACTURER_UNIVERSAL_R141",
    ]
    """The tire manufacturer.

    Valid values: `MANUFACTURER_BENDIX`, `MANUFACTURER_CONTINENTAL`,
    `MANUFACTURER_DORAN`, `MANUFACTURER_HENDRICKSON`, `MANUFACTURER_INVALID`,
    `MANUFACTURER_PRESSURE_PRO`, `MANUFACTURER_UNIVERSAL_J1939`,
    `MANUFACTURER_UNIVERSAL_R141`
    """

    has_cautionary_tire_fault_codes: Optional[bool] = FieldInfo(alias="hasCautionaryTireFaultCodes", default=None)
    """
    If true then alert over pressure, under pressure, across axle fault, or leak
    detected fault codes. Defaults to false.
    """

    has_critical_tire_fault_codes: Optional[bool] = FieldInfo(alias="hasCriticalTireFaultCodes", default=None)
    """
    If true then alert over temperature or extreme pressure over or under fault
    codes. Defaults to false.
    """

    specific_tire_fault_codes: Optional[
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
        ]
    ] = FieldInfo(alias="specificTireFaultCodes", default=None)
    """The list of specific tire fault codes to be alerted on."""


class DataTriggerTriggerParamsUnassignedDriving(BaseModel):
    min_duration_milliseconds: int = FieldInfo(alias="minDurationMilliseconds")
    """The number of milliseconds the trigger needs to stay active before alerting."""


class DataTriggerTriggerParamsVehicleBatteryVoltage(BaseModel):
    battery_volts: int = FieldInfo(alias="batteryVolts")
    """The battery volt threshold value."""

    min_duration_milliseconds: int = FieldInfo(alias="minDurationMilliseconds")
    """The number of milliseconds the trigger needs to stay active before alerting."""

    operation: Literal["GREATER", "LESS"]
    """How to evaluate the threshold. Valid values: `GREATER`, `LESS`"""


class DataTriggerTriggerParamsVehicleFaultCodeSpecificFaultCode(BaseModel):
    fault_code: str = FieldInfo(alias="faultCode")
    """The specific fault code name."""

    type: Literal["INVALID_FAULT_CODE_TYPE", "J1939_DTC", "J1939_SPN", "PASSENGER_DTC"]
    """The specific fault code type.

    Valid values: `INVALID_FAULT_CODE_TYPE`, `J1939_DTC`, `J1939_SPN`,
    `PASSENGER_DTC`
    """


class DataTriggerTriggerParamsVehicleFaultCode(BaseModel):
    has_any_amber_warning_lamp_codes: Optional[bool] = FieldInfo(alias="hasAnyAmberWarningLampCodes", default=None)
    """If true then alert on codes for less serious errors that do not warrant
    stopping.

    Defaults to false.
    """

    has_any_fault_codes: Optional[bool] = FieldInfo(alias="hasAnyFaultCodes", default=None)
    """If true this means that any code is alertable. Defaults to false."""

    has_any_malfunction_indicator_lamp_codes: Optional[bool] = FieldInfo(
        alias="hasAnyMalfunctionIndicatorLampCodes", default=None
    )
    """If true then alert on emission-related codes. Defaults to false."""

    has_any_protection_lamp_codes: Optional[bool] = FieldInfo(alias="hasAnyProtectionLampCodes", default=None)
    """If true then alert on codes for non-electric vehicle parts. Defaults to false."""

    has_any_red_stop_lamp_codes: Optional[bool] = FieldInfo(alias="hasAnyRedStopLampCodes", default=None)
    """If true then alert when the vehicle warrants stopping. Defaults to false."""

    has_any_trailer_abs_lamp_codes: Optional[bool] = FieldInfo(alias="hasAnyTrailerAbsLampCodes", default=None)
    """If true then alert when the ABS light is on. Defaults to false."""

    specific_fault_codes: Optional[List[DataTriggerTriggerParamsVehicleFaultCodeSpecificFaultCode]] = FieldInfo(
        alias="specificFaultCodes", default=None
    )
    """The list of specific fault codes to be alerted on."""


class DataTriggerTriggerParams(BaseModel):
    ambient_temperature: Optional[DataTriggerTriggerParamsAmbientTemperature] = FieldInfo(
        alias="ambientTemperature", default=None
    )
    """Details specific to Ambient Temperature."""

    cell_signal_loss: Optional[DataTriggerTriggerParamsCellSignalLoss] = FieldInfo(alias="cellSignalLoss", default=None)
    """Details specific to Cell Signal Loss"""

    def_level: Optional[DataTriggerTriggerParamsDefLevel] = FieldInfo(alias="defLevel", default=None)
    """Details specific to DEF Level"""

    device_movement: Optional[DataTriggerTriggerParamsDeviceMovement] = FieldInfo(alias="deviceMovement", default=None)
    """Details specific to Device Movement"""

    document_submitted: Optional[DataTriggerTriggerParamsDocumentSubmitted] = FieldInfo(
        alias="documentSubmitted", default=None
    )
    """Details specific to Driver Document Submitted"""

    dvir_submitted_device: Optional[DataTriggerTriggerParamsDvirSubmittedDevice] = FieldInfo(
        alias="dvirSubmittedDevice", default=None
    )
    """Details specific to DVIR Submitted by Device"""

    engine_idle: Optional[DataTriggerTriggerParamsEngineIdle] = FieldInfo(alias="engineIdle", default=None)
    """Details specific to Engine Idle"""

    engine_off: Optional[DataTriggerTriggerParamsEngineOff] = FieldInfo(alias="engineOff", default=None)
    """Details specific to Engine Off"""

    engine_on: Optional[DataTriggerTriggerParamsEngineOn] = FieldInfo(alias="engineOn", default=None)
    """Details specific to Engine On"""

    fuel_level: Optional[DataTriggerTriggerParamsFuelLevel] = FieldInfo(alias="fuelLevel", default=None)
    """Details specific to Fuel Level Percentage"""

    gateway_disconnected: Optional[DataTriggerTriggerParamsGatewayDisconnected] = FieldInfo(
        alias="gatewayDisconnected", default=None
    )
    """Details specific to Gateway Disconnected"""

    gateway_unplugged: Optional[DataTriggerTriggerParamsGatewayUnplugged] = FieldInfo(
        alias="gatewayUnplugged", default=None
    )
    """Details specific to Gateway Unplugged"""

    geofence_entry: Optional[DataTriggerTriggerParamsGeofenceEntry] = FieldInfo(alias="geofenceEntry", default=None)
    """Details specific to Geofence Entry"""

    geofence_exit: Optional[DataTriggerTriggerParamsGeofenceExit] = FieldInfo(alias="geofenceExit", default=None)
    """Details specific to Geofence Exit"""

    gps_signal_loss: Optional[DataTriggerTriggerParamsGpsSignalLoss] = FieldInfo(alias="gpsSignalLoss", default=None)
    """Details specific to GPS Signal Loss"""

    harsh_event: Optional[DataTriggerTriggerParamsHarshEvent] = FieldInfo(alias="harshEvent", default=None)
    """Details specific to Harsh Events"""

    hos_violation: Optional[DataTriggerTriggerParamsHosViolation] = FieldInfo(alias="hosViolation", default=None)
    """Details specific to HOS Violation"""

    inside_geofence: Optional[DataTriggerTriggerParamsInsideGeofence] = FieldInfo(alias="insideGeofence", default=None)
    """Details specific to Inside Geofence"""

    out_of_route: Optional[DataTriggerTriggerParamsOutOfRoute] = FieldInfo(alias="outOfRoute", default=None)
    """Details specific to Out Of Route"""

    outside_geofence: Optional[DataTriggerTriggerParamsOutsideGeofence] = FieldInfo(
        alias="outsideGeofence", default=None
    )
    """Details specific to Outside Geofence"""

    panic_button: Optional[DataTriggerTriggerParamsPanicButton] = FieldInfo(alias="panicButton", default=None)
    """Details specific to Panic Button"""

    route_stop_estimated_arrival: Optional[DataTriggerTriggerParamsRouteStopEstimatedArrival] = FieldInfo(
        alias="routeStopEstimatedArrival", default=None
    )
    """Details specific to Route Stop Estimated Arrival"""

    scheduled_maintenance: Optional[DataTriggerTriggerParamsScheduledMaintenance] = FieldInfo(
        alias="scheduledMaintenance", default=None
    )
    """Details specific to Scheduled Maintenance by Date"""

    scheduled_maintenance_by_engine_hours: Optional[DataTriggerTriggerParamsScheduledMaintenanceByEngineHours] = (
        FieldInfo(alias="scheduledMaintenanceByEngineHours", default=None)
    )
    """Details specific to Scheduled Maintenance By Engine Hours"""

    scheduled_maintenance_odometer: Optional[DataTriggerTriggerParamsScheduledMaintenanceOdometer] = FieldInfo(
        alias="scheduledMaintenanceOdometer", default=None
    )
    """Details specific to Scheduled Maintenance by Odometer"""

    speed: Optional[DataTriggerTriggerParamsSpeed] = None
    """Details specific to Speed"""

    tire_fault_code: Optional[DataTriggerTriggerParamsTireFaultCode] = FieldInfo(alias="tireFaultCode", default=None)
    """Details specific to Tire Fault Code.

    At least one fault code or fault code group must be selected.
    """

    unassigned_driving: Optional[DataTriggerTriggerParamsUnassignedDriving] = FieldInfo(
        alias="unassignedDriving", default=None
    )
    """Details specific to Unassigned Driving"""

    vehicle_battery_voltage: Optional[DataTriggerTriggerParamsVehicleBatteryVoltage] = FieldInfo(
        alias="vehicleBatteryVoltage", default=None
    )
    """Details specific to Vehicle Battery Voltage"""

    vehicle_fault_code: Optional[DataTriggerTriggerParamsVehicleFaultCode] = FieldInfo(
        alias="vehicleFaultCode", default=None
    )
    """Details specific to Vehicle Fault Code.

    At least one fault code or fault code group must be selected.
    """


class DataTrigger(BaseModel):
    trigger_type_id: int = FieldInfo(alias="triggerTypeId")
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

    trigger_params: Optional[DataTriggerTriggerParams] = FieldInfo(alias="triggerParams", default=None)
    """The trigger type specific details.

    Only the field that corresponds to the trigger type is filled in.
    """


class DataOperationalSettingsTimeRange(BaseModel):
    days_of_week: List[Literal["FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"]] = (
        FieldInfo(alias="daysOfWeek")
    )
    """Which days this timezone applies to."""

    end_time: str = FieldInfo(alias="endTime")
    """The time of day at which the time range starts.

    In 24 hour kitchen clock format.
    """

    start_time: str = FieldInfo(alias="startTime")
    """The time of day at which the time range starts.

    In 24 hour kitchen clock format.
    """

    timezone: str
    """
    The timezone of the time range uses
    [IANA timezone database](https://www.iana.org/time-zones) keys (e.g.
    `America/Los_Angeles`, `America/New_York`, `Europe/London`, etc.). You can find
    a mapping of common timezone formats to IANA timezone keys
    [here](https://unicode.org/cldr/charts/latest/supplemental/zone_tzid.html).
    """


class DataOperationalSettings(BaseModel):
    time_ranges: List[DataOperationalSettingsTimeRange] = FieldInfo(alias="timeRanges")
    """The time ranges this alert applies to."""

    time_range_type: Literal["activeBetween", "inactiveBetween"] = FieldInfo(alias="timeRangeType")
    """The type of time ranges. Valid values: `activeBetween`, `inactiveBetween`"""


class Data(BaseModel):
    id: str
    """The unqiue Samsara id of the alert configuration."""

    actions: List[DataAction]
    """An array of actions."""

    created_at_time: str = FieldInfo(alias="createdAtTime")
    """The time the configuration was created in RFC 3339 format."""

    is_enabled: bool = FieldInfo(alias="isEnabled")
    """Whether the alert is enabled or not."""

    last_modified_at_time: str = FieldInfo(alias="lastModifiedAtTime")
    """The time the configuration was last modified in RFC 3339 format."""

    name: str
    """The custom name of the configuration."""

    scope: DataScope
    """What the triggers are scoped to. These are the objects this alert applies to."""

    triggers: List[DataTrigger]
    """An array of triggers."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    operational_settings: Optional[DataOperationalSettings] = FieldInfo(alias="operationalSettings", default=None)
    """Settings on when the alert should be operational."""


class ConfigurationCreateResponse(BaseModel):
    data: Data
    """The configuration of a alert."""
