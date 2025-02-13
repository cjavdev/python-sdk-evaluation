# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "DriversFuelEnergyListResponse",
    "Data",
    "DataDriverReport",
    "DataDriverReportDriver",
    "DataDriverReportEstFuelEnergyCost",
    "Pagination",
]


class DataDriverReportDriver(BaseModel):
    id: str
    """ID of the driver"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the driver"""


class DataDriverReportEstFuelEnergyCost(BaseModel):
    amount: float
    """Amount of the currency."""

    currency_code: str = FieldInfo(alias="currencyCode")
    """Type of the currency."""


class DataDriverReport(BaseModel):
    distance_traveled_meters: float = FieldInfo(alias="distanceTraveledMeters")
    """Meters traveled over the given time range."""

    driver: DataDriverReportDriver
    """A minified driver object.

    This object is only returned if the route is assigned to the driver.
    """

    efficiency_mpge: float = FieldInfo(alias="efficiencyMpge")
    """Efficiency in MPG or MPGE over the given time range.

    For fuel vehicles this will be provided in MPG, for hybrid and electric vehicles
    this will be provided in MPGE. MPG/MPGE values are provided based on US gallons.
    """

    est_fuel_energy_cost: DataDriverReportEstFuelEnergyCost = FieldInfo(alias="estFuelEnergyCost")
    """Estimated cost of fuel and energy over the given time range."""

    energy_used_kwh: Optional[float] = FieldInfo(alias="energyUsedKwh", default=None)
    """Kilowatt-hours of energy used over the given time range.

    Only provided for hybrid and electric vehicles.
    """

    engine_idle_time_duration_ms: Optional[int] = FieldInfo(alias="engineIdleTimeDurationMs", default=None)
    """Milliseconds of engine idle time over the given time range.

    Only provided for fuel and hybrid vehicles.
    """

    engine_run_time_duration_ms: Optional[int] = FieldInfo(alias="engineRunTimeDurationMs", default=None)
    """Milliseconds of engine run time over the given time range.

    Only provided for fuel and hybrid vehicles.
    """

    est_carbon_emissions_kg: Optional[float] = FieldInfo(alias="estCarbonEmissionsKg", default=None)
    """Estimated kilograms of carbon emissions over the given time range.

    Only provided for fuel and hybrid vehicles.
    """

    fuel_consumed_ml: Optional[float] = FieldInfo(alias="fuelConsumedMl", default=None)
    """Milliliters of fuel consumed over the given time range.

    Only provided for fuel and hybrid vehicles.
    """


class Data(BaseModel):
    driver_reports: List[DataDriverReport] = FieldInfo(alias="driverReports")
    """List of summarized driver reports."""


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


class DriversFuelEnergyListResponse(BaseModel):
    data: Data
    """Dictionary containing summarized driver report data."""

    pagination: Pagination
    """Pagination parameters."""
