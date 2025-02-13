# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ComplianceUpdateParams"]


class ComplianceUpdateParams(TypedDict, total=False):
    allow_unregulated_vehicles_enabled: Annotated[bool, PropertyInfo(alias="allowUnregulatedVehiclesEnabled")]
    """[deprecated] Allow Unregulated Vehicles.

    This setting is deprecated as all organizations can now mark vehicles as
    unregulated.
    """

    canada_hos_enabled: Annotated[bool, PropertyInfo(alias="canadaHosEnabled")]
    """Enable Canada HOS"""

    carrier_name: Annotated[str, PropertyInfo(alias="carrierName")]
    """Carrier Name / Principal Place of Business Name"""

    dot_number: Annotated[int, PropertyInfo(alias="dotNumber")]
    """Carrier US DOT Number"""

    driver_auto_duty_enabled: Annotated[bool, PropertyInfo(alias="driverAutoDutyEnabled")]
    """Enable Driver Auto-Duty"""

    edit_certified_logs_enabled: Annotated[bool, PropertyInfo(alias="editCertifiedLogsEnabled")]
    """Drivers Can Edit Certified Log"""

    force_manual_location_for_duty_status_changes_enabled: Annotated[
        bool, PropertyInfo(alias="forceManualLocationForDutyStatusChangesEnabled")
    ]
    """Force Manual Location For Duty Status Changes"""

    force_review_unassigned_hos_enabled: Annotated[bool, PropertyInfo(alias="forceReviewUnassignedHosEnabled")]
    """Force Review of Unassigned HOS"""

    main_office_formatted_address: Annotated[str, PropertyInfo(alias="mainOfficeFormattedAddress")]
    """Main Office Address / Principal Place of Businesss Address"""

    persistent_duty_status_enabled: Annotated[bool, PropertyInfo(alias="persistentDutyStatusEnabled")]
    """Persistent Duty Status"""
