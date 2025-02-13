# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StatRetrieveParams"]


class StatRetrieveParams(TypedDict, total=False):
    types: Required[
        List[
            Literal[
                "gatewayEngineStates",
                "obdEngineStates",
                "fuelPercents",
                "engineRpm",
                "gatewayEngineSeconds",
                "obdEngineSeconds",
                "gatewayJ1939EngineSeconds",
                "gpsOdometerMeters",
                "gps",
            ]
        ]
    ]
    """The types of equipment stats you want to query.

    Currently, you may submit up to 3 types.

    - `engineRpm`: The revolutions per minute of the engine.
    - `fuelPercents`: The percent of fuel in the unit of equipment.
    - `obdEngineSeconds`: The number of seconds the engine has been running since it
      was new. This value is provided directly from on-board diagnostics.
    - `gatewayEngineSeconds`: An approximation of the number of seconds the engine
      has been running since it was new, based on the amount of time the asset
      gateway has been receiving power with an offset provided manually through the
      Samsara cloud dashboard. This is supported with the following hardware
      configurations:
      - AG24/AG26/AG46P + APWR cable
        ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d)
        required)
      - AG52 + BPWR/BEQP cable
        ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d)
        required).
    - `gatewayJ1939EngineSeconds`: An approximation of the number of seconds the
      engine has been running since it was new, based on the amount of time the AG26
      device is receiving power via J1939/CAT cable and an offset provided manually
      through the Samsara cloud dashboard.
    - `obdEngineStates`: The state of the engine read from on-board diagnostics. Can
      be `Off`, `On`, or `Idle`.
    - `gatewayEngineStates`: An approximation of engine state based on readings the
      AG26 receives from the aux/digio cable. Can be `Off` or `On`.
    - `gpsOdometerMeters`: An approximation of odometer reading based on GPS
      calculations since the AG26 was activated, and a manual odometer offset
      provided in the Samsara cloud dashboard. Valid values: `Off`, `On`.
    - `gps`: GPS data including lat/long, heading, speed, address book entry (if
      exists), and a reverse geocoded address.
    """

    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    equipment_ids: Annotated[List[str], PropertyInfo(alias="equipmentIds")]
    """A filter on the data based on this comma-separated list of equipment IDs.

    Example: `equipmentIds=1234,5678`
    """

    parent_tag_ids: Annotated[List[str], PropertyInfo(alias="parentTagIds")]
    """
    A filter on the data based on this comma-separated list of parent tag IDs, for
    use by orgs with tag hierarchies. Specifying a parent tag will implicitly
    include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    """

    tag_ids: Annotated[List[str], PropertyInfo(alias="tagIds")]
    """A filter on the data based on this comma-separated list of tag IDs.

    Example: `tagIds=1234,5678`
    """
