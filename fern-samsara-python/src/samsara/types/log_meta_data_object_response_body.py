# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from .vehicle_response_response_body import VehicleResponseResponseBody
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class LogMetaDataObjectResponseBody(UniversalBaseModel):
    """
    The metadata of the log.
    """

    adverse_driving_claimed: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="adverseDrivingClaimed")
    ] = pydantic.Field(default=None)
    """
    Whether the driver has claimed the [Adverse Driving Exemption](https://kb.samsara.com/hc/en-us/articles/360047336792-Adverse-Driving-Exemption) for this HOS day chart.
    """

    big_day_claimed: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="bigDayClaimed")] = (
        pydantic.Field(default=None)
    )
    """
    Whether the driver has claimed the [Big Day Exemption](https://kb.samsara.com/hc/en-us/articles/360057113891-16-Hour-Short-Haul-Exemption-Big-Day-) for this HOS day chart.
    """

    carrier_formatted_address: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="carrierFormattedAddress")
    ] = pydantic.Field(default=None)
    """
    The address of the carrier used for this HOS chart.
    """

    carrier_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="carrierName")] = (
        pydantic.Field(default=None)
    )
    """
    The name of the carrier used for this HOS chart.
    """

    carrier_us_dot_number: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="carrierUsDotNumber")
    ] = pydantic.Field(default=None)
    """
    The US DOT number of the carrier used for this HOS chart.
    """

    certified_at_time: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="certifiedAtTime")] = (
        pydantic.Field(default=None)
    )
    """
    The time this log was certified in RFC 3339 format.
    """

    home_terminal_formatted_address: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="homeTerminalFormattedAddress")
    ] = pydantic.Field(default=None)
    """
    The address of the Home Terminal used for this HOS chart.
    """

    home_terminal_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="homeTerminalName")] = (
        pydantic.Field(default=None)
    )
    """
    The name of the Home Terminal used for this HOS chart.
    """

    is_certified: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isCertified")] = (
        pydantic.Field(default=None)
    )
    """
    Whether this HOS day chart was certified by the driver.
    """

    is_us_short_haul_active: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isUsShortHaulActive")
    ] = pydantic.Field(default=None)
    """
    Whether the driver has the 150 air-mile Short Haul Exemption active for this HOS day chart.
    """

    shipping_docs: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="shippingDocs")] = (
        pydantic.Field(default=None)
    )
    """
    List of shipping document names associated with the driver for the day. This field maps to Shipping ID in the dashboard.
    """

    trailer_names: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="trailerNames")
    ] = pydantic.Field(default=None)
    """
    List of trailer names associated with the driver for the day. If a trailer was associated with a log through the driver app the trailer name will be the trailer ID.
    """

    vehicles: typing.Optional[typing.List[VehicleResponseResponseBody]] = pydantic.Field(default=None)
    """
    List of vehicles associated with the driver for the day.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
