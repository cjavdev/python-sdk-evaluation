# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "DataInputListResponse",
    "Data",
    "DataFftSpectraPoint",
    "DataFftSpectraPointFftSpectra",
    "DataJ1939D1StatusPoint",
    "DataJ1939D1StatusPointValue",
    "DataLocationPoint",
    "DataLocationPointGpsLocation",
    "DataLocationPointGpsLocationPlace",
    "DataNumberPoint",
    "DataStringPoint",
    "Pagination",
]


class DataFftSpectraPointFftSpectra(BaseModel):
    frequencies: Optional[List[float]] = None
    """Frequencies"""

    x: Optional[List[float]] = None
    """X-axis data"""

    y: Optional[List[float]] = None
    """Y-axis data"""

    z: Optional[List[float]] = None
    """Z-axis data"""


class DataFftSpectraPoint(BaseModel):
    fft_spectra: Optional[DataFftSpectraPointFftSpectra] = FieldInfo(alias="fftSpectra", default=None)
    """FFT spectrum data"""

    time: Optional[str] = None
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""


class DataJ1939D1StatusPointValue(BaseModel):
    amber_lamp_status: Optional[float] = FieldInfo(alias="amberLampStatus", default=None)

    fmi: Optional[float] = None

    mil_status: Optional[float] = FieldInfo(alias="milStatus", default=None)

    occurance_count: Optional[float] = FieldInfo(alias="occuranceCount", default=None)

    protect_lamp_status: Optional[float] = FieldInfo(alias="protectLampStatus", default=None)

    red_lamp_status: Optional[float] = FieldInfo(alias="redLampStatus", default=None)

    spn: Optional[float] = None

    tx_id: Optional[float] = FieldInfo(alias="txId", default=None)


class DataJ1939D1StatusPoint(BaseModel):
    time: Optional[str] = None
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Optional[List[DataJ1939D1StatusPointValue]] = None
    """List of active statuses."""


class DataLocationPointGpsLocationPlace(BaseModel):
    city: Optional[str] = None
    """City"""

    house_number: Optional[str] = FieldInfo(alias="houseNumber", default=None)
    """House number"""

    neighborhood: Optional[str] = None
    """Neighborhood"""

    poi: Optional[str] = None
    """POI"""

    postcode: Optional[str] = None
    """Postcode"""

    state: Optional[str] = None
    """State"""

    street: Optional[str] = None
    """Street"""


class DataLocationPointGpsLocation(BaseModel):
    formatted_address: Optional[str] = FieldInfo(alias="formattedAddress", default=None)
    """Formatted address of the location"""

    gps_meters_per_second: Optional[float] = FieldInfo(alias="gpsMetersPerSecond", default=None)
    """Speed of GPS (meters per second)"""

    heading_degrees: Optional[float] = FieldInfo(alias="headingDegrees", default=None)
    """Heading degrees"""

    latitude: Optional[float] = None
    """Latitude of the location"""

    longitude: Optional[float] = None
    """Longitude of the location"""

    place: Optional[DataLocationPointGpsLocationPlace] = None
    """Address of the location"""


class DataLocationPoint(BaseModel):
    gps_location: Optional[DataLocationPointGpsLocation] = FieldInfo(alias="gpsLocation", default=None)
    """GPS location information of the data input's datapoint."""

    time: Optional[str] = None
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""


class DataNumberPoint(BaseModel):
    time: Optional[str] = None
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Optional[float] = None
    """Numeric value of the data point."""


class DataStringPoint(BaseModel):
    time: Optional[str] = None
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Optional[str] = None
    """String value of the data point."""


class Data(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the data input."""

    asset_id: Optional[str] = FieldInfo(alias="assetId", default=None)
    """Unique identifier for the data input's asset."""

    data_group: Optional[str] = FieldInfo(alias="dataGroup", default=None)
    """Data group for this data input."""

    fft_spectra_points: Optional[List[DataFftSpectraPoint]] = FieldInfo(alias="fftSpectraPoints", default=None)
    """List of FFT spectra data points from the data input."""

    j1939_d1_status_points: Optional[List[DataJ1939D1StatusPoint]] = FieldInfo(
        alias="j1939D1StatusPoints", default=None
    )
    """List of active J1939D1 statuses."""

    location_points: Optional[List[DataLocationPoint]] = FieldInfo(alias="locationPoints", default=None)
    """List of location data points from the data input."""

    name: Optional[str] = None
    """Name of this data input."""

    number_points: Optional[List[DataNumberPoint]] = FieldInfo(alias="numberPoints", default=None)
    """List of numeric data points from the data input."""

    string_points: Optional[List[DataStringPoint]] = FieldInfo(alias="stringPoints", default=None)
    """List of string data points from the data input."""

    units: Optional[str] = None
    """Units of data for this data input."""


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


class DataInputListResponse(BaseModel):
    data: Optional[List[Data]] = None
    """An array of data input data points.

    Each object in the array represents a data input and will contain its associated
    data points.
    """

    pagination: Optional[Pagination] = None
    """Pagination parameters."""
