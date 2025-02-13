# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["CustomReportsGetCustomReportRunDataResponseBody", "Data", "DataColumn", "Pagination"]


class DataColumn(BaseModel):
    display_name: str = FieldInfo(alias="displayName")
    """
    The display name of the column that appears in the dashboard or exported csv,
    xlsx, and pdf reports. This value can contain whitespaces and special
    characters. It is not used to key the values below in the `data` array.
    """

    type: Literal["string", "numeric"]
    """The type of data for this column. Valid values: `string`, `numeric`"""

    base_unit: Optional[
        Literal[
            "bar",
            "celsius",
            "fahrenheit",
            "foot",
            "gallon",
            "galpermi",
            "gforce",
            "gperliter",
            "gperm",
            "impgallon",
            "impgalpermi",
            "inch",
            "kelvin",
            "kgpergallon",
            "kgperkm",
            "kgperliter",
            "kgpermi",
            "kilogram",
            "kilometer",
            "kilopascal",
            "kilowatthour",
            "kmperhr",
            "lbpermi",
            "liter",
            "lper100km",
            "lperkm",
            "lperm",
            "meter",
            "meterspersec",
            "mile",
            "milliknot",
            "milliseconds",
            "millivolt",
            "mipergal",
            "miperhr",
            "miperimpgal",
            "pound",
            "poundsPerSquareInch",
            "poundspergallon",
            "poundsperliter",
            "volt",
            "watthour",
        ]
    ] = FieldInfo(alias="baseUnit", default=None)
    """[deprecated] Use unit instead.

    Valid values: `bar`, `celsius`, `fahrenheit`, `foot`, `gallon`, `galpermi`,
    `gforce`, `gperliter`, `gperm`, `impgallon`, `impgalpermi`, `inch`, `kelvin`,
    `kgpergallon`, `kgperkm`, `kgperliter`, `kgpermi`, `kilogram`, `kilometer`,
    `kilopascal`, `kilowatthour`, `kmperhr`, `lbpermi`, `liter`, `lper100km`,
    `lperkm`, `lperm`, `meter`, `meterspersec`, `mile`, `milliknot`, `milliseconds`,
    `millivolt`, `mipergal`, `miperhr`, `miperimpgal`, `pound`,
    `poundsPerSquareInch`, `poundspergallon`, `poundsperliter`, `volt`, `watthour`
    """

    unit: Optional[
        Literal[
            "bar",
            "degreesCelsius",
            "degreesFahrenheit",
            "feet",
            "gForces",
            "gallons",
            "gallonsPerMile",
            "gramsPerLiter",
            "gramsPerMeter",
            "imperialGallons",
            "imperialGallonsPerMile",
            "inches",
            "kelvin",
            "kilograms",
            "kilogramsPerGallon",
            "kilogramsPerKilometer",
            "kilogramsPerLiter",
            "kilogramsPerMile",
            "kilometers",
            "kilometersPerHour",
            "kilopascals",
            "kilowattHours",
            "liters",
            "litersPer100Kilometers",
            "litersPerKilometer",
            "litersPerMeter",
            "meters",
            "metersPerSecond",
            "miles",
            "milesPerGallon",
            "milesPerHour",
            "milesPerImperialGallon",
            "milliknots",
            "milliseconds",
            "millivolts",
            "pounds",
            "poundsPerGallon",
            "poundsPerLiter",
            "poundsPerMile",
            "poundsPerSquareInch",
            "volts",
            "wattHours",
        ]
    ] = None
    """The unit of the data for this column.

    If the data is a string or custom score (ie, anticipation score), unit will not
    be returned. Valid values: `bar`, `degreesCelsius`, `degreesFahrenheit`, `feet`,
    `gForces`, `gallons`, `gallonsPerMile`, `gramsPerLiter`, `gramsPerMeter`,
    `imperialGallons`, `imperialGallonsPerMile`, `inches`, `kelvin`, `kilograms`,
    `kilogramsPerGallon`, `kilogramsPerKilometer`, `kilogramsPerLiter`,
    `kilogramsPerMile`, `kilometers`, `kilometersPerHour`, `kilopascals`,
    `kilowattHours`, `liters`, `litersPer100Kilometers`, `litersPerKilometer`,
    `litersPerMeter`, `meters`, `metersPerSecond`, `miles`, `milesPerGallon`,
    `milesPerHour`, `milesPerImperialGallon`, `milliknots`, `milliseconds`,
    `millivolts`, `pounds`, `poundsPerGallon`, `poundsPerLiter`, `poundsPerMile`,
    `poundsPerSquareInch`, `volts`, `wattHours`
    """


class Data(BaseModel):
    rows: List[List[object]]
    """An array of arrays that represents each row in a custom report.

    The first index represents which row the data is for and the second index
    represents which column the data is for. For example, rows[1][3] accesses the
    second row's fourth column data.
    """

    columns: Optional[List[DataColumn]] = None
    """An array of objects containing data about column definitions"""


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


class CustomReportsGetCustomReportRunDataResponseBody(BaseModel):
    data: Data

    pagination: Pagination
    """Pagination parameters."""
