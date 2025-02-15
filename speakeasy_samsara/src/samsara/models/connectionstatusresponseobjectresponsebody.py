"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ConnectionStatusResponseObjectResponseBodyHealthStatus(str, Enum):
    r"""The most recent health status of the gateway.  Valid values: `Status Not Set`, `Connected`, `Not Installed`, `Power Source Off - Active Vehicle`, `Power Source Off - Inactive Vehicle`, `Weak Cellular Signal`, `Requires Investigation`, `Requires Charge`, `Unsupported Product`, `Low Battery. Replace Device.`, `Low Vehicle Battery`, `Unplugged`, `Low Charging State`, `Vehicle Off`, `Weak GPS Signal`, `Low Gateway Battery`, `Low Gateway Battery (AG24)`, `Low Gateway Battery (AG45)`, `Low Gateway Battery (AG26)`, `Low Gateway Battery (AG46)`, `Low Gateway Battery (AG46-P)`, `Temporarily Offline`, `Prolonged Offline`, `Recently Offline`, `Replacement Required`, `Status Unknown`"""

    STATUS_NOT_SET = "Status Not Set"
    CONNECTED = "Connected"
    NOT_INSTALLED = "Not Installed"
    POWER_SOURCE_OFF_ACTIVE_VEHICLE = "Power Source Off - Active Vehicle"
    POWER_SOURCE_OFF_INACTIVE_VEHICLE = "Power Source Off - Inactive Vehicle"
    WEAK_CELLULAR_SIGNAL = "Weak Cellular Signal"
    REQUIRES_INVESTIGATION = "Requires Investigation"
    REQUIRES_CHARGE = "Requires Charge"
    UNSUPPORTED_PRODUCT = "Unsupported Product"
    LOW_BATTERY_REPLACE_DEVICE_ = "Low Battery. Replace Device."
    LOW_VEHICLE_BATTERY = "Low Vehicle Battery"
    UNPLUGGED = "Unplugged"
    LOW_CHARGING_STATE = "Low Charging State"
    VEHICLE_OFF = "Vehicle Off"
    WEAK_GPS_SIGNAL = "Weak GPS Signal"
    LOW_GATEWAY_BATTERY = "Low Gateway Battery"
    LOW_GATEWAY_BATTERY_AG24_ = "Low Gateway Battery (AG24)"
    LOW_GATEWAY_BATTERY_AG45_ = "Low Gateway Battery (AG45)"
    LOW_GATEWAY_BATTERY_AG26_ = "Low Gateway Battery (AG26)"
    LOW_GATEWAY_BATTERY_AG46_ = "Low Gateway Battery (AG46)"
    LOW_GATEWAY_BATTERY_AG46_P_ = "Low Gateway Battery (AG46-P)"
    TEMPORARILY_OFFLINE = "Temporarily Offline"
    PROLONGED_OFFLINE = "Prolonged Offline"
    RECENTLY_OFFLINE = "Recently Offline"
    REPLACEMENT_REQUIRED = "Replacement Required"
    STATUS_UNKNOWN = "Status Unknown"


class ConnectionStatusResponseObjectResponseBodyTypedDict(TypedDict):
    r"""An objecting containing information about the connectivity status of the gateway"""

    health_status: NotRequired[ConnectionStatusResponseObjectResponseBodyHealthStatus]
    r"""The most recent health status of the gateway.  Valid values: `Status Not Set`, `Connected`, `Not Installed`, `Power Source Off - Active Vehicle`, `Power Source Off - Inactive Vehicle`, `Weak Cellular Signal`, `Requires Investigation`, `Requires Charge`, `Unsupported Product`, `Low Battery. Replace Device.`, `Low Vehicle Battery`, `Unplugged`, `Low Charging State`, `Vehicle Off`, `Weak GPS Signal`, `Low Gateway Battery`, `Low Gateway Battery (AG24)`, `Low Gateway Battery (AG45)`, `Low Gateway Battery (AG26)`, `Low Gateway Battery (AG46)`, `Low Gateway Battery (AG46-P)`, `Temporarily Offline`, `Prolonged Offline`, `Recently Offline`, `Replacement Required`, `Status Unknown`"""
    last_connected: NotRequired[str]
    r"""The last time the gateway was connected in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""


class ConnectionStatusResponseObjectResponseBody(BaseModel):
    r"""An objecting containing information about the connectivity status of the gateway"""

    health_status: Annotated[
        Optional[ConnectionStatusResponseObjectResponseBodyHealthStatus],
        pydantic.Field(alias="healthStatus"),
    ] = None
    r"""The most recent health status of the gateway.  Valid values: `Status Not Set`, `Connected`, `Not Installed`, `Power Source Off - Active Vehicle`, `Power Source Off - Inactive Vehicle`, `Weak Cellular Signal`, `Requires Investigation`, `Requires Charge`, `Unsupported Product`, `Low Battery. Replace Device.`, `Low Vehicle Battery`, `Unplugged`, `Low Charging State`, `Vehicle Off`, `Weak GPS Signal`, `Low Gateway Battery`, `Low Gateway Battery (AG24)`, `Low Gateway Battery (AG45)`, `Low Gateway Battery (AG26)`, `Low Gateway Battery (AG46)`, `Low Gateway Battery (AG46-P)`, `Temporarily Offline`, `Prolonged Offline`, `Recently Offline`, `Replacement Required`, `Status Unknown`"""

    last_connected: Annotated[Optional[str], pydantic.Field(alias="lastConnected")] = (
        None
    )
    r"""The last time the gateway was connected in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""
