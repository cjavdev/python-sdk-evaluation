# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["IftaVehicleListParams"]


class IftaVehicleListParams(TypedDict, total=False):
    year: Required[int]
    """The year of the requested IFTA report summary.

    Must be provided with a month or quarter param. Example: `year=2021`
    """

    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    fuel_type: Annotated[
        Literal[
            "Unspecified",
            "A55",
            "Biodiesel",
            "CompressedNaturalGas",
            "Diesel",
            "E85",
            "Electricity",
            "Ethanol",
            "Gasohol",
            "Gasoline",
            "Hydrogen",
            "LiquifiedNaturalGas",
            "M85",
            "Methanol",
            "Propane",
            "Other",
        ],
        PropertyInfo(alias="fuelType"),
    ]
    """A filter on the data based on this comma-separated list of IFTA fuel types.

    Example: `fuelType=Diesel` Valid values: `Unspecified`, `A55`, `Biodiesel`,
    `CompressedNaturalGas`, `Diesel`, `E85`, `Electricity`, `Ethanol`, `Gasohol`,
    `Gasoline`, `Hydrogen`, `LiquifiedNaturalGas`, `M85`, `Methanol`, `Propane`,
    `Other`
    """

    jurisdictions: str
    """A filter on the data based on this comma-separated list of jurisdictions.

    Example: `jurisdictions=GA`
    """

    month: Literal[
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    """The month of the requested IFTA report summary.

    Can not be provided with the quarter param. Example: `month=January` Valid
    values: `January`, `February`, `March`, `April`, `May`, `June`, `July`,
    `August`, `September`, `October`, `November`, `December`
    """

    parent_tag_ids: Annotated[str, PropertyInfo(alias="parentTagIds")]
    """
    A filter on the data based on this comma-separated list of parent tag IDs, for
    use by orgs with tag hierarchies. Specifying a parent tag will implicitly
    include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    """

    quarter: Literal["Q1", "Q2", "Q3", "Q4"]
    """The quarter of the requested IFTA report summary.

    Can not be provided with the month param. Q1: January, February, March. Q2:
    April, May, June. Q3: July, August, September. Q4: October, November, December.
    Example: `quarter=Q1` Valid values: `Q1`, `Q2`, `Q3`, `Q4`
    """

    tag_ids: Annotated[str, PropertyInfo(alias="tagIds")]
    """A filter on the data based on this comma-separated list of tag IDs.

    Example: `tagIds=1234,5678`
    """

    vehicle_ids: Annotated[str, PropertyInfo(alias="vehicleIds")]
    """
    A filter on the data based on this comma-separated list of vehicle IDs and
    externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    """
