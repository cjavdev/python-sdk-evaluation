# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .vehicle_stats_nfc_card_scan_card import VehicleStatsNfcCardScanCard
import typing
from .vehicle_stats_decorations import VehicleStatsDecorations
from .vehicle_stats_aux_input_time import VehicleStatsAuxInputTime
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class VehicleStatsNfcCardScanWithDecoration(UniversalBaseModel):
    """
    Data for the nfc card and the time that it was scanned.
    """

    card: VehicleStatsNfcCardScanCard
    decorations: typing.Optional[VehicleStatsDecorations] = None
    time: VehicleStatsAuxInputTime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
