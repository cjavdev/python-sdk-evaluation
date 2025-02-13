# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SettingsPatchDriverAppSettingsResponseBody", "Data", "DataGamificationConfig", "DataTrailerSelectionConfig"]


class DataGamificationConfig(BaseModel):
    anonymize_driver_names: Optional[bool] = FieldInfo(alias="anonymizeDriverNames", default=None)
    """
    Hide the names of other drivers when viewing the driver leaderboard in the
    mobile app.
    """


class DataTrailerSelectionConfig(BaseModel):
    driver_trailer_creation_enabled: Optional[bool] = FieldInfo(alias="driverTrailerCreationEnabled", default=None)
    """Allow drivers to create new trailers in the Samsara Driver app."""

    max_num_of_trailers_selected: Optional[int] = FieldInfo(alias="maxNumOfTrailersSelected", default=None)
    """Trailer selection limit."""

    org_trailer_search: Optional[bool] = FieldInfo(alias="orgTrailerSearch", default=None)
    """
    Allow drivers to search for trailers outside of their selection tag when
    connected to the internet
    """


class Data(BaseModel):
    driver_fleet_id: Optional[str] = FieldInfo(alias="driverFleetId", default=None)
    """Login user name for the fleet driver app"""

    gamification: Optional[bool] = None
    """Driver gamification feature.

    Enabling this will turn on the feature for all drivers using the mobile app.
    Drivers can be configured into peer groups within the Drivers Page. Unconfigured
    drivers will be grouped on an organization level.
    """

    gamification_config: Optional[DataGamificationConfig] = FieldInfo(alias="gamificationConfig", default=None)
    """Gamification configuration for the Driver App."""

    org_vehicle_search: Optional[bool] = FieldInfo(alias="orgVehicleSearch", default=None)
    """
    Allow drivers to search for vehicles outside of their selection tag when
    connected to the internet.
    """

    trailer_selection: Optional[bool] = FieldInfo(alias="trailerSelection", default=None)
    """Allow drivers to see and select trailers in the Samsara Driver app."""

    trailer_selection_config: Optional[DataTrailerSelectionConfig] = FieldInfo(
        alias="trailerSelectionConfig", default=None
    )
    """Trailer selection setting configuration for the Driver App."""


class SettingsPatchDriverAppSettingsResponseBody(BaseModel):
    data: Data
    """The configuration settings for the Samsara Driver App.

    Can be set or updated through the Samsara Settings page or the API at any time.
    """
