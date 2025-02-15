# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .fft_spectra_data_point import FftSpectraDataPoint
from ..core.serialization import FieldMetadata
import pydantic
from .j_1939_d_1_status_data_point import J1939D1StatusDataPoint
from .location_data_point import LocationDataPoint
from .number_data_point import NumberDataPoint
from .string_data_point import StringDataPoint
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class DataInputResponseAllOf(UniversalBaseModel):
    fft_spectra_points: typing_extensions.Annotated[
        typing.Optional[typing.List[FftSpectraDataPoint]], FieldMetadata(alias="fftSpectraPoints")
    ] = pydantic.Field(default=None)
    """
    List of FFT spectra data points from the data input.
    """

    j_1939_d_1_status_points: typing_extensions.Annotated[
        typing.Optional[typing.List[J1939D1StatusDataPoint]], FieldMetadata(alias="j1939D1StatusPoints")
    ] = pydantic.Field(default=None)
    """
    List of active J1939D1 statuses.
    """

    location_points: typing_extensions.Annotated[
        typing.Optional[typing.List[LocationDataPoint]], FieldMetadata(alias="locationPoints")
    ] = pydantic.Field(default=None)
    """
    List of location data points from the data input.
    """

    number_points: typing_extensions.Annotated[
        typing.Optional[typing.List[NumberDataPoint]], FieldMetadata(alias="numberPoints")
    ] = pydantic.Field(default=None)
    """
    List of numeric data points from the data input.
    """

    string_points: typing_extensions.Annotated[
        typing.Optional[typing.List[StringDataPoint]], FieldMetadata(alias="stringPoints")
    ] = pydantic.Field(default=None)
    """
    List of string data points from the data input.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
