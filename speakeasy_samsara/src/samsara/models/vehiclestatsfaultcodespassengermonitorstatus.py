"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .vehiclestatsfaultcodespassengermonitorstatusvalue import (
    VehicleStatsFaultCodesPassengerMonitorStatusValue,
)
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class VehicleStatsFaultCodesPassengerMonitorStatusTypedDict(TypedDict):
    r"""Readings from engine sensors"""

    catalyst: NotRequired[VehicleStatsFaultCodesPassengerMonitorStatusValue]
    r"""Enum of monitor status:
    -U: Unsupported
    -N: Not Complete
    -R: Complete

    """
    comprehensive: NotRequired[VehicleStatsFaultCodesPassengerMonitorStatusValue]
    r"""Enum of monitor status:
    -U: Unsupported
    -N: Not Complete
    -R: Complete

    """
    egr: NotRequired[VehicleStatsFaultCodesPassengerMonitorStatusValue]
    r"""Enum of monitor status:
    -U: Unsupported
    -N: Not Complete
    -R: Complete

    """
    evap_system: NotRequired[VehicleStatsFaultCodesPassengerMonitorStatusValue]
    r"""Enum of monitor status:
    -U: Unsupported
    -N: Not Complete
    -R: Complete

    """
    fuel: NotRequired[VehicleStatsFaultCodesPassengerMonitorStatusValue]
    r"""Enum of monitor status:
    -U: Unsupported
    -N: Not Complete
    -R: Complete

    """
    heated_catalyst: NotRequired[VehicleStatsFaultCodesPassengerMonitorStatusValue]
    r"""Enum of monitor status:
    -U: Unsupported
    -N: Not Complete
    -R: Complete

    """
    heated_o2_sensor: NotRequired[VehicleStatsFaultCodesPassengerMonitorStatusValue]
    r"""Enum of monitor status:
    -U: Unsupported
    -N: Not Complete
    -R: Complete

    """
    iso_sae_reserved: NotRequired[VehicleStatsFaultCodesPassengerMonitorStatusValue]
    r"""Enum of monitor status:
    -U: Unsupported
    -N: Not Complete
    -R: Complete

    """
    misfire: NotRequired[VehicleStatsFaultCodesPassengerMonitorStatusValue]
    r"""Enum of monitor status:
    -U: Unsupported
    -N: Not Complete
    -R: Complete

    """
    not_ready_count: NotRequired[int]
    r"""Count of the number of sensors reporting N: Not Complete"""
    o2_sensor: NotRequired[VehicleStatsFaultCodesPassengerMonitorStatusValue]
    r"""Enum of monitor status:
    -U: Unsupported
    -N: Not Complete
    -R: Complete

    """
    secondary_air: NotRequired[VehicleStatsFaultCodesPassengerMonitorStatusValue]
    r"""Enum of monitor status:
    -U: Unsupported
    -N: Not Complete
    -R: Complete

    """


class VehicleStatsFaultCodesPassengerMonitorStatus(BaseModel):
    r"""Readings from engine sensors"""

    catalyst: Optional[VehicleStatsFaultCodesPassengerMonitorStatusValue] = None
    r"""Enum of monitor status:
    -U: Unsupported
    -N: Not Complete
    -R: Complete

    """

    comprehensive: Optional[VehicleStatsFaultCodesPassengerMonitorStatusValue] = None
    r"""Enum of monitor status:
    -U: Unsupported
    -N: Not Complete
    -R: Complete

    """

    egr: Optional[VehicleStatsFaultCodesPassengerMonitorStatusValue] = None
    r"""Enum of monitor status:
    -U: Unsupported
    -N: Not Complete
    -R: Complete

    """

    evap_system: Annotated[
        Optional[VehicleStatsFaultCodesPassengerMonitorStatusValue],
        pydantic.Field(alias="evapSystem"),
    ] = None
    r"""Enum of monitor status:
    -U: Unsupported
    -N: Not Complete
    -R: Complete

    """

    fuel: Optional[VehicleStatsFaultCodesPassengerMonitorStatusValue] = None
    r"""Enum of monitor status:
    -U: Unsupported
    -N: Not Complete
    -R: Complete

    """

    heated_catalyst: Annotated[
        Optional[VehicleStatsFaultCodesPassengerMonitorStatusValue],
        pydantic.Field(alias="heatedCatalyst"),
    ] = None
    r"""Enum of monitor status:
    -U: Unsupported
    -N: Not Complete
    -R: Complete

    """

    heated_o2_sensor: Annotated[
        Optional[VehicleStatsFaultCodesPassengerMonitorStatusValue],
        pydantic.Field(alias="heatedO2Sensor"),
    ] = None
    r"""Enum of monitor status:
    -U: Unsupported
    -N: Not Complete
    -R: Complete

    """

    iso_sae_reserved: Annotated[
        Optional[VehicleStatsFaultCodesPassengerMonitorStatusValue],
        pydantic.Field(alias="isoSaeReserved"),
    ] = None
    r"""Enum of monitor status:
    -U: Unsupported
    -N: Not Complete
    -R: Complete

    """

    misfire: Optional[VehicleStatsFaultCodesPassengerMonitorStatusValue] = None
    r"""Enum of monitor status:
    -U: Unsupported
    -N: Not Complete
    -R: Complete

    """

    not_ready_count: Annotated[Optional[int], pydantic.Field(alias="notReadyCount")] = (
        None
    )
    r"""Count of the number of sensors reporting N: Not Complete"""

    o2_sensor: Annotated[
        Optional[VehicleStatsFaultCodesPassengerMonitorStatusValue],
        pydantic.Field(alias="o2Sensor"),
    ] = None
    r"""Enum of monitor status:
    -U: Unsupported
    -N: Not Complete
    -R: Complete

    """

    secondary_air: Annotated[
        Optional[VehicleStatsFaultCodesPassengerMonitorStatusValue],
        pydantic.Field(alias="secondaryAir"),
    ] = None
    r"""Enum of monitor status:
    -U: Unsupported
    -N: Not Complete
    -R: Complete

    """
