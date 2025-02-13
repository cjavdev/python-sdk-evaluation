# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .goa_gateway_tiny_response_response_body_model import GoaGatewayTinyResponseResponseBodyModel
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class GoaGatewayTinyResponseResponseBody(UniversalBaseModel):
    """
    A minified gateway object
    """

    model: GoaGatewayTinyResponseResponseBodyModel = pydantic.Field()
    """
    The model of the gateway installed on the asset.  Valid values: `AG15`, `AG24`, `AG24EU`, `AG26`, `AG26EU`, `AG41`, `AG41EU`, `AG45`, `AG45EU`, `AG46`, `AG46EU`, `AG46P`, `AG46PEU`, `AG51`, `AG51EU`, `AG52`, `AG52EU`, `AG53`, `AG53EU`, `IG15`, `IG21`, `IG41`, `IG61`, `SG1`, `SG1B`, `SG1G`, `SG1G32`, `SG1x`, `VG32`, `VG33`, `VG34`, `VG34EU`, `VG34FN`, `VG34M`, `VG54ATT`, `VG54EU`, `VG54FN`, `VG54NA`, `VG54NAE`, `VG54NAH`, `VG55EU`, `VG55FN`, `VG55NA`
    """

    serial: str = pydantic.Field()
    """
    The serial number of the gateway installed on the asset.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
