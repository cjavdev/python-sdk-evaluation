# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "IftaVehicleListResponse",
    "Data",
    "DataVehicleReport",
    "DataVehicleReportJurisdiction",
    "DataVehicleReportVehicle",
    "DataTroubleshooting",
    "Pagination",
]


class DataVehicleReportJurisdiction(BaseModel):
    jurisdiction: str
    """Jurisdiction code."""

    taxable_meters: float = FieldInfo(alias="taxableMeters")
    """Distance in meters traveled on public roads in an IFTA jurisdiction."""

    total_meters: float = FieldInfo(alias="totalMeters")
    """Total meters driven in this jurisdiction, taxable and non-taxable."""

    tax_paid_liters: Optional[float] = FieldInfo(alias="taxPaidLiters", default=None)
    """Liters purchased for all qualified vehicles."""


class DataVehicleReportVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the vehicle"""


class DataVehicleReport(BaseModel):
    jurisdictions: List[DataVehicleReportJurisdiction]
    """List of jurisdiction summaries."""

    vehicle: DataVehicleReportVehicle
    """A minified vehicle object.

    This object is only returned if the route is assigned to the vehicle.
    """


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
    vehicle_reports: List[DataVehicleReport] = FieldInfo(alias="vehicleReports")
    """List of summarized vehicle reports."""

    year: int
    """The specified year for this IFTA report."""

    month: Optional[str] = None
    """The specified month duration for this IFTA report."""

    quarter: Optional[str] = None
    """The specified quarter duration for this IFTA report."""

    troubleshooting: Optional[DataTroubleshooting] = None
    """IFTA report troubleshooting information."""


class Pagination(BaseModel):
    end_cursor: str = FieldInfo(alias="endCursor")
    """Cursor identifier representing the last element in the response.

    This value should be used in conjunction with a subsequent request's 'after'
    query parameter. This may be an empty string if there are no more pages left to
    view.
    """

    has_next_page: bool = FieldInfo(alias="hasNextPage")
    """
    True if there are more pages of results immediately available after this
    endCursor.
    """


class IftaVehicleListResponse(BaseModel):
    data: Data
    """Dictionary containing summarized vehicle report data."""

    pagination: Pagination
    """Pagination parameters."""
