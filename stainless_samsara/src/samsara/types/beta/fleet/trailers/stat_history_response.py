# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "StatHistoryResponse",
    "Data",
    "DataCarrierReeferState",
    "DataCarrierReeferStateDecorations",
    "DataCarrierReeferStateDecorationsCarrierReeferState",
    "DataCarrierReeferStateDecorationsGps",
    "DataCarrierReeferStateDecorationsGpsReverseGeo",
    "DataCarrierReeferStateDecorationsGpsOdometerMeters",
    "DataCarrierReeferStateDecorationsReeferAlarms",
    "DataCarrierReeferStateDecorationsReeferAlarmsAlarm",
    "DataCarrierReeferStateDecorationsReeferAmbientAirTemperatureMilliC",
    "DataCarrierReeferStateDecorationsReeferDoorStateZone1",
    "DataCarrierReeferStateDecorationsReeferDoorStateZone2",
    "DataCarrierReeferStateDecorationsReeferDoorStateZone3",
    "DataCarrierReeferStateDecorationsReeferFuelPercent",
    "DataCarrierReeferStateDecorationsReeferObdEngineSeconds",
    "DataCarrierReeferStateDecorationsReeferReturnAirTemperatureMilliCZone1",
    "DataCarrierReeferStateDecorationsReeferReturnAirTemperatureMilliCZone2",
    "DataCarrierReeferStateDecorationsReeferReturnAirTemperatureMilliCZone3",
    "DataCarrierReeferStateDecorationsReeferRunMode",
    "DataCarrierReeferStateDecorationsReeferSetPointTemperatureMilliCZone1",
    "DataCarrierReeferStateDecorationsReeferSetPointTemperatureMilliCZone2",
    "DataCarrierReeferStateDecorationsReeferSetPointTemperatureMilliCZone3",
    "DataCarrierReeferStateDecorationsReeferStateZone1",
    "DataCarrierReeferStateDecorationsReeferStateZone2",
    "DataCarrierReeferStateDecorationsReeferStateZone3",
    "DataCarrierReeferStateDecorationsReeferSupplyAirTemperatureMilliCZone1",
    "DataCarrierReeferStateDecorationsReeferSupplyAirTemperatureMilliCZone2",
    "DataCarrierReeferStateDecorationsReeferSupplyAirTemperatureMilliCZone3",
    "DataGp",
    "DataGpDecorations",
    "DataGpDecorationsCarrierReeferState",
    "DataGpDecorationsGps",
    "DataGpDecorationsGpsReverseGeo",
    "DataGpDecorationsGpsOdometerMeters",
    "DataGpDecorationsReeferAlarms",
    "DataGpDecorationsReeferAlarmsAlarm",
    "DataGpDecorationsReeferAmbientAirTemperatureMilliC",
    "DataGpDecorationsReeferDoorStateZone1",
    "DataGpDecorationsReeferDoorStateZone2",
    "DataGpDecorationsReeferDoorStateZone3",
    "DataGpDecorationsReeferFuelPercent",
    "DataGpDecorationsReeferObdEngineSeconds",
    "DataGpDecorationsReeferReturnAirTemperatureMilliCZone1",
    "DataGpDecorationsReeferReturnAirTemperatureMilliCZone2",
    "DataGpDecorationsReeferReturnAirTemperatureMilliCZone3",
    "DataGpDecorationsReeferRunMode",
    "DataGpDecorationsReeferSetPointTemperatureMilliCZone1",
    "DataGpDecorationsReeferSetPointTemperatureMilliCZone2",
    "DataGpDecorationsReeferSetPointTemperatureMilliCZone3",
    "DataGpDecorationsReeferStateZone1",
    "DataGpDecorationsReeferStateZone2",
    "DataGpDecorationsReeferStateZone3",
    "DataGpDecorationsReeferSupplyAirTemperatureMilliCZone1",
    "DataGpDecorationsReeferSupplyAirTemperatureMilliCZone2",
    "DataGpDecorationsReeferSupplyAirTemperatureMilliCZone3",
    "DataGpReverseGeo",
    "DataGpsOdometerMeter",
    "DataGpsOdometerMeterDecorations",
    "DataGpsOdometerMeterDecorationsCarrierReeferState",
    "DataGpsOdometerMeterDecorationsGps",
    "DataGpsOdometerMeterDecorationsGpsReverseGeo",
    "DataGpsOdometerMeterDecorationsGpsOdometerMeters",
    "DataGpsOdometerMeterDecorationsReeferAlarms",
    "DataGpsOdometerMeterDecorationsReeferAlarmsAlarm",
    "DataGpsOdometerMeterDecorationsReeferAmbientAirTemperatureMilliC",
    "DataGpsOdometerMeterDecorationsReeferDoorStateZone1",
    "DataGpsOdometerMeterDecorationsReeferDoorStateZone2",
    "DataGpsOdometerMeterDecorationsReeferDoorStateZone3",
    "DataGpsOdometerMeterDecorationsReeferFuelPercent",
    "DataGpsOdometerMeterDecorationsReeferObdEngineSeconds",
    "DataGpsOdometerMeterDecorationsReeferReturnAirTemperatureMilliCZone1",
    "DataGpsOdometerMeterDecorationsReeferReturnAirTemperatureMilliCZone2",
    "DataGpsOdometerMeterDecorationsReeferReturnAirTemperatureMilliCZone3",
    "DataGpsOdometerMeterDecorationsReeferRunMode",
    "DataGpsOdometerMeterDecorationsReeferSetPointTemperatureMilliCZone1",
    "DataGpsOdometerMeterDecorationsReeferSetPointTemperatureMilliCZone2",
    "DataGpsOdometerMeterDecorationsReeferSetPointTemperatureMilliCZone3",
    "DataGpsOdometerMeterDecorationsReeferStateZone1",
    "DataGpsOdometerMeterDecorationsReeferStateZone2",
    "DataGpsOdometerMeterDecorationsReeferStateZone3",
    "DataGpsOdometerMeterDecorationsReeferSupplyAirTemperatureMilliCZone1",
    "DataGpsOdometerMeterDecorationsReeferSupplyAirTemperatureMilliCZone2",
    "DataGpsOdometerMeterDecorationsReeferSupplyAirTemperatureMilliCZone3",
    "DataReeferAlarm",
    "DataReeferAlarmAlarm",
    "DataReeferAlarmDecorations",
    "DataReeferAlarmDecorationsCarrierReeferState",
    "DataReeferAlarmDecorationsGps",
    "DataReeferAlarmDecorationsGpsReverseGeo",
    "DataReeferAlarmDecorationsGpsOdometerMeters",
    "DataReeferAlarmDecorationsReeferAlarms",
    "DataReeferAlarmDecorationsReeferAlarmsAlarm",
    "DataReeferAlarmDecorationsReeferAmbientAirTemperatureMilliC",
    "DataReeferAlarmDecorationsReeferDoorStateZone1",
    "DataReeferAlarmDecorationsReeferDoorStateZone2",
    "DataReeferAlarmDecorationsReeferDoorStateZone3",
    "DataReeferAlarmDecorationsReeferFuelPercent",
    "DataReeferAlarmDecorationsReeferObdEngineSeconds",
    "DataReeferAlarmDecorationsReeferReturnAirTemperatureMilliCZone1",
    "DataReeferAlarmDecorationsReeferReturnAirTemperatureMilliCZone2",
    "DataReeferAlarmDecorationsReeferReturnAirTemperatureMilliCZone3",
    "DataReeferAlarmDecorationsReeferRunMode",
    "DataReeferAlarmDecorationsReeferSetPointTemperatureMilliCZone1",
    "DataReeferAlarmDecorationsReeferSetPointTemperatureMilliCZone2",
    "DataReeferAlarmDecorationsReeferSetPointTemperatureMilliCZone3",
    "DataReeferAlarmDecorationsReeferStateZone1",
    "DataReeferAlarmDecorationsReeferStateZone2",
    "DataReeferAlarmDecorationsReeferStateZone3",
    "DataReeferAlarmDecorationsReeferSupplyAirTemperatureMilliCZone1",
    "DataReeferAlarmDecorationsReeferSupplyAirTemperatureMilliCZone2",
    "DataReeferAlarmDecorationsReeferSupplyAirTemperatureMilliCZone3",
    "DataReeferAmbientAirTemperatureMilliC",
    "DataReeferAmbientAirTemperatureMilliCDecorations",
    "DataReeferAmbientAirTemperatureMilliCDecorationsCarrierReeferState",
    "DataReeferAmbientAirTemperatureMilliCDecorationsGps",
    "DataReeferAmbientAirTemperatureMilliCDecorationsGpsReverseGeo",
    "DataReeferAmbientAirTemperatureMilliCDecorationsGpsOdometerMeters",
    "DataReeferAmbientAirTemperatureMilliCDecorationsReeferAlarms",
    "DataReeferAmbientAirTemperatureMilliCDecorationsReeferAlarmsAlarm",
    "DataReeferAmbientAirTemperatureMilliCDecorationsReeferAmbientAirTemperatureMilliC",
    "DataReeferAmbientAirTemperatureMilliCDecorationsReeferDoorStateZone1",
    "DataReeferAmbientAirTemperatureMilliCDecorationsReeferDoorStateZone2",
    "DataReeferAmbientAirTemperatureMilliCDecorationsReeferDoorStateZone3",
    "DataReeferAmbientAirTemperatureMilliCDecorationsReeferFuelPercent",
    "DataReeferAmbientAirTemperatureMilliCDecorationsReeferObdEngineSeconds",
    "DataReeferAmbientAirTemperatureMilliCDecorationsReeferReturnAirTemperatureMilliCZone1",
    "DataReeferAmbientAirTemperatureMilliCDecorationsReeferReturnAirTemperatureMilliCZone2",
    "DataReeferAmbientAirTemperatureMilliCDecorationsReeferReturnAirTemperatureMilliCZone3",
    "DataReeferAmbientAirTemperatureMilliCDecorationsReeferRunMode",
    "DataReeferAmbientAirTemperatureMilliCDecorationsReeferSetPointTemperatureMilliCZone1",
    "DataReeferAmbientAirTemperatureMilliCDecorationsReeferSetPointTemperatureMilliCZone2",
    "DataReeferAmbientAirTemperatureMilliCDecorationsReeferSetPointTemperatureMilliCZone3",
    "DataReeferAmbientAirTemperatureMilliCDecorationsReeferStateZone1",
    "DataReeferAmbientAirTemperatureMilliCDecorationsReeferStateZone2",
    "DataReeferAmbientAirTemperatureMilliCDecorationsReeferStateZone3",
    "DataReeferAmbientAirTemperatureMilliCDecorationsReeferSupplyAirTemperatureMilliCZone1",
    "DataReeferAmbientAirTemperatureMilliCDecorationsReeferSupplyAirTemperatureMilliCZone2",
    "DataReeferAmbientAirTemperatureMilliCDecorationsReeferSupplyAirTemperatureMilliCZone3",
    "DataReeferDoorStateZone1",
    "DataReeferDoorStateZone1Decorations",
    "DataReeferDoorStateZone1DecorationsCarrierReeferState",
    "DataReeferDoorStateZone1DecorationsGps",
    "DataReeferDoorStateZone1DecorationsGpsReverseGeo",
    "DataReeferDoorStateZone1DecorationsGpsOdometerMeters",
    "DataReeferDoorStateZone1DecorationsReeferAlarms",
    "DataReeferDoorStateZone1DecorationsReeferAlarmsAlarm",
    "DataReeferDoorStateZone1DecorationsReeferAmbientAirTemperatureMilliC",
    "DataReeferDoorStateZone1DecorationsReeferDoorStateZone1",
    "DataReeferDoorStateZone1DecorationsReeferDoorStateZone2",
    "DataReeferDoorStateZone1DecorationsReeferDoorStateZone3",
    "DataReeferDoorStateZone1DecorationsReeferFuelPercent",
    "DataReeferDoorStateZone1DecorationsReeferObdEngineSeconds",
    "DataReeferDoorStateZone1DecorationsReeferReturnAirTemperatureMilliCZone1",
    "DataReeferDoorStateZone1DecorationsReeferReturnAirTemperatureMilliCZone2",
    "DataReeferDoorStateZone1DecorationsReeferReturnAirTemperatureMilliCZone3",
    "DataReeferDoorStateZone1DecorationsReeferRunMode",
    "DataReeferDoorStateZone1DecorationsReeferSetPointTemperatureMilliCZone1",
    "DataReeferDoorStateZone1DecorationsReeferSetPointTemperatureMilliCZone2",
    "DataReeferDoorStateZone1DecorationsReeferSetPointTemperatureMilliCZone3",
    "DataReeferDoorStateZone1DecorationsReeferStateZone1",
    "DataReeferDoorStateZone1DecorationsReeferStateZone2",
    "DataReeferDoorStateZone1DecorationsReeferStateZone3",
    "DataReeferDoorStateZone1DecorationsReeferSupplyAirTemperatureMilliCZone1",
    "DataReeferDoorStateZone1DecorationsReeferSupplyAirTemperatureMilliCZone2",
    "DataReeferDoorStateZone1DecorationsReeferSupplyAirTemperatureMilliCZone3",
    "DataReeferDoorStateZone2",
    "DataReeferDoorStateZone2Decorations",
    "DataReeferDoorStateZone2DecorationsCarrierReeferState",
    "DataReeferDoorStateZone2DecorationsGps",
    "DataReeferDoorStateZone2DecorationsGpsReverseGeo",
    "DataReeferDoorStateZone2DecorationsGpsOdometerMeters",
    "DataReeferDoorStateZone2DecorationsReeferAlarms",
    "DataReeferDoorStateZone2DecorationsReeferAlarmsAlarm",
    "DataReeferDoorStateZone2DecorationsReeferAmbientAirTemperatureMilliC",
    "DataReeferDoorStateZone2DecorationsReeferDoorStateZone1",
    "DataReeferDoorStateZone2DecorationsReeferDoorStateZone2",
    "DataReeferDoorStateZone2DecorationsReeferDoorStateZone3",
    "DataReeferDoorStateZone2DecorationsReeferFuelPercent",
    "DataReeferDoorStateZone2DecorationsReeferObdEngineSeconds",
    "DataReeferDoorStateZone2DecorationsReeferReturnAirTemperatureMilliCZone1",
    "DataReeferDoorStateZone2DecorationsReeferReturnAirTemperatureMilliCZone2",
    "DataReeferDoorStateZone2DecorationsReeferReturnAirTemperatureMilliCZone3",
    "DataReeferDoorStateZone2DecorationsReeferRunMode",
    "DataReeferDoorStateZone2DecorationsReeferSetPointTemperatureMilliCZone1",
    "DataReeferDoorStateZone2DecorationsReeferSetPointTemperatureMilliCZone2",
    "DataReeferDoorStateZone2DecorationsReeferSetPointTemperatureMilliCZone3",
    "DataReeferDoorStateZone2DecorationsReeferStateZone1",
    "DataReeferDoorStateZone2DecorationsReeferStateZone2",
    "DataReeferDoorStateZone2DecorationsReeferStateZone3",
    "DataReeferDoorStateZone2DecorationsReeferSupplyAirTemperatureMilliCZone1",
    "DataReeferDoorStateZone2DecorationsReeferSupplyAirTemperatureMilliCZone2",
    "DataReeferDoorStateZone2DecorationsReeferSupplyAirTemperatureMilliCZone3",
    "DataReeferDoorStateZone3",
    "DataReeferDoorStateZone3Decorations",
    "DataReeferDoorStateZone3DecorationsCarrierReeferState",
    "DataReeferDoorStateZone3DecorationsGps",
    "DataReeferDoorStateZone3DecorationsGpsReverseGeo",
    "DataReeferDoorStateZone3DecorationsGpsOdometerMeters",
    "DataReeferDoorStateZone3DecorationsReeferAlarms",
    "DataReeferDoorStateZone3DecorationsReeferAlarmsAlarm",
    "DataReeferDoorStateZone3DecorationsReeferAmbientAirTemperatureMilliC",
    "DataReeferDoorStateZone3DecorationsReeferDoorStateZone1",
    "DataReeferDoorStateZone3DecorationsReeferDoorStateZone2",
    "DataReeferDoorStateZone3DecorationsReeferDoorStateZone3",
    "DataReeferDoorStateZone3DecorationsReeferFuelPercent",
    "DataReeferDoorStateZone3DecorationsReeferObdEngineSeconds",
    "DataReeferDoorStateZone3DecorationsReeferReturnAirTemperatureMilliCZone1",
    "DataReeferDoorStateZone3DecorationsReeferReturnAirTemperatureMilliCZone2",
    "DataReeferDoorStateZone3DecorationsReeferReturnAirTemperatureMilliCZone3",
    "DataReeferDoorStateZone3DecorationsReeferRunMode",
    "DataReeferDoorStateZone3DecorationsReeferSetPointTemperatureMilliCZone1",
    "DataReeferDoorStateZone3DecorationsReeferSetPointTemperatureMilliCZone2",
    "DataReeferDoorStateZone3DecorationsReeferSetPointTemperatureMilliCZone3",
    "DataReeferDoorStateZone3DecorationsReeferStateZone1",
    "DataReeferDoorStateZone3DecorationsReeferStateZone2",
    "DataReeferDoorStateZone3DecorationsReeferStateZone3",
    "DataReeferDoorStateZone3DecorationsReeferSupplyAirTemperatureMilliCZone1",
    "DataReeferDoorStateZone3DecorationsReeferSupplyAirTemperatureMilliCZone2",
    "DataReeferDoorStateZone3DecorationsReeferSupplyAirTemperatureMilliCZone3",
    "DataReeferFuelPercent",
    "DataReeferFuelPercentDecorations",
    "DataReeferFuelPercentDecorationsCarrierReeferState",
    "DataReeferFuelPercentDecorationsGps",
    "DataReeferFuelPercentDecorationsGpsReverseGeo",
    "DataReeferFuelPercentDecorationsGpsOdometerMeters",
    "DataReeferFuelPercentDecorationsReeferAlarms",
    "DataReeferFuelPercentDecorationsReeferAlarmsAlarm",
    "DataReeferFuelPercentDecorationsReeferAmbientAirTemperatureMilliC",
    "DataReeferFuelPercentDecorationsReeferDoorStateZone1",
    "DataReeferFuelPercentDecorationsReeferDoorStateZone2",
    "DataReeferFuelPercentDecorationsReeferDoorStateZone3",
    "DataReeferFuelPercentDecorationsReeferFuelPercent",
    "DataReeferFuelPercentDecorationsReeferObdEngineSeconds",
    "DataReeferFuelPercentDecorationsReeferReturnAirTemperatureMilliCZone1",
    "DataReeferFuelPercentDecorationsReeferReturnAirTemperatureMilliCZone2",
    "DataReeferFuelPercentDecorationsReeferReturnAirTemperatureMilliCZone3",
    "DataReeferFuelPercentDecorationsReeferRunMode",
    "DataReeferFuelPercentDecorationsReeferSetPointTemperatureMilliCZone1",
    "DataReeferFuelPercentDecorationsReeferSetPointTemperatureMilliCZone2",
    "DataReeferFuelPercentDecorationsReeferSetPointTemperatureMilliCZone3",
    "DataReeferFuelPercentDecorationsReeferStateZone1",
    "DataReeferFuelPercentDecorationsReeferStateZone2",
    "DataReeferFuelPercentDecorationsReeferStateZone3",
    "DataReeferFuelPercentDecorationsReeferSupplyAirTemperatureMilliCZone1",
    "DataReeferFuelPercentDecorationsReeferSupplyAirTemperatureMilliCZone2",
    "DataReeferFuelPercentDecorationsReeferSupplyAirTemperatureMilliCZone3",
    "DataReeferObdEngineSecond",
    "DataReeferObdEngineSecondDecorations",
    "DataReeferObdEngineSecondDecorationsCarrierReeferState",
    "DataReeferObdEngineSecondDecorationsGps",
    "DataReeferObdEngineSecondDecorationsGpsReverseGeo",
    "DataReeferObdEngineSecondDecorationsGpsOdometerMeters",
    "DataReeferObdEngineSecondDecorationsReeferAlarms",
    "DataReeferObdEngineSecondDecorationsReeferAlarmsAlarm",
    "DataReeferObdEngineSecondDecorationsReeferAmbientAirTemperatureMilliC",
    "DataReeferObdEngineSecondDecorationsReeferDoorStateZone1",
    "DataReeferObdEngineSecondDecorationsReeferDoorStateZone2",
    "DataReeferObdEngineSecondDecorationsReeferDoorStateZone3",
    "DataReeferObdEngineSecondDecorationsReeferFuelPercent",
    "DataReeferObdEngineSecondDecorationsReeferObdEngineSeconds",
    "DataReeferObdEngineSecondDecorationsReeferReturnAirTemperatureMilliCZone1",
    "DataReeferObdEngineSecondDecorationsReeferReturnAirTemperatureMilliCZone2",
    "DataReeferObdEngineSecondDecorationsReeferReturnAirTemperatureMilliCZone3",
    "DataReeferObdEngineSecondDecorationsReeferRunMode",
    "DataReeferObdEngineSecondDecorationsReeferSetPointTemperatureMilliCZone1",
    "DataReeferObdEngineSecondDecorationsReeferSetPointTemperatureMilliCZone2",
    "DataReeferObdEngineSecondDecorationsReeferSetPointTemperatureMilliCZone3",
    "DataReeferObdEngineSecondDecorationsReeferStateZone1",
    "DataReeferObdEngineSecondDecorationsReeferStateZone2",
    "DataReeferObdEngineSecondDecorationsReeferStateZone3",
    "DataReeferObdEngineSecondDecorationsReeferSupplyAirTemperatureMilliCZone1",
    "DataReeferObdEngineSecondDecorationsReeferSupplyAirTemperatureMilliCZone2",
    "DataReeferObdEngineSecondDecorationsReeferSupplyAirTemperatureMilliCZone3",
    "DataReeferReturnAirTemperatureMilliCZone1",
    "DataReeferReturnAirTemperatureMilliCZone1Decorations",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsCarrierReeferState",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsGps",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsGpsReverseGeo",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsGpsOdometerMeters",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferAlarms",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferAlarmsAlarm",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferAmbientAirTemperatureMilliC",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferDoorStateZone1",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferDoorStateZone2",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferDoorStateZone3",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferFuelPercent",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferObdEngineSeconds",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone1",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone2",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone3",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferRunMode",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone1",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone2",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone3",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferStateZone1",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferStateZone2",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferStateZone3",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone1",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone2",
    "DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone3",
    "DataReeferReturnAirTemperatureMilliCZone2",
    "DataReeferReturnAirTemperatureMilliCZone2Decorations",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsCarrierReeferState",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsGps",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsGpsReverseGeo",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsGpsOdometerMeters",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferAlarms",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferAlarmsAlarm",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferAmbientAirTemperatureMilliC",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferDoorStateZone1",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferDoorStateZone2",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferDoorStateZone3",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferFuelPercent",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferObdEngineSeconds",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone1",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone2",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone3",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferRunMode",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone1",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone2",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone3",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferStateZone1",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferStateZone2",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferStateZone3",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone1",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone2",
    "DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone3",
    "DataReeferReturnAirTemperatureMilliCZone3",
    "DataReeferReturnAirTemperatureMilliCZone3Decorations",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsCarrierReeferState",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsGps",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsGpsReverseGeo",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsGpsOdometerMeters",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferAlarms",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferAlarmsAlarm",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferAmbientAirTemperatureMilliC",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferDoorStateZone1",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferDoorStateZone2",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferDoorStateZone3",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferFuelPercent",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferObdEngineSeconds",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone1",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone2",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone3",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferRunMode",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone1",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone2",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone3",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferStateZone1",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferStateZone2",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferStateZone3",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone1",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone2",
    "DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone3",
    "DataReeferRunMode",
    "DataReeferRunModeDecorations",
    "DataReeferRunModeDecorationsCarrierReeferState",
    "DataReeferRunModeDecorationsGps",
    "DataReeferRunModeDecorationsGpsReverseGeo",
    "DataReeferRunModeDecorationsGpsOdometerMeters",
    "DataReeferRunModeDecorationsReeferAlarms",
    "DataReeferRunModeDecorationsReeferAlarmsAlarm",
    "DataReeferRunModeDecorationsReeferAmbientAirTemperatureMilliC",
    "DataReeferRunModeDecorationsReeferDoorStateZone1",
    "DataReeferRunModeDecorationsReeferDoorStateZone2",
    "DataReeferRunModeDecorationsReeferDoorStateZone3",
    "DataReeferRunModeDecorationsReeferFuelPercent",
    "DataReeferRunModeDecorationsReeferObdEngineSeconds",
    "DataReeferRunModeDecorationsReeferReturnAirTemperatureMilliCZone1",
    "DataReeferRunModeDecorationsReeferReturnAirTemperatureMilliCZone2",
    "DataReeferRunModeDecorationsReeferReturnAirTemperatureMilliCZone3",
    "DataReeferRunModeDecorationsReeferRunMode",
    "DataReeferRunModeDecorationsReeferSetPointTemperatureMilliCZone1",
    "DataReeferRunModeDecorationsReeferSetPointTemperatureMilliCZone2",
    "DataReeferRunModeDecorationsReeferSetPointTemperatureMilliCZone3",
    "DataReeferRunModeDecorationsReeferStateZone1",
    "DataReeferRunModeDecorationsReeferStateZone2",
    "DataReeferRunModeDecorationsReeferStateZone3",
    "DataReeferRunModeDecorationsReeferSupplyAirTemperatureMilliCZone1",
    "DataReeferRunModeDecorationsReeferSupplyAirTemperatureMilliCZone2",
    "DataReeferRunModeDecorationsReeferSupplyAirTemperatureMilliCZone3",
    "DataReeferSetPointTemperatureMilliCZone1",
    "DataReeferSetPointTemperatureMilliCZone1Decorations",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsCarrierReeferState",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsGps",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsGpsReverseGeo",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsGpsOdometerMeters",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsReeferAlarms",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsReeferAlarmsAlarm",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsReeferAmbientAirTemperatureMilliC",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsReeferDoorStateZone1",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsReeferDoorStateZone2",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsReeferDoorStateZone3",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsReeferFuelPercent",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsReeferObdEngineSeconds",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone1",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone2",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone3",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsReeferRunMode",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone1",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone2",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone3",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsReeferStateZone1",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsReeferStateZone2",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsReeferStateZone3",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone1",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone2",
    "DataReeferSetPointTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone3",
    "DataReeferSetPointTemperatureMilliCZone2",
    "DataReeferSetPointTemperatureMilliCZone2Decorations",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsCarrierReeferState",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsGps",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsGpsReverseGeo",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsGpsOdometerMeters",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsReeferAlarms",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsReeferAlarmsAlarm",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsReeferAmbientAirTemperatureMilliC",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsReeferDoorStateZone1",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsReeferDoorStateZone2",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsReeferDoorStateZone3",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsReeferFuelPercent",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsReeferObdEngineSeconds",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone1",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone2",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone3",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsReeferRunMode",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone1",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone2",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone3",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsReeferStateZone1",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsReeferStateZone2",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsReeferStateZone3",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone1",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone2",
    "DataReeferSetPointTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone3",
    "DataReeferSetPointTemperatureMilliCZone3",
    "DataReeferSetPointTemperatureMilliCZone3Decorations",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsCarrierReeferState",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsGps",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsGpsReverseGeo",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsGpsOdometerMeters",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsReeferAlarms",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsReeferAlarmsAlarm",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsReeferAmbientAirTemperatureMilliC",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsReeferDoorStateZone1",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsReeferDoorStateZone2",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsReeferDoorStateZone3",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsReeferFuelPercent",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsReeferObdEngineSeconds",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone1",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone2",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone3",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsReeferRunMode",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone1",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone2",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone3",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsReeferStateZone1",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsReeferStateZone2",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsReeferStateZone3",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone1",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone2",
    "DataReeferSetPointTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone3",
    "DataReeferStateZone1",
    "DataReeferStateZone1Decorations",
    "DataReeferStateZone1DecorationsCarrierReeferState",
    "DataReeferStateZone1DecorationsGps",
    "DataReeferStateZone1DecorationsGpsReverseGeo",
    "DataReeferStateZone1DecorationsGpsOdometerMeters",
    "DataReeferStateZone1DecorationsReeferAlarms",
    "DataReeferStateZone1DecorationsReeferAlarmsAlarm",
    "DataReeferStateZone1DecorationsReeferAmbientAirTemperatureMilliC",
    "DataReeferStateZone1DecorationsReeferDoorStateZone1",
    "DataReeferStateZone1DecorationsReeferDoorStateZone2",
    "DataReeferStateZone1DecorationsReeferDoorStateZone3",
    "DataReeferStateZone1DecorationsReeferFuelPercent",
    "DataReeferStateZone1DecorationsReeferObdEngineSeconds",
    "DataReeferStateZone1DecorationsReeferReturnAirTemperatureMilliCZone1",
    "DataReeferStateZone1DecorationsReeferReturnAirTemperatureMilliCZone2",
    "DataReeferStateZone1DecorationsReeferReturnAirTemperatureMilliCZone3",
    "DataReeferStateZone1DecorationsReeferRunMode",
    "DataReeferStateZone1DecorationsReeferSetPointTemperatureMilliCZone1",
    "DataReeferStateZone1DecorationsReeferSetPointTemperatureMilliCZone2",
    "DataReeferStateZone1DecorationsReeferSetPointTemperatureMilliCZone3",
    "DataReeferStateZone1DecorationsReeferStateZone1",
    "DataReeferStateZone1DecorationsReeferStateZone2",
    "DataReeferStateZone1DecorationsReeferStateZone3",
    "DataReeferStateZone1DecorationsReeferSupplyAirTemperatureMilliCZone1",
    "DataReeferStateZone1DecorationsReeferSupplyAirTemperatureMilliCZone2",
    "DataReeferStateZone1DecorationsReeferSupplyAirTemperatureMilliCZone3",
    "DataReeferStateZone2",
    "DataReeferStateZone2Decorations",
    "DataReeferStateZone2DecorationsCarrierReeferState",
    "DataReeferStateZone2DecorationsGps",
    "DataReeferStateZone2DecorationsGpsReverseGeo",
    "DataReeferStateZone2DecorationsGpsOdometerMeters",
    "DataReeferStateZone2DecorationsReeferAlarms",
    "DataReeferStateZone2DecorationsReeferAlarmsAlarm",
    "DataReeferStateZone2DecorationsReeferAmbientAirTemperatureMilliC",
    "DataReeferStateZone2DecorationsReeferDoorStateZone1",
    "DataReeferStateZone2DecorationsReeferDoorStateZone2",
    "DataReeferStateZone2DecorationsReeferDoorStateZone3",
    "DataReeferStateZone2DecorationsReeferFuelPercent",
    "DataReeferStateZone2DecorationsReeferObdEngineSeconds",
    "DataReeferStateZone2DecorationsReeferReturnAirTemperatureMilliCZone1",
    "DataReeferStateZone2DecorationsReeferReturnAirTemperatureMilliCZone2",
    "DataReeferStateZone2DecorationsReeferReturnAirTemperatureMilliCZone3",
    "DataReeferStateZone2DecorationsReeferRunMode",
    "DataReeferStateZone2DecorationsReeferSetPointTemperatureMilliCZone1",
    "DataReeferStateZone2DecorationsReeferSetPointTemperatureMilliCZone2",
    "DataReeferStateZone2DecorationsReeferSetPointTemperatureMilliCZone3",
    "DataReeferStateZone2DecorationsReeferStateZone1",
    "DataReeferStateZone2DecorationsReeferStateZone2",
    "DataReeferStateZone2DecorationsReeferStateZone3",
    "DataReeferStateZone2DecorationsReeferSupplyAirTemperatureMilliCZone1",
    "DataReeferStateZone2DecorationsReeferSupplyAirTemperatureMilliCZone2",
    "DataReeferStateZone2DecorationsReeferSupplyAirTemperatureMilliCZone3",
    "DataReeferStateZone3",
    "DataReeferStateZone3Decorations",
    "DataReeferStateZone3DecorationsCarrierReeferState",
    "DataReeferStateZone3DecorationsGps",
    "DataReeferStateZone3DecorationsGpsReverseGeo",
    "DataReeferStateZone3DecorationsGpsOdometerMeters",
    "DataReeferStateZone3DecorationsReeferAlarms",
    "DataReeferStateZone3DecorationsReeferAlarmsAlarm",
    "DataReeferStateZone3DecorationsReeferAmbientAirTemperatureMilliC",
    "DataReeferStateZone3DecorationsReeferDoorStateZone1",
    "DataReeferStateZone3DecorationsReeferDoorStateZone2",
    "DataReeferStateZone3DecorationsReeferDoorStateZone3",
    "DataReeferStateZone3DecorationsReeferFuelPercent",
    "DataReeferStateZone3DecorationsReeferObdEngineSeconds",
    "DataReeferStateZone3DecorationsReeferReturnAirTemperatureMilliCZone1",
    "DataReeferStateZone3DecorationsReeferReturnAirTemperatureMilliCZone2",
    "DataReeferStateZone3DecorationsReeferReturnAirTemperatureMilliCZone3",
    "DataReeferStateZone3DecorationsReeferRunMode",
    "DataReeferStateZone3DecorationsReeferSetPointTemperatureMilliCZone1",
    "DataReeferStateZone3DecorationsReeferSetPointTemperatureMilliCZone2",
    "DataReeferStateZone3DecorationsReeferSetPointTemperatureMilliCZone3",
    "DataReeferStateZone3DecorationsReeferStateZone1",
    "DataReeferStateZone3DecorationsReeferStateZone2",
    "DataReeferStateZone3DecorationsReeferStateZone3",
    "DataReeferStateZone3DecorationsReeferSupplyAirTemperatureMilliCZone1",
    "DataReeferStateZone3DecorationsReeferSupplyAirTemperatureMilliCZone2",
    "DataReeferStateZone3DecorationsReeferSupplyAirTemperatureMilliCZone3",
    "DataReeferSupplyAirTemperatureMilliCZone1",
    "DataReeferSupplyAirTemperatureMilliCZone1Decorations",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsCarrierReeferState",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsGps",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsGpsReverseGeo",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsGpsOdometerMeters",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferAlarms",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferAlarmsAlarm",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferAmbientAirTemperatureMilliC",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferDoorStateZone1",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferDoorStateZone2",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferDoorStateZone3",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferFuelPercent",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferObdEngineSeconds",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone1",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone2",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone3",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferRunMode",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone1",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone2",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone3",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferStateZone1",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferStateZone2",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferStateZone3",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone1",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone2",
    "DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone3",
    "DataReeferSupplyAirTemperatureMilliCZone2",
    "DataReeferSupplyAirTemperatureMilliCZone2Decorations",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsCarrierReeferState",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsGps",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsGpsReverseGeo",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsGpsOdometerMeters",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferAlarms",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferAlarmsAlarm",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferAmbientAirTemperatureMilliC",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferDoorStateZone1",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferDoorStateZone2",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferDoorStateZone3",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferFuelPercent",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferObdEngineSeconds",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone1",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone2",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone3",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferRunMode",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone1",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone2",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone3",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferStateZone1",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferStateZone2",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferStateZone3",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone1",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone2",
    "DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone3",
    "DataReeferSupplyAirTemperatureMilliCZone3",
    "DataReeferSupplyAirTemperatureMilliCZone3Decorations",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsCarrierReeferState",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsGps",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsGpsReverseGeo",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsGpsOdometerMeters",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferAlarms",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferAlarmsAlarm",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferAmbientAirTemperatureMilliC",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferDoorStateZone1",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferDoorStateZone2",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferDoorStateZone3",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferFuelPercent",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferObdEngineSeconds",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone1",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone2",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone3",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferRunMode",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone1",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone2",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone3",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferStateZone1",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferStateZone2",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferStateZone3",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone1",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone2",
    "DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone3",
    "Pagination",
]


class DataCarrierReeferStateDecorationsCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataCarrierReeferStateDecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataCarrierReeferStateDecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataCarrierReeferStateDecorationsGpsReverseGeo] = FieldInfo(alias="reverseGeo", default=None)
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataCarrierReeferStateDecorationsGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataCarrierReeferStateDecorationsReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataCarrierReeferStateDecorationsReeferAlarms(BaseModel):
    alarms: List[DataCarrierReeferStateDecorationsReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataCarrierReeferStateDecorationsReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataCarrierReeferStateDecorationsReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataCarrierReeferStateDecorationsReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataCarrierReeferStateDecorationsReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataCarrierReeferStateDecorationsReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataCarrierReeferStateDecorationsReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataCarrierReeferStateDecorationsReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataCarrierReeferStateDecorationsReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataCarrierReeferStateDecorationsReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataCarrierReeferStateDecorationsReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataCarrierReeferStateDecorationsReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataCarrierReeferStateDecorationsReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataCarrierReeferStateDecorationsReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataCarrierReeferStateDecorationsReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataCarrierReeferStateDecorationsReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataCarrierReeferStateDecorationsReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataCarrierReeferStateDecorationsReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataCarrierReeferStateDecorationsReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataCarrierReeferStateDecorationsReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataCarrierReeferStateDecorations(BaseModel):
    carrier_reefer_state: Optional[DataCarrierReeferStateDecorationsCarrierReeferState] = FieldInfo(
        alias="carrierReeferState", default=None
    )
    """Reefer state event."""

    gps: Optional[DataCarrierReeferStateDecorationsGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataCarrierReeferStateDecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataCarrierReeferStateDecorationsReeferAlarms] = FieldInfo(
        alias="reeferAlarms", default=None
    )
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[
        DataCarrierReeferStateDecorationsReeferAmbientAirTemperatureMilliC
    ] = FieldInfo(alias="reeferAmbientAirTemperatureMilliC", default=None)
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataCarrierReeferStateDecorationsReeferDoorStateZone1] = FieldInfo(
        alias="reeferDoorStateZone1", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataCarrierReeferStateDecorationsReeferDoorStateZone2] = FieldInfo(
        alias="reeferDoorStateZone2", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataCarrierReeferStateDecorationsReeferDoorStateZone3] = FieldInfo(
        alias="reeferDoorStateZone3", default=None
    )
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataCarrierReeferStateDecorationsReeferFuelPercent] = FieldInfo(
        alias="reeferFuelPercent", default=None
    )
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataCarrierReeferStateDecorationsReeferObdEngineSeconds] = FieldInfo(
        alias="reeferObdEngineSeconds", default=None
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[
        DataCarrierReeferStateDecorationsReeferReturnAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone1", default=None)
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[
        DataCarrierReeferStateDecorationsReeferReturnAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone2", default=None)
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[
        DataCarrierReeferStateDecorationsReeferReturnAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone3", default=None)
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataCarrierReeferStateDecorationsReeferRunMode] = FieldInfo(
        alias="reeferRunMode", default=None
    )
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[
        DataCarrierReeferStateDecorationsReeferSetPointTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone1", default=None)
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[
        DataCarrierReeferStateDecorationsReeferSetPointTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone2", default=None)
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[
        DataCarrierReeferStateDecorationsReeferSetPointTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone3", default=None)
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataCarrierReeferStateDecorationsReeferStateZone1] = FieldInfo(
        alias="reeferStateZone1", default=None
    )
    """Reefer state event."""

    reefer_state_zone2: Optional[DataCarrierReeferStateDecorationsReeferStateZone2] = FieldInfo(
        alias="reeferStateZone2", default=None
    )
    """Reefer state event."""

    reefer_state_zone3: Optional[DataCarrierReeferStateDecorationsReeferStateZone3] = FieldInfo(
        alias="reeferStateZone3", default=None
    )
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[
        DataCarrierReeferStateDecorationsReeferSupplyAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone1", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[
        DataCarrierReeferStateDecorationsReeferSupplyAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone2", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[
        DataCarrierReeferStateDecorationsReeferSupplyAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone3", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """


class DataCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    decorations: Optional[DataCarrierReeferStateDecorations] = None
    """Decorated values for the primary trailer stat datapoints."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataGpDecorationsCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataGpDecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataGpDecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataGpDecorationsGpsReverseGeo] = FieldInfo(alias="reverseGeo", default=None)
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataGpDecorationsGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataGpDecorationsReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataGpDecorationsReeferAlarms(BaseModel):
    alarms: List[DataGpDecorationsReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataGpDecorationsReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataGpDecorationsReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataGpDecorationsReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataGpDecorationsReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataGpDecorationsReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataGpDecorationsReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataGpDecorationsReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataGpDecorationsReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataGpDecorationsReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataGpDecorationsReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataGpDecorationsReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataGpDecorationsReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataGpDecorationsReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataGpDecorationsReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataGpDecorationsReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataGpDecorationsReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataGpDecorationsReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataGpDecorationsReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataGpDecorationsReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataGpDecorations(BaseModel):
    carrier_reefer_state: Optional[DataGpDecorationsCarrierReeferState] = FieldInfo(
        alias="carrierReeferState", default=None
    )
    """Reefer state event."""

    gps: Optional[DataGpDecorationsGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataGpDecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataGpDecorationsReeferAlarms] = FieldInfo(alias="reeferAlarms", default=None)
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[DataGpDecorationsReeferAmbientAirTemperatureMilliC] = FieldInfo(
        alias="reeferAmbientAirTemperatureMilliC", default=None
    )
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataGpDecorationsReeferDoorStateZone1] = FieldInfo(
        alias="reeferDoorStateZone1", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataGpDecorationsReeferDoorStateZone2] = FieldInfo(
        alias="reeferDoorStateZone2", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataGpDecorationsReeferDoorStateZone3] = FieldInfo(
        alias="reeferDoorStateZone3", default=None
    )
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataGpDecorationsReeferFuelPercent] = FieldInfo(
        alias="reeferFuelPercent", default=None
    )
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataGpDecorationsReeferObdEngineSeconds] = FieldInfo(
        alias="reeferObdEngineSeconds", default=None
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[DataGpDecorationsReeferReturnAirTemperatureMilliCZone1] = (
        FieldInfo(alias="reeferReturnAirTemperatureMilliCZone1", default=None)
    )
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[DataGpDecorationsReeferReturnAirTemperatureMilliCZone2] = (
        FieldInfo(alias="reeferReturnAirTemperatureMilliCZone2", default=None)
    )
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[DataGpDecorationsReeferReturnAirTemperatureMilliCZone3] = (
        FieldInfo(alias="reeferReturnAirTemperatureMilliCZone3", default=None)
    )
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataGpDecorationsReeferRunMode] = FieldInfo(alias="reeferRunMode", default=None)
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[DataGpDecorationsReeferSetPointTemperatureMilliCZone1] = (
        FieldInfo(alias="reeferSetPointTemperatureMilliCZone1", default=None)
    )
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[DataGpDecorationsReeferSetPointTemperatureMilliCZone2] = (
        FieldInfo(alias="reeferSetPointTemperatureMilliCZone2", default=None)
    )
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[DataGpDecorationsReeferSetPointTemperatureMilliCZone3] = (
        FieldInfo(alias="reeferSetPointTemperatureMilliCZone3", default=None)
    )
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataGpDecorationsReeferStateZone1] = FieldInfo(alias="reeferStateZone1", default=None)
    """Reefer state event."""

    reefer_state_zone2: Optional[DataGpDecorationsReeferStateZone2] = FieldInfo(alias="reeferStateZone2", default=None)
    """Reefer state event."""

    reefer_state_zone3: Optional[DataGpDecorationsReeferStateZone3] = FieldInfo(alias="reeferStateZone3", default=None)
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[DataGpDecorationsReeferSupplyAirTemperatureMilliCZone1] = (
        FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone1", default=None)
    )
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[DataGpDecorationsReeferSupplyAirTemperatureMilliCZone2] = (
        FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone2", default=None)
    )
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[DataGpDecorationsReeferSupplyAirTemperatureMilliCZone3] = (
        FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone3", default=None)
    )
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """


class DataGpReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataGp(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    decorations: Optional[DataGpDecorations] = None
    """Decorated values for the primary trailer stat datapoints."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataGpReverseGeo] = FieldInfo(alias="reverseGeo", default=None)
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataGpsOdometerMeterDecorationsCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataGpsOdometerMeterDecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataGpsOdometerMeterDecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataGpsOdometerMeterDecorationsGpsReverseGeo] = FieldInfo(alias="reverseGeo", default=None)
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataGpsOdometerMeterDecorationsGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataGpsOdometerMeterDecorationsReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataGpsOdometerMeterDecorationsReeferAlarms(BaseModel):
    alarms: List[DataGpsOdometerMeterDecorationsReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataGpsOdometerMeterDecorationsReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataGpsOdometerMeterDecorationsReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataGpsOdometerMeterDecorationsReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataGpsOdometerMeterDecorationsReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataGpsOdometerMeterDecorationsReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataGpsOdometerMeterDecorationsReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataGpsOdometerMeterDecorationsReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataGpsOdometerMeterDecorationsReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataGpsOdometerMeterDecorationsReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataGpsOdometerMeterDecorationsReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataGpsOdometerMeterDecorationsReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataGpsOdometerMeterDecorationsReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataGpsOdometerMeterDecorationsReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataGpsOdometerMeterDecorationsReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataGpsOdometerMeterDecorationsReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataGpsOdometerMeterDecorationsReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataGpsOdometerMeterDecorationsReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataGpsOdometerMeterDecorationsReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataGpsOdometerMeterDecorationsReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataGpsOdometerMeterDecorations(BaseModel):
    carrier_reefer_state: Optional[DataGpsOdometerMeterDecorationsCarrierReeferState] = FieldInfo(
        alias="carrierReeferState", default=None
    )
    """Reefer state event."""

    gps: Optional[DataGpsOdometerMeterDecorationsGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataGpsOdometerMeterDecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataGpsOdometerMeterDecorationsReeferAlarms] = FieldInfo(alias="reeferAlarms", default=None)
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[
        DataGpsOdometerMeterDecorationsReeferAmbientAirTemperatureMilliC
    ] = FieldInfo(alias="reeferAmbientAirTemperatureMilliC", default=None)
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataGpsOdometerMeterDecorationsReeferDoorStateZone1] = FieldInfo(
        alias="reeferDoorStateZone1", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataGpsOdometerMeterDecorationsReeferDoorStateZone2] = FieldInfo(
        alias="reeferDoorStateZone2", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataGpsOdometerMeterDecorationsReeferDoorStateZone3] = FieldInfo(
        alias="reeferDoorStateZone3", default=None
    )
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataGpsOdometerMeterDecorationsReeferFuelPercent] = FieldInfo(
        alias="reeferFuelPercent", default=None
    )
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataGpsOdometerMeterDecorationsReeferObdEngineSeconds] = FieldInfo(
        alias="reeferObdEngineSeconds", default=None
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[
        DataGpsOdometerMeterDecorationsReeferReturnAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone1", default=None)
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[
        DataGpsOdometerMeterDecorationsReeferReturnAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone2", default=None)
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[
        DataGpsOdometerMeterDecorationsReeferReturnAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone3", default=None)
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataGpsOdometerMeterDecorationsReeferRunMode] = FieldInfo(
        alias="reeferRunMode", default=None
    )
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[
        DataGpsOdometerMeterDecorationsReeferSetPointTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone1", default=None)
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[
        DataGpsOdometerMeterDecorationsReeferSetPointTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone2", default=None)
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[
        DataGpsOdometerMeterDecorationsReeferSetPointTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone3", default=None)
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataGpsOdometerMeterDecorationsReeferStateZone1] = FieldInfo(
        alias="reeferStateZone1", default=None
    )
    """Reefer state event."""

    reefer_state_zone2: Optional[DataGpsOdometerMeterDecorationsReeferStateZone2] = FieldInfo(
        alias="reeferStateZone2", default=None
    )
    """Reefer state event."""

    reefer_state_zone3: Optional[DataGpsOdometerMeterDecorationsReeferStateZone3] = FieldInfo(
        alias="reeferStateZone3", default=None
    )
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[
        DataGpsOdometerMeterDecorationsReeferSupplyAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone1", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[
        DataGpsOdometerMeterDecorationsReeferSupplyAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone2", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[
        DataGpsOdometerMeterDecorationsReeferSupplyAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone3", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """


class DataGpsOdometerMeter(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """

    decorations: Optional[DataGpsOdometerMeterDecorations] = None
    """Decorated values for the primary trailer stat datapoints."""


class DataReeferAlarmAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataReeferAlarmDecorationsCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataReeferAlarmDecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataReeferAlarmDecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataReeferAlarmDecorationsGpsReverseGeo] = FieldInfo(alias="reverseGeo", default=None)
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataReeferAlarmDecorationsGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataReeferAlarmDecorationsReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataReeferAlarmDecorationsReeferAlarms(BaseModel):
    alarms: List[DataReeferAlarmDecorationsReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataReeferAlarmDecorationsReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataReeferAlarmDecorationsReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferAlarmDecorationsReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferAlarmDecorationsReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferAlarmDecorationsReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataReeferAlarmDecorationsReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataReeferAlarmDecorationsReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferAlarmDecorationsReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferAlarmDecorationsReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferAlarmDecorationsReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataReeferAlarmDecorationsReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferAlarmDecorationsReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferAlarmDecorationsReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferAlarmDecorationsReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataReeferAlarmDecorationsReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataReeferAlarmDecorationsReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataReeferAlarmDecorationsReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferAlarmDecorationsReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferAlarmDecorationsReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferAlarmDecorations(BaseModel):
    carrier_reefer_state: Optional[DataReeferAlarmDecorationsCarrierReeferState] = FieldInfo(
        alias="carrierReeferState", default=None
    )
    """Reefer state event."""

    gps: Optional[DataReeferAlarmDecorationsGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataReeferAlarmDecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataReeferAlarmDecorationsReeferAlarms] = FieldInfo(alias="reeferAlarms", default=None)
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[DataReeferAlarmDecorationsReeferAmbientAirTemperatureMilliC] = (
        FieldInfo(alias="reeferAmbientAirTemperatureMilliC", default=None)
    )
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataReeferAlarmDecorationsReeferDoorStateZone1] = FieldInfo(
        alias="reeferDoorStateZone1", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataReeferAlarmDecorationsReeferDoorStateZone2] = FieldInfo(
        alias="reeferDoorStateZone2", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataReeferAlarmDecorationsReeferDoorStateZone3] = FieldInfo(
        alias="reeferDoorStateZone3", default=None
    )
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataReeferAlarmDecorationsReeferFuelPercent] = FieldInfo(
        alias="reeferFuelPercent", default=None
    )
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataReeferAlarmDecorationsReeferObdEngineSeconds] = FieldInfo(
        alias="reeferObdEngineSeconds", default=None
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[
        DataReeferAlarmDecorationsReeferReturnAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone1", default=None)
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[
        DataReeferAlarmDecorationsReeferReturnAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone2", default=None)
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[
        DataReeferAlarmDecorationsReeferReturnAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone3", default=None)
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataReeferAlarmDecorationsReeferRunMode] = FieldInfo(alias="reeferRunMode", default=None)
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[
        DataReeferAlarmDecorationsReeferSetPointTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone1", default=None)
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[
        DataReeferAlarmDecorationsReeferSetPointTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone2", default=None)
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[
        DataReeferAlarmDecorationsReeferSetPointTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone3", default=None)
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataReeferAlarmDecorationsReeferStateZone1] = FieldInfo(
        alias="reeferStateZone1", default=None
    )
    """Reefer state event."""

    reefer_state_zone2: Optional[DataReeferAlarmDecorationsReeferStateZone2] = FieldInfo(
        alias="reeferStateZone2", default=None
    )
    """Reefer state event."""

    reefer_state_zone3: Optional[DataReeferAlarmDecorationsReeferStateZone3] = FieldInfo(
        alias="reeferStateZone3", default=None
    )
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[
        DataReeferAlarmDecorationsReeferSupplyAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone1", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[
        DataReeferAlarmDecorationsReeferSupplyAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone2", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[
        DataReeferAlarmDecorationsReeferSupplyAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone3", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """


class DataReeferAlarm(BaseModel):
    alarms: List[DataReeferAlarmAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    decorations: Optional[DataReeferAlarmDecorations] = None
    """Decorated values for the primary trailer stat datapoints."""


class DataReeferAmbientAirTemperatureMilliCDecorationsCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataReeferAmbientAirTemperatureMilliCDecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataReeferAmbientAirTemperatureMilliCDecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataReeferAmbientAirTemperatureMilliCDecorationsGpsReverseGeo] = FieldInfo(
        alias="reverseGeo", default=None
    )
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataReeferAmbientAirTemperatureMilliCDecorationsGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataReeferAmbientAirTemperatureMilliCDecorationsReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataReeferAmbientAirTemperatureMilliCDecorationsReeferAlarms(BaseModel):
    alarms: List[DataReeferAmbientAirTemperatureMilliCDecorationsReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataReeferAmbientAirTemperatureMilliCDecorationsReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataReeferAmbientAirTemperatureMilliCDecorationsReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferAmbientAirTemperatureMilliCDecorationsReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferAmbientAirTemperatureMilliCDecorationsReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferAmbientAirTemperatureMilliCDecorationsReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataReeferAmbientAirTemperatureMilliCDecorationsReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataReeferAmbientAirTemperatureMilliCDecorationsReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferAmbientAirTemperatureMilliCDecorationsReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferAmbientAirTemperatureMilliCDecorationsReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferAmbientAirTemperatureMilliCDecorationsReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataReeferAmbientAirTemperatureMilliCDecorationsReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferAmbientAirTemperatureMilliCDecorationsReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferAmbientAirTemperatureMilliCDecorationsReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferAmbientAirTemperatureMilliCDecorationsReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataReeferAmbientAirTemperatureMilliCDecorationsReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataReeferAmbientAirTemperatureMilliCDecorationsReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataReeferAmbientAirTemperatureMilliCDecorationsReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferAmbientAirTemperatureMilliCDecorationsReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferAmbientAirTemperatureMilliCDecorationsReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferAmbientAirTemperatureMilliCDecorations(BaseModel):
    carrier_reefer_state: Optional[DataReeferAmbientAirTemperatureMilliCDecorationsCarrierReeferState] = FieldInfo(
        alias="carrierReeferState", default=None
    )
    """Reefer state event."""

    gps: Optional[DataReeferAmbientAirTemperatureMilliCDecorationsGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataReeferAmbientAirTemperatureMilliCDecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataReeferAmbientAirTemperatureMilliCDecorationsReeferAlarms] = FieldInfo(
        alias="reeferAlarms", default=None
    )
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[
        DataReeferAmbientAirTemperatureMilliCDecorationsReeferAmbientAirTemperatureMilliC
    ] = FieldInfo(alias="reeferAmbientAirTemperatureMilliC", default=None)
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataReeferAmbientAirTemperatureMilliCDecorationsReeferDoorStateZone1] = FieldInfo(
        alias="reeferDoorStateZone1", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataReeferAmbientAirTemperatureMilliCDecorationsReeferDoorStateZone2] = FieldInfo(
        alias="reeferDoorStateZone2", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataReeferAmbientAirTemperatureMilliCDecorationsReeferDoorStateZone3] = FieldInfo(
        alias="reeferDoorStateZone3", default=None
    )
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataReeferAmbientAirTemperatureMilliCDecorationsReeferFuelPercent] = FieldInfo(
        alias="reeferFuelPercent", default=None
    )
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataReeferAmbientAirTemperatureMilliCDecorationsReeferObdEngineSeconds] = (
        FieldInfo(alias="reeferObdEngineSeconds", default=None)
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[
        DataReeferAmbientAirTemperatureMilliCDecorationsReeferReturnAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone1", default=None)
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[
        DataReeferAmbientAirTemperatureMilliCDecorationsReeferReturnAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone2", default=None)
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[
        DataReeferAmbientAirTemperatureMilliCDecorationsReeferReturnAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone3", default=None)
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataReeferAmbientAirTemperatureMilliCDecorationsReeferRunMode] = FieldInfo(
        alias="reeferRunMode", default=None
    )
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[
        DataReeferAmbientAirTemperatureMilliCDecorationsReeferSetPointTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone1", default=None)
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[
        DataReeferAmbientAirTemperatureMilliCDecorationsReeferSetPointTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone2", default=None)
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[
        DataReeferAmbientAirTemperatureMilliCDecorationsReeferSetPointTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone3", default=None)
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataReeferAmbientAirTemperatureMilliCDecorationsReeferStateZone1] = FieldInfo(
        alias="reeferStateZone1", default=None
    )
    """Reefer state event."""

    reefer_state_zone2: Optional[DataReeferAmbientAirTemperatureMilliCDecorationsReeferStateZone2] = FieldInfo(
        alias="reeferStateZone2", default=None
    )
    """Reefer state event."""

    reefer_state_zone3: Optional[DataReeferAmbientAirTemperatureMilliCDecorationsReeferStateZone3] = FieldInfo(
        alias="reeferStateZone3", default=None
    )
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[
        DataReeferAmbientAirTemperatureMilliCDecorationsReeferSupplyAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone1", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[
        DataReeferAmbientAirTemperatureMilliCDecorationsReeferSupplyAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone2", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[
        DataReeferAmbientAirTemperatureMilliCDecorationsReeferSupplyAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone3", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """


class DataReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""

    decorations: Optional[DataReeferAmbientAirTemperatureMilliCDecorations] = None
    """Decorated values for the primary trailer stat datapoints."""


class DataReeferDoorStateZone1DecorationsCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataReeferDoorStateZone1DecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataReeferDoorStateZone1DecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataReeferDoorStateZone1DecorationsGpsReverseGeo] = FieldInfo(
        alias="reverseGeo", default=None
    )
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataReeferDoorStateZone1DecorationsGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataReeferDoorStateZone1DecorationsReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataReeferDoorStateZone1DecorationsReeferAlarms(BaseModel):
    alarms: List[DataReeferDoorStateZone1DecorationsReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataReeferDoorStateZone1DecorationsReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataReeferDoorStateZone1DecorationsReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferDoorStateZone1DecorationsReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferDoorStateZone1DecorationsReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferDoorStateZone1DecorationsReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataReeferDoorStateZone1DecorationsReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataReeferDoorStateZone1DecorationsReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone1DecorationsReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone1DecorationsReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone1DecorationsReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataReeferDoorStateZone1DecorationsReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone1DecorationsReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone1DecorationsReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone1DecorationsReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataReeferDoorStateZone1DecorationsReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataReeferDoorStateZone1DecorationsReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataReeferDoorStateZone1DecorationsReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone1DecorationsReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone1DecorationsReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone1Decorations(BaseModel):
    carrier_reefer_state: Optional[DataReeferDoorStateZone1DecorationsCarrierReeferState] = FieldInfo(
        alias="carrierReeferState", default=None
    )
    """Reefer state event."""

    gps: Optional[DataReeferDoorStateZone1DecorationsGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataReeferDoorStateZone1DecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataReeferDoorStateZone1DecorationsReeferAlarms] = FieldInfo(
        alias="reeferAlarms", default=None
    )
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[
        DataReeferDoorStateZone1DecorationsReeferAmbientAirTemperatureMilliC
    ] = FieldInfo(alias="reeferAmbientAirTemperatureMilliC", default=None)
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataReeferDoorStateZone1DecorationsReeferDoorStateZone1] = FieldInfo(
        alias="reeferDoorStateZone1", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataReeferDoorStateZone1DecorationsReeferDoorStateZone2] = FieldInfo(
        alias="reeferDoorStateZone2", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataReeferDoorStateZone1DecorationsReeferDoorStateZone3] = FieldInfo(
        alias="reeferDoorStateZone3", default=None
    )
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataReeferDoorStateZone1DecorationsReeferFuelPercent] = FieldInfo(
        alias="reeferFuelPercent", default=None
    )
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataReeferDoorStateZone1DecorationsReeferObdEngineSeconds] = FieldInfo(
        alias="reeferObdEngineSeconds", default=None
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[
        DataReeferDoorStateZone1DecorationsReeferReturnAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone1", default=None)
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[
        DataReeferDoorStateZone1DecorationsReeferReturnAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone2", default=None)
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[
        DataReeferDoorStateZone1DecorationsReeferReturnAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone3", default=None)
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataReeferDoorStateZone1DecorationsReeferRunMode] = FieldInfo(
        alias="reeferRunMode", default=None
    )
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[
        DataReeferDoorStateZone1DecorationsReeferSetPointTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone1", default=None)
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[
        DataReeferDoorStateZone1DecorationsReeferSetPointTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone2", default=None)
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[
        DataReeferDoorStateZone1DecorationsReeferSetPointTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone3", default=None)
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataReeferDoorStateZone1DecorationsReeferStateZone1] = FieldInfo(
        alias="reeferStateZone1", default=None
    )
    """Reefer state event."""

    reefer_state_zone2: Optional[DataReeferDoorStateZone1DecorationsReeferStateZone2] = FieldInfo(
        alias="reeferStateZone2", default=None
    )
    """Reefer state event."""

    reefer_state_zone3: Optional[DataReeferDoorStateZone1DecorationsReeferStateZone3] = FieldInfo(
        alias="reeferStateZone3", default=None
    )
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[
        DataReeferDoorStateZone1DecorationsReeferSupplyAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone1", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[
        DataReeferDoorStateZone1DecorationsReeferSupplyAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone2", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[
        DataReeferDoorStateZone1DecorationsReeferSupplyAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone3", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """


class DataReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""

    decorations: Optional[DataReeferDoorStateZone1Decorations] = None
    """Decorated values for the primary trailer stat datapoints."""


class DataReeferDoorStateZone2DecorationsCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataReeferDoorStateZone2DecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataReeferDoorStateZone2DecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataReeferDoorStateZone2DecorationsGpsReverseGeo] = FieldInfo(
        alias="reverseGeo", default=None
    )
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataReeferDoorStateZone2DecorationsGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataReeferDoorStateZone2DecorationsReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataReeferDoorStateZone2DecorationsReeferAlarms(BaseModel):
    alarms: List[DataReeferDoorStateZone2DecorationsReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataReeferDoorStateZone2DecorationsReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataReeferDoorStateZone2DecorationsReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferDoorStateZone2DecorationsReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferDoorStateZone2DecorationsReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferDoorStateZone2DecorationsReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataReeferDoorStateZone2DecorationsReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataReeferDoorStateZone2DecorationsReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone2DecorationsReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone2DecorationsReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone2DecorationsReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataReeferDoorStateZone2DecorationsReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone2DecorationsReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone2DecorationsReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone2DecorationsReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataReeferDoorStateZone2DecorationsReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataReeferDoorStateZone2DecorationsReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataReeferDoorStateZone2DecorationsReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone2DecorationsReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone2DecorationsReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone2Decorations(BaseModel):
    carrier_reefer_state: Optional[DataReeferDoorStateZone2DecorationsCarrierReeferState] = FieldInfo(
        alias="carrierReeferState", default=None
    )
    """Reefer state event."""

    gps: Optional[DataReeferDoorStateZone2DecorationsGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataReeferDoorStateZone2DecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataReeferDoorStateZone2DecorationsReeferAlarms] = FieldInfo(
        alias="reeferAlarms", default=None
    )
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[
        DataReeferDoorStateZone2DecorationsReeferAmbientAirTemperatureMilliC
    ] = FieldInfo(alias="reeferAmbientAirTemperatureMilliC", default=None)
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataReeferDoorStateZone2DecorationsReeferDoorStateZone1] = FieldInfo(
        alias="reeferDoorStateZone1", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataReeferDoorStateZone2DecorationsReeferDoorStateZone2] = FieldInfo(
        alias="reeferDoorStateZone2", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataReeferDoorStateZone2DecorationsReeferDoorStateZone3] = FieldInfo(
        alias="reeferDoorStateZone3", default=None
    )
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataReeferDoorStateZone2DecorationsReeferFuelPercent] = FieldInfo(
        alias="reeferFuelPercent", default=None
    )
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataReeferDoorStateZone2DecorationsReeferObdEngineSeconds] = FieldInfo(
        alias="reeferObdEngineSeconds", default=None
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[
        DataReeferDoorStateZone2DecorationsReeferReturnAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone1", default=None)
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[
        DataReeferDoorStateZone2DecorationsReeferReturnAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone2", default=None)
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[
        DataReeferDoorStateZone2DecorationsReeferReturnAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone3", default=None)
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataReeferDoorStateZone2DecorationsReeferRunMode] = FieldInfo(
        alias="reeferRunMode", default=None
    )
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[
        DataReeferDoorStateZone2DecorationsReeferSetPointTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone1", default=None)
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[
        DataReeferDoorStateZone2DecorationsReeferSetPointTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone2", default=None)
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[
        DataReeferDoorStateZone2DecorationsReeferSetPointTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone3", default=None)
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataReeferDoorStateZone2DecorationsReeferStateZone1] = FieldInfo(
        alias="reeferStateZone1", default=None
    )
    """Reefer state event."""

    reefer_state_zone2: Optional[DataReeferDoorStateZone2DecorationsReeferStateZone2] = FieldInfo(
        alias="reeferStateZone2", default=None
    )
    """Reefer state event."""

    reefer_state_zone3: Optional[DataReeferDoorStateZone2DecorationsReeferStateZone3] = FieldInfo(
        alias="reeferStateZone3", default=None
    )
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[
        DataReeferDoorStateZone2DecorationsReeferSupplyAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone1", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[
        DataReeferDoorStateZone2DecorationsReeferSupplyAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone2", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[
        DataReeferDoorStateZone2DecorationsReeferSupplyAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone3", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """


class DataReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""

    decorations: Optional[DataReeferDoorStateZone2Decorations] = None
    """Decorated values for the primary trailer stat datapoints."""


class DataReeferDoorStateZone3DecorationsCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataReeferDoorStateZone3DecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataReeferDoorStateZone3DecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataReeferDoorStateZone3DecorationsGpsReverseGeo] = FieldInfo(
        alias="reverseGeo", default=None
    )
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataReeferDoorStateZone3DecorationsGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataReeferDoorStateZone3DecorationsReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataReeferDoorStateZone3DecorationsReeferAlarms(BaseModel):
    alarms: List[DataReeferDoorStateZone3DecorationsReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataReeferDoorStateZone3DecorationsReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataReeferDoorStateZone3DecorationsReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferDoorStateZone3DecorationsReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferDoorStateZone3DecorationsReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferDoorStateZone3DecorationsReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataReeferDoorStateZone3DecorationsReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataReeferDoorStateZone3DecorationsReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone3DecorationsReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone3DecorationsReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone3DecorationsReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataReeferDoorStateZone3DecorationsReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone3DecorationsReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone3DecorationsReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone3DecorationsReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataReeferDoorStateZone3DecorationsReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataReeferDoorStateZone3DecorationsReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataReeferDoorStateZone3DecorationsReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone3DecorationsReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone3DecorationsReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferDoorStateZone3Decorations(BaseModel):
    carrier_reefer_state: Optional[DataReeferDoorStateZone3DecorationsCarrierReeferState] = FieldInfo(
        alias="carrierReeferState", default=None
    )
    """Reefer state event."""

    gps: Optional[DataReeferDoorStateZone3DecorationsGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataReeferDoorStateZone3DecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataReeferDoorStateZone3DecorationsReeferAlarms] = FieldInfo(
        alias="reeferAlarms", default=None
    )
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[
        DataReeferDoorStateZone3DecorationsReeferAmbientAirTemperatureMilliC
    ] = FieldInfo(alias="reeferAmbientAirTemperatureMilliC", default=None)
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataReeferDoorStateZone3DecorationsReeferDoorStateZone1] = FieldInfo(
        alias="reeferDoorStateZone1", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataReeferDoorStateZone3DecorationsReeferDoorStateZone2] = FieldInfo(
        alias="reeferDoorStateZone2", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataReeferDoorStateZone3DecorationsReeferDoorStateZone3] = FieldInfo(
        alias="reeferDoorStateZone3", default=None
    )
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataReeferDoorStateZone3DecorationsReeferFuelPercent] = FieldInfo(
        alias="reeferFuelPercent", default=None
    )
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataReeferDoorStateZone3DecorationsReeferObdEngineSeconds] = FieldInfo(
        alias="reeferObdEngineSeconds", default=None
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[
        DataReeferDoorStateZone3DecorationsReeferReturnAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone1", default=None)
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[
        DataReeferDoorStateZone3DecorationsReeferReturnAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone2", default=None)
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[
        DataReeferDoorStateZone3DecorationsReeferReturnAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone3", default=None)
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataReeferDoorStateZone3DecorationsReeferRunMode] = FieldInfo(
        alias="reeferRunMode", default=None
    )
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[
        DataReeferDoorStateZone3DecorationsReeferSetPointTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone1", default=None)
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[
        DataReeferDoorStateZone3DecorationsReeferSetPointTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone2", default=None)
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[
        DataReeferDoorStateZone3DecorationsReeferSetPointTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone3", default=None)
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataReeferDoorStateZone3DecorationsReeferStateZone1] = FieldInfo(
        alias="reeferStateZone1", default=None
    )
    """Reefer state event."""

    reefer_state_zone2: Optional[DataReeferDoorStateZone3DecorationsReeferStateZone2] = FieldInfo(
        alias="reeferStateZone2", default=None
    )
    """Reefer state event."""

    reefer_state_zone3: Optional[DataReeferDoorStateZone3DecorationsReeferStateZone3] = FieldInfo(
        alias="reeferStateZone3", default=None
    )
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[
        DataReeferDoorStateZone3DecorationsReeferSupplyAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone1", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[
        DataReeferDoorStateZone3DecorationsReeferSupplyAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone2", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[
        DataReeferDoorStateZone3DecorationsReeferSupplyAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone3", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """


class DataReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""

    decorations: Optional[DataReeferDoorStateZone3Decorations] = None
    """Decorated values for the primary trailer stat datapoints."""


class DataReeferFuelPercentDecorationsCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataReeferFuelPercentDecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataReeferFuelPercentDecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataReeferFuelPercentDecorationsGpsReverseGeo] = FieldInfo(alias="reverseGeo", default=None)
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataReeferFuelPercentDecorationsGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataReeferFuelPercentDecorationsReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataReeferFuelPercentDecorationsReeferAlarms(BaseModel):
    alarms: List[DataReeferFuelPercentDecorationsReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataReeferFuelPercentDecorationsReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataReeferFuelPercentDecorationsReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferFuelPercentDecorationsReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferFuelPercentDecorationsReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferFuelPercentDecorationsReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataReeferFuelPercentDecorationsReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataReeferFuelPercentDecorationsReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferFuelPercentDecorationsReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferFuelPercentDecorationsReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferFuelPercentDecorationsReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataReeferFuelPercentDecorationsReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferFuelPercentDecorationsReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferFuelPercentDecorationsReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferFuelPercentDecorationsReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataReeferFuelPercentDecorationsReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataReeferFuelPercentDecorationsReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataReeferFuelPercentDecorationsReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferFuelPercentDecorationsReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferFuelPercentDecorationsReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferFuelPercentDecorations(BaseModel):
    carrier_reefer_state: Optional[DataReeferFuelPercentDecorationsCarrierReeferState] = FieldInfo(
        alias="carrierReeferState", default=None
    )
    """Reefer state event."""

    gps: Optional[DataReeferFuelPercentDecorationsGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataReeferFuelPercentDecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataReeferFuelPercentDecorationsReeferAlarms] = FieldInfo(
        alias="reeferAlarms", default=None
    )
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[
        DataReeferFuelPercentDecorationsReeferAmbientAirTemperatureMilliC
    ] = FieldInfo(alias="reeferAmbientAirTemperatureMilliC", default=None)
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataReeferFuelPercentDecorationsReeferDoorStateZone1] = FieldInfo(
        alias="reeferDoorStateZone1", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataReeferFuelPercentDecorationsReeferDoorStateZone2] = FieldInfo(
        alias="reeferDoorStateZone2", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataReeferFuelPercentDecorationsReeferDoorStateZone3] = FieldInfo(
        alias="reeferDoorStateZone3", default=None
    )
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataReeferFuelPercentDecorationsReeferFuelPercent] = FieldInfo(
        alias="reeferFuelPercent", default=None
    )
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataReeferFuelPercentDecorationsReeferObdEngineSeconds] = FieldInfo(
        alias="reeferObdEngineSeconds", default=None
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[
        DataReeferFuelPercentDecorationsReeferReturnAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone1", default=None)
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[
        DataReeferFuelPercentDecorationsReeferReturnAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone2", default=None)
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[
        DataReeferFuelPercentDecorationsReeferReturnAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone3", default=None)
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataReeferFuelPercentDecorationsReeferRunMode] = FieldInfo(
        alias="reeferRunMode", default=None
    )
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[
        DataReeferFuelPercentDecorationsReeferSetPointTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone1", default=None)
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[
        DataReeferFuelPercentDecorationsReeferSetPointTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone2", default=None)
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[
        DataReeferFuelPercentDecorationsReeferSetPointTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone3", default=None)
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataReeferFuelPercentDecorationsReeferStateZone1] = FieldInfo(
        alias="reeferStateZone1", default=None
    )
    """Reefer state event."""

    reefer_state_zone2: Optional[DataReeferFuelPercentDecorationsReeferStateZone2] = FieldInfo(
        alias="reeferStateZone2", default=None
    )
    """Reefer state event."""

    reefer_state_zone3: Optional[DataReeferFuelPercentDecorationsReeferStateZone3] = FieldInfo(
        alias="reeferStateZone3", default=None
    )
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[
        DataReeferFuelPercentDecorationsReeferSupplyAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone1", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[
        DataReeferFuelPercentDecorationsReeferSupplyAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone2", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[
        DataReeferFuelPercentDecorationsReeferSupplyAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone3", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """


class DataReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""

    decorations: Optional[DataReeferFuelPercentDecorations] = None
    """Decorated values for the primary trailer stat datapoints."""


class DataReeferObdEngineSecondDecorationsCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataReeferObdEngineSecondDecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataReeferObdEngineSecondDecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataReeferObdEngineSecondDecorationsGpsReverseGeo] = FieldInfo(
        alias="reverseGeo", default=None
    )
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataReeferObdEngineSecondDecorationsGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataReeferObdEngineSecondDecorationsReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataReeferObdEngineSecondDecorationsReeferAlarms(BaseModel):
    alarms: List[DataReeferObdEngineSecondDecorationsReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataReeferObdEngineSecondDecorationsReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataReeferObdEngineSecondDecorationsReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferObdEngineSecondDecorationsReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferObdEngineSecondDecorationsReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferObdEngineSecondDecorationsReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataReeferObdEngineSecondDecorationsReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataReeferObdEngineSecondDecorationsReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferObdEngineSecondDecorationsReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferObdEngineSecondDecorationsReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferObdEngineSecondDecorationsReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataReeferObdEngineSecondDecorationsReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferObdEngineSecondDecorationsReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferObdEngineSecondDecorationsReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferObdEngineSecondDecorationsReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataReeferObdEngineSecondDecorationsReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataReeferObdEngineSecondDecorationsReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataReeferObdEngineSecondDecorationsReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferObdEngineSecondDecorationsReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferObdEngineSecondDecorationsReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferObdEngineSecondDecorations(BaseModel):
    carrier_reefer_state: Optional[DataReeferObdEngineSecondDecorationsCarrierReeferState] = FieldInfo(
        alias="carrierReeferState", default=None
    )
    """Reefer state event."""

    gps: Optional[DataReeferObdEngineSecondDecorationsGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataReeferObdEngineSecondDecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataReeferObdEngineSecondDecorationsReeferAlarms] = FieldInfo(
        alias="reeferAlarms", default=None
    )
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[
        DataReeferObdEngineSecondDecorationsReeferAmbientAirTemperatureMilliC
    ] = FieldInfo(alias="reeferAmbientAirTemperatureMilliC", default=None)
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataReeferObdEngineSecondDecorationsReeferDoorStateZone1] = FieldInfo(
        alias="reeferDoorStateZone1", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataReeferObdEngineSecondDecorationsReeferDoorStateZone2] = FieldInfo(
        alias="reeferDoorStateZone2", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataReeferObdEngineSecondDecorationsReeferDoorStateZone3] = FieldInfo(
        alias="reeferDoorStateZone3", default=None
    )
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataReeferObdEngineSecondDecorationsReeferFuelPercent] = FieldInfo(
        alias="reeferFuelPercent", default=None
    )
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataReeferObdEngineSecondDecorationsReeferObdEngineSeconds] = FieldInfo(
        alias="reeferObdEngineSeconds", default=None
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[
        DataReeferObdEngineSecondDecorationsReeferReturnAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone1", default=None)
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[
        DataReeferObdEngineSecondDecorationsReeferReturnAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone2", default=None)
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[
        DataReeferObdEngineSecondDecorationsReeferReturnAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone3", default=None)
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataReeferObdEngineSecondDecorationsReeferRunMode] = FieldInfo(
        alias="reeferRunMode", default=None
    )
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[
        DataReeferObdEngineSecondDecorationsReeferSetPointTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone1", default=None)
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[
        DataReeferObdEngineSecondDecorationsReeferSetPointTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone2", default=None)
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[
        DataReeferObdEngineSecondDecorationsReeferSetPointTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone3", default=None)
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataReeferObdEngineSecondDecorationsReeferStateZone1] = FieldInfo(
        alias="reeferStateZone1", default=None
    )
    """Reefer state event."""

    reefer_state_zone2: Optional[DataReeferObdEngineSecondDecorationsReeferStateZone2] = FieldInfo(
        alias="reeferStateZone2", default=None
    )
    """Reefer state event."""

    reefer_state_zone3: Optional[DataReeferObdEngineSecondDecorationsReeferStateZone3] = FieldInfo(
        alias="reeferStateZone3", default=None
    )
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[
        DataReeferObdEngineSecondDecorationsReeferSupplyAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone1", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[
        DataReeferObdEngineSecondDecorationsReeferSupplyAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone2", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[
        DataReeferObdEngineSecondDecorationsReeferSupplyAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone3", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """


class DataReeferObdEngineSecond(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """

    decorations: Optional[DataReeferObdEngineSecondDecorations] = None
    """Decorated values for the primary trailer stat datapoints."""


class DataReeferReturnAirTemperatureMilliCZone1DecorationsCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataReeferReturnAirTemperatureMilliCZone1DecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataReeferReturnAirTemperatureMilliCZone1DecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataReeferReturnAirTemperatureMilliCZone1DecorationsGpsReverseGeo] = FieldInfo(
        alias="reverseGeo", default=None
    )
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataReeferReturnAirTemperatureMilliCZone1DecorationsGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferAlarms(BaseModel):
    alarms: List[DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone1Decorations(BaseModel):
    carrier_reefer_state: Optional[DataReeferReturnAirTemperatureMilliCZone1DecorationsCarrierReeferState] = FieldInfo(
        alias="carrierReeferState", default=None
    )
    """Reefer state event."""

    gps: Optional[DataReeferReturnAirTemperatureMilliCZone1DecorationsGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataReeferReturnAirTemperatureMilliCZone1DecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferAlarms] = FieldInfo(
        alias="reeferAlarms", default=None
    )
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[
        DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferAmbientAirTemperatureMilliC
    ] = FieldInfo(alias="reeferAmbientAirTemperatureMilliC", default=None)
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferDoorStateZone1] = (
        FieldInfo(alias="reeferDoorStateZone1", default=None)
    )
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferDoorStateZone2] = (
        FieldInfo(alias="reeferDoorStateZone2", default=None)
    )
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferDoorStateZone3] = (
        FieldInfo(alias="reeferDoorStateZone3", default=None)
    )
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferFuelPercent] = FieldInfo(
        alias="reeferFuelPercent", default=None
    )
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferObdEngineSeconds] = (
        FieldInfo(alias="reeferObdEngineSeconds", default=None)
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[
        DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone1", default=None)
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[
        DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone2", default=None)
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[
        DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone3", default=None)
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferRunMode] = FieldInfo(
        alias="reeferRunMode", default=None
    )
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[
        DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone1", default=None)
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[
        DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone2", default=None)
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[
        DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone3", default=None)
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferStateZone1] = FieldInfo(
        alias="reeferStateZone1", default=None
    )
    """Reefer state event."""

    reefer_state_zone2: Optional[DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferStateZone2] = FieldInfo(
        alias="reeferStateZone2", default=None
    )
    """Reefer state event."""

    reefer_state_zone3: Optional[DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferStateZone3] = FieldInfo(
        alias="reeferStateZone3", default=None
    )
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[
        DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone1", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[
        DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone2", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[
        DataReeferReturnAirTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone3", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """


class DataReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""

    decorations: Optional[DataReeferReturnAirTemperatureMilliCZone1Decorations] = None
    """Decorated values for the primary trailer stat datapoints."""


class DataReeferReturnAirTemperatureMilliCZone2DecorationsCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataReeferReturnAirTemperatureMilliCZone2DecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataReeferReturnAirTemperatureMilliCZone2DecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataReeferReturnAirTemperatureMilliCZone2DecorationsGpsReverseGeo] = FieldInfo(
        alias="reverseGeo", default=None
    )
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataReeferReturnAirTemperatureMilliCZone2DecorationsGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferAlarms(BaseModel):
    alarms: List[DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone2Decorations(BaseModel):
    carrier_reefer_state: Optional[DataReeferReturnAirTemperatureMilliCZone2DecorationsCarrierReeferState] = FieldInfo(
        alias="carrierReeferState", default=None
    )
    """Reefer state event."""

    gps: Optional[DataReeferReturnAirTemperatureMilliCZone2DecorationsGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataReeferReturnAirTemperatureMilliCZone2DecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferAlarms] = FieldInfo(
        alias="reeferAlarms", default=None
    )
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[
        DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferAmbientAirTemperatureMilliC
    ] = FieldInfo(alias="reeferAmbientAirTemperatureMilliC", default=None)
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferDoorStateZone1] = (
        FieldInfo(alias="reeferDoorStateZone1", default=None)
    )
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferDoorStateZone2] = (
        FieldInfo(alias="reeferDoorStateZone2", default=None)
    )
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferDoorStateZone3] = (
        FieldInfo(alias="reeferDoorStateZone3", default=None)
    )
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferFuelPercent] = FieldInfo(
        alias="reeferFuelPercent", default=None
    )
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferObdEngineSeconds] = (
        FieldInfo(alias="reeferObdEngineSeconds", default=None)
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[
        DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone1", default=None)
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[
        DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone2", default=None)
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[
        DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone3", default=None)
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferRunMode] = FieldInfo(
        alias="reeferRunMode", default=None
    )
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[
        DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone1", default=None)
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[
        DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone2", default=None)
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[
        DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone3", default=None)
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferStateZone1] = FieldInfo(
        alias="reeferStateZone1", default=None
    )
    """Reefer state event."""

    reefer_state_zone2: Optional[DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferStateZone2] = FieldInfo(
        alias="reeferStateZone2", default=None
    )
    """Reefer state event."""

    reefer_state_zone3: Optional[DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferStateZone3] = FieldInfo(
        alias="reeferStateZone3", default=None
    )
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[
        DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone1", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[
        DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone2", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[
        DataReeferReturnAirTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone3", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """


class DataReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""

    decorations: Optional[DataReeferReturnAirTemperatureMilliCZone2Decorations] = None
    """Decorated values for the primary trailer stat datapoints."""


class DataReeferReturnAirTemperatureMilliCZone3DecorationsCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataReeferReturnAirTemperatureMilliCZone3DecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataReeferReturnAirTemperatureMilliCZone3DecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataReeferReturnAirTemperatureMilliCZone3DecorationsGpsReverseGeo] = FieldInfo(
        alias="reverseGeo", default=None
    )
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataReeferReturnAirTemperatureMilliCZone3DecorationsGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferAlarms(BaseModel):
    alarms: List[DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone3Decorations(BaseModel):
    carrier_reefer_state: Optional[DataReeferReturnAirTemperatureMilliCZone3DecorationsCarrierReeferState] = FieldInfo(
        alias="carrierReeferState", default=None
    )
    """Reefer state event."""

    gps: Optional[DataReeferReturnAirTemperatureMilliCZone3DecorationsGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataReeferReturnAirTemperatureMilliCZone3DecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferAlarms] = FieldInfo(
        alias="reeferAlarms", default=None
    )
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[
        DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferAmbientAirTemperatureMilliC
    ] = FieldInfo(alias="reeferAmbientAirTemperatureMilliC", default=None)
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferDoorStateZone1] = (
        FieldInfo(alias="reeferDoorStateZone1", default=None)
    )
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferDoorStateZone2] = (
        FieldInfo(alias="reeferDoorStateZone2", default=None)
    )
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferDoorStateZone3] = (
        FieldInfo(alias="reeferDoorStateZone3", default=None)
    )
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferFuelPercent] = FieldInfo(
        alias="reeferFuelPercent", default=None
    )
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferObdEngineSeconds] = (
        FieldInfo(alias="reeferObdEngineSeconds", default=None)
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[
        DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone1", default=None)
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[
        DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone2", default=None)
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[
        DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone3", default=None)
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferRunMode] = FieldInfo(
        alias="reeferRunMode", default=None
    )
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[
        DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone1", default=None)
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[
        DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone2", default=None)
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[
        DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone3", default=None)
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferStateZone1] = FieldInfo(
        alias="reeferStateZone1", default=None
    )
    """Reefer state event."""

    reefer_state_zone2: Optional[DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferStateZone2] = FieldInfo(
        alias="reeferStateZone2", default=None
    )
    """Reefer state event."""

    reefer_state_zone3: Optional[DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferStateZone3] = FieldInfo(
        alias="reeferStateZone3", default=None
    )
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[
        DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone1", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[
        DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone2", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[
        DataReeferReturnAirTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone3", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """


class DataReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""

    decorations: Optional[DataReeferReturnAirTemperatureMilliCZone3Decorations] = None
    """Decorated values for the primary trailer stat datapoints."""


class DataReeferRunModeDecorationsCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataReeferRunModeDecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataReeferRunModeDecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataReeferRunModeDecorationsGpsReverseGeo] = FieldInfo(alias="reverseGeo", default=None)
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataReeferRunModeDecorationsGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataReeferRunModeDecorationsReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataReeferRunModeDecorationsReeferAlarms(BaseModel):
    alarms: List[DataReeferRunModeDecorationsReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataReeferRunModeDecorationsReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataReeferRunModeDecorationsReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferRunModeDecorationsReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferRunModeDecorationsReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferRunModeDecorationsReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataReeferRunModeDecorationsReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataReeferRunModeDecorationsReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferRunModeDecorationsReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferRunModeDecorationsReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferRunModeDecorationsReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataReeferRunModeDecorationsReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferRunModeDecorationsReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferRunModeDecorationsReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferRunModeDecorationsReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataReeferRunModeDecorationsReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataReeferRunModeDecorationsReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataReeferRunModeDecorationsReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferRunModeDecorationsReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferRunModeDecorationsReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferRunModeDecorations(BaseModel):
    carrier_reefer_state: Optional[DataReeferRunModeDecorationsCarrierReeferState] = FieldInfo(
        alias="carrierReeferState", default=None
    )
    """Reefer state event."""

    gps: Optional[DataReeferRunModeDecorationsGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataReeferRunModeDecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataReeferRunModeDecorationsReeferAlarms] = FieldInfo(alias="reeferAlarms", default=None)
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[DataReeferRunModeDecorationsReeferAmbientAirTemperatureMilliC] = (
        FieldInfo(alias="reeferAmbientAirTemperatureMilliC", default=None)
    )
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataReeferRunModeDecorationsReeferDoorStateZone1] = FieldInfo(
        alias="reeferDoorStateZone1", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataReeferRunModeDecorationsReeferDoorStateZone2] = FieldInfo(
        alias="reeferDoorStateZone2", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataReeferRunModeDecorationsReeferDoorStateZone3] = FieldInfo(
        alias="reeferDoorStateZone3", default=None
    )
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataReeferRunModeDecorationsReeferFuelPercent] = FieldInfo(
        alias="reeferFuelPercent", default=None
    )
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataReeferRunModeDecorationsReeferObdEngineSeconds] = FieldInfo(
        alias="reeferObdEngineSeconds", default=None
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[
        DataReeferRunModeDecorationsReeferReturnAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone1", default=None)
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[
        DataReeferRunModeDecorationsReeferReturnAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone2", default=None)
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[
        DataReeferRunModeDecorationsReeferReturnAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone3", default=None)
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataReeferRunModeDecorationsReeferRunMode] = FieldInfo(
        alias="reeferRunMode", default=None
    )
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[
        DataReeferRunModeDecorationsReeferSetPointTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone1", default=None)
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[
        DataReeferRunModeDecorationsReeferSetPointTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone2", default=None)
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[
        DataReeferRunModeDecorationsReeferSetPointTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone3", default=None)
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataReeferRunModeDecorationsReeferStateZone1] = FieldInfo(
        alias="reeferStateZone1", default=None
    )
    """Reefer state event."""

    reefer_state_zone2: Optional[DataReeferRunModeDecorationsReeferStateZone2] = FieldInfo(
        alias="reeferStateZone2", default=None
    )
    """Reefer state event."""

    reefer_state_zone3: Optional[DataReeferRunModeDecorationsReeferStateZone3] = FieldInfo(
        alias="reeferStateZone3", default=None
    )
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[
        DataReeferRunModeDecorationsReeferSupplyAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone1", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[
        DataReeferRunModeDecorationsReeferSupplyAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone2", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[
        DataReeferRunModeDecorationsReeferSupplyAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone3", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """


class DataReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""

    decorations: Optional[DataReeferRunModeDecorations] = None
    """Decorated values for the primary trailer stat datapoints."""


class DataReeferSetPointTemperatureMilliCZone1DecorationsCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataReeferSetPointTemperatureMilliCZone1DecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataReeferSetPointTemperatureMilliCZone1DecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataReeferSetPointTemperatureMilliCZone1DecorationsGpsReverseGeo] = FieldInfo(
        alias="reverseGeo", default=None
    )
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataReeferSetPointTemperatureMilliCZone1DecorationsGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataReeferSetPointTemperatureMilliCZone1DecorationsReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataReeferSetPointTemperatureMilliCZone1DecorationsReeferAlarms(BaseModel):
    alarms: List[DataReeferSetPointTemperatureMilliCZone1DecorationsReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataReeferSetPointTemperatureMilliCZone1DecorationsReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone1DecorationsReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferSetPointTemperatureMilliCZone1DecorationsReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferSetPointTemperatureMilliCZone1DecorationsReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferSetPointTemperatureMilliCZone1DecorationsReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataReeferSetPointTemperatureMilliCZone1DecorationsReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataReeferSetPointTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone1DecorationsReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataReeferSetPointTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone1DecorationsReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataReeferSetPointTemperatureMilliCZone1DecorationsReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataReeferSetPointTemperatureMilliCZone1DecorationsReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataReeferSetPointTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone1Decorations(BaseModel):
    carrier_reefer_state: Optional[DataReeferSetPointTemperatureMilliCZone1DecorationsCarrierReeferState] = FieldInfo(
        alias="carrierReeferState", default=None
    )
    """Reefer state event."""

    gps: Optional[DataReeferSetPointTemperatureMilliCZone1DecorationsGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataReeferSetPointTemperatureMilliCZone1DecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataReeferSetPointTemperatureMilliCZone1DecorationsReeferAlarms] = FieldInfo(
        alias="reeferAlarms", default=None
    )
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[
        DataReeferSetPointTemperatureMilliCZone1DecorationsReeferAmbientAirTemperatureMilliC
    ] = FieldInfo(alias="reeferAmbientAirTemperatureMilliC", default=None)
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataReeferSetPointTemperatureMilliCZone1DecorationsReeferDoorStateZone1] = (
        FieldInfo(alias="reeferDoorStateZone1", default=None)
    )
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataReeferSetPointTemperatureMilliCZone1DecorationsReeferDoorStateZone2] = (
        FieldInfo(alias="reeferDoorStateZone2", default=None)
    )
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataReeferSetPointTemperatureMilliCZone1DecorationsReeferDoorStateZone3] = (
        FieldInfo(alias="reeferDoorStateZone3", default=None)
    )
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataReeferSetPointTemperatureMilliCZone1DecorationsReeferFuelPercent] = FieldInfo(
        alias="reeferFuelPercent", default=None
    )
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataReeferSetPointTemperatureMilliCZone1DecorationsReeferObdEngineSeconds] = (
        FieldInfo(alias="reeferObdEngineSeconds", default=None)
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[
        DataReeferSetPointTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone1", default=None)
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[
        DataReeferSetPointTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone2", default=None)
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[
        DataReeferSetPointTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone3", default=None)
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataReeferSetPointTemperatureMilliCZone1DecorationsReeferRunMode] = FieldInfo(
        alias="reeferRunMode", default=None
    )
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[
        DataReeferSetPointTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone1", default=None)
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[
        DataReeferSetPointTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone2", default=None)
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[
        DataReeferSetPointTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone3", default=None)
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataReeferSetPointTemperatureMilliCZone1DecorationsReeferStateZone1] = FieldInfo(
        alias="reeferStateZone1", default=None
    )
    """Reefer state event."""

    reefer_state_zone2: Optional[DataReeferSetPointTemperatureMilliCZone1DecorationsReeferStateZone2] = FieldInfo(
        alias="reeferStateZone2", default=None
    )
    """Reefer state event."""

    reefer_state_zone3: Optional[DataReeferSetPointTemperatureMilliCZone1DecorationsReeferStateZone3] = FieldInfo(
        alias="reeferStateZone3", default=None
    )
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[
        DataReeferSetPointTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone1", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[
        DataReeferSetPointTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone2", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[
        DataReeferSetPointTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone3", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """


class DataReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""

    decorations: Optional[DataReeferSetPointTemperatureMilliCZone1Decorations] = None
    """Decorated values for the primary trailer stat datapoints."""


class DataReeferSetPointTemperatureMilliCZone2DecorationsCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataReeferSetPointTemperatureMilliCZone2DecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataReeferSetPointTemperatureMilliCZone2DecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataReeferSetPointTemperatureMilliCZone2DecorationsGpsReverseGeo] = FieldInfo(
        alias="reverseGeo", default=None
    )
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataReeferSetPointTemperatureMilliCZone2DecorationsGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataReeferSetPointTemperatureMilliCZone2DecorationsReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataReeferSetPointTemperatureMilliCZone2DecorationsReeferAlarms(BaseModel):
    alarms: List[DataReeferSetPointTemperatureMilliCZone2DecorationsReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataReeferSetPointTemperatureMilliCZone2DecorationsReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone2DecorationsReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferSetPointTemperatureMilliCZone2DecorationsReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferSetPointTemperatureMilliCZone2DecorationsReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferSetPointTemperatureMilliCZone2DecorationsReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataReeferSetPointTemperatureMilliCZone2DecorationsReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataReeferSetPointTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone2DecorationsReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataReeferSetPointTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone2DecorationsReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataReeferSetPointTemperatureMilliCZone2DecorationsReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataReeferSetPointTemperatureMilliCZone2DecorationsReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataReeferSetPointTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone2Decorations(BaseModel):
    carrier_reefer_state: Optional[DataReeferSetPointTemperatureMilliCZone2DecorationsCarrierReeferState] = FieldInfo(
        alias="carrierReeferState", default=None
    )
    """Reefer state event."""

    gps: Optional[DataReeferSetPointTemperatureMilliCZone2DecorationsGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataReeferSetPointTemperatureMilliCZone2DecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataReeferSetPointTemperatureMilliCZone2DecorationsReeferAlarms] = FieldInfo(
        alias="reeferAlarms", default=None
    )
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[
        DataReeferSetPointTemperatureMilliCZone2DecorationsReeferAmbientAirTemperatureMilliC
    ] = FieldInfo(alias="reeferAmbientAirTemperatureMilliC", default=None)
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataReeferSetPointTemperatureMilliCZone2DecorationsReeferDoorStateZone1] = (
        FieldInfo(alias="reeferDoorStateZone1", default=None)
    )
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataReeferSetPointTemperatureMilliCZone2DecorationsReeferDoorStateZone2] = (
        FieldInfo(alias="reeferDoorStateZone2", default=None)
    )
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataReeferSetPointTemperatureMilliCZone2DecorationsReeferDoorStateZone3] = (
        FieldInfo(alias="reeferDoorStateZone3", default=None)
    )
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataReeferSetPointTemperatureMilliCZone2DecorationsReeferFuelPercent] = FieldInfo(
        alias="reeferFuelPercent", default=None
    )
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataReeferSetPointTemperatureMilliCZone2DecorationsReeferObdEngineSeconds] = (
        FieldInfo(alias="reeferObdEngineSeconds", default=None)
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[
        DataReeferSetPointTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone1", default=None)
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[
        DataReeferSetPointTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone2", default=None)
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[
        DataReeferSetPointTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone3", default=None)
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataReeferSetPointTemperatureMilliCZone2DecorationsReeferRunMode] = FieldInfo(
        alias="reeferRunMode", default=None
    )
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[
        DataReeferSetPointTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone1", default=None)
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[
        DataReeferSetPointTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone2", default=None)
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[
        DataReeferSetPointTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone3", default=None)
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataReeferSetPointTemperatureMilliCZone2DecorationsReeferStateZone1] = FieldInfo(
        alias="reeferStateZone1", default=None
    )
    """Reefer state event."""

    reefer_state_zone2: Optional[DataReeferSetPointTemperatureMilliCZone2DecorationsReeferStateZone2] = FieldInfo(
        alias="reeferStateZone2", default=None
    )
    """Reefer state event."""

    reefer_state_zone3: Optional[DataReeferSetPointTemperatureMilliCZone2DecorationsReeferStateZone3] = FieldInfo(
        alias="reeferStateZone3", default=None
    )
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[
        DataReeferSetPointTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone1", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[
        DataReeferSetPointTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone2", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[
        DataReeferSetPointTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone3", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """


class DataReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""

    decorations: Optional[DataReeferSetPointTemperatureMilliCZone2Decorations] = None
    """Decorated values for the primary trailer stat datapoints."""


class DataReeferSetPointTemperatureMilliCZone3DecorationsCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataReeferSetPointTemperatureMilliCZone3DecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataReeferSetPointTemperatureMilliCZone3DecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataReeferSetPointTemperatureMilliCZone3DecorationsGpsReverseGeo] = FieldInfo(
        alias="reverseGeo", default=None
    )
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataReeferSetPointTemperatureMilliCZone3DecorationsGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataReeferSetPointTemperatureMilliCZone3DecorationsReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataReeferSetPointTemperatureMilliCZone3DecorationsReeferAlarms(BaseModel):
    alarms: List[DataReeferSetPointTemperatureMilliCZone3DecorationsReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataReeferSetPointTemperatureMilliCZone3DecorationsReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone3DecorationsReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferSetPointTemperatureMilliCZone3DecorationsReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferSetPointTemperatureMilliCZone3DecorationsReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferSetPointTemperatureMilliCZone3DecorationsReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataReeferSetPointTemperatureMilliCZone3DecorationsReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataReeferSetPointTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone3DecorationsReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataReeferSetPointTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone3DecorationsReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataReeferSetPointTemperatureMilliCZone3DecorationsReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataReeferSetPointTemperatureMilliCZone3DecorationsReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataReeferSetPointTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone3Decorations(BaseModel):
    carrier_reefer_state: Optional[DataReeferSetPointTemperatureMilliCZone3DecorationsCarrierReeferState] = FieldInfo(
        alias="carrierReeferState", default=None
    )
    """Reefer state event."""

    gps: Optional[DataReeferSetPointTemperatureMilliCZone3DecorationsGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataReeferSetPointTemperatureMilliCZone3DecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataReeferSetPointTemperatureMilliCZone3DecorationsReeferAlarms] = FieldInfo(
        alias="reeferAlarms", default=None
    )
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[
        DataReeferSetPointTemperatureMilliCZone3DecorationsReeferAmbientAirTemperatureMilliC
    ] = FieldInfo(alias="reeferAmbientAirTemperatureMilliC", default=None)
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataReeferSetPointTemperatureMilliCZone3DecorationsReeferDoorStateZone1] = (
        FieldInfo(alias="reeferDoorStateZone1", default=None)
    )
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataReeferSetPointTemperatureMilliCZone3DecorationsReeferDoorStateZone2] = (
        FieldInfo(alias="reeferDoorStateZone2", default=None)
    )
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataReeferSetPointTemperatureMilliCZone3DecorationsReeferDoorStateZone3] = (
        FieldInfo(alias="reeferDoorStateZone3", default=None)
    )
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataReeferSetPointTemperatureMilliCZone3DecorationsReeferFuelPercent] = FieldInfo(
        alias="reeferFuelPercent", default=None
    )
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataReeferSetPointTemperatureMilliCZone3DecorationsReeferObdEngineSeconds] = (
        FieldInfo(alias="reeferObdEngineSeconds", default=None)
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[
        DataReeferSetPointTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone1", default=None)
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[
        DataReeferSetPointTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone2", default=None)
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[
        DataReeferSetPointTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone3", default=None)
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataReeferSetPointTemperatureMilliCZone3DecorationsReeferRunMode] = FieldInfo(
        alias="reeferRunMode", default=None
    )
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[
        DataReeferSetPointTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone1", default=None)
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[
        DataReeferSetPointTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone2", default=None)
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[
        DataReeferSetPointTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone3", default=None)
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataReeferSetPointTemperatureMilliCZone3DecorationsReeferStateZone1] = FieldInfo(
        alias="reeferStateZone1", default=None
    )
    """Reefer state event."""

    reefer_state_zone2: Optional[DataReeferSetPointTemperatureMilliCZone3DecorationsReeferStateZone2] = FieldInfo(
        alias="reeferStateZone2", default=None
    )
    """Reefer state event."""

    reefer_state_zone3: Optional[DataReeferSetPointTemperatureMilliCZone3DecorationsReeferStateZone3] = FieldInfo(
        alias="reeferStateZone3", default=None
    )
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[
        DataReeferSetPointTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone1", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[
        DataReeferSetPointTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone2", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[
        DataReeferSetPointTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone3", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """


class DataReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""

    decorations: Optional[DataReeferSetPointTemperatureMilliCZone3Decorations] = None
    """Decorated values for the primary trailer stat datapoints."""


class DataReeferStateZone1DecorationsCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataReeferStateZone1DecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataReeferStateZone1DecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataReeferStateZone1DecorationsGpsReverseGeo] = FieldInfo(alias="reverseGeo", default=None)
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataReeferStateZone1DecorationsGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataReeferStateZone1DecorationsReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataReeferStateZone1DecorationsReeferAlarms(BaseModel):
    alarms: List[DataReeferStateZone1DecorationsReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataReeferStateZone1DecorationsReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataReeferStateZone1DecorationsReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferStateZone1DecorationsReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferStateZone1DecorationsReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferStateZone1DecorationsReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataReeferStateZone1DecorationsReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataReeferStateZone1DecorationsReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferStateZone1DecorationsReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferStateZone1DecorationsReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferStateZone1DecorationsReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataReeferStateZone1DecorationsReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferStateZone1DecorationsReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferStateZone1DecorationsReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferStateZone1DecorationsReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataReeferStateZone1DecorationsReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataReeferStateZone1DecorationsReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataReeferStateZone1DecorationsReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferStateZone1DecorationsReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferStateZone1DecorationsReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferStateZone1Decorations(BaseModel):
    carrier_reefer_state: Optional[DataReeferStateZone1DecorationsCarrierReeferState] = FieldInfo(
        alias="carrierReeferState", default=None
    )
    """Reefer state event."""

    gps: Optional[DataReeferStateZone1DecorationsGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataReeferStateZone1DecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataReeferStateZone1DecorationsReeferAlarms] = FieldInfo(alias="reeferAlarms", default=None)
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[
        DataReeferStateZone1DecorationsReeferAmbientAirTemperatureMilliC
    ] = FieldInfo(alias="reeferAmbientAirTemperatureMilliC", default=None)
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataReeferStateZone1DecorationsReeferDoorStateZone1] = FieldInfo(
        alias="reeferDoorStateZone1", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataReeferStateZone1DecorationsReeferDoorStateZone2] = FieldInfo(
        alias="reeferDoorStateZone2", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataReeferStateZone1DecorationsReeferDoorStateZone3] = FieldInfo(
        alias="reeferDoorStateZone3", default=None
    )
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataReeferStateZone1DecorationsReeferFuelPercent] = FieldInfo(
        alias="reeferFuelPercent", default=None
    )
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataReeferStateZone1DecorationsReeferObdEngineSeconds] = FieldInfo(
        alias="reeferObdEngineSeconds", default=None
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[
        DataReeferStateZone1DecorationsReeferReturnAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone1", default=None)
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[
        DataReeferStateZone1DecorationsReeferReturnAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone2", default=None)
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[
        DataReeferStateZone1DecorationsReeferReturnAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone3", default=None)
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataReeferStateZone1DecorationsReeferRunMode] = FieldInfo(
        alias="reeferRunMode", default=None
    )
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[
        DataReeferStateZone1DecorationsReeferSetPointTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone1", default=None)
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[
        DataReeferStateZone1DecorationsReeferSetPointTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone2", default=None)
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[
        DataReeferStateZone1DecorationsReeferSetPointTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone3", default=None)
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataReeferStateZone1DecorationsReeferStateZone1] = FieldInfo(
        alias="reeferStateZone1", default=None
    )
    """Reefer state event."""

    reefer_state_zone2: Optional[DataReeferStateZone1DecorationsReeferStateZone2] = FieldInfo(
        alias="reeferStateZone2", default=None
    )
    """Reefer state event."""

    reefer_state_zone3: Optional[DataReeferStateZone1DecorationsReeferStateZone3] = FieldInfo(
        alias="reeferStateZone3", default=None
    )
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[
        DataReeferStateZone1DecorationsReeferSupplyAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone1", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[
        DataReeferStateZone1DecorationsReeferSupplyAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone2", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[
        DataReeferStateZone1DecorationsReeferSupplyAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone3", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """


class DataReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    decorations: Optional[DataReeferStateZone1Decorations] = None
    """Decorated values for the primary trailer stat datapoints."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataReeferStateZone2DecorationsCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataReeferStateZone2DecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataReeferStateZone2DecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataReeferStateZone2DecorationsGpsReverseGeo] = FieldInfo(alias="reverseGeo", default=None)
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataReeferStateZone2DecorationsGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataReeferStateZone2DecorationsReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataReeferStateZone2DecorationsReeferAlarms(BaseModel):
    alarms: List[DataReeferStateZone2DecorationsReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataReeferStateZone2DecorationsReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataReeferStateZone2DecorationsReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferStateZone2DecorationsReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferStateZone2DecorationsReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferStateZone2DecorationsReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataReeferStateZone2DecorationsReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataReeferStateZone2DecorationsReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferStateZone2DecorationsReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferStateZone2DecorationsReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferStateZone2DecorationsReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataReeferStateZone2DecorationsReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferStateZone2DecorationsReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferStateZone2DecorationsReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferStateZone2DecorationsReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataReeferStateZone2DecorationsReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataReeferStateZone2DecorationsReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataReeferStateZone2DecorationsReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferStateZone2DecorationsReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferStateZone2DecorationsReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferStateZone2Decorations(BaseModel):
    carrier_reefer_state: Optional[DataReeferStateZone2DecorationsCarrierReeferState] = FieldInfo(
        alias="carrierReeferState", default=None
    )
    """Reefer state event."""

    gps: Optional[DataReeferStateZone2DecorationsGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataReeferStateZone2DecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataReeferStateZone2DecorationsReeferAlarms] = FieldInfo(alias="reeferAlarms", default=None)
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[
        DataReeferStateZone2DecorationsReeferAmbientAirTemperatureMilliC
    ] = FieldInfo(alias="reeferAmbientAirTemperatureMilliC", default=None)
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataReeferStateZone2DecorationsReeferDoorStateZone1] = FieldInfo(
        alias="reeferDoorStateZone1", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataReeferStateZone2DecorationsReeferDoorStateZone2] = FieldInfo(
        alias="reeferDoorStateZone2", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataReeferStateZone2DecorationsReeferDoorStateZone3] = FieldInfo(
        alias="reeferDoorStateZone3", default=None
    )
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataReeferStateZone2DecorationsReeferFuelPercent] = FieldInfo(
        alias="reeferFuelPercent", default=None
    )
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataReeferStateZone2DecorationsReeferObdEngineSeconds] = FieldInfo(
        alias="reeferObdEngineSeconds", default=None
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[
        DataReeferStateZone2DecorationsReeferReturnAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone1", default=None)
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[
        DataReeferStateZone2DecorationsReeferReturnAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone2", default=None)
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[
        DataReeferStateZone2DecorationsReeferReturnAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone3", default=None)
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataReeferStateZone2DecorationsReeferRunMode] = FieldInfo(
        alias="reeferRunMode", default=None
    )
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[
        DataReeferStateZone2DecorationsReeferSetPointTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone1", default=None)
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[
        DataReeferStateZone2DecorationsReeferSetPointTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone2", default=None)
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[
        DataReeferStateZone2DecorationsReeferSetPointTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone3", default=None)
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataReeferStateZone2DecorationsReeferStateZone1] = FieldInfo(
        alias="reeferStateZone1", default=None
    )
    """Reefer state event."""

    reefer_state_zone2: Optional[DataReeferStateZone2DecorationsReeferStateZone2] = FieldInfo(
        alias="reeferStateZone2", default=None
    )
    """Reefer state event."""

    reefer_state_zone3: Optional[DataReeferStateZone2DecorationsReeferStateZone3] = FieldInfo(
        alias="reeferStateZone3", default=None
    )
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[
        DataReeferStateZone2DecorationsReeferSupplyAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone1", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[
        DataReeferStateZone2DecorationsReeferSupplyAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone2", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[
        DataReeferStateZone2DecorationsReeferSupplyAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone3", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """


class DataReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    decorations: Optional[DataReeferStateZone2Decorations] = None
    """Decorated values for the primary trailer stat datapoints."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataReeferStateZone3DecorationsCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataReeferStateZone3DecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataReeferStateZone3DecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataReeferStateZone3DecorationsGpsReverseGeo] = FieldInfo(alias="reverseGeo", default=None)
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataReeferStateZone3DecorationsGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataReeferStateZone3DecorationsReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataReeferStateZone3DecorationsReeferAlarms(BaseModel):
    alarms: List[DataReeferStateZone3DecorationsReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataReeferStateZone3DecorationsReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataReeferStateZone3DecorationsReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferStateZone3DecorationsReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferStateZone3DecorationsReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferStateZone3DecorationsReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataReeferStateZone3DecorationsReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataReeferStateZone3DecorationsReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferStateZone3DecorationsReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferStateZone3DecorationsReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferStateZone3DecorationsReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataReeferStateZone3DecorationsReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferStateZone3DecorationsReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferStateZone3DecorationsReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferStateZone3DecorationsReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataReeferStateZone3DecorationsReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataReeferStateZone3DecorationsReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataReeferStateZone3DecorationsReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferStateZone3DecorationsReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferStateZone3DecorationsReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferStateZone3Decorations(BaseModel):
    carrier_reefer_state: Optional[DataReeferStateZone3DecorationsCarrierReeferState] = FieldInfo(
        alias="carrierReeferState", default=None
    )
    """Reefer state event."""

    gps: Optional[DataReeferStateZone3DecorationsGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataReeferStateZone3DecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataReeferStateZone3DecorationsReeferAlarms] = FieldInfo(alias="reeferAlarms", default=None)
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[
        DataReeferStateZone3DecorationsReeferAmbientAirTemperatureMilliC
    ] = FieldInfo(alias="reeferAmbientAirTemperatureMilliC", default=None)
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataReeferStateZone3DecorationsReeferDoorStateZone1] = FieldInfo(
        alias="reeferDoorStateZone1", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataReeferStateZone3DecorationsReeferDoorStateZone2] = FieldInfo(
        alias="reeferDoorStateZone2", default=None
    )
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataReeferStateZone3DecorationsReeferDoorStateZone3] = FieldInfo(
        alias="reeferDoorStateZone3", default=None
    )
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataReeferStateZone3DecorationsReeferFuelPercent] = FieldInfo(
        alias="reeferFuelPercent", default=None
    )
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataReeferStateZone3DecorationsReeferObdEngineSeconds] = FieldInfo(
        alias="reeferObdEngineSeconds", default=None
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[
        DataReeferStateZone3DecorationsReeferReturnAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone1", default=None)
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[
        DataReeferStateZone3DecorationsReeferReturnAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone2", default=None)
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[
        DataReeferStateZone3DecorationsReeferReturnAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone3", default=None)
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataReeferStateZone3DecorationsReeferRunMode] = FieldInfo(
        alias="reeferRunMode", default=None
    )
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[
        DataReeferStateZone3DecorationsReeferSetPointTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone1", default=None)
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[
        DataReeferStateZone3DecorationsReeferSetPointTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone2", default=None)
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[
        DataReeferStateZone3DecorationsReeferSetPointTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone3", default=None)
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataReeferStateZone3DecorationsReeferStateZone1] = FieldInfo(
        alias="reeferStateZone1", default=None
    )
    """Reefer state event."""

    reefer_state_zone2: Optional[DataReeferStateZone3DecorationsReeferStateZone2] = FieldInfo(
        alias="reeferStateZone2", default=None
    )
    """Reefer state event."""

    reefer_state_zone3: Optional[DataReeferStateZone3DecorationsReeferStateZone3] = FieldInfo(
        alias="reeferStateZone3", default=None
    )
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[
        DataReeferStateZone3DecorationsReeferSupplyAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone1", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[
        DataReeferStateZone3DecorationsReeferSupplyAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone2", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[
        DataReeferStateZone3DecorationsReeferSupplyAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone3", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """


class DataReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    decorations: Optional[DataReeferStateZone3Decorations] = None
    """Decorated values for the primary trailer stat datapoints."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataReeferSupplyAirTemperatureMilliCZone1DecorationsGpsReverseGeo] = FieldInfo(
        alias="reverseGeo", default=None
    )
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferAlarms(BaseModel):
    alarms: List[DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone1Decorations(BaseModel):
    carrier_reefer_state: Optional[DataReeferSupplyAirTemperatureMilliCZone1DecorationsCarrierReeferState] = FieldInfo(
        alias="carrierReeferState", default=None
    )
    """Reefer state event."""

    gps: Optional[DataReeferSupplyAirTemperatureMilliCZone1DecorationsGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataReeferSupplyAirTemperatureMilliCZone1DecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferAlarms] = FieldInfo(
        alias="reeferAlarms", default=None
    )
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[
        DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferAmbientAirTemperatureMilliC
    ] = FieldInfo(alias="reeferAmbientAirTemperatureMilliC", default=None)
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferDoorStateZone1] = (
        FieldInfo(alias="reeferDoorStateZone1", default=None)
    )
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferDoorStateZone2] = (
        FieldInfo(alias="reeferDoorStateZone2", default=None)
    )
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferDoorStateZone3] = (
        FieldInfo(alias="reeferDoorStateZone3", default=None)
    )
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferFuelPercent] = FieldInfo(
        alias="reeferFuelPercent", default=None
    )
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferObdEngineSeconds] = (
        FieldInfo(alias="reeferObdEngineSeconds", default=None)
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[
        DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone1", default=None)
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[
        DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone2", default=None)
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[
        DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferReturnAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone3", default=None)
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferRunMode] = FieldInfo(
        alias="reeferRunMode", default=None
    )
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[
        DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone1", default=None)
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[
        DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone2", default=None)
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[
        DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferSetPointTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone3", default=None)
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferStateZone1] = FieldInfo(
        alias="reeferStateZone1", default=None
    )
    """Reefer state event."""

    reefer_state_zone2: Optional[DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferStateZone2] = FieldInfo(
        alias="reeferStateZone2", default=None
    )
    """Reefer state event."""

    reefer_state_zone3: Optional[DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferStateZone3] = FieldInfo(
        alias="reeferStateZone3", default=None
    )
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[
        DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone1", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[
        DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone2", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[
        DataReeferSupplyAirTemperatureMilliCZone1DecorationsReeferSupplyAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone3", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """


class DataReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""

    decorations: Optional[DataReeferSupplyAirTemperatureMilliCZone1Decorations] = None
    """Decorated values for the primary trailer stat datapoints."""


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataReeferSupplyAirTemperatureMilliCZone2DecorationsGpsReverseGeo] = FieldInfo(
        alias="reverseGeo", default=None
    )
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferAlarms(BaseModel):
    alarms: List[DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone2Decorations(BaseModel):
    carrier_reefer_state: Optional[DataReeferSupplyAirTemperatureMilliCZone2DecorationsCarrierReeferState] = FieldInfo(
        alias="carrierReeferState", default=None
    )
    """Reefer state event."""

    gps: Optional[DataReeferSupplyAirTemperatureMilliCZone2DecorationsGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataReeferSupplyAirTemperatureMilliCZone2DecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferAlarms] = FieldInfo(
        alias="reeferAlarms", default=None
    )
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[
        DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferAmbientAirTemperatureMilliC
    ] = FieldInfo(alias="reeferAmbientAirTemperatureMilliC", default=None)
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferDoorStateZone1] = (
        FieldInfo(alias="reeferDoorStateZone1", default=None)
    )
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferDoorStateZone2] = (
        FieldInfo(alias="reeferDoorStateZone2", default=None)
    )
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferDoorStateZone3] = (
        FieldInfo(alias="reeferDoorStateZone3", default=None)
    )
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferFuelPercent] = FieldInfo(
        alias="reeferFuelPercent", default=None
    )
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferObdEngineSeconds] = (
        FieldInfo(alias="reeferObdEngineSeconds", default=None)
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[
        DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone1", default=None)
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[
        DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone2", default=None)
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[
        DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferReturnAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone3", default=None)
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferRunMode] = FieldInfo(
        alias="reeferRunMode", default=None
    )
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[
        DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone1", default=None)
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[
        DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone2", default=None)
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[
        DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferSetPointTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone3", default=None)
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferStateZone1] = FieldInfo(
        alias="reeferStateZone1", default=None
    )
    """Reefer state event."""

    reefer_state_zone2: Optional[DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferStateZone2] = FieldInfo(
        alias="reeferStateZone2", default=None
    )
    """Reefer state event."""

    reefer_state_zone3: Optional[DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferStateZone3] = FieldInfo(
        alias="reeferStateZone3", default=None
    )
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[
        DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone1", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[
        DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone2", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[
        DataReeferSupplyAirTemperatureMilliCZone2DecorationsReeferSupplyAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone3", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """


class DataReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""

    decorations: Optional[DataReeferSupplyAirTemperatureMilliCZone2Decorations] = None
    """Decorated values for the primary trailer stat datapoints."""


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataReeferSupplyAirTemperatureMilliCZone3DecorationsGpsReverseGeo] = FieldInfo(
        alias="reverseGeo", default=None
    )
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferAlarms(BaseModel):
    alarms: List[DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone3Decorations(BaseModel):
    carrier_reefer_state: Optional[DataReeferSupplyAirTemperatureMilliCZone3DecorationsCarrierReeferState] = FieldInfo(
        alias="carrierReeferState", default=None
    )
    """Reefer state event."""

    gps: Optional[DataReeferSupplyAirTemperatureMilliCZone3DecorationsGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataReeferSupplyAirTemperatureMilliCZone3DecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferAlarms] = FieldInfo(
        alias="reeferAlarms", default=None
    )
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[
        DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferAmbientAirTemperatureMilliC
    ] = FieldInfo(alias="reeferAmbientAirTemperatureMilliC", default=None)
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferDoorStateZone1] = (
        FieldInfo(alias="reeferDoorStateZone1", default=None)
    )
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferDoorStateZone2] = (
        FieldInfo(alias="reeferDoorStateZone2", default=None)
    )
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferDoorStateZone3] = (
        FieldInfo(alias="reeferDoorStateZone3", default=None)
    )
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferFuelPercent] = FieldInfo(
        alias="reeferFuelPercent", default=None
    )
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferObdEngineSeconds] = (
        FieldInfo(alias="reeferObdEngineSeconds", default=None)
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[
        DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone1", default=None)
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[
        DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone2", default=None)
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[
        DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferReturnAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferReturnAirTemperatureMilliCZone3", default=None)
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferRunMode] = FieldInfo(
        alias="reeferRunMode", default=None
    )
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[
        DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone1", default=None)
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[
        DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone2", default=None)
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[
        DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferSetPointTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSetPointTemperatureMilliCZone3", default=None)
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferStateZone1] = FieldInfo(
        alias="reeferStateZone1", default=None
    )
    """Reefer state event."""

    reefer_state_zone2: Optional[DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferStateZone2] = FieldInfo(
        alias="reeferStateZone2", default=None
    )
    """Reefer state event."""

    reefer_state_zone3: Optional[DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferStateZone3] = FieldInfo(
        alias="reeferStateZone3", default=None
    )
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[
        DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone1
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone1", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[
        DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone2
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone2", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[
        DataReeferSupplyAirTemperatureMilliCZone3DecorationsReeferSupplyAirTemperatureMilliCZone3
    ] = FieldInfo(alias="reeferSupplyAirTemperatureMilliCZone3", default=None)
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """


class DataReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""

    decorations: Optional[DataReeferSupplyAirTemperatureMilliCZone3Decorations] = None
    """Decorated values for the primary trailer stat datapoints."""


class Data(BaseModel):
    id: str
    """ID of the trailer."""

    name: str
    """Name of the vehicle."""

    carrier_reefer_state: Optional[List[DataCarrierReeferState]] = FieldInfo(alias="carrierReeferState", default=None)
    """A list of engine state points."""

    gps: Optional[List[DataGp]] = None
    """A list of GPS points."""

    gps_odometer_meters: Optional[List[DataGpsOdometerMeter]] = FieldInfo(alias="gpsOdometerMeters", default=None)
    """A list of odometer points."""

    reefer_alarms: Optional[List[DataReeferAlarm]] = FieldInfo(alias="reeferAlarms", default=None)
    """A list of reefer alarm points."""

    reefer_ambient_air_temperature_milli_c: Optional[List[DataReeferAmbientAirTemperatureMilliC]] = FieldInfo(
        alias="reeferAmbientAirTemperatureMilliC", default=None
    )
    """A list of ambient air temperature points."""

    reefer_door_state_zone1: Optional[List[DataReeferDoorStateZone1]] = FieldInfo(
        alias="reeferDoorStateZone1", default=None
    )
    """A list of door state points."""

    reefer_door_state_zone2: Optional[List[DataReeferDoorStateZone2]] = FieldInfo(
        alias="reeferDoorStateZone2", default=None
    )
    """A list of door state points."""

    reefer_door_state_zone3: Optional[List[DataReeferDoorStateZone3]] = FieldInfo(
        alias="reeferDoorStateZone3", default=None
    )
    """A list of door state points."""

    reefer_fuel_percent: Optional[List[DataReeferFuelPercent]] = FieldInfo(alias="reeferFuelPercent", default=None)
    """A list of fuel percent points."""

    reefer_obd_engine_seconds: Optional[List[DataReeferObdEngineSecond]] = FieldInfo(
        alias="reeferObdEngineSeconds", default=None
    )
    """A list of engine second points"""

    reefer_return_air_temperature_milli_c_zone1: Optional[List[DataReeferReturnAirTemperatureMilliCZone1]] = FieldInfo(
        alias="reeferReturnAirTemperatureMilliCZone1", default=None
    )
    """A list of return air temperature points."""

    reefer_return_air_temperature_milli_c_zone2: Optional[List[DataReeferReturnAirTemperatureMilliCZone2]] = FieldInfo(
        alias="reeferReturnAirTemperatureMilliCZone2", default=None
    )
    """A list of return air temperature points."""

    reefer_return_air_temperature_milli_c_zone3: Optional[List[DataReeferReturnAirTemperatureMilliCZone3]] = FieldInfo(
        alias="reeferReturnAirTemperatureMilliCZone3", default=None
    )
    """A list of return air temperature points."""

    reefer_run_mode: Optional[List[DataReeferRunMode]] = FieldInfo(alias="reeferRunMode", default=None)
    """A list of run mode points"""

    reefer_set_point_temperature_milli_c_zone1: Optional[List[DataReeferSetPointTemperatureMilliCZone1]] = FieldInfo(
        alias="reeferSetPointTemperatureMilliCZone1", default=None
    )
    """A list of set point temperature points."""

    reefer_set_point_temperature_milli_c_zone2: Optional[List[DataReeferSetPointTemperatureMilliCZone2]] = FieldInfo(
        alias="reeferSetPointTemperatureMilliCZone2", default=None
    )
    """A list of set point temperature points."""

    reefer_set_point_temperature_milli_c_zone3: Optional[List[DataReeferSetPointTemperatureMilliCZone3]] = FieldInfo(
        alias="reeferSetPointTemperatureMilliCZone3", default=None
    )
    """A list of set point temperature points."""

    reefer_state_zone1: Optional[List[DataReeferStateZone1]] = FieldInfo(alias="reeferStateZone1", default=None)
    """A list of engine state points."""

    reefer_state_zone2: Optional[List[DataReeferStateZone2]] = FieldInfo(alias="reeferStateZone2", default=None)
    """A list of engine state points."""

    reefer_state_zone3: Optional[List[DataReeferStateZone3]] = FieldInfo(alias="reeferStateZone3", default=None)
    """A list of engine state points."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[List[DataReeferSupplyAirTemperatureMilliCZone1]] = FieldInfo(
        alias="reeferSupplyAirTemperatureMilliCZone1", default=None
    )
    """A list of supply air temperature points."""

    reefer_supply_air_temperature_milli_c_zone2: Optional[List[DataReeferSupplyAirTemperatureMilliCZone2]] = FieldInfo(
        alias="reeferSupplyAirTemperatureMilliCZone2", default=None
    )
    """A list of supply air temperature points."""

    reefer_supply_air_temperature_milli_c_zone3: Optional[List[DataReeferSupplyAirTemperatureMilliCZone3]] = FieldInfo(
        alias="reeferSupplyAirTemperatureMilliCZone3", default=None
    )
    """A list of supply air temperature points."""


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


class StatHistoryResponse(BaseModel):
    data: List[Data]
    """List of trailers and their stats"""

    pagination: Pagination
    """Pagination parameters."""
