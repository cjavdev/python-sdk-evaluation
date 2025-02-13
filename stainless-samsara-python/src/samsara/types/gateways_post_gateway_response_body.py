# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "GatewaysPostGatewayResponseBody",
    "Data",
    "DataAccessoryDevice",
    "DataAsset",
    "DataConnectionStatus",
    "DataDataUsageLast30Days",
]


class DataAccessoryDevice(BaseModel):
    model: Optional[str] = None
    """Product model name of the device"""

    serial: Optional[str] = None
    """The serial number of the accessory device."""


class DataAsset(BaseModel):
    id: Optional[str] = None
    """The unique Samsara ID of the asset where the gateway is installed.

    This is automatically generated when the asset is created and cannot be changed.
    Use this ID on PATCH vehicle, equipment, or trailer endpoints to update the
    asset
    """

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""


class DataConnectionStatus(BaseModel):
    health_status: Optional[
        Literal[
            "Status Not Set",
            "Connected",
            "Not Installed",
            "Power Source Off - Active Vehicle",
            "Power Source Off - Inactive Vehicle",
            "Weak Cellular Signal",
            "Requires Investigation",
            "Requires Charge",
            "Unsupported Product",
            "Low Battery. Replace Device.",
            "Low Vehicle Battery",
            "Unplugged",
            "Low Charging State",
            "Vehicle Off",
            "Weak GPS Signal",
            "Low Gateway Battery",
            "Low Gateway Battery (AG24)",
            "Low Gateway Battery (AG45)",
            "Low Gateway Battery (AG26)",
            "Low Gateway Battery (AG46)",
            "Low Gateway Battery (AG46-P)",
            "Temporarily Offline",
            "Prolonged Offline",
            "Recently Offline",
            "Replacement Required",
            "Status Unknown",
        ]
    ] = FieldInfo(alias="healthStatus", default=None)
    """The most recent health status of the gateway.

    Valid values: `Status Not Set`, `Connected`, `Not Installed`,
    `Power Source Off - Active Vehicle`, `Power Source Off - Inactive Vehicle`,
    `Weak Cellular Signal`, `Requires Investigation`, `Requires Charge`,
    `Unsupported Product`, `Low Battery. Replace Device.`, `Low Vehicle Battery`,
    `Unplugged`, `Low Charging State`, `Vehicle Off`, `Weak GPS Signal`,
    `Low Gateway Battery`, `Low Gateway Battery (AG24)`,
    `Low Gateway Battery (AG45)`, `Low Gateway Battery (AG26)`,
    `Low Gateway Battery (AG46)`, `Low Gateway Battery (AG46-P)`,
    `Temporarily Offline`, `Prolonged Offline`, `Recently Offline`,
    `Replacement Required`, `Status Unknown`
    """

    last_connected: Optional[str] = FieldInfo(alias="lastConnected", default=None)
    """The last time the gateway was connected in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """


class DataDataUsageLast30Days(BaseModel):
    cellular_data_usage_bytes: Optional[int] = FieldInfo(alias="cellularDataUsageBytes", default=None)
    """Celluar data usage in bytes."""

    hotspot_usage_bytes: Optional[int] = FieldInfo(alias="hotspotUsageBytes", default=None)
    """Wifi hotspot data usage in bytes."""


class Data(BaseModel):
    model: Literal[
        "AG15",
        "AG24",
        "AG24EU",
        "AG26",
        "AG26EU",
        "AG41",
        "AG41EU",
        "AG45",
        "AG45EU",
        "AG46",
        "AG46EU",
        "AG46P",
        "AG46PEU",
        "AG51",
        "AG51EU",
        "AG52",
        "AG52EU",
        "AG53",
        "AG53EU",
        "IG15",
        "IG21",
        "IG41",
        "IG61",
        "SG1",
        "SG1B",
        "SG1G",
        "SG1G32",
        "SG1x",
        "VG32",
        "VG33",
        "VG34",
        "VG34EU",
        "VG34FN",
        "VG34M",
        "VG54ATT",
        "VG54EU",
        "VG54FN",
        "VG54NA",
        "VG54NAE",
        "VG54NAH",
        "VG55EU",
        "VG55FN",
        "VG55NA",
    ]
    """The model of the gateway installed on the asset.

    Valid values: `AG15`, `AG24`, `AG24EU`, `AG26`, `AG26EU`, `AG41`, `AG41EU`,
    `AG45`, `AG45EU`, `AG46`, `AG46EU`, `AG46P`, `AG46PEU`, `AG51`, `AG51EU`,
    `AG52`, `AG52EU`, `AG53`, `AG53EU`, `IG15`, `IG21`, `IG41`, `IG61`, `SG1`,
    `SG1B`, `SG1G`, `SG1G32`, `SG1x`, `VG32`, `VG33`, `VG34`, `VG34EU`, `VG34FN`,
    `VG34M`, `VG54ATT`, `VG54EU`, `VG54FN`, `VG54NA`, `VG54NAE`, `VG54NAH`,
    `VG55EU`, `VG55FN`, `VG55NA`
    """

    serial: str
    """The serial number of the gateway installed on the asset."""

    accessory_devices: Optional[List[DataAccessoryDevice]] = FieldInfo(alias="accessoryDevices", default=None)
    """Accessory devices on gateway"""

    asset: Optional[DataAsset] = None
    """An object containing information about the asset the gateway is installed on"""

    connection_status: Optional[DataConnectionStatus] = FieldInfo(alias="connectionStatus", default=None)
    """
    An objecting containing information about the connectivity status of the gateway
    """

    data_usage_last30_days: Optional[DataDataUsageLast30Days] = FieldInfo(alias="dataUsageLast30Days", default=None)
    """
    An object containing information about the gateway data usage in mb for the last
    30 days.
    """


class GatewaysPostGatewayResponseBody(BaseModel):
    data: Data
