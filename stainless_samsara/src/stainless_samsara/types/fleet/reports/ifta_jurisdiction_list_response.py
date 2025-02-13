# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["IftaJurisdictionListResponse", "Data", "DataJurisdictionReport", "DataTroubleshooting"]


class DataJurisdictionReport(BaseModel):
    jurisdiction: str
    """Jurisdiction code."""

    taxable_meters: float = FieldInfo(alias="taxableMeters")
    """Distance in meters traveled on public roads in an IFTA jurisdiction."""

    total_meters: float = FieldInfo(alias="totalMeters")
    """Total meters driven in this jurisdiction, taxable and non-taxable."""

    tax_paid_liters: Optional[float] = FieldInfo(alias="taxPaidLiters", default=None)
    """Liters purchased for all qualified vehicles."""


class DataTroubleshooting(BaseModel):
    no_purchases_found: bool = FieldInfo(alias="noPurchasesFound")
    """Whether or not fuel purchases were found for this report."""

    unassigned_fuel_type_purchases: int = FieldInfo(alias="unassignedFuelTypePurchases")
    """The number of fuel purchases without a fuel type assigned.

    Fuel purchases are used to calculate tax paid gallons.
    """

    unassigned_fuel_type_vehicles: int = FieldInfo(alias="unassignedFuelTypeVehicles")
    """The number of vehicles without a fuel type assigned.

    Vehicles without an assigned fuel type may affect total mileage.
    """

    unassigned_vehicle_purchases: int = FieldInfo(alias="unassignedVehiclePurchases")
    """
    Purchases without an assigned fuel type may affect tax-paid gallons and fleet
    mpg.
    """


class Data(BaseModel):
    jurisdiction_reports: List[DataJurisdictionReport] = FieldInfo(alias="jurisdictionReports")
    """List of summarized jurisdiction reports."""

    year: int
    """The specified year for this IFTA report."""

    month: Optional[str] = None
    """The specified month duration for this IFTA report."""

    quarter: Optional[str] = None
    """The specified quarter duration for this IFTA report."""

    troubleshooting: Optional[DataTroubleshooting] = None
    """IFTA report troubleshooting information."""


class IftaJurisdictionListResponse(BaseModel):
    data: Data
    """Dictionary containing summarized jurisdiction report data."""
