# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AssetCreateParams"]


class AssetCreateParams(TypedDict, total=False):
    external_ids: Annotated[Dict[str, str], PropertyInfo(alias="externalIds")]
    """A map of external ids"""

    license_plate: Annotated[str, PropertyInfo(alias="licensePlate")]
    """The license plate of the asset."""

    make: str
    """The manufacturer of the asset.

    (If a VIN is entered and the system detects it is registered to a different
    manufacturer than provided an error will be returned).
    """

    model: str
    """The manufacturer model of the asset.

    (If a VIN is entered and the system detects it is registered to a different
    model than provided an error will be returned).
    """

    name: str
    """The human-readable name of the asset.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    notes: str
    """These are generic notes about the asset.

    Can be set or updated through the Samsara Dashboard or the API at any time.
    """

    regulation_mode: Annotated[Literal["mixed", "regulated", "unregulated"], PropertyInfo(alias="regulationMode")]
    """
    Whether or not the asset is regulated, unregulated (non-CMV), or a mixed use
    unregulated asset. Primarily used with vehicles. Valid values: `mixed`,
    `regulated`, `unregulated`
    """

    serial_number: Annotated[str, PropertyInfo(alias="serialNumber")]
    """The serial number of the asset."""

    type: Literal["uncategorized", "trailer", "equipment", "unpowered", "vehicle"]
    """The operational context in which the asset interacts with the Samsara system.

    Examples: Vehicle (eg: truck, bus...), Trailer (eg: dry van, reefer,
    flatbed...), Powered Equipment (eg: dozer, crane...), Unpowered Equipment (eg:
    container, dumpster...), or Uncategorized. Valid values: `uncategorized`,
    `trailer`, `equipment`, `unpowered`, `vehicle`
    """

    vin: str
    """The vehicle identification number of the asset."""

    year: int
    """The year of manufacture of the asset.

    (If a VIN is entered and the system detects it is registered to a different year
    than provided an error will be returned).
    """
