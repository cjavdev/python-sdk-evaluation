# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SettingsGetComplianceSettingsResponseBody", "Data"]


class Data(BaseModel):
    allow_unregulated_vehicles_enabled: Optional[bool] = FieldInfo(
        alias="allowUnregulatedVehiclesEnabled", default=None
    )
    """[deprecated] Allow Unregulated Vehicles.

    This setting is deprecated as all organizations can now mark vehicles as
    unregulated.
    """

    canada_hos_enabled: Optional[bool] = FieldInfo(alias="canadaHosEnabled", default=None)
    """Enable Canada HOS"""

    carrier_name: Optional[str] = FieldInfo(alias="carrierName", default=None)
    """Carrier name of the organization"""

    dot_number: Optional[int] = FieldInfo(alias="dotNumber", default=None)
    """DOT Number"""

    driver_auto_duty_enabled: Optional[bool] = FieldInfo(alias="driverAutoDutyEnabled", default=None)
    """Enable Driver Auto-Duty"""

    edit_certified_logs_enabled: Optional[bool] = FieldInfo(alias="editCertifiedLogsEnabled", default=None)
    """Drivers Can Edit Certified Log"""

    force_manual_location_for_duty_status_changes_enabled: Optional[bool] = FieldInfo(
        alias="forceManualLocationForDutyStatusChangesEnabled", default=None
    )
    """Force Manual Location For Duty Status Changes"""

    force_review_unassigned_hos_enabled: Optional[bool] = FieldInfo(
        alias="forceReviewUnassignedHosEnabled", default=None
    )
    """Force Review of Unassigned HOS"""

    main_office_formatted_address: Optional[str] = FieldInfo(alias="mainOfficeFormattedAddress", default=None)
    """Office Address"""

    persistent_duty_status_enabled: Optional[bool] = FieldInfo(alias="persistentDutyStatusEnabled", default=None)
    """Persistent Duty Status"""


class SettingsGetComplianceSettingsResponseBody(BaseModel):
    data: Data
    """
    Information set here will be displayed in roadside inspections and in the
    transferred US DOT datafile.
    """
