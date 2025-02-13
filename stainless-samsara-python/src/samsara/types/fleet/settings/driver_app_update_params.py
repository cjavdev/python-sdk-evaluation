# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DriverAppUpdateParams", "GamificationConfig", "TrailerSelectionConfig"]


class DriverAppUpdateParams(TypedDict, total=False):
    driver_fleet_id: Annotated[str, PropertyInfo(alias="driverFleetId")]
    """Global login user name for the fleet driver app"""

    gamification: bool
    """Driver gamification feature.

    Enabling this will turn on the feature for all drivers using the mobile app.
    Drivers can be configured into peer groups within the Drivers Page. Unconfigured
    drivers will be grouped on an organization level.
    """

    gamification_config: Annotated[GamificationConfig, PropertyInfo(alias="gamificationConfig")]
    """Gamification configuration for the Driver App."""

    org_vehicle_search: Annotated[bool, PropertyInfo(alias="orgVehicleSearch")]
    """
    Allow drivers to search for vehicles outside of their selection tag when
    connected to the internet.
    """

    trailer_selection: Annotated[bool, PropertyInfo(alias="trailerSelection")]
    """Allow drivers to see and select trailers in the Samsara Driver app."""

    trailer_selection_config: Annotated[TrailerSelectionConfig, PropertyInfo(alias="trailerSelectionConfig")]
    """Trailer selection setting configuration for the Driver App."""


class GamificationConfig(TypedDict, total=False):
    anonymize_driver_names: Annotated[bool, PropertyInfo(alias="anonymizeDriverNames")]
    """
    Hide the names of other drivers when viewing the driver leaderboard in the
    mobile app.
    """


class TrailerSelectionConfig(TypedDict, total=False):
    driver_trailer_creation_enabled: Annotated[bool, PropertyInfo(alias="driverTrailerCreationEnabled")]
    """Allow drivers to create new trailers in the Samsara Driver app."""

    max_num_of_trailers_selected: Annotated[int, PropertyInfo(alias="maxNumOfTrailersSelected")]
    """Trailer selection limit."""

    org_trailer_search: Annotated[bool, PropertyInfo(alias="orgTrailerSearch")]
    """
    Allow drivers to search for trailers outside of their selection tag when
    connected to the internet
    """
