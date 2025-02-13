# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "IncidentStreamResponse",
    "Data",
    "DataCondition",
    "DataConditionDetails",
    "DataConditionDetailsAmbientTemperature",
    "DataConditionDetailsAmbientTemperatureSensor",
    "DataConditionDetailsAmbientTemperatureSensorProduct",
    "DataConditionDetailsAmbientTemperatureSensorTag",
    "DataConditionDetailsCameraConnectorDisconected",
    "DataConditionDetailsCameraConnectorDisconectedDriver",
    "DataConditionDetailsCameraConnectorDisconectedDriverAttribute",
    "DataConditionDetailsCameraConnectorDisconectedDriverTag",
    "DataConditionDetailsCameraConnectorDisconectedTrailer",
    "DataConditionDetailsCameraConnectorDisconectedTrailerAttribute",
    "DataConditionDetailsCameraConnectorDisconectedTrailerTag",
    "DataConditionDetailsCameraConnectorDisconectedVehicle",
    "DataConditionDetailsCameraConnectorDisconectedVehicleAttribute",
    "DataConditionDetailsCameraConnectorDisconectedVehicleStaticAssignedDriver",
    "DataConditionDetailsCameraConnectorDisconectedVehicleTag",
    "DataConditionDetailsCameraStreamIssue",
    "DataConditionDetailsCameraStreamIssueCameraDevice",
    "DataConditionDetailsCameraStreamIssueCameraDeviceSite",
    "DataConditionDetailsCameraStreamIssueCameraDeviceSiteTag",
    "DataConditionDetailsCameraStreamIssueCameraDeviceTag",
    "DataConditionDetailsCellSignalLoss",
    "DataConditionDetailsCellSignalLossDriver",
    "DataConditionDetailsCellSignalLossDriverAttribute",
    "DataConditionDetailsCellSignalLossDriverTag",
    "DataConditionDetailsCellSignalLossTrailer",
    "DataConditionDetailsCellSignalLossTrailerAttribute",
    "DataConditionDetailsCellSignalLossTrailerTag",
    "DataConditionDetailsCellSignalLossVehicle",
    "DataConditionDetailsCellSignalLossVehicleAttribute",
    "DataConditionDetailsCellSignalLossVehicleStaticAssignedDriver",
    "DataConditionDetailsCellSignalLossVehicleTag",
    "DataConditionDetailsCloudBackupUploadIssue",
    "DataConditionDetailsCloudBackupUploadIssueDriver",
    "DataConditionDetailsCloudBackupUploadIssueDriverAttribute",
    "DataConditionDetailsCloudBackupUploadIssueDriverTag",
    "DataConditionDetailsCloudBackupUploadIssueTrailer",
    "DataConditionDetailsCloudBackupUploadIssueTrailerAttribute",
    "DataConditionDetailsCloudBackupUploadIssueTrailerTag",
    "DataConditionDetailsCloudBackupUploadIssueVehicle",
    "DataConditionDetailsCloudBackupUploadIssueVehicleAttribute",
    "DataConditionDetailsCloudBackupUploadIssueVehicleStaticAssignedDriver",
    "DataConditionDetailsCloudBackupUploadIssueVehicleTag",
    "DataConditionDetailsDashcamDisconnected",
    "DataConditionDetailsDashcamDisconnectedDriver",
    "DataConditionDetailsDashcamDisconnectedDriverAttribute",
    "DataConditionDetailsDashcamDisconnectedDriverTag",
    "DataConditionDetailsDashcamDisconnectedTrailer",
    "DataConditionDetailsDashcamDisconnectedTrailerAttribute",
    "DataConditionDetailsDashcamDisconnectedTrailerTag",
    "DataConditionDetailsDashcamDisconnectedVehicle",
    "DataConditionDetailsDashcamDisconnectedVehicleAttribute",
    "DataConditionDetailsDashcamDisconnectedVehicleStaticAssignedDriver",
    "DataConditionDetailsDashcamDisconnectedVehicleTag",
    "DataConditionDetailsDataInputValue",
    "DataConditionDetailsDataInputValueMachineInput",
    "DataConditionDetailsDeviceMovement",
    "DataConditionDetailsDeviceMovementDriver",
    "DataConditionDetailsDeviceMovementDriverAttribute",
    "DataConditionDetailsDeviceMovementDriverTag",
    "DataConditionDetailsDeviceMovementTrailer",
    "DataConditionDetailsDeviceMovementTrailerAttribute",
    "DataConditionDetailsDeviceMovementTrailerTag",
    "DataConditionDetailsDeviceMovementVehicle",
    "DataConditionDetailsDeviceMovementVehicleAttribute",
    "DataConditionDetailsDeviceMovementVehicleStaticAssignedDriver",
    "DataConditionDetailsDeviceMovementVehicleTag",
    "DataConditionDetailsDeviceMovementStopped",
    "DataConditionDetailsDeviceMovementStoppedDriver",
    "DataConditionDetailsDeviceMovementStoppedDriverAttribute",
    "DataConditionDetailsDeviceMovementStoppedDriverTag",
    "DataConditionDetailsDeviceMovementStoppedTrailer",
    "DataConditionDetailsDeviceMovementStoppedTrailerAttribute",
    "DataConditionDetailsDeviceMovementStoppedTrailerTag",
    "DataConditionDetailsDeviceMovementStoppedVehicle",
    "DataConditionDetailsDeviceMovementStoppedVehicleAttribute",
    "DataConditionDetailsDeviceMovementStoppedVehicleStaticAssignedDriver",
    "DataConditionDetailsDeviceMovementStoppedVehicleTag",
    "DataConditionDetailsDriverAppSignIn",
    "DataConditionDetailsDriverAppSignInDriver",
    "DataConditionDetailsDriverAppSignInDriverAttribute",
    "DataConditionDetailsDriverAppSignInDriverTag",
    "DataConditionDetailsDriverAppSignOut",
    "DataConditionDetailsDriverAppSignOutDriver",
    "DataConditionDetailsDriverAppSignOutDriverAttribute",
    "DataConditionDetailsDriverAppSignOutDriverTag",
    "DataConditionDetailsDriverDocumentSubmitted",
    "DataConditionDetailsDriverDocumentSubmittedDocument",
    "DataConditionDetailsDriverDocumentSubmittedDocumentDocumentType",
    "DataConditionDetailsDriverDocumentSubmittedDocumentDriver",
    "DataConditionDetailsDriverDocumentSubmittedDocumentField",
    "DataConditionDetailsDriverDocumentSubmittedDocumentFieldValue",
    "DataConditionDetailsDriverDocumentSubmittedDocumentFieldValueBarcodeValue",
    "DataConditionDetailsDriverDocumentSubmittedDocumentFieldValueDateTimeValue",
    "DataConditionDetailsDriverDocumentSubmittedDocumentFieldValueMultipleChoiceValue",
    "DataConditionDetailsDriverDocumentSubmittedDocumentFieldValuePhotoValue",
    "DataConditionDetailsDriverDocumentSubmittedDocumentFieldValueScannedDocumentValue",
    "DataConditionDetailsDriverDocumentSubmittedDocumentFieldValueSignatureValue",
    "DataConditionDetailsDriverDocumentSubmittedDocumentConditionalFieldSection",
    "DataConditionDetailsDriverDocumentSubmittedDocumentRoute",
    "DataConditionDetailsDriverDocumentSubmittedDocumentRouteStop",
    "DataConditionDetailsDriverDocumentSubmittedDocumentVehicle",
    "DataConditionDetailsDriverMessageReceived",
    "DataConditionDetailsDriverMessageReceivedDriver",
    "DataConditionDetailsDriverMessageReceivedDriverAttribute",
    "DataConditionDetailsDriverMessageReceivedDriverTag",
    "DataConditionDetailsDriverMessageSent",
    "DataConditionDetailsDriverMessageSentDriver",
    "DataConditionDetailsDriverMessageSentDriverAttribute",
    "DataConditionDetailsDriverMessageSentDriverTag",
    "DataConditionDetailsDriverRecorded",
    "DataConditionDetailsDriverRecordedDriver",
    "DataConditionDetailsDriverRecordedDriverAttribute",
    "DataConditionDetailsDriverRecordedDriverTag",
    "DataConditionDetailsDriverRecordedVehicle",
    "DataConditionDetailsDriverRecordedVehicleAttribute",
    "DataConditionDetailsDriverRecordedVehicleStaticAssignedDriver",
    "DataConditionDetailsDriverRecordedVehicleTag",
    "DataConditionDetailsDvirSubmittedDevice",
    "DataConditionDetailsDvirSubmittedDeviceDriver",
    "DataConditionDetailsDvirSubmittedDeviceDvir",
    "DataConditionDetailsDvirSubmittedDeviceDvirAuthorSignature",
    "DataConditionDetailsDvirSubmittedDeviceDvirAuthorSignatureSignatoryUser",
    "DataConditionDetailsDvirSubmittedDeviceDvirDefect",
    "DataConditionDetailsDvirSubmittedDeviceDvirDefectResolvedBy",
    "DataConditionDetailsDvirSubmittedDeviceDvirDefectTrailer",
    "DataConditionDetailsDvirSubmittedDeviceDvirDefectVehicle",
    "DataConditionDetailsDvirSubmittedDeviceDvirDefectVehicleGateway",
    "DataConditionDetailsDvirSubmittedDeviceDvirSecondSignature",
    "DataConditionDetailsDvirSubmittedDeviceDvirSecondSignatureSignatoryUser",
    "DataConditionDetailsDvirSubmittedDeviceDvirThirdSignature",
    "DataConditionDetailsDvirSubmittedDeviceDvirThirdSignatureSignatoryUser",
    "DataConditionDetailsDvirSubmittedDeviceDvirTrailer",
    "DataConditionDetailsDvirSubmittedDeviceVehicle",
    "DataConditionDetailsDvirSubmittedDeviceVehicleGateway",
    "DataConditionDetailsEngineIdle",
    "DataConditionDetailsEngineIdleDriver",
    "DataConditionDetailsEngineIdleDriverAttribute",
    "DataConditionDetailsEngineIdleDriverTag",
    "DataConditionDetailsEngineIdleVehicle",
    "DataConditionDetailsEngineIdleVehicleAttribute",
    "DataConditionDetailsEngineIdleVehicleStaticAssignedDriver",
    "DataConditionDetailsEngineIdleVehicleTag",
    "DataConditionDetailsEngineOff",
    "DataConditionDetailsEngineOffDriver",
    "DataConditionDetailsEngineOffDriverAttribute",
    "DataConditionDetailsEngineOffDriverTag",
    "DataConditionDetailsEngineOffTrailer",
    "DataConditionDetailsEngineOffTrailerAttribute",
    "DataConditionDetailsEngineOffTrailerTag",
    "DataConditionDetailsEngineOffVehicle",
    "DataConditionDetailsEngineOffVehicleAttribute",
    "DataConditionDetailsEngineOffVehicleStaticAssignedDriver",
    "DataConditionDetailsEngineOffVehicleTag",
    "DataConditionDetailsEngineOn",
    "DataConditionDetailsEngineOnDriver",
    "DataConditionDetailsEngineOnDriverAttribute",
    "DataConditionDetailsEngineOnDriverTag",
    "DataConditionDetailsEngineOnTrailer",
    "DataConditionDetailsEngineOnTrailerAttribute",
    "DataConditionDetailsEngineOnTrailerTag",
    "DataConditionDetailsEngineOnVehicle",
    "DataConditionDetailsEngineOnVehicleAttribute",
    "DataConditionDetailsEngineOnVehicleStaticAssignedDriver",
    "DataConditionDetailsEngineOnVehicleTag",
    "DataConditionDetailsFormSubmitted",
    "DataConditionDetailsFormSubmittedForm",
    "DataConditionDetailsFormSubmittedFormField",
    "DataConditionDetailsFormSubmittedFormFieldAssetValue",
    "DataConditionDetailsFormSubmittedFormFieldAssetValueAsset",
    "DataConditionDetailsFormSubmittedFormFieldCheckBoxesValue",
    "DataConditionDetailsFormSubmittedFormFieldDateTimeValue",
    "DataConditionDetailsFormSubmittedFormFieldIssue",
    "DataConditionDetailsFormSubmittedFormFieldMediaList",
    "DataConditionDetailsFormSubmittedFormFieldMediaValue",
    "DataConditionDetailsFormSubmittedFormFieldMediaValueMediaList",
    "DataConditionDetailsFormSubmittedFormFieldMultipleChoiceValue",
    "DataConditionDetailsFormSubmittedFormFieldNumberValue",
    "DataConditionDetailsFormSubmittedFormFieldPersonValue",
    "DataConditionDetailsFormSubmittedFormFieldPersonValuePerson",
    "DataConditionDetailsFormSubmittedFormFieldPersonValuePersonPolymorphicUserID",
    "DataConditionDetailsFormSubmittedFormFieldSignatureValue",
    "DataConditionDetailsFormSubmittedFormFieldSignatureValueMedia",
    "DataConditionDetailsFormSubmittedFormFieldTableValue",
    "DataConditionDetailsFormSubmittedFormFieldTableValueColumn",
    "DataConditionDetailsFormSubmittedFormFieldTableValueRow",
    "DataConditionDetailsFormSubmittedFormFieldTableValueRowCell",
    "DataConditionDetailsFormSubmittedFormFieldTableValueRowCellCheckBoxesValue",
    "DataConditionDetailsFormSubmittedFormFieldTableValueRowCellDateTimeValue",
    "DataConditionDetailsFormSubmittedFormFieldTableValueRowCellMediaValue",
    "DataConditionDetailsFormSubmittedFormFieldTableValueRowCellMediaValueMediaList",
    "DataConditionDetailsFormSubmittedFormFieldTableValueRowCellMultipleChoiceValue",
    "DataConditionDetailsFormSubmittedFormFieldTableValueRowCellNumberValue",
    "DataConditionDetailsFormSubmittedFormFieldTableValueRowCellPersonValue",
    "DataConditionDetailsFormSubmittedFormFieldTableValueRowCellPersonValuePerson",
    "DataConditionDetailsFormSubmittedFormFieldTableValueRowCellPersonValuePersonPolymorphicUserID",
    "DataConditionDetailsFormSubmittedFormFieldTableValueRowCellSignatureValue",
    "DataConditionDetailsFormSubmittedFormFieldTableValueRowCellSignatureValueMedia",
    "DataConditionDetailsFormSubmittedFormFieldTableValueRowCellTextValue",
    "DataConditionDetailsFormSubmittedFormFieldTextValue",
    "DataConditionDetailsFormSubmittedFormFormTemplate",
    "DataConditionDetailsFormSubmittedFormSubmittedBy",
    "DataConditionDetailsFormSubmittedFormAsset",
    "DataConditionDetailsFormSubmittedFormAssignedTo",
    "DataConditionDetailsFormSubmittedFormLocation",
    "DataConditionDetailsFormSubmittedFormScore",
    "DataConditionDetailsFuelLevelPercentage",
    "DataConditionDetailsFuelLevelPercentageDriver",
    "DataConditionDetailsFuelLevelPercentageDriverAttribute",
    "DataConditionDetailsFuelLevelPercentageDriverTag",
    "DataConditionDetailsFuelLevelPercentageTrailer",
    "DataConditionDetailsFuelLevelPercentageTrailerAttribute",
    "DataConditionDetailsFuelLevelPercentageTrailerTag",
    "DataConditionDetailsFuelLevelPercentageVehicle",
    "DataConditionDetailsFuelLevelPercentageVehicleAttribute",
    "DataConditionDetailsFuelLevelPercentageVehicleStaticAssignedDriver",
    "DataConditionDetailsFuelLevelPercentageVehicleTag",
    "DataConditionDetailsGatewayDisconnected",
    "DataConditionDetailsGatewayDisconnectedDriver",
    "DataConditionDetailsGatewayDisconnectedDriverAttribute",
    "DataConditionDetailsGatewayDisconnectedDriverTag",
    "DataConditionDetailsGatewayDisconnectedTrailer",
    "DataConditionDetailsGatewayDisconnectedTrailerAttribute",
    "DataConditionDetailsGatewayDisconnectedTrailerTag",
    "DataConditionDetailsGatewayDisconnectedVehicle",
    "DataConditionDetailsGatewayDisconnectedVehicleAttribute",
    "DataConditionDetailsGatewayDisconnectedVehicleStaticAssignedDriver",
    "DataConditionDetailsGatewayDisconnectedVehicleTag",
    "DataConditionDetailsGatewayUnplugged",
    "DataConditionDetailsGatewayUnpluggedVehicle",
    "DataConditionDetailsGeofenceEntry",
    "DataConditionDetailsGeofenceEntryAddress",
    "DataConditionDetailsGeofenceEntryAddressGeofence",
    "DataConditionDetailsGeofenceEntryAddressGeofenceCircle",
    "DataConditionDetailsGeofenceEntryAddressGeofencePolygon",
    "DataConditionDetailsGeofenceEntryAddressGeofencePolygonVertex",
    "DataConditionDetailsGeofenceEntryAddressGeofenceSettings",
    "DataConditionDetailsGeofenceEntryAddressGeofenceSettingsShowAddress",
    "DataConditionDetailsGeofenceEntryVehicle",
    "DataConditionDetailsGeofenceEntryVehicleGateway",
    "DataConditionDetailsGeofenceExit",
    "DataConditionDetailsGeofenceExitAddress",
    "DataConditionDetailsGeofenceExitAddressGeofence",
    "DataConditionDetailsGeofenceExitAddressGeofenceCircle",
    "DataConditionDetailsGeofenceExitAddressGeofencePolygon",
    "DataConditionDetailsGeofenceExitAddressGeofencePolygonVertex",
    "DataConditionDetailsGeofenceExitAddressGeofenceSettings",
    "DataConditionDetailsGeofenceExitAddressGeofenceSettingsShowAddress",
    "DataConditionDetailsGeofenceExitVehicle",
    "DataConditionDetailsGeofenceExitVehicleGateway",
    "DataConditionDetailsGpsSignalLoss",
    "DataConditionDetailsGpsSignalLossDriver",
    "DataConditionDetailsGpsSignalLossDriverAttribute",
    "DataConditionDetailsGpsSignalLossDriverTag",
    "DataConditionDetailsGpsSignalLossTrailer",
    "DataConditionDetailsGpsSignalLossTrailerAttribute",
    "DataConditionDetailsGpsSignalLossTrailerTag",
    "DataConditionDetailsGpsSignalLossVehicle",
    "DataConditionDetailsGpsSignalLossVehicleAttribute",
    "DataConditionDetailsGpsSignalLossVehicleStaticAssignedDriver",
    "DataConditionDetailsGpsSignalLossVehicleTag",
    "DataConditionDetailsHarshEvent",
    "DataConditionDetailsHarshEventDriver",
    "DataConditionDetailsHarshEventDriverAttribute",
    "DataConditionDetailsHarshEventDriverTag",
    "DataConditionDetailsHarshEventVehicle",
    "DataConditionDetailsHarshEventVehicleAttribute",
    "DataConditionDetailsHarshEventVehicleStaticAssignedDriver",
    "DataConditionDetailsHarshEventVehicleTag",
    "DataConditionDetailsHosViolation",
    "DataConditionDetailsHosViolationDriver",
    "DataConditionDetailsHosViolationDriverAttribute",
    "DataConditionDetailsHosViolationDriverTag",
    "DataConditionDetailsInactivity",
    "DataConditionDetailsInactivityCameraStream",
    "DataConditionDetailsInactivityCameraStreamCameraDevice",
    "DataConditionDetailsInactivityCameraStreamCameraDeviceSite",
    "DataConditionDetailsInactivityCameraStreamCameraDeviceSiteTag",
    "DataConditionDetailsInactivityCameraStreamCameraDeviceTag",
    "DataConditionDetailsInactivityCameraStreamTag",
    "DataConditionDetailsInsideGeofence",
    "DataConditionDetailsInsideGeofenceDriver",
    "DataConditionDetailsInsideGeofenceDriverAttribute",
    "DataConditionDetailsInsideGeofenceDriverTag",
    "DataConditionDetailsInsideGeofenceTrailer",
    "DataConditionDetailsInsideGeofenceTrailerAttribute",
    "DataConditionDetailsInsideGeofenceTrailerTag",
    "DataConditionDetailsInsideGeofenceVehicle",
    "DataConditionDetailsInsideGeofenceVehicleAttribute",
    "DataConditionDetailsInsideGeofenceVehicleStaticAssignedDriver",
    "DataConditionDetailsInsideGeofenceVehicleTag",
    "DataConditionDetailsIssueCreated",
    "DataConditionDetailsIssueCreatedIssue",
    "DataConditionDetailsIssueCreatedIssueIssueSource",
    "DataConditionDetailsIssueCreatedIssueSubmittedBy",
    "DataConditionDetailsIssueCreatedIssueAsset",
    "DataConditionDetailsIssueCreatedIssueAssignedTo",
    "DataConditionDetailsIssueCreatedIssueMediaList",
    "DataConditionDetailsJammingDetected",
    "DataConditionDetailsJammingDetectedDriver",
    "DataConditionDetailsJammingDetectedDriverAttribute",
    "DataConditionDetailsJammingDetectedDriverTag",
    "DataConditionDetailsJammingDetectedTrailer",
    "DataConditionDetailsJammingDetectedTrailerAttribute",
    "DataConditionDetailsJammingDetectedTrailerTag",
    "DataConditionDetailsJammingDetectedVehicle",
    "DataConditionDetailsJammingDetectedVehicleAttribute",
    "DataConditionDetailsJammingDetectedVehicleStaticAssignedDriver",
    "DataConditionDetailsJammingDetectedVehicleTag",
    "DataConditionDetailsMotionDetected",
    "DataConditionDetailsMotionDetectedCameraStream",
    "DataConditionDetailsMotionDetectedCameraStreamCameraDevice",
    "DataConditionDetailsMotionDetectedCameraStreamCameraDeviceSite",
    "DataConditionDetailsMotionDetectedCameraStreamCameraDeviceSiteTag",
    "DataConditionDetailsMotionDetectedCameraStreamCameraDeviceTag",
    "DataConditionDetailsMotionDetectedCameraStreamTag",
    "DataConditionDetailsOutOfRoute",
    "DataConditionDetailsOutOfRouteDriver",
    "DataConditionDetailsOutOfRouteDriverAttribute",
    "DataConditionDetailsOutOfRouteDriverTag",
    "DataConditionDetailsOutOfRouteTrailer",
    "DataConditionDetailsOutOfRouteTrailerAttribute",
    "DataConditionDetailsOutOfRouteTrailerTag",
    "DataConditionDetailsOutOfRouteVehicle",
    "DataConditionDetailsOutOfRouteVehicleAttribute",
    "DataConditionDetailsOutOfRouteVehicleStaticAssignedDriver",
    "DataConditionDetailsOutOfRouteVehicleTag",
    "DataConditionDetailsOutsideGeofence",
    "DataConditionDetailsOutsideGeofenceDriver",
    "DataConditionDetailsOutsideGeofenceDriverAttribute",
    "DataConditionDetailsOutsideGeofenceDriverTag",
    "DataConditionDetailsOutsideGeofenceTrailer",
    "DataConditionDetailsOutsideGeofenceTrailerAttribute",
    "DataConditionDetailsOutsideGeofenceTrailerTag",
    "DataConditionDetailsOutsideGeofenceVehicle",
    "DataConditionDetailsOutsideGeofenceVehicleAttribute",
    "DataConditionDetailsOutsideGeofenceVehicleStaticAssignedDriver",
    "DataConditionDetailsOutsideGeofenceVehicleTag",
    "DataConditionDetailsPanicButton",
    "DataConditionDetailsPanicButtonDriver",
    "DataConditionDetailsPanicButtonDriverAttribute",
    "DataConditionDetailsPanicButtonDriverTag",
    "DataConditionDetailsPanicButtonTrailer",
    "DataConditionDetailsPanicButtonTrailerAttribute",
    "DataConditionDetailsPanicButtonTrailerTag",
    "DataConditionDetailsPanicButtonVehicle",
    "DataConditionDetailsPanicButtonVehicleAttribute",
    "DataConditionDetailsPanicButtonVehicleStaticAssignedDriver",
    "DataConditionDetailsPanicButtonVehicleTag",
    "DataConditionDetailsPersonDetected",
    "DataConditionDetailsPersonDetectedCameraStream",
    "DataConditionDetailsPersonDetectedCameraStreamCameraDevice",
    "DataConditionDetailsPersonDetectedCameraStreamCameraDeviceSite",
    "DataConditionDetailsPersonDetectedCameraStreamCameraDeviceSiteTag",
    "DataConditionDetailsPersonDetectedCameraStreamCameraDeviceTag",
    "DataConditionDetailsPersonDetectedCameraStreamTag",
    "DataConditionDetailsReeferTemperature",
    "DataConditionDetailsReeferTemperatureDriver",
    "DataConditionDetailsReeferTemperatureDriverAttribute",
    "DataConditionDetailsReeferTemperatureDriverTag",
    "DataConditionDetailsReeferTemperatureTrailer",
    "DataConditionDetailsReeferTemperatureTrailerAttribute",
    "DataConditionDetailsReeferTemperatureTrailerTag",
    "DataConditionDetailsReeferTemperatureVehicle",
    "DataConditionDetailsReeferTemperatureVehicleAttribute",
    "DataConditionDetailsReeferTemperatureVehicleStaticAssignedDriver",
    "DataConditionDetailsReeferTemperatureVehicleTag",
    "DataConditionDetailsRouteStopArrival",
    "DataConditionDetailsRouteStopArrivalRoute",
    "DataConditionDetailsRouteStopArrivalRouteSettings",
    "DataConditionDetailsRouteStopArrivalRouteStop",
    "DataConditionDetailsRouteStopArrivalRouteStopAddress",
    "DataConditionDetailsRouteStopArrivalRouteStopDocument",
    "DataConditionDetailsRouteStopArrivalRouteStopLocationLiveSharingLink",
    "DataConditionDetailsRouteStopArrivalRouteStopSingleUseLocation",
    "DataConditionDetailsRouteStopArrivalRouteStopDetails",
    "DataConditionDetailsRouteStopArrivalDriver",
    "DataConditionDetailsRouteStopArrivalVehicle",
    "DataConditionDetailsRouteStopArrivalVehicleGateway",
    "DataConditionDetailsRouteStopDeparture",
    "DataConditionDetailsRouteStopDepartureRoute",
    "DataConditionDetailsRouteStopDepartureRouteSettings",
    "DataConditionDetailsRouteStopDepartureRouteStop",
    "DataConditionDetailsRouteStopDepartureRouteStopAddress",
    "DataConditionDetailsRouteStopDepartureRouteStopDocument",
    "DataConditionDetailsRouteStopDepartureRouteStopLocationLiveSharingLink",
    "DataConditionDetailsRouteStopDepartureRouteStopSingleUseLocation",
    "DataConditionDetailsRouteStopDepartureRouteStopDetails",
    "DataConditionDetailsRouteStopDepartureDriver",
    "DataConditionDetailsRouteStopDepartureVehicle",
    "DataConditionDetailsRouteStopDepartureVehicleGateway",
    "DataConditionDetailsRouteStopEta",
    "DataConditionDetailsRouteStopEtaDriver",
    "DataConditionDetailsRouteStopEtaDriverAttribute",
    "DataConditionDetailsRouteStopEtaDriverTag",
    "DataConditionDetailsRouteStopEtaTrailer",
    "DataConditionDetailsRouteStopEtaTrailerAttribute",
    "DataConditionDetailsRouteStopEtaTrailerTag",
    "DataConditionDetailsRouteStopEtaVehicle",
    "DataConditionDetailsRouteStopEtaVehicleAttribute",
    "DataConditionDetailsRouteStopEtaVehicleStaticAssignedDriver",
    "DataConditionDetailsRouteStopEtaVehicleTag",
    "DataConditionDetailsScheduledMaintenance",
    "DataConditionDetailsScheduledMaintenanceDriver",
    "DataConditionDetailsScheduledMaintenanceDriverAttribute",
    "DataConditionDetailsScheduledMaintenanceDriverTag",
    "DataConditionDetailsScheduledMaintenanceTrailer",
    "DataConditionDetailsScheduledMaintenanceTrailerAttribute",
    "DataConditionDetailsScheduledMaintenanceTrailerTag",
    "DataConditionDetailsScheduledMaintenanceVehicle",
    "DataConditionDetailsScheduledMaintenanceVehicleAttribute",
    "DataConditionDetailsScheduledMaintenanceVehicleStaticAssignedDriver",
    "DataConditionDetailsScheduledMaintenanceVehicleTag",
    "DataConditionDetailsScheduledMaintenanceByEngineHours",
    "DataConditionDetailsScheduledMaintenanceByEngineHoursDriver",
    "DataConditionDetailsScheduledMaintenanceByEngineHoursDriverAttribute",
    "DataConditionDetailsScheduledMaintenanceByEngineHoursDriverTag",
    "DataConditionDetailsScheduledMaintenanceByEngineHoursTrailer",
    "DataConditionDetailsScheduledMaintenanceByEngineHoursTrailerAttribute",
    "DataConditionDetailsScheduledMaintenanceByEngineHoursTrailerTag",
    "DataConditionDetailsScheduledMaintenanceByEngineHoursVehicle",
    "DataConditionDetailsScheduledMaintenanceByEngineHoursVehicleAttribute",
    "DataConditionDetailsScheduledMaintenanceByEngineHoursVehicleStaticAssignedDriver",
    "DataConditionDetailsScheduledMaintenanceByEngineHoursVehicleTag",
    "DataConditionDetailsScheduledMaintenanceOdometer",
    "DataConditionDetailsScheduledMaintenanceOdometerDriver",
    "DataConditionDetailsScheduledMaintenanceOdometerDriverAttribute",
    "DataConditionDetailsScheduledMaintenanceOdometerDriverTag",
    "DataConditionDetailsScheduledMaintenanceOdometerTrailer",
    "DataConditionDetailsScheduledMaintenanceOdometerTrailerAttribute",
    "DataConditionDetailsScheduledMaintenanceOdometerTrailerTag",
    "DataConditionDetailsScheduledMaintenanceOdometerVehicle",
    "DataConditionDetailsScheduledMaintenanceOdometerVehicleAttribute",
    "DataConditionDetailsScheduledMaintenanceOdometerVehicleStaticAssignedDriver",
    "DataConditionDetailsScheduledMaintenanceOdometerVehicleTag",
    "DataConditionDetailsSevereSpeeding",
    "DataConditionDetailsSevereSpeedingData",
    "DataConditionDetailsSevereSpeedingDataVehicle",
    "DataConditionDetailsSiteGatewayDisconnected",
    "DataConditionDetailsSiteGatewayDisconnectedDriver",
    "DataConditionDetailsSiteGatewayDisconnectedDriverAttribute",
    "DataConditionDetailsSiteGatewayDisconnectedDriverTag",
    "DataConditionDetailsSiteGatewayDisconnectedTrailer",
    "DataConditionDetailsSiteGatewayDisconnectedTrailerAttribute",
    "DataConditionDetailsSiteGatewayDisconnectedTrailerTag",
    "DataConditionDetailsSiteGatewayDisconnectedVehicle",
    "DataConditionDetailsSiteGatewayDisconnectedVehicleAttribute",
    "DataConditionDetailsSiteGatewayDisconnectedVehicleStaticAssignedDriver",
    "DataConditionDetailsSiteGatewayDisconnectedVehicleTag",
    "DataConditionDetailsSpeed",
    "DataConditionDetailsSpeedDriver",
    "DataConditionDetailsSpeedDriverAttribute",
    "DataConditionDetailsSpeedDriverTag",
    "DataConditionDetailsSpeedTrailer",
    "DataConditionDetailsSpeedTrailerAttribute",
    "DataConditionDetailsSpeedTrailerTag",
    "DataConditionDetailsSpeedVehicle",
    "DataConditionDetailsSpeedVehicleAttribute",
    "DataConditionDetailsSpeedVehicleStaticAssignedDriver",
    "DataConditionDetailsSpeedVehicleTag",
    "DataConditionDetailsTamperingDetected",
    "DataConditionDetailsTamperingDetectedDriver",
    "DataConditionDetailsTamperingDetectedDriverAttribute",
    "DataConditionDetailsTamperingDetectedDriverTag",
    "DataConditionDetailsTamperingDetectedTrailer",
    "DataConditionDetailsTamperingDetectedTrailerAttribute",
    "DataConditionDetailsTamperingDetectedTrailerTag",
    "DataConditionDetailsTamperingDetectedVehicle",
    "DataConditionDetailsTamperingDetectedVehicleAttribute",
    "DataConditionDetailsTamperingDetectedVehicleStaticAssignedDriver",
    "DataConditionDetailsTamperingDetectedVehicleTag",
    "DataConditionDetailsTireFaults",
    "DataConditionDetailsTireFaultsDriver",
    "DataConditionDetailsTireFaultsDriverAttribute",
    "DataConditionDetailsTireFaultsDriverTag",
    "DataConditionDetailsTireFaultsTrailer",
    "DataConditionDetailsTireFaultsTrailerAttribute",
    "DataConditionDetailsTireFaultsTrailerTag",
    "DataConditionDetailsTireFaultsVehicle",
    "DataConditionDetailsTireFaultsVehicleAttribute",
    "DataConditionDetailsTireFaultsVehicleStaticAssignedDriver",
    "DataConditionDetailsTireFaultsVehicleTag",
    "DataConditionDetailsUnassignedDriving",
    "DataConditionDetailsUnassignedDrivingDriver",
    "DataConditionDetailsUnassignedDrivingDriverAttribute",
    "DataConditionDetailsUnassignedDrivingDriverTag",
    "DataConditionDetailsUnassignedDrivingVehicle",
    "DataConditionDetailsUnassignedDrivingVehicleAttribute",
    "DataConditionDetailsUnassignedDrivingVehicleStaticAssignedDriver",
    "DataConditionDetailsUnassignedDrivingVehicleTag",
    "DataConditionDetailsVehicleBatteryVoltage",
    "DataConditionDetailsVehicleBatteryVoltageDriver",
    "DataConditionDetailsVehicleBatteryVoltageDriverAttribute",
    "DataConditionDetailsVehicleBatteryVoltageDriverTag",
    "DataConditionDetailsVehicleBatteryVoltageTrailer",
    "DataConditionDetailsVehicleBatteryVoltageTrailerAttribute",
    "DataConditionDetailsVehicleBatteryVoltageTrailerTag",
    "DataConditionDetailsVehicleBatteryVoltageVehicle",
    "DataConditionDetailsVehicleBatteryVoltageVehicleAttribute",
    "DataConditionDetailsVehicleBatteryVoltageVehicleStaticAssignedDriver",
    "DataConditionDetailsVehicleBatteryVoltageVehicleTag",
    "DataConditionDetailsVehicleDefLevelPercentage",
    "DataConditionDetailsVehicleDefLevelPercentageDriver",
    "DataConditionDetailsVehicleDefLevelPercentageDriverAttribute",
    "DataConditionDetailsVehicleDefLevelPercentageDriverTag",
    "DataConditionDetailsVehicleDefLevelPercentageTrailer",
    "DataConditionDetailsVehicleDefLevelPercentageTrailerAttribute",
    "DataConditionDetailsVehicleDefLevelPercentageTrailerTag",
    "DataConditionDetailsVehicleDefLevelPercentageVehicle",
    "DataConditionDetailsVehicleDefLevelPercentageVehicleAttribute",
    "DataConditionDetailsVehicleDefLevelPercentageVehicleStaticAssignedDriver",
    "DataConditionDetailsVehicleDefLevelPercentageVehicleTag",
    "DataConditionDetailsVehicleDetected",
    "DataConditionDetailsVehicleDetectedCameraStream",
    "DataConditionDetailsVehicleDetectedCameraStreamCameraDevice",
    "DataConditionDetailsVehicleDetectedCameraStreamCameraDeviceSite",
    "DataConditionDetailsVehicleDetectedCameraStreamCameraDeviceSiteTag",
    "DataConditionDetailsVehicleDetectedCameraStreamCameraDeviceTag",
    "DataConditionDetailsVehicleDetectedCameraStreamTag",
    "DataConditionDetailsVehicleFaults",
    "DataConditionDetailsVehicleFaultsDriver",
    "DataConditionDetailsVehicleFaultsDriverAttribute",
    "DataConditionDetailsVehicleFaultsDriverTag",
    "DataConditionDetailsVehicleFaultsTrailer",
    "DataConditionDetailsVehicleFaultsTrailerAttribute",
    "DataConditionDetailsVehicleFaultsTrailerTag",
    "DataConditionDetailsVehicleFaultsVehicle",
    "DataConditionDetailsVehicleFaultsVehicleAttribute",
    "DataConditionDetailsVehicleFaultsVehicleStaticAssignedDriver",
    "DataConditionDetailsVehicleFaultsVehicleTag",
    "Pagination",
]


class DataConditionDetailsAmbientTemperatureSensorProduct(BaseModel):
    short_name: Optional[str] = FieldInfo(alias="shortName", default=None)
    """The short name associated with the product."""


class DataConditionDetailsAmbientTemperatureSensorTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsAmbientTemperatureSensor(BaseModel):
    id: str
    """Thye ID of the sensor associated with the alert"""

    name: Optional[str] = None
    """The name of the sensor."""

    pinned_device_id: Optional[str] = FieldInfo(alias="pinnedDeviceId", default=None)
    """The Pinned Device ID associated with the alert"""

    product: Optional[DataConditionDetailsAmbientTemperatureSensorProduct] = None
    """The product associated with the alert"""

    tags: Optional[List[DataConditionDetailsAmbientTemperatureSensorTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the sensor.
    """


class DataConditionDetailsAmbientTemperature(BaseModel):
    sensor: Optional[DataConditionDetailsAmbientTemperatureSensor] = None
    """A sensor associated with the alert."""


class DataConditionDetailsCameraConnectorDisconectedDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsCameraConnectorDisconectedDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsCameraConnectorDisconectedDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsCameraConnectorDisconectedDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsCameraConnectorDisconectedDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsCameraConnectorDisconectedTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsCameraConnectorDisconectedTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsCameraConnectorDisconectedTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsCameraConnectorDisconectedTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsCameraConnectorDisconectedTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsCameraConnectorDisconectedVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsCameraConnectorDisconectedVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsCameraConnectorDisconectedVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsCameraConnectorDisconectedVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsCameraConnectorDisconectedVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsCameraConnectorDisconectedVehicleStaticAssignedDriver] = (
        FieldInfo(alias="staticAssignedDriver", default=None)
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsCameraConnectorDisconectedVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsCameraConnectorDisconected(BaseModel):
    driver: Optional[DataConditionDetailsCameraConnectorDisconectedDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsCameraConnectorDisconectedTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsCameraConnectorDisconectedVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsCameraStreamIssueCameraDeviceSiteTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsCameraStreamIssueCameraDeviceSite(BaseModel):
    id: str
    """The ID of the site associated with the alert"""

    name: Optional[str] = None
    """The name of the site"""

    tags: Optional[List[DataConditionDetailsCameraStreamIssueCameraDeviceSiteTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Site.
    """


class DataConditionDetailsCameraStreamIssueCameraDeviceTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsCameraStreamIssueCameraDevice(BaseModel):
    id: str
    """The ID of the camera device associated with the alert"""

    name: Optional[str] = None
    """The name of the camera device"""

    sites: Optional[List[DataConditionDetailsCameraStreamIssueCameraDeviceSite]] = None
    """The list of sites associated with the camera device."""

    tags: Optional[List[DataConditionDetailsCameraStreamIssueCameraDeviceTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the camera device.
    """


class DataConditionDetailsCameraStreamIssue(BaseModel):
    camera_device: Optional[DataConditionDetailsCameraStreamIssueCameraDevice] = FieldInfo(
        alias="cameraDevice", default=None
    )
    """A camera device associated with the alert"""


class DataConditionDetailsCellSignalLossDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsCellSignalLossDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsCellSignalLossDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsCellSignalLossDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsCellSignalLossDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsCellSignalLossTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsCellSignalLossTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsCellSignalLossTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsCellSignalLossTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsCellSignalLossTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsCellSignalLossVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsCellSignalLossVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsCellSignalLossVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsCellSignalLossVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsCellSignalLossVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsCellSignalLossVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsCellSignalLossVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsCellSignalLoss(BaseModel):
    driver: Optional[DataConditionDetailsCellSignalLossDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsCellSignalLossTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsCellSignalLossVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsCloudBackupUploadIssueDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsCloudBackupUploadIssueDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsCloudBackupUploadIssueDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsCloudBackupUploadIssueDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsCloudBackupUploadIssueDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsCloudBackupUploadIssueTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsCloudBackupUploadIssueTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsCloudBackupUploadIssueTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsCloudBackupUploadIssueTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsCloudBackupUploadIssueTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsCloudBackupUploadIssueVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsCloudBackupUploadIssueVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsCloudBackupUploadIssueVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsCloudBackupUploadIssueVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsCloudBackupUploadIssueVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsCloudBackupUploadIssueVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsCloudBackupUploadIssueVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsCloudBackupUploadIssue(BaseModel):
    driver: Optional[DataConditionDetailsCloudBackupUploadIssueDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsCloudBackupUploadIssueTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsCloudBackupUploadIssueVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsDashcamDisconnectedDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsDashcamDisconnectedDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsDashcamDisconnectedDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsDashcamDisconnectedDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsDashcamDisconnectedDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsDashcamDisconnectedTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsDashcamDisconnectedTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsDashcamDisconnectedTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsDashcamDisconnectedTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsDashcamDisconnectedTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsDashcamDisconnectedVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsDashcamDisconnectedVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsDashcamDisconnectedVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsDashcamDisconnectedVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsDashcamDisconnectedVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsDashcamDisconnectedVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsDashcamDisconnectedVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsDashcamDisconnected(BaseModel):
    driver: Optional[DataConditionDetailsDashcamDisconnectedDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsDashcamDisconnectedTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsDashcamDisconnectedVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsDataInputValueMachineInput(BaseModel):
    id: str
    """The ID of the machine input associated with the alert."""

    name: Optional[str] = None
    """The name of the machine input."""


class DataConditionDetailsDataInputValue(BaseModel):
    machine_input: Optional[DataConditionDetailsDataInputValueMachineInput] = FieldInfo(
        alias="machineInput", default=None
    )
    """A machine input associated with the alert"""


class DataConditionDetailsDeviceMovementDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsDeviceMovementDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsDeviceMovementDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsDeviceMovementDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsDeviceMovementDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsDeviceMovementTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsDeviceMovementTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsDeviceMovementTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsDeviceMovementTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsDeviceMovementTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsDeviceMovementVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsDeviceMovementVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsDeviceMovementVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsDeviceMovementVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsDeviceMovementVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsDeviceMovementVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsDeviceMovementVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsDeviceMovement(BaseModel):
    driver: Optional[DataConditionDetailsDeviceMovementDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsDeviceMovementTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsDeviceMovementVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsDeviceMovementStoppedDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsDeviceMovementStoppedDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsDeviceMovementStoppedDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsDeviceMovementStoppedDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsDeviceMovementStoppedDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsDeviceMovementStoppedTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsDeviceMovementStoppedTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsDeviceMovementStoppedTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsDeviceMovementStoppedTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsDeviceMovementStoppedTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsDeviceMovementStoppedVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsDeviceMovementStoppedVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsDeviceMovementStoppedVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsDeviceMovementStoppedVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsDeviceMovementStoppedVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsDeviceMovementStoppedVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsDeviceMovementStoppedVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsDeviceMovementStopped(BaseModel):
    driver: Optional[DataConditionDetailsDeviceMovementStoppedDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsDeviceMovementStoppedTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsDeviceMovementStoppedVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsDriverAppSignInDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsDriverAppSignInDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsDriverAppSignInDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsDriverAppSignInDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsDriverAppSignInDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsDriverAppSignIn(BaseModel):
    driver: Optional[DataConditionDetailsDriverAppSignInDriver] = None
    """A driver associated with the alert"""


class DataConditionDetailsDriverAppSignOutDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsDriverAppSignOutDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsDriverAppSignOutDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsDriverAppSignOutDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsDriverAppSignOutDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsDriverAppSignOut(BaseModel):
    driver: Optional[DataConditionDetailsDriverAppSignOutDriver] = None
    """A driver associated with the alert"""


class DataConditionDetailsDriverDocumentSubmittedDocumentDocumentType(BaseModel):
    id: Optional[str] = None
    """ID of the document type."""

    name: Optional[str] = None
    """Name of the document type."""


class DataConditionDetailsDriverDocumentSubmittedDocumentDriver(BaseModel):
    id: str
    """ID of the driver"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the driver"""


class DataConditionDetailsDriverDocumentSubmittedDocumentFieldValueBarcodeValue(BaseModel):
    barcode_type: Optional[str] = FieldInfo(alias="barcodeType", default=None)
    """The barcode type that was scanned."""

    barcode_value: Optional[str] = FieldInfo(alias="barcodeValue", default=None)
    """The captured barcode value."""


class DataConditionDetailsDriverDocumentSubmittedDocumentFieldValueDateTimeValue(BaseModel):
    date_time: Optional[datetime] = FieldInfo(alias="dateTime", default=None)
    """Date time value inin RFC 3339 format."""


class DataConditionDetailsDriverDocumentSubmittedDocumentFieldValueMultipleChoiceValue(BaseModel):
    selected: Optional[bool] = None
    """Boolean representing if the choice has been selected."""

    value: Optional[str] = None
    """Description of the choice."""


class DataConditionDetailsDriverDocumentSubmittedDocumentFieldValuePhotoValue(BaseModel):
    id: Optional[str] = None
    """Id of the photo."""

    url: Optional[str] = None
    """Url of the photo."""


class DataConditionDetailsDriverDocumentSubmittedDocumentFieldValueScannedDocumentValue(BaseModel):
    id: Optional[str] = None
    """Id of the scanned document."""

    url: Optional[str] = None
    """Url of the scanned document."""


class DataConditionDetailsDriverDocumentSubmittedDocumentFieldValueSignatureValue(BaseModel):
    id: Optional[str] = None
    """Id of the signature field."""

    name: Optional[str] = None
    """Name of the signee for a signature field."""

    signed_at_time: Optional[datetime] = FieldInfo(alias="signedAtTime", default=None)
    """Time the signature was captured in RFC 3339 format."""

    url: Optional[str] = None
    """Url of a signature field's PNG signature image."""


class DataConditionDetailsDriverDocumentSubmittedDocumentFieldValue(BaseModel):
    barcode_value: Optional[List[DataConditionDetailsDriverDocumentSubmittedDocumentFieldValueBarcodeValue]] = (
        FieldInfo(alias="barcodeValue", default=None)
    )
    """The value of a barcode scanning field.

    Only present for barcode scanning fields.
    """

    date_time_value: Optional[DataConditionDetailsDriverDocumentSubmittedDocumentFieldValueDateTimeValue] = FieldInfo(
        alias="dateTimeValue", default=None
    )
    """The value of a date time field. Only present for date time fields."""

    multiple_choice_value: Optional[
        List[DataConditionDetailsDriverDocumentSubmittedDocumentFieldValueMultipleChoiceValue]
    ] = FieldInfo(alias="multipleChoiceValue", default=None)
    """The value of a multiple choice field. Only present for multiple choice fields."""

    number_value: Optional[float] = FieldInfo(alias="numberValue", default=None)
    """The value of a number field. Only present for number fields."""

    photo_value: Optional[List[DataConditionDetailsDriverDocumentSubmittedDocumentFieldValuePhotoValue]] = FieldInfo(
        alias="photoValue", default=None
    )
    """The value of a photo field. Only present for photo fields."""

    scanned_document_value: Optional[
        List[DataConditionDetailsDriverDocumentSubmittedDocumentFieldValueScannedDocumentValue]
    ] = FieldInfo(alias="scannedDocumentValue", default=None)
    """The value of a scanned document field.

    Only present for scanned document fields.
    """

    signature_value: Optional[DataConditionDetailsDriverDocumentSubmittedDocumentFieldValueSignatureValue] = FieldInfo(
        alias="signatureValue", default=None
    )
    """The value of a signature field. Only present for signature fields."""

    string_value: Optional[str] = FieldInfo(alias="stringValue", default=None)
    """The value of a string field. Only present for string fields."""


class DataConditionDetailsDriverDocumentSubmittedDocumentField(BaseModel):
    label: str
    """The name of the field."""

    type: Literal["photo", "string", "number", "multipleChoice", "signature", "dateTime", "scannedDocument", "barcode"]
    """The type of field.

    Valid values: `photo`, `string`, `number`, `multipleChoice`, `signature`,
    `dateTime`, `scannedDocument`, `barcode`
    """

    value: DataConditionDetailsDriverDocumentSubmittedDocumentFieldValue
    """The value of the document field. The shape of value depends on the type."""


class DataConditionDetailsDriverDocumentSubmittedDocumentConditionalFieldSection(BaseModel):
    conditional_field_first_index: Optional[int] = FieldInfo(alias="conditionalFieldFirstIndex", default=None)
    """
    The index of the first conditional field associated with the
    triggeringFieldValue in the fieldTypes list.
    """

    conditional_field_last_index: Optional[int] = FieldInfo(alias="conditionalFieldLastIndex", default=None)
    """
    The index of the last conditional field associated with the triggeringFieldValue
    in the fieldTypes list.
    """

    triggering_field_index: Optional[int] = FieldInfo(alias="triggeringFieldIndex", default=None)
    """
    The index of the multiple choice field in the fieldTypes list that triggers one
    or more conditional fields.
    """

    triggering_field_value: Optional[str] = FieldInfo(alias="triggeringFieldValue", default=None)
    """The multiple choice option value that triggers the conditional fields."""


class DataConditionDetailsDriverDocumentSubmittedDocumentRoute(BaseModel):
    id: str
    """Unique identifier for the route."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the route."""


class DataConditionDetailsDriverDocumentSubmittedDocumentRouteStop(BaseModel):
    id: Optional[str] = None
    """Id of the route stop"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the route stop"""


class DataConditionDetailsDriverDocumentSubmittedDocumentVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the vehicle"""


class DataConditionDetailsDriverDocumentSubmittedDocument(BaseModel):
    id: str
    """Universally unique identifier for the document."""

    created_at_time: datetime = FieldInfo(alias="createdAtTime")
    """Time the document was created in RFC 3339 format."""

    document_type: DataConditionDetailsDriverDocumentSubmittedDocumentDocumentType = FieldInfo(alias="documentType")
    """A minified document type object"""

    driver: DataConditionDetailsDriverDocumentSubmittedDocumentDriver
    """A minified driver object.

    This object is only returned if the route is assigned to the driver.
    """

    fields: List[DataConditionDetailsDriverDocumentSubmittedDocumentField]
    """The fields associated with this document."""

    state: Literal["submitted", "required", "archived"]
    """The condition of the document created for the driver.

    Can be either Required or Submitted. Required documents are pre-populated
    documents for the Driver to fill out in the Driver App and have not yet been
    submitted. Submitted documents have been submitted by the driver in the Driver
    App. Archived documents have been archived by the admin in the cloud dashboard.
    Valid values: `submitted`, `required`, `archived`
    """

    conditional_field_sections: Optional[
        List[DataConditionDetailsDriverDocumentSubmittedDocumentConditionalFieldSection]
    ] = FieldInfo(alias="conditionalFieldSections", default=None)
    """List of the document conditional field sections."""

    name: Optional[str] = None
    """Name of the document."""

    notes: Optional[str] = None
    """Notes on the document."""

    route: Optional[DataConditionDetailsDriverDocumentSubmittedDocumentRoute] = None
    """A minified representation of a single route."""

    route_stop: Optional[DataConditionDetailsDriverDocumentSubmittedDocumentRouteStop] = FieldInfo(
        alias="routeStop", default=None
    )
    """A minified route stop object"""

    updated_at_time: Optional[datetime] = FieldInfo(alias="updatedAtTime", default=None)
    """Time the document was updated in RFC 3339 format."""

    vehicle: Optional[DataConditionDetailsDriverDocumentSubmittedDocumentVehicle] = None
    """A minified vehicle object.

    This object is only returned if the route is assigned to the vehicle.
    """


class DataConditionDetailsDriverDocumentSubmitted(BaseModel):
    document: Optional[DataConditionDetailsDriverDocumentSubmittedDocument] = None
    """A single document."""


class DataConditionDetailsDriverMessageReceivedDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsDriverMessageReceivedDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsDriverMessageReceivedDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsDriverMessageReceivedDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsDriverMessageReceivedDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsDriverMessageReceived(BaseModel):
    driver: Optional[DataConditionDetailsDriverMessageReceivedDriver] = None
    """A driver associated with the alert"""


class DataConditionDetailsDriverMessageSentDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsDriverMessageSentDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsDriverMessageSentDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsDriverMessageSentDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsDriverMessageSentDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsDriverMessageSent(BaseModel):
    driver: Optional[DataConditionDetailsDriverMessageSentDriver] = None
    """A driver associated with the alert"""


class DataConditionDetailsDriverRecordedDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsDriverRecordedDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsDriverRecordedDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsDriverRecordedDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsDriverRecordedDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsDriverRecordedVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsDriverRecordedVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsDriverRecordedVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsDriverRecordedVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsDriverRecordedVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsDriverRecordedVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsDriverRecordedVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsDriverRecorded(BaseModel):
    driver: Optional[DataConditionDetailsDriverRecordedDriver] = None
    """A driver associated with the alert"""

    vehicle: Optional[DataConditionDetailsDriverRecordedVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsDvirSubmittedDeviceDriver(BaseModel):
    id: str
    """ID of the driver"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the driver"""


class DataConditionDetailsDvirSubmittedDeviceDvirAuthorSignatureSignatoryUser(BaseModel):
    id: str
    """ID of the user."""

    name: str
    """Name of the user."""


class DataConditionDetailsDvirSubmittedDeviceDvirAuthorSignature(BaseModel):
    signatory_user: DataConditionDetailsDvirSubmittedDeviceDvirAuthorSignatureSignatoryUser = FieldInfo(
        alias="signatoryUser"
    )
    """The user who signed the DVIR."""

    signed_at_time: str = FieldInfo(alias="signedAtTime")
    """The time when the DVIR was signed. UTC timestamp in RFC 3339 format."""

    type: Literal["driver", "mechanic"]
    """Whether the DVIR was submitted by a driver or mechanic.

    Valid values: `driver`, `mechanic`
    """


class DataConditionDetailsDvirSubmittedDeviceDvirDefectResolvedBy(BaseModel):
    id: str
    """ID of the entity that resolved this defect.

    If the defect was resolved by a driver, this will be a Samsara Driver ID. If the
    defect was resolved by a mechanic, this will be the Samsara Dashboard User ID of
    the mechanic.
    """

    name: str
    """Name of the person who resolved this defect."""

    type: Literal["driver", "mechanic"]
    """Indicates whether this defect was resolved by a driver or a mechanic.

    Valid values: `driver`, `mechanic`
    """


class DataConditionDetailsDvirSubmittedDeviceDvirDefectTrailer(BaseModel):
    id: Optional[str] = None
    """ID of the trailer"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the trailer"""


class DataConditionDetailsDvirSubmittedDeviceDvirDefectVehicleGateway(BaseModel):
    model: Literal[
        "AG15",
        "AG24",
        "AG24EU",
        "AG26",
        "AG26EU",
        "AG41",
        "AG41EU",
        "AG45",
        "AG45EU",
        "AG46",
        "AG46EU",
        "AG46P",
        "AG46PEU",
        "AG51",
        "AG51EU",
        "AG52",
        "AG52EU",
        "AG53",
        "AG53EU",
        "IG15",
        "IG21",
        "IG41",
        "IG61",
        "SG1",
        "SG1B",
        "SG1G",
        "SG1G32",
        "SG1x",
        "VG32",
        "VG33",
        "VG34",
        "VG34EU",
        "VG34FN",
        "VG34M",
        "VG54ATT",
        "VG54EU",
        "VG54FN",
        "VG54NA",
        "VG54NAE",
        "VG54NAH",
        "VG55EU",
        "VG55FN",
        "VG55NA",
    ]
    """The model of the gateway installed on the asset.

    Valid values: `AG15`, `AG24`, `AG24EU`, `AG26`, `AG26EU`, `AG41`, `AG41EU`,
    `AG45`, `AG45EU`, `AG46`, `AG46EU`, `AG46P`, `AG46PEU`, `AG51`, `AG51EU`,
    `AG52`, `AG52EU`, `AG53`, `AG53EU`, `IG15`, `IG21`, `IG41`, `IG61`, `SG1`,
    `SG1B`, `SG1G`, `SG1G32`, `SG1x`, `VG32`, `VG33`, `VG34`, `VG34EU`, `VG34FN`,
    `VG34M`, `VG54ATT`, `VG54EU`, `VG54FN`, `VG54NA`, `VG54NAE`, `VG54NAH`,
    `VG55EU`, `VG55FN`, `VG55NA`
    """

    serial: str
    """The serial number of the gateway installed on the asset."""


class DataConditionDetailsDvirSubmittedDeviceDvirDefectVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle"""

    asset_type: Optional[Literal["uncategorized", "trailer", "equipment", "unpowered", "vehicle"]] = FieldInfo(
        alias="assetType", default=None
    )
    """The type of the asset.

    Valid values: `uncategorized`, `trailer`, `equipment`, `unpowered`, `vehicle`
    """

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    gateway: Optional[DataConditionDetailsDvirSubmittedDeviceDvirDefectVehicleGateway] = None
    """A minified gateway object"""

    license_plate: Optional[str] = FieldInfo(alias="licensePlate", default=None)
    """The license plate of the vehicle."""

    name: Optional[str] = None
    """Name of the vehicle"""

    vin: Optional[str] = None
    """The VIN of the vehicle."""


class DataConditionDetailsDvirSubmittedDeviceDvirDefect(BaseModel):
    id: str
    """The ID of the defect."""

    created_at_time: str = FieldInfo(alias="createdAtTime")
    """Time when the defect was created. UTC timestamp in RFC 3339 format."""

    defect_type: str = FieldInfo(alias="defectType")
    """The type of DVIR defect."""

    is_resolved: bool = FieldInfo(alias="isResolved")
    """Signifies if this defect is resolved."""

    comment: Optional[str] = None
    """Comment on the defect."""

    mechanic_notes: Optional[str] = FieldInfo(alias="mechanicNotes", default=None)
    """The mechanic notes on this defect."""

    mechanic_notes_updated_at_time: Optional[str] = FieldInfo(alias="mechanicNotesUpdatedAtTime", default=None)
    """Time when mechanic notes were last updated. UTC timestamp in RFC 3339 format."""

    resolved_at_time: Optional[str] = FieldInfo(alias="resolvedAtTime", default=None)
    """Time when this defect was resolved.

    Will not be returned if the defect is unresolved. UTC timestamp in RFC 3339
    format.
    """

    resolved_by: Optional[DataConditionDetailsDvirSubmittedDeviceDvirDefectResolvedBy] = FieldInfo(
        alias="resolvedBy", default=None
    )
    """The person who resolved this defect."""

    trailer: Optional[DataConditionDetailsDvirSubmittedDeviceDvirDefectTrailer] = None
    """A minified trailer object"""

    vehicle: Optional[DataConditionDetailsDvirSubmittedDeviceDvirDefectVehicle] = None
    """A minified vehicle object.

    This object is only returned if the route is assigned to the vehicle.
    """


class DataConditionDetailsDvirSubmittedDeviceDvirSecondSignatureSignatoryUser(BaseModel):
    id: str
    """ID of the user."""

    name: str
    """Name of the user."""


class DataConditionDetailsDvirSubmittedDeviceDvirSecondSignature(BaseModel):
    signatory_user: DataConditionDetailsDvirSubmittedDeviceDvirSecondSignatureSignatoryUser = FieldInfo(
        alias="signatoryUser"
    )
    """The user who signed the DVIR."""

    signed_at_time: str = FieldInfo(alias="signedAtTime")
    """The time when the DVIR was signed. UTC timestamp in RFC 3339 format."""

    type: Literal["driver", "mechanic"]
    """Whether the DVIR was submitted by a driver or mechanic.

    Valid values: `driver`, `mechanic`
    """


class DataConditionDetailsDvirSubmittedDeviceDvirThirdSignatureSignatoryUser(BaseModel):
    id: str
    """ID of the user."""

    name: str
    """Name of the user."""


class DataConditionDetailsDvirSubmittedDeviceDvirThirdSignature(BaseModel):
    signatory_user: DataConditionDetailsDvirSubmittedDeviceDvirThirdSignatureSignatoryUser = FieldInfo(
        alias="signatoryUser"
    )
    """The user who signed the DVIR."""

    signed_at_time: str = FieldInfo(alias="signedAtTime")
    """The time when the DVIR was signed. UTC timestamp in RFC 3339 format."""

    type: Literal["driver", "mechanic"]
    """Whether the DVIR was submitted by a driver or mechanic.

    Valid values: `driver`, `mechanic`
    """


class DataConditionDetailsDvirSubmittedDeviceDvirTrailer(BaseModel):
    id: Optional[str] = None
    """ID of the trailer"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the trailer"""


class DataConditionDetailsDvirSubmittedDeviceDvir(BaseModel):
    id: str
    """The unique id of the DVIR"""

    author_signature: DataConditionDetailsDvirSubmittedDeviceDvirAuthorSignature = FieldInfo(alias="authorSignature")
    """An author signature for DVIRs with a signed time."""

    end_time: str = FieldInfo(alias="endTime")
    """Time when the driver signed and completed this DVIR.

    UTC timestamp in RFC 3339 format.
    """

    needs_correction: bool = FieldInfo(alias="needsCorrection")
    """Indicates if a defect needs correction."""

    safety_status: Literal["safe", "unsafe", "resolved"] = FieldInfo(alias="safetyStatus")
    """The condition of vehicle on which DVIR was done.

    Valid values: `safe`, `unsafe`, `resolved`
    """

    start_time: str = FieldInfo(alias="startTime")
    """Time when driver began filling out this DVIR in RFC 3339 format."""

    type: Literal["preTrip", "postTrip", "mechanic", "unspecified"]
    """Inspection type of the DVIR.

    Valid values: `preTrip`, `postTrip`, `mechanic`, `unspecified`
    """

    defects: Optional[List[DataConditionDetailsDvirSubmittedDeviceDvirDefect]] = None
    """Defects registered for the DVIR."""

    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Optional string if your jurisdiction requires a location of the DVIR."""

    mechanic_notes: Optional[str] = FieldInfo(alias="mechanicNotes", default=None)
    """The mechanics notes on the DVIR."""

    odometer_meters: Optional[int] = FieldInfo(alias="odometerMeters", default=None)
    """The odometer reading in meters."""

    second_signature: Optional[DataConditionDetailsDvirSubmittedDeviceDvirSecondSignature] = FieldInfo(
        alias="secondSignature", default=None
    )
    """An author signature for DVIRs with a signed time."""

    third_signature: Optional[DataConditionDetailsDvirSubmittedDeviceDvirThirdSignature] = FieldInfo(
        alias="thirdSignature", default=None
    )
    """An author signature for DVIRs with a signed time."""

    trailer: Optional[DataConditionDetailsDvirSubmittedDeviceDvirTrailer] = None
    """A minified trailer object"""


class DataConditionDetailsDvirSubmittedDeviceVehicleGateway(BaseModel):
    model: Literal[
        "AG15",
        "AG24",
        "AG24EU",
        "AG26",
        "AG26EU",
        "AG41",
        "AG41EU",
        "AG45",
        "AG45EU",
        "AG46",
        "AG46EU",
        "AG46P",
        "AG46PEU",
        "AG51",
        "AG51EU",
        "AG52",
        "AG52EU",
        "AG53",
        "AG53EU",
        "IG15",
        "IG21",
        "IG41",
        "IG61",
        "SG1",
        "SG1B",
        "SG1G",
        "SG1G32",
        "SG1x",
        "VG32",
        "VG33",
        "VG34",
        "VG34EU",
        "VG34FN",
        "VG34M",
        "VG54ATT",
        "VG54EU",
        "VG54FN",
        "VG54NA",
        "VG54NAE",
        "VG54NAH",
        "VG55EU",
        "VG55FN",
        "VG55NA",
    ]
    """The model of the gateway installed on the asset.

    Valid values: `AG15`, `AG24`, `AG24EU`, `AG26`, `AG26EU`, `AG41`, `AG41EU`,
    `AG45`, `AG45EU`, `AG46`, `AG46EU`, `AG46P`, `AG46PEU`, `AG51`, `AG51EU`,
    `AG52`, `AG52EU`, `AG53`, `AG53EU`, `IG15`, `IG21`, `IG41`, `IG61`, `SG1`,
    `SG1B`, `SG1G`, `SG1G32`, `SG1x`, `VG32`, `VG33`, `VG34`, `VG34EU`, `VG34FN`,
    `VG34M`, `VG54ATT`, `VG54EU`, `VG54FN`, `VG54NA`, `VG54NAE`, `VG54NAH`,
    `VG55EU`, `VG55FN`, `VG55NA`
    """

    serial: str
    """The serial number of the gateway installed on the asset."""


class DataConditionDetailsDvirSubmittedDeviceVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle"""

    asset_type: Optional[Literal["uncategorized", "trailer", "equipment", "unpowered", "vehicle"]] = FieldInfo(
        alias="assetType", default=None
    )
    """The type of the asset.

    Valid values: `uncategorized`, `trailer`, `equipment`, `unpowered`, `vehicle`
    """

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    gateway: Optional[DataConditionDetailsDvirSubmittedDeviceVehicleGateway] = None
    """A minified gateway object"""

    license_plate: Optional[str] = FieldInfo(alias="licensePlate", default=None)
    """The license plate of the vehicle."""

    name: Optional[str] = None
    """Name of the vehicle"""

    vin: Optional[str] = None
    """The VIN of the vehicle."""


class DataConditionDetailsDvirSubmittedDevice(BaseModel):
    driver: Optional[DataConditionDetailsDvirSubmittedDeviceDriver] = None
    """A minified driver object.

    This object is only returned if the route is assigned to the driver.
    """

    dvir: Optional[DataConditionDetailsDvirSubmittedDeviceDvir] = None
    """A DVIR description"""

    vehicle: Optional[DataConditionDetailsDvirSubmittedDeviceVehicle] = None
    """A minified vehicle object.

    This object is only returned if the route is assigned to the vehicle.
    """


class DataConditionDetailsEngineIdleDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsEngineIdleDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsEngineIdleDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsEngineIdleDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsEngineIdleDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsEngineIdleVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsEngineIdleVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsEngineIdleVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsEngineIdleVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsEngineIdleVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsEngineIdleVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsEngineIdleVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsEngineIdle(BaseModel):
    driver: Optional[DataConditionDetailsEngineIdleDriver] = None
    """A driver associated with the alert"""

    vehicle: Optional[DataConditionDetailsEngineIdleVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsEngineOffDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsEngineOffDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsEngineOffDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsEngineOffDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsEngineOffDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsEngineOffTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsEngineOffTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsEngineOffTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsEngineOffTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsEngineOffTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsEngineOffVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsEngineOffVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsEngineOffVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsEngineOffVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsEngineOffVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsEngineOffVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsEngineOffVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsEngineOff(BaseModel):
    driver: Optional[DataConditionDetailsEngineOffDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsEngineOffTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsEngineOffVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsEngineOnDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsEngineOnDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsEngineOnDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsEngineOnDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsEngineOnDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsEngineOnTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsEngineOnTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsEngineOnTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsEngineOnTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsEngineOnTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsEngineOnVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsEngineOnVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsEngineOnVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsEngineOnVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsEngineOnVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsEngineOnVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsEngineOnVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsEngineOn(BaseModel):
    driver: Optional[DataConditionDetailsEngineOnDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsEngineOnTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsEngineOnVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsFormSubmittedFormFieldAssetValueAsset(BaseModel):
    entry_type: Literal["tracked", "untracked"] = FieldInfo(alias="entryType")
    """The type of entry for the asset. Valid values: `tracked`, `untracked`"""

    id: Optional[str] = None
    """ID of a tracked asset. Included if 'entryType' is 'tracked'."""

    name: Optional[str] = None
    """Name of an untracked (i.e. manually entered) asset."""


class DataConditionDetailsFormSubmittedFormFieldAssetValue(BaseModel):
    asset: DataConditionDetailsFormSubmittedFormFieldAssetValueAsset
    """Tracked or untracked (i.e. manually entered) asset object."""


class DataConditionDetailsFormSubmittedFormFieldCheckBoxesValue(BaseModel):
    value: List[str]
    """List of selected options."""


class DataConditionDetailsFormSubmittedFormFieldDateTimeValue(BaseModel):
    type: Literal["datetime", "date", "time"]
    """The type of datetime format. Valid values: `datetime`, `date`, `time`"""

    value: datetime
    """UTC timestamp in RFC 3339 format."""


class DataConditionDetailsFormSubmittedFormFieldIssue(BaseModel):
    id: str
    """ID of the issue created from this form input field input object."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""


class DataConditionDetailsFormSubmittedFormFieldMediaList(BaseModel):
    id: str
    """ID of the media record."""

    processing_status: Literal["unknown", "processing", "finished"] = FieldInfo(alias="processingStatus")
    """Status of the media record. Valid values: `unknown`, `processing`, `finished`"""

    url: Optional[str] = None
    """URL containing a link to associated media content.

    Included if 'processingStatus' is 'finished'.
    """

    url_expires_at: Optional[datetime] = FieldInfo(alias="urlExpiresAt", default=None)
    """Expiration time of the media record 'url'. UTC timestamp in RFC 3339 format."""


class DataConditionDetailsFormSubmittedFormFieldMediaValueMediaList(BaseModel):
    id: str
    """ID of the media record."""

    processing_status: Literal["unknown", "processing", "finished"] = FieldInfo(alias="processingStatus")
    """Status of the media record. Valid values: `unknown`, `processing`, `finished`"""

    url: Optional[str] = None
    """URL containing a link to associated media content.

    Included if 'processingStatus' is 'finished'.
    """

    url_expires_at: Optional[datetime] = FieldInfo(alias="urlExpiresAt", default=None)
    """Expiration time of the media record 'url'. UTC timestamp in RFC 3339 format."""


class DataConditionDetailsFormSubmittedFormFieldMediaValue(BaseModel):
    media_list: List[DataConditionDetailsFormSubmittedFormFieldMediaValueMediaList] = FieldInfo(alias="mediaList")
    """List of forms media record objects."""


class DataConditionDetailsFormSubmittedFormFieldMultipleChoiceValue(BaseModel):
    value: str
    """Selected choice."""


class DataConditionDetailsFormSubmittedFormFieldNumberValue(BaseModel):
    value: float
    """Number value."""


class DataConditionDetailsFormSubmittedFormFieldPersonValuePersonPolymorphicUserID(BaseModel):
    id: str
    """ID of the polymorphic user."""

    type: Literal["driver", "user"]
    """The type of the polymorphic user. Valid values: `driver`, `user`"""


class DataConditionDetailsFormSubmittedFormFieldPersonValuePerson(BaseModel):
    entry_type: Literal["tracked", "untracked"] = FieldInfo(alias="entryType")
    """The type of entry for the person. Valid values: `tracked`, `untracked`"""

    name: Optional[str] = None
    """Name of an untracked (i.e. manually entered) person."""

    polymorphic_user_id: Optional[DataConditionDetailsFormSubmittedFormFieldPersonValuePersonPolymorphicUserID] = (
        FieldInfo(alias="polymorphicUserId", default=None)
    )
    """User or driver object."""


class DataConditionDetailsFormSubmittedFormFieldPersonValue(BaseModel):
    person: DataConditionDetailsFormSubmittedFormFieldPersonValuePerson
    """Tracked or untracked (i.e. manually entered) person object."""


class DataConditionDetailsFormSubmittedFormFieldSignatureValueMedia(BaseModel):
    id: str
    """ID of the media record."""

    processing_status: Literal["unknown", "processing", "finished"] = FieldInfo(alias="processingStatus")
    """Status of the media record. Valid values: `unknown`, `processing`, `finished`"""

    url: Optional[str] = None
    """URL containing a link to associated media content.

    Included if 'processingStatus' is 'finished'.
    """

    url_expires_at: Optional[datetime] = FieldInfo(alias="urlExpiresAt", default=None)
    """Expiration time of the media record 'url'. UTC timestamp in RFC 3339 format."""


class DataConditionDetailsFormSubmittedFormFieldSignatureValue(BaseModel):
    media: DataConditionDetailsFormSubmittedFormFieldSignatureValueMedia
    """Forms media record object."""


class DataConditionDetailsFormSubmittedFormFieldTableValueColumn(BaseModel):
    id: str
    """Unique identifier for the column."""

    label: str
    """Label of the column."""

    type: Literal["text, number, datetime, check_boxes, multiple_choice, signature, media, person"]
    """Type of the column field.

    Valid values:
    `text, number, datetime, check_boxes, multiple_choice, signature, media, person`
    """


class DataConditionDetailsFormSubmittedFormFieldTableValueRowCellCheckBoxesValue(BaseModel):
    value: List[str]
    """List of selected options."""


class DataConditionDetailsFormSubmittedFormFieldTableValueRowCellDateTimeValue(BaseModel):
    type: Literal["datetime", "date", "time"]
    """The type of datetime format. Valid values: `datetime`, `date`, `time`"""

    value: datetime
    """UTC timestamp in RFC 3339 format."""


class DataConditionDetailsFormSubmittedFormFieldTableValueRowCellMediaValueMediaList(BaseModel):
    id: str
    """ID of the media record."""

    processing_status: Literal["unknown", "processing", "finished"] = FieldInfo(alias="processingStatus")
    """Status of the media record. Valid values: `unknown`, `processing`, `finished`"""

    url: Optional[str] = None
    """URL containing a link to associated media content.

    Included if 'processingStatus' is 'finished'.
    """

    url_expires_at: Optional[datetime] = FieldInfo(alias="urlExpiresAt", default=None)
    """Expiration time of the media record 'url'. UTC timestamp in RFC 3339 format."""


class DataConditionDetailsFormSubmittedFormFieldTableValueRowCellMediaValue(BaseModel):
    media_list: List[DataConditionDetailsFormSubmittedFormFieldTableValueRowCellMediaValueMediaList] = FieldInfo(
        alias="mediaList"
    )
    """List of forms media record objects."""


class DataConditionDetailsFormSubmittedFormFieldTableValueRowCellMultipleChoiceValue(BaseModel):
    value: str
    """Selected choice."""


class DataConditionDetailsFormSubmittedFormFieldTableValueRowCellNumberValue(BaseModel):
    value: float
    """Number value."""


class DataConditionDetailsFormSubmittedFormFieldTableValueRowCellPersonValuePersonPolymorphicUserID(BaseModel):
    id: str
    """ID of the polymorphic user."""

    type: Literal["driver", "user"]
    """The type of the polymorphic user. Valid values: `driver`, `user`"""


class DataConditionDetailsFormSubmittedFormFieldTableValueRowCellPersonValuePerson(BaseModel):
    entry_type: Literal["tracked", "untracked"] = FieldInfo(alias="entryType")
    """The type of entry for the person. Valid values: `tracked`, `untracked`"""

    name: Optional[str] = None
    """Name of an untracked (i.e. manually entered) person."""

    polymorphic_user_id: Optional[
        DataConditionDetailsFormSubmittedFormFieldTableValueRowCellPersonValuePersonPolymorphicUserID
    ] = FieldInfo(alias="polymorphicUserId", default=None)
    """User or driver object."""


class DataConditionDetailsFormSubmittedFormFieldTableValueRowCellPersonValue(BaseModel):
    person: DataConditionDetailsFormSubmittedFormFieldTableValueRowCellPersonValuePerson
    """Tracked or untracked (i.e. manually entered) person object."""


class DataConditionDetailsFormSubmittedFormFieldTableValueRowCellSignatureValueMedia(BaseModel):
    id: str
    """ID of the media record."""

    processing_status: Literal["unknown", "processing", "finished"] = FieldInfo(alias="processingStatus")
    """Status of the media record. Valid values: `unknown`, `processing`, `finished`"""

    url: Optional[str] = None
    """URL containing a link to associated media content.

    Included if 'processingStatus' is 'finished'.
    """

    url_expires_at: Optional[datetime] = FieldInfo(alias="urlExpiresAt", default=None)
    """Expiration time of the media record 'url'. UTC timestamp in RFC 3339 format."""


class DataConditionDetailsFormSubmittedFormFieldTableValueRowCellSignatureValue(BaseModel):
    media: DataConditionDetailsFormSubmittedFormFieldTableValueRowCellSignatureValueMedia
    """Forms media record object."""


class DataConditionDetailsFormSubmittedFormFieldTableValueRowCellTextValue(BaseModel):
    value: str
    """Text value."""


class DataConditionDetailsFormSubmittedFormFieldTableValueRowCell(BaseModel):
    id: str
    """Unique identifier for the cell."""

    type: Literal["number, text, multiple_choice, check_boxes, datetime, signature, media, person"]
    """Type of the cell field.

    Valid values:
    `number, text, multiple_choice, check_boxes, datetime, signature, media, person`
    """

    check_boxes_value: Optional[DataConditionDetailsFormSubmittedFormFieldTableValueRowCellCheckBoxesValue] = FieldInfo(
        alias="checkBoxesValue", default=None
    )
    """The value of a check boxes form input field."""

    date_time_value: Optional[DataConditionDetailsFormSubmittedFormFieldTableValueRowCellDateTimeValue] = FieldInfo(
        alias="dateTimeValue", default=None
    )
    """The value of a datetime form input field."""

    media_value: Optional[DataConditionDetailsFormSubmittedFormFieldTableValueRowCellMediaValue] = FieldInfo(
        alias="mediaValue", default=None
    )
    """The value of a media form input field."""

    multiple_choice_value: Optional[DataConditionDetailsFormSubmittedFormFieldTableValueRowCellMultipleChoiceValue] = (
        FieldInfo(alias="multipleChoiceValue", default=None)
    )
    """The value of a multiple choice form input field."""

    number_value: Optional[DataConditionDetailsFormSubmittedFormFieldTableValueRowCellNumberValue] = FieldInfo(
        alias="numberValue", default=None
    )
    """The value of a number form input field."""

    person_value: Optional[DataConditionDetailsFormSubmittedFormFieldTableValueRowCellPersonValue] = FieldInfo(
        alias="personValue", default=None
    )
    """The value of a person form input field."""

    signature_value: Optional[DataConditionDetailsFormSubmittedFormFieldTableValueRowCellSignatureValue] = FieldInfo(
        alias="signatureValue", default=None
    )
    """The value of a signature form input field."""

    text_value: Optional[DataConditionDetailsFormSubmittedFormFieldTableValueRowCellTextValue] = FieldInfo(
        alias="textValue", default=None
    )
    """The value of a text form input field."""


class DataConditionDetailsFormSubmittedFormFieldTableValueRow(BaseModel):
    id: str
    """Unique identifier for the row."""

    cells: List[DataConditionDetailsFormSubmittedFormFieldTableValueRowCell]
    """List of cells in the row."""


class DataConditionDetailsFormSubmittedFormFieldTableValue(BaseModel):
    columns: List[DataConditionDetailsFormSubmittedFormFieldTableValueColumn]
    """List of table columns."""

    rows: List[DataConditionDetailsFormSubmittedFormFieldTableValueRow]
    """List of table rows."""


class DataConditionDetailsFormSubmittedFormFieldTextValue(BaseModel):
    value: str
    """Text value."""


class DataConditionDetailsFormSubmittedFormField(BaseModel):
    id: str
    """ID of the forms input field object."""

    type: Literal["number, text, multiple_choice, check_boxes, datetime, signature, media, asset, table"]
    """Type of the field.

    Valid values:
    `number, text, multiple_choice, check_boxes, datetime, signature, media, asset, table`
    """

    asset_value: Optional[DataConditionDetailsFormSubmittedFormFieldAssetValue] = FieldInfo(
        alias="assetValue", default=None
    )
    """The value of an asset form input field."""

    check_boxes_value: Optional[DataConditionDetailsFormSubmittedFormFieldCheckBoxesValue] = FieldInfo(
        alias="checkBoxesValue", default=None
    )
    """The value of a check boxes form input field."""

    date_time_value: Optional[DataConditionDetailsFormSubmittedFormFieldDateTimeValue] = FieldInfo(
        alias="dateTimeValue", default=None
    )
    """The value of a datetime form input field."""

    issue: Optional[DataConditionDetailsFormSubmittedFormFieldIssue] = None
    """Issue created from this form input field input object."""

    label: Optional[str] = None
    """Forms input field label."""

    media_list: Optional[List[DataConditionDetailsFormSubmittedFormFieldMediaList]] = FieldInfo(
        alias="mediaList", default=None
    )
    """List of forms media record objects."""

    media_value: Optional[DataConditionDetailsFormSubmittedFormFieldMediaValue] = FieldInfo(
        alias="mediaValue", default=None
    )
    """The value of a media form input field."""

    multiple_choice_value: Optional[DataConditionDetailsFormSubmittedFormFieldMultipleChoiceValue] = FieldInfo(
        alias="multipleChoiceValue", default=None
    )
    """The value of a multiple choice form input field."""

    note: Optional[str] = None
    """A note attached to the field input."""

    number_value: Optional[DataConditionDetailsFormSubmittedFormFieldNumberValue] = FieldInfo(
        alias="numberValue", default=None
    )
    """The value of a number form input field."""

    person_value: Optional[DataConditionDetailsFormSubmittedFormFieldPersonValue] = FieldInfo(
        alias="personValue", default=None
    )
    """The value of a person form input field."""

    signature_value: Optional[DataConditionDetailsFormSubmittedFormFieldSignatureValue] = FieldInfo(
        alias="signatureValue", default=None
    )
    """The value of a signature form input field."""

    table_value: Optional[DataConditionDetailsFormSubmittedFormFieldTableValue] = FieldInfo(
        alias="tableValue", default=None
    )
    """The value of a table form input field."""

    text_value: Optional[DataConditionDetailsFormSubmittedFormFieldTextValue] = FieldInfo(
        alias="textValue", default=None
    )
    """The value of a text form input field."""


class DataConditionDetailsFormSubmittedFormFormTemplate(BaseModel):
    id: str
    """ID of the form template."""

    revision_id: str = FieldInfo(alias="revisionId")
    """ID of the form template revision."""


class DataConditionDetailsFormSubmittedFormSubmittedBy(BaseModel):
    id: str
    """ID of the polymorphic user."""

    type: Literal["driver", "user"]
    """The type of the polymorphic user. Valid values: `driver`, `user`"""


class DataConditionDetailsFormSubmittedFormAsset(BaseModel):
    entry_type: Literal["tracked", "untracked"] = FieldInfo(alias="entryType")
    """The type of entry for the asset. Valid values: `tracked`, `untracked`"""

    id: Optional[str] = None
    """ID of a tracked asset. Included if 'entryType' is 'tracked'."""

    name: Optional[str] = None
    """Name of an untracked (i.e. manually entered) asset."""


class DataConditionDetailsFormSubmittedFormAssignedTo(BaseModel):
    id: str
    """ID of the polymorphic user."""

    type: Literal["driver", "user"]
    """The type of the polymorphic user. Valid values: `driver`, `user`"""


class DataConditionDetailsFormSubmittedFormLocation(BaseModel):
    latitude: float
    """Latitude of a location."""

    longitude: float
    """Longitude of a location."""


class DataConditionDetailsFormSubmittedFormScore(BaseModel):
    max_points: float = FieldInfo(alias="maxPoints")
    """Total possible points of the form submission."""

    score_percent: float = FieldInfo(alias="scorePercent")
    """Percentage score of the form submission, calculated as scorePoints / maxPoints."""

    score_points: float = FieldInfo(alias="scorePoints")
    """Score, in points, of the form submission."""


class DataConditionDetailsFormSubmittedForm(BaseModel):
    id: str
    """ID of the form submission."""

    created_at_time: datetime = FieldInfo(alias="createdAtTime")
    """Creation time of the form submission. UTC timestamp in RFC 3339 format."""

    fields: List[DataConditionDetailsFormSubmittedFormField]
    """List of field inputs in a form submission."""

    form_template: DataConditionDetailsFormSubmittedFormFormTemplate = FieldInfo(alias="formTemplate")
    """Form template reference object."""

    status: Literal["toDo", "submitted", "dismissed"]
    """State for the Form Submission.

    Always returned. Valid values: `toDo`, `submitted`, `dismissed`
    """

    submitted_at_time: datetime = FieldInfo(alias="submittedAtTime")
    """Submission time of the form submission. UTC timestamp in RFC 3339 format."""

    submitted_by: DataConditionDetailsFormSubmittedFormSubmittedBy = FieldInfo(alias="submittedBy")
    """User or driver object."""

    updated_at_time: datetime = FieldInfo(alias="updatedAtTime")
    """Update time of the form submission. UTC timestamp in RFC 3339 format."""

    asset: Optional[DataConditionDetailsFormSubmittedFormAsset] = None
    """Tracked or untracked (i.e. manually entered) asset object."""

    assigned_at_time: Optional[datetime] = FieldInfo(alias="assignedAtTime", default=None)
    """Assignment time of the form submission.

    Sometimes returned if the submission was assigned to a user or driver. UTC
    timestamp in RFC 3339 format.
    """

    assigned_to: Optional[DataConditionDetailsFormSubmittedFormAssignedTo] = FieldInfo(alias="assignedTo", default=None)
    """User or driver object."""

    due_at_time: Optional[datetime] = FieldInfo(alias="dueAtTime", default=None)
    """Time of when the submission is due.

    Sometimes returned, if the submission has a due date. UTC timestamp in RFC 3339
    format.
    """

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    is_required: Optional[bool] = FieldInfo(alias="isRequired", default=None)
    """Indicates whether the worker is required to complete this form or not.

    Sometimes returned if the submission was assigned to a user or driver.
    """

    location: Optional[DataConditionDetailsFormSubmittedFormLocation] = None
    """Form template location object."""

    score: Optional[DataConditionDetailsFormSubmittedFormScore] = None
    """Forms score object."""

    title: Optional[str] = None
    """Title of the form submission. Sometimes returned if the submission has a title."""


class DataConditionDetailsFormSubmitted(BaseModel):
    form: DataConditionDetailsFormSubmittedForm
    """Form Submission response object."""


class DataConditionDetailsFuelLevelPercentageDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsFuelLevelPercentageDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsFuelLevelPercentageDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsFuelLevelPercentageDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsFuelLevelPercentageDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsFuelLevelPercentageTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsFuelLevelPercentageTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsFuelLevelPercentageTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsFuelLevelPercentageTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsFuelLevelPercentageTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsFuelLevelPercentageVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsFuelLevelPercentageVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsFuelLevelPercentageVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsFuelLevelPercentageVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsFuelLevelPercentageVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsFuelLevelPercentageVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsFuelLevelPercentageVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsFuelLevelPercentage(BaseModel):
    driver: Optional[DataConditionDetailsFuelLevelPercentageDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsFuelLevelPercentageTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsFuelLevelPercentageVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsGatewayDisconnectedDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsGatewayDisconnectedDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsGatewayDisconnectedDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsGatewayDisconnectedDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsGatewayDisconnectedDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsGatewayDisconnectedTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsGatewayDisconnectedTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsGatewayDisconnectedTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsGatewayDisconnectedTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsGatewayDisconnectedTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsGatewayDisconnectedVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsGatewayDisconnectedVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsGatewayDisconnectedVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsGatewayDisconnectedVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsGatewayDisconnectedVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsGatewayDisconnectedVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsGatewayDisconnectedVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsGatewayDisconnected(BaseModel):
    driver: Optional[DataConditionDetailsGatewayDisconnectedDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsGatewayDisconnectedTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsGatewayDisconnectedVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsGatewayUnpluggedVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the vehicle"""


class DataConditionDetailsGatewayUnplugged(BaseModel):
    model: Literal[
        "AG15",
        "AG24",
        "AG24EU",
        "AG26",
        "AG26EU",
        "AG41",
        "AG41EU",
        "AG45",
        "AG45EU",
        "AG46",
        "AG46EU",
        "AG46P",
        "AG46PEU",
        "AG51",
        "AG51EU",
        "AG52",
        "AG52EU",
        "AG53",
        "AG53EU",
        "IG15",
        "IG21",
        "IG41",
        "IG61",
        "SG1",
        "SG1B",
        "SG1G",
        "SG1G32",
        "SG1x",
        "VG32",
        "VG33",
        "VG34",
        "VG34EU",
        "VG34FN",
        "VG34M",
        "VG54ATT",
        "VG54EU",
        "VG54FN",
        "VG54NA",
        "VG54NAE",
        "VG54NAH",
        "VG55EU",
        "VG55FN",
        "VG55NA",
    ]
    """The model of the gateway installed on the asset.

    Valid values: `AG15`, `AG24`, `AG24EU`, `AG26`, `AG26EU`, `AG41`, `AG41EU`,
    `AG45`, `AG45EU`, `AG46`, `AG46EU`, `AG46P`, `AG46PEU`, `AG51`, `AG51EU`,
    `AG52`, `AG52EU`, `AG53`, `AG53EU`, `IG15`, `IG21`, `IG41`, `IG61`, `SG1`,
    `SG1B`, `SG1G`, `SG1G32`, `SG1x`, `VG32`, `VG33`, `VG34`, `VG34EU`, `VG34FN`,
    `VG34M`, `VG54ATT`, `VG54EU`, `VG54FN`, `VG54NA`, `VG54NAE`, `VG54NAH`,
    `VG55EU`, `VG55FN`, `VG55NA`
    """

    serial: str
    """The serial number of the gateway installed on the asset."""

    vehicle: Optional[DataConditionDetailsGatewayUnpluggedVehicle] = None
    """A minified vehicle object.

    This object is only returned if the route is assigned to the vehicle.
    """


class DataConditionDetailsGeofenceEntryAddressGeofenceCircle(BaseModel):
    radius_meters: int = FieldInfo(alias="radiusMeters")
    """The radius of the circular geofence in meters."""

    latitude: Optional[float] = None
    """Latitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """

    longitude: Optional[float] = None
    """Longitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """


class DataConditionDetailsGeofenceEntryAddressGeofencePolygonVertex(BaseModel):
    latitude: float
    """The latitude of a geofence vertex in decimal degrees."""

    longitude: float
    """The longitude of a geofence vertex in decimal degrees."""


class DataConditionDetailsGeofenceEntryAddressGeofencePolygon(BaseModel):
    vertices: Optional[List[DataConditionDetailsGeofenceEntryAddressGeofencePolygonVertex]] = None
    """The vertices of the polygon geofence.

    These geofence vertices describe the perimeter of the polygon, and must consist
    of at least 3 vertices and less than 40.
    """


class DataConditionDetailsGeofenceEntryAddressGeofenceSettingsShowAddress(BaseModel):
    latitude: float
    """The latitude of a geofence vertex in decimal degrees."""

    longitude: float
    """The longitude of a geofence vertex in decimal degrees."""


class DataConditionDetailsGeofenceEntryAddressGeofenceSettings(BaseModel):
    show_addresses: Optional[List[DataConditionDetailsGeofenceEntryAddressGeofenceSettingsShowAddress]] = FieldInfo(
        alias="showAddresses", default=None
    )
    """The geofence setting.

    If this setting set to true, then underlying geofence addresses will be shown in
    reports instead of a geofence's name.
    """


class DataConditionDetailsGeofenceEntryAddressGeofence(BaseModel):
    circle: Optional[DataConditionDetailsGeofenceEntryAddressGeofenceCircle] = None
    """Information about a circular geofence.

    This field is only needed if the geofence is a circle.
    """

    polygon: Optional[DataConditionDetailsGeofenceEntryAddressGeofencePolygon] = None
    """Information about a polygon geofence.

    This field is only needed if the geofence is a polygon.
    """

    settings: Optional[DataConditionDetailsGeofenceEntryAddressGeofenceSettings] = None
    """Information about a geofence settings."""


class DataConditionDetailsGeofenceEntryAddress(BaseModel):
    id: str
    """Id of the address"""

    formatted_address: str = FieldInfo(alias="formattedAddress")
    """
    The full street address for this address/geofence, as it might be recognized by
    Google Maps.
    """

    name: str
    """Name of the address"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    geofence: Optional[DataConditionDetailsGeofenceEntryAddressGeofence] = None
    """The geofence that defines this address and its bounds.

    This can either be a circle or a polygon, but not both.
    """


class DataConditionDetailsGeofenceEntryVehicleGateway(BaseModel):
    model: Literal[
        "AG15",
        "AG24",
        "AG24EU",
        "AG26",
        "AG26EU",
        "AG41",
        "AG41EU",
        "AG45",
        "AG45EU",
        "AG46",
        "AG46EU",
        "AG46P",
        "AG46PEU",
        "AG51",
        "AG51EU",
        "AG52",
        "AG52EU",
        "AG53",
        "AG53EU",
        "IG15",
        "IG21",
        "IG41",
        "IG61",
        "SG1",
        "SG1B",
        "SG1G",
        "SG1G32",
        "SG1x",
        "VG32",
        "VG33",
        "VG34",
        "VG34EU",
        "VG34FN",
        "VG34M",
        "VG54ATT",
        "VG54EU",
        "VG54FN",
        "VG54NA",
        "VG54NAE",
        "VG54NAH",
        "VG55EU",
        "VG55FN",
        "VG55NA",
    ]
    """The model of the gateway installed on the asset.

    Valid values: `AG15`, `AG24`, `AG24EU`, `AG26`, `AG26EU`, `AG41`, `AG41EU`,
    `AG45`, `AG45EU`, `AG46`, `AG46EU`, `AG46P`, `AG46PEU`, `AG51`, `AG51EU`,
    `AG52`, `AG52EU`, `AG53`, `AG53EU`, `IG15`, `IG21`, `IG41`, `IG61`, `SG1`,
    `SG1B`, `SG1G`, `SG1G32`, `SG1x`, `VG32`, `VG33`, `VG34`, `VG34EU`, `VG34FN`,
    `VG34M`, `VG54ATT`, `VG54EU`, `VG54FN`, `VG54NA`, `VG54NAE`, `VG54NAH`,
    `VG55EU`, `VG55FN`, `VG55NA`
    """

    serial: str
    """The serial number of the gateway installed on the asset."""


class DataConditionDetailsGeofenceEntryVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle"""

    asset_type: Optional[Literal["uncategorized", "trailer", "equipment", "unpowered", "vehicle"]] = FieldInfo(
        alias="assetType", default=None
    )
    """The type of the asset.

    Valid values: `uncategorized`, `trailer`, `equipment`, `unpowered`, `vehicle`
    """

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    gateway: Optional[DataConditionDetailsGeofenceEntryVehicleGateway] = None
    """A minified gateway object"""

    license_plate: Optional[str] = FieldInfo(alias="licensePlate", default=None)
    """The license plate of the vehicle."""

    name: Optional[str] = None
    """Name of the vehicle"""

    vin: Optional[str] = None
    """The VIN of the vehicle."""


class DataConditionDetailsGeofenceEntry(BaseModel):
    address: Optional[DataConditionDetailsGeofenceEntryAddress] = None
    """A minimal Address object representation used in AddressEventObject objects"""

    vehicle: Optional[DataConditionDetailsGeofenceEntryVehicle] = None
    """A minified vehicle object.

    This object is only returned if the route is assigned to the vehicle.
    """


class DataConditionDetailsGeofenceExitAddressGeofenceCircle(BaseModel):
    radius_meters: int = FieldInfo(alias="radiusMeters")
    """The radius of the circular geofence in meters."""

    latitude: Optional[float] = None
    """Latitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """

    longitude: Optional[float] = None
    """Longitude of the address.

    Will be geocoded from formattedAddress if not provided.
    """


class DataConditionDetailsGeofenceExitAddressGeofencePolygonVertex(BaseModel):
    latitude: float
    """The latitude of a geofence vertex in decimal degrees."""

    longitude: float
    """The longitude of a geofence vertex in decimal degrees."""


class DataConditionDetailsGeofenceExitAddressGeofencePolygon(BaseModel):
    vertices: Optional[List[DataConditionDetailsGeofenceExitAddressGeofencePolygonVertex]] = None
    """The vertices of the polygon geofence.

    These geofence vertices describe the perimeter of the polygon, and must consist
    of at least 3 vertices and less than 40.
    """


class DataConditionDetailsGeofenceExitAddressGeofenceSettingsShowAddress(BaseModel):
    latitude: float
    """The latitude of a geofence vertex in decimal degrees."""

    longitude: float
    """The longitude of a geofence vertex in decimal degrees."""


class DataConditionDetailsGeofenceExitAddressGeofenceSettings(BaseModel):
    show_addresses: Optional[List[DataConditionDetailsGeofenceExitAddressGeofenceSettingsShowAddress]] = FieldInfo(
        alias="showAddresses", default=None
    )
    """The geofence setting.

    If this setting set to true, then underlying geofence addresses will be shown in
    reports instead of a geofence's name.
    """


class DataConditionDetailsGeofenceExitAddressGeofence(BaseModel):
    circle: Optional[DataConditionDetailsGeofenceExitAddressGeofenceCircle] = None
    """Information about a circular geofence.

    This field is only needed if the geofence is a circle.
    """

    polygon: Optional[DataConditionDetailsGeofenceExitAddressGeofencePolygon] = None
    """Information about a polygon geofence.

    This field is only needed if the geofence is a polygon.
    """

    settings: Optional[DataConditionDetailsGeofenceExitAddressGeofenceSettings] = None
    """Information about a geofence settings."""


class DataConditionDetailsGeofenceExitAddress(BaseModel):
    id: str
    """Id of the address"""

    formatted_address: str = FieldInfo(alias="formattedAddress")
    """
    The full street address for this address/geofence, as it might be recognized by
    Google Maps.
    """

    name: str
    """Name of the address"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    geofence: Optional[DataConditionDetailsGeofenceExitAddressGeofence] = None
    """The geofence that defines this address and its bounds.

    This can either be a circle or a polygon, but not both.
    """


class DataConditionDetailsGeofenceExitVehicleGateway(BaseModel):
    model: Literal[
        "AG15",
        "AG24",
        "AG24EU",
        "AG26",
        "AG26EU",
        "AG41",
        "AG41EU",
        "AG45",
        "AG45EU",
        "AG46",
        "AG46EU",
        "AG46P",
        "AG46PEU",
        "AG51",
        "AG51EU",
        "AG52",
        "AG52EU",
        "AG53",
        "AG53EU",
        "IG15",
        "IG21",
        "IG41",
        "IG61",
        "SG1",
        "SG1B",
        "SG1G",
        "SG1G32",
        "SG1x",
        "VG32",
        "VG33",
        "VG34",
        "VG34EU",
        "VG34FN",
        "VG34M",
        "VG54ATT",
        "VG54EU",
        "VG54FN",
        "VG54NA",
        "VG54NAE",
        "VG54NAH",
        "VG55EU",
        "VG55FN",
        "VG55NA",
    ]
    """The model of the gateway installed on the asset.

    Valid values: `AG15`, `AG24`, `AG24EU`, `AG26`, `AG26EU`, `AG41`, `AG41EU`,
    `AG45`, `AG45EU`, `AG46`, `AG46EU`, `AG46P`, `AG46PEU`, `AG51`, `AG51EU`,
    `AG52`, `AG52EU`, `AG53`, `AG53EU`, `IG15`, `IG21`, `IG41`, `IG61`, `SG1`,
    `SG1B`, `SG1G`, `SG1G32`, `SG1x`, `VG32`, `VG33`, `VG34`, `VG34EU`, `VG34FN`,
    `VG34M`, `VG54ATT`, `VG54EU`, `VG54FN`, `VG54NA`, `VG54NAE`, `VG54NAH`,
    `VG55EU`, `VG55FN`, `VG55NA`
    """

    serial: str
    """The serial number of the gateway installed on the asset."""


class DataConditionDetailsGeofenceExitVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle"""

    asset_type: Optional[Literal["uncategorized", "trailer", "equipment", "unpowered", "vehicle"]] = FieldInfo(
        alias="assetType", default=None
    )
    """The type of the asset.

    Valid values: `uncategorized`, `trailer`, `equipment`, `unpowered`, `vehicle`
    """

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    gateway: Optional[DataConditionDetailsGeofenceExitVehicleGateway] = None
    """A minified gateway object"""

    license_plate: Optional[str] = FieldInfo(alias="licensePlate", default=None)
    """The license plate of the vehicle."""

    name: Optional[str] = None
    """Name of the vehicle"""

    vin: Optional[str] = None
    """The VIN of the vehicle."""


class DataConditionDetailsGeofenceExit(BaseModel):
    address: Optional[DataConditionDetailsGeofenceExitAddress] = None
    """A minimal Address object representation used in AddressEventObject objects"""

    vehicle: Optional[DataConditionDetailsGeofenceExitVehicle] = None
    """A minified vehicle object.

    This object is only returned if the route is assigned to the vehicle.
    """


class DataConditionDetailsGpsSignalLossDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsGpsSignalLossDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsGpsSignalLossDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsGpsSignalLossDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsGpsSignalLossDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsGpsSignalLossTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsGpsSignalLossTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsGpsSignalLossTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsGpsSignalLossTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsGpsSignalLossTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsGpsSignalLossVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsGpsSignalLossVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsGpsSignalLossVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsGpsSignalLossVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsGpsSignalLossVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsGpsSignalLossVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsGpsSignalLossVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsGpsSignalLoss(BaseModel):
    driver: Optional[DataConditionDetailsGpsSignalLossDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsGpsSignalLossTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsGpsSignalLossVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsHarshEventDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsHarshEventDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsHarshEventDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsHarshEventDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsHarshEventDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsHarshEventVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsHarshEventVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsHarshEventVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsHarshEventVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsHarshEventVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsHarshEventVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsHarshEventVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsHarshEvent(BaseModel):
    driver: Optional[DataConditionDetailsHarshEventDriver] = None
    """A driver associated with the alert"""

    vehicle: Optional[DataConditionDetailsHarshEventVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsHosViolationDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsHosViolationDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsHosViolationDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsHosViolationDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsHosViolationDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsHosViolation(BaseModel):
    driver: Optional[DataConditionDetailsHosViolationDriver] = None
    """A driver associated with the alert"""


class DataConditionDetailsInactivityCameraStreamCameraDeviceSiteTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsInactivityCameraStreamCameraDeviceSite(BaseModel):
    id: str
    """The ID of the site associated with the alert"""

    name: Optional[str] = None
    """The name of the site"""

    tags: Optional[List[DataConditionDetailsInactivityCameraStreamCameraDeviceSiteTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Site.
    """


class DataConditionDetailsInactivityCameraStreamCameraDeviceTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsInactivityCameraStreamCameraDevice(BaseModel):
    id: str
    """The ID of the camera device associated with the alert"""

    name: Optional[str] = None
    """The name of the camera device"""

    sites: Optional[List[DataConditionDetailsInactivityCameraStreamCameraDeviceSite]] = None
    """The list of sites associated with the camera device."""

    tags: Optional[List[DataConditionDetailsInactivityCameraStreamCameraDeviceTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the camera device.
    """


class DataConditionDetailsInactivityCameraStreamTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsInactivityCameraStream(BaseModel):
    id: str
    """The ID of the camera stream associated with the alert."""

    camera_device: Optional[DataConditionDetailsInactivityCameraStreamCameraDevice] = FieldInfo(
        alias="cameraDevice", default=None
    )
    """A camera device associated with the alert"""

    name: Optional[str] = None
    """The name of the camera stream."""

    tags: Optional[List[DataConditionDetailsInactivityCameraStreamTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the camera stream.
    """


class DataConditionDetailsInactivity(BaseModel):
    camera_stream: Optional[DataConditionDetailsInactivityCameraStream] = FieldInfo(alias="cameraStream", default=None)
    """A camera stream associated with the alert."""


class DataConditionDetailsInsideGeofenceDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsInsideGeofenceDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsInsideGeofenceDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsInsideGeofenceDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsInsideGeofenceDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsInsideGeofenceTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsInsideGeofenceTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsInsideGeofenceTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsInsideGeofenceTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsInsideGeofenceTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsInsideGeofenceVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsInsideGeofenceVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsInsideGeofenceVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsInsideGeofenceVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsInsideGeofenceVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsInsideGeofenceVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsInsideGeofenceVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsInsideGeofence(BaseModel):
    driver: Optional[DataConditionDetailsInsideGeofenceDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsInsideGeofenceTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsInsideGeofenceVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsIssueCreatedIssueIssueSource(BaseModel):
    type: Literal["form", "ad-hoc"]
    """The type of issue source. Valid values: `form`, `ad-hoc`"""

    id: Optional[str] = None
    """ID of the issue's source object.

    The format depends on the 'type'. Included if 'type' is not 'ad-hoc'.
    """


class DataConditionDetailsIssueCreatedIssueSubmittedBy(BaseModel):
    id: str
    """ID of the polymorphic user."""

    type: Literal["driver", "user"]
    """The type of the polymorphic user. Valid values: `driver`, `user`"""


class DataConditionDetailsIssueCreatedIssueAsset(BaseModel):
    entry_type: Literal["tracked", "untracked"] = FieldInfo(alias="entryType")
    """The type of entry for the asset. Valid values: `tracked`, `untracked`"""

    id: Optional[str] = None
    """ID of a tracked asset. Included if 'entryType' is 'tracked'."""

    name: Optional[str] = None
    """Name of an untracked (i.e. manually entered) asset."""


class DataConditionDetailsIssueCreatedIssueAssignedTo(BaseModel):
    id: str
    """ID of the polymorphic user."""

    type: Literal["driver", "user"]
    """The type of the polymorphic user. Valid values: `driver`, `user`"""


class DataConditionDetailsIssueCreatedIssueMediaList(BaseModel):
    id: str
    """ID of the media record."""

    processing_status: Literal["unknown", "processing", "finished"] = FieldInfo(alias="processingStatus")
    """Status of the media record. Valid values: `unknown`, `processing`, `finished`"""

    url: Optional[str] = None
    """URL containing a link to associated media content.

    Included if 'processingStatus' is 'finished'.
    """

    url_expires_at: Optional[datetime] = FieldInfo(alias="urlExpiresAt", default=None)
    """Expiration time of the media record 'url'. UTC timestamp in RFC 3339 format."""


class DataConditionDetailsIssueCreatedIssue(BaseModel):
    id: str
    """ID of the issue."""

    created_at_time: datetime = FieldInfo(alias="createdAtTime")
    """Creation time of the issue. UTC timestamp in RFC 3339 format."""

    issue_source: DataConditionDetailsIssueCreatedIssueIssueSource = FieldInfo(alias="issueSource")
    """Contains information about where an issue came from."""

    status: Literal["open", "inProgress", "resolved", "dismissed"]
    """Status of the issue.

    Valid values: `open`, `inProgress`, `resolved`, `dismissed`
    """

    submitted_at_time: datetime = FieldInfo(alias="submittedAtTime")
    """Submission time of the issue. UTC timestamp in RFC 3339 format."""

    submitted_by: DataConditionDetailsIssueCreatedIssueSubmittedBy = FieldInfo(alias="submittedBy")
    """User or driver object."""

    title: str
    """Title of the issue."""

    updated_at_time: datetime = FieldInfo(alias="updatedAtTime")
    """Update time of the issue. UTC timestamp in RFC 3339 format."""

    asset: Optional[DataConditionDetailsIssueCreatedIssueAsset] = None
    """Tracked or untracked (i.e. manually entered) asset object."""

    assigned_to: Optional[DataConditionDetailsIssueCreatedIssueAssignedTo] = FieldInfo(alias="assignedTo", default=None)
    """User or driver object."""

    description: Optional[str] = None
    """Description of the issue. Included if the issue was given a description."""

    due_date: Optional[datetime] = FieldInfo(alias="dueDate", default=None)
    """Due date of the issue.

    UTC timestamp in RFC 3339 format. Included if the issue was assigned a due date.
    """

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    media_list: Optional[List[DataConditionDetailsIssueCreatedIssueMediaList]] = FieldInfo(
        alias="mediaList", default=None
    )
    """List of media objects for the issue. Included if the issue has media."""

    priority: Optional[Literal["low", "medium", "high"]] = None
    """Priority of the issue.

    Included if the issue was assigned a priority. Valid values: `low`, `medium`,
    `high`
    """


class DataConditionDetailsIssueCreated(BaseModel):
    issue: DataConditionDetailsIssueCreatedIssue
    """Issue response object."""


class DataConditionDetailsJammingDetectedDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsJammingDetectedDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsJammingDetectedDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsJammingDetectedDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsJammingDetectedDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsJammingDetectedTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsJammingDetectedTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsJammingDetectedTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsJammingDetectedTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsJammingDetectedTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsJammingDetectedVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsJammingDetectedVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsJammingDetectedVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsJammingDetectedVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsJammingDetectedVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsJammingDetectedVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsJammingDetectedVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsJammingDetected(BaseModel):
    driver: Optional[DataConditionDetailsJammingDetectedDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsJammingDetectedTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsJammingDetectedVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsMotionDetectedCameraStreamCameraDeviceSiteTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsMotionDetectedCameraStreamCameraDeviceSite(BaseModel):
    id: str
    """The ID of the site associated with the alert"""

    name: Optional[str] = None
    """The name of the site"""

    tags: Optional[List[DataConditionDetailsMotionDetectedCameraStreamCameraDeviceSiteTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Site.
    """


class DataConditionDetailsMotionDetectedCameraStreamCameraDeviceTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsMotionDetectedCameraStreamCameraDevice(BaseModel):
    id: str
    """The ID of the camera device associated with the alert"""

    name: Optional[str] = None
    """The name of the camera device"""

    sites: Optional[List[DataConditionDetailsMotionDetectedCameraStreamCameraDeviceSite]] = None
    """The list of sites associated with the camera device."""

    tags: Optional[List[DataConditionDetailsMotionDetectedCameraStreamCameraDeviceTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the camera device.
    """


class DataConditionDetailsMotionDetectedCameraStreamTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsMotionDetectedCameraStream(BaseModel):
    id: str
    """The ID of the camera stream associated with the alert."""

    camera_device: Optional[DataConditionDetailsMotionDetectedCameraStreamCameraDevice] = FieldInfo(
        alias="cameraDevice", default=None
    )
    """A camera device associated with the alert"""

    name: Optional[str] = None
    """The name of the camera stream."""

    tags: Optional[List[DataConditionDetailsMotionDetectedCameraStreamTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the camera stream.
    """


class DataConditionDetailsMotionDetected(BaseModel):
    camera_stream: Optional[DataConditionDetailsMotionDetectedCameraStream] = FieldInfo(
        alias="cameraStream", default=None
    )
    """A camera stream associated with the alert."""


class DataConditionDetailsOutOfRouteDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsOutOfRouteDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsOutOfRouteDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsOutOfRouteDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsOutOfRouteDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsOutOfRouteTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsOutOfRouteTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsOutOfRouteTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsOutOfRouteTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsOutOfRouteTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsOutOfRouteVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsOutOfRouteVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsOutOfRouteVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsOutOfRouteVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsOutOfRouteVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsOutOfRouteVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsOutOfRouteVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsOutOfRoute(BaseModel):
    driver: Optional[DataConditionDetailsOutOfRouteDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsOutOfRouteTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsOutOfRouteVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsOutsideGeofenceDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsOutsideGeofenceDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsOutsideGeofenceDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsOutsideGeofenceDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsOutsideGeofenceDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsOutsideGeofenceTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsOutsideGeofenceTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsOutsideGeofenceTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsOutsideGeofenceTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsOutsideGeofenceTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsOutsideGeofenceVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsOutsideGeofenceVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsOutsideGeofenceVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsOutsideGeofenceVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsOutsideGeofenceVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsOutsideGeofenceVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsOutsideGeofenceVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsOutsideGeofence(BaseModel):
    driver: Optional[DataConditionDetailsOutsideGeofenceDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsOutsideGeofenceTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsOutsideGeofenceVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsPanicButtonDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsPanicButtonDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsPanicButtonDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsPanicButtonDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsPanicButtonDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsPanicButtonTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsPanicButtonTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsPanicButtonTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsPanicButtonTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsPanicButtonTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsPanicButtonVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsPanicButtonVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsPanicButtonVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsPanicButtonVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsPanicButtonVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsPanicButtonVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsPanicButtonVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsPanicButton(BaseModel):
    driver: Optional[DataConditionDetailsPanicButtonDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsPanicButtonTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsPanicButtonVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsPersonDetectedCameraStreamCameraDeviceSiteTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsPersonDetectedCameraStreamCameraDeviceSite(BaseModel):
    id: str
    """The ID of the site associated with the alert"""

    name: Optional[str] = None
    """The name of the site"""

    tags: Optional[List[DataConditionDetailsPersonDetectedCameraStreamCameraDeviceSiteTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Site.
    """


class DataConditionDetailsPersonDetectedCameraStreamCameraDeviceTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsPersonDetectedCameraStreamCameraDevice(BaseModel):
    id: str
    """The ID of the camera device associated with the alert"""

    name: Optional[str] = None
    """The name of the camera device"""

    sites: Optional[List[DataConditionDetailsPersonDetectedCameraStreamCameraDeviceSite]] = None
    """The list of sites associated with the camera device."""

    tags: Optional[List[DataConditionDetailsPersonDetectedCameraStreamCameraDeviceTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the camera device.
    """


class DataConditionDetailsPersonDetectedCameraStreamTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsPersonDetectedCameraStream(BaseModel):
    id: str
    """The ID of the camera stream associated with the alert."""

    camera_device: Optional[DataConditionDetailsPersonDetectedCameraStreamCameraDevice] = FieldInfo(
        alias="cameraDevice", default=None
    )
    """A camera device associated with the alert"""

    name: Optional[str] = None
    """The name of the camera stream."""

    tags: Optional[List[DataConditionDetailsPersonDetectedCameraStreamTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the camera stream.
    """


class DataConditionDetailsPersonDetected(BaseModel):
    camera_stream: Optional[DataConditionDetailsPersonDetectedCameraStream] = FieldInfo(
        alias="cameraStream", default=None
    )
    """A camera stream associated with the alert."""


class DataConditionDetailsReeferTemperatureDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsReeferTemperatureDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsReeferTemperatureDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsReeferTemperatureDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsReeferTemperatureDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsReeferTemperatureTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsReeferTemperatureTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsReeferTemperatureTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsReeferTemperatureTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsReeferTemperatureTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsReeferTemperatureVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsReeferTemperatureVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsReeferTemperatureVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsReeferTemperatureVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsReeferTemperatureVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsReeferTemperatureVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsReeferTemperatureVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsReeferTemperature(BaseModel):
    driver: Optional[DataConditionDetailsReeferTemperatureDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsReeferTemperatureTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsReeferTemperatureVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsRouteStopArrivalRouteSettings(BaseModel):
    route_completion_condition: Optional[Literal["arriveLastStop", "departLastStop"]] = FieldInfo(
        alias="routeCompletionCondition", default=None
    )
    """
    Defaults to 'arriveLastStop' which ends the route upon arriving at the final
    stop. The condition 'departLastStop' ends the route upon departing the last
    stop. If 'arriveLastStop' is set, then the departure time of the final stop
    should not be set. Valid values: `arriveLastStop`, `departLastStop`
    """

    route_starting_condition: Optional[Literal["departFirstStop", "arriveFirstStop"]] = FieldInfo(
        alias="routeStartingCondition", default=None
    )
    """
    Defaults to 'departFirstStop' which starts the route upon departing the first
    stop in the route. The condition 'arriveFirstStop' starts the route upon
    arriving at the first stop in the route. If 'departFirstStop' is set, the
    arrival time of the first stop should not be set. Valid values:
    `departFirstStop`, `arriveFirstStop`
    """


class DataConditionDetailsRouteStopArrivalRouteStopAddress(BaseModel):
    id: str
    """Id of the address"""

    name: str
    """Name of the address"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""


class DataConditionDetailsRouteStopArrivalRouteStopDocument(BaseModel):
    id: str
    """Id of the document"""

    name: Optional[str] = None
    """Name of the document"""


class DataConditionDetailsRouteStopArrivalRouteStopLocationLiveSharingLink(BaseModel):
    live_sharing_url: str = FieldInfo(alias="liveSharingUrl")
    """The shareable URL of the vehicle's location."""

    name: str
    """Name of the Live Sharing Link."""

    expires_at_time: Optional[str] = FieldInfo(alias="expiresAtTime", default=None)
    """Date that this link expires, in RFC 3339 format."""


class DataConditionDetailsRouteStopArrivalRouteStopSingleUseLocation(BaseModel):
    latitude: float
    """The latitude of the location"""

    longitude: float
    """The longitude of the location"""

    address: Optional[str] = None
    """Address of the stop."""


class DataConditionDetailsRouteStopArrivalRouteStop(BaseModel):
    id: str
    """Id of the stop"""

    name: str
    """Name of the stop"""

    state: Literal["unassigned", "scheduled", "en route", "skipped", "arrived", "departed"]
    """The current state of the route stop.

    Valid values: `unassigned`, `scheduled`, `en route`, `skipped`, `arrived`,
    `departed`
    """

    actual_arrival_time: Optional[datetime] = FieldInfo(alias="actualArrivalTime", default=None)
    """Actual arrival time, if it exists, for the route stop in RFC 3339 format."""

    actual_departure_time: Optional[datetime] = FieldInfo(alias="actualDepartureTime", default=None)
    """Actual departure time, if it exists, for the route stop in RFC 3339 format."""

    address: Optional[DataConditionDetailsRouteStopArrivalRouteStopAddress] = None
    """A minified Address object"""

    documents: Optional[List[DataConditionDetailsRouteStopArrivalRouteStopDocument]] = None
    """List of documents associated with the stop."""

    en_route_time: Optional[datetime] = FieldInfo(alias="enRouteTime", default=None)
    """The time the stop became en-route, in RFC 3339 format."""

    eta: Optional[datetime] = None
    """
    Estimated time of arrival, if this stop is currently en-route, in RFC 3339
    format.
    """

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    live_sharing_url: Optional[str] = FieldInfo(alias="liveSharingUrl", default=None)
    """The shareable url of the stop's current status."""

    location_live_sharing_links: Optional[
        List[DataConditionDetailsRouteStopArrivalRouteStopLocationLiveSharingLink]
    ] = FieldInfo(alias="locationLiveSharingLinks", default=None)
    """List of shareable, non-expired 'By Location' Live Sharing Links."""

    notes: Optional[str] = None
    """Notes for the stop"""

    ontime_window_after_arrival_ms: Optional[int] = FieldInfo(alias="ontimeWindowAfterArrivalMs", default=None)
    """
    Specifies the time window (in milliseconds) after a stop's scheduled arrival
    time during which the stop is considered 'on-time'.
    """

    ontime_window_before_arrival_ms: Optional[int] = FieldInfo(alias="ontimeWindowBeforeArrivalMs", default=None)
    """
    Specifies the time window (in milliseconds) before a stop's scheduled arrival
    time during which the stop is considered 'on-time'.
    """

    scheduled_arrival_time: Optional[datetime] = FieldInfo(alias="scheduledArrivalTime", default=None)
    """Scheduled arrival time, if it exists, for the stop in RFC 3339 format."""

    scheduled_departure_time: Optional[datetime] = FieldInfo(alias="scheduledDepartureTime", default=None)
    """Scheduled departure time, if it exists, for the stop in RFC 3339 format."""

    single_use_location: Optional[DataConditionDetailsRouteStopArrivalRouteStopSingleUseLocation] = FieldInfo(
        alias="singleUseLocation", default=None
    )
    """
    This field is used to indicate stops along the route for which an address has
    not been persisted. This field is mutually exclusive with addressId.
    """

    skipped_time: Optional[datetime] = FieldInfo(alias="skippedTime", default=None)
    """Skipped time, if it exists, for the route stop in RFC 3339 format."""


class DataConditionDetailsRouteStopArrivalRoute(BaseModel):
    id: str
    """ID of the route"""

    actual_route_end_time: Optional[datetime] = FieldInfo(alias="actualRouteEndTime", default=None)
    """Actual end time, if it exists, for the route in RFC 3339 format."""

    actual_route_start_time: Optional[datetime] = FieldInfo(alias="actualRouteStartTime", default=None)
    """Actual start time, if it exists, for the route in RFC 3339 format."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Route name"""

    notes: Optional[str] = None
    """Notes for the route"""

    scheduled_route_end_time: Optional[datetime] = FieldInfo(alias="scheduledRouteEndTime", default=None)
    """Scheduled end time, if it exists, for the route in RFC 3339 format."""

    scheduled_route_start_time: Optional[datetime] = FieldInfo(alias="scheduledRouteStartTime", default=None)
    """Scheduled start time, if it exists, for the route in RFC 3339 format."""

    settings: Optional[DataConditionDetailsRouteStopArrivalRouteSettings] = None
    """
    An optional dictionary, only necessary to override the defaults for route start
    and end conditions.
    """

    stops: Optional[List[DataConditionDetailsRouteStopArrivalRouteStop]] = None
    """List of stops along the route"""


class DataConditionDetailsRouteStopArrivalRouteStopDetails(BaseModel):
    id: str
    """Unique identifier for the route stop."""

    state: Literal["unassigned", "scheduled", "en route", "skipped", "arrived", "departed"]
    """The current state of the route stop.

    Valid values: `unassigned`, `scheduled`, `en route`, `skipped`, `arrived`,
    `departed`
    """

    actual_arrival_time: Optional[datetime] = FieldInfo(alias="actualArrivalTime", default=None)
    """Actual arrival time, if it exists, for the route stop in RFC 3339 format."""

    actual_departure_time: Optional[datetime] = FieldInfo(alias="actualDepartureTime", default=None)
    """Actual departure time, if it exists, for the route stop in RFC 3339 format."""

    en_route_time: Optional[datetime] = FieldInfo(alias="enRouteTime", default=None)
    """The time the stop became en-route, in RFC 3339 format."""

    eta: Optional[datetime] = None
    """
    Estimated time of arrival, if this stop is currently en-route, in RFC 3339
    format.
    """

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    live_sharing_url: Optional[str] = FieldInfo(alias="liveSharingUrl", default=None)
    """The shareable url of the stop's current status."""

    skipped_time: Optional[datetime] = FieldInfo(alias="skippedTime", default=None)
    """Skipped time, if it exists, for the route stop in RFC 3339 format."""


class DataConditionDetailsRouteStopArrivalDriver(BaseModel):
    id: str
    """ID of the driver"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the driver"""


class DataConditionDetailsRouteStopArrivalVehicleGateway(BaseModel):
    model: Literal[
        "AG15",
        "AG24",
        "AG24EU",
        "AG26",
        "AG26EU",
        "AG41",
        "AG41EU",
        "AG45",
        "AG45EU",
        "AG46",
        "AG46EU",
        "AG46P",
        "AG46PEU",
        "AG51",
        "AG51EU",
        "AG52",
        "AG52EU",
        "AG53",
        "AG53EU",
        "IG15",
        "IG21",
        "IG41",
        "IG61",
        "SG1",
        "SG1B",
        "SG1G",
        "SG1G32",
        "SG1x",
        "VG32",
        "VG33",
        "VG34",
        "VG34EU",
        "VG34FN",
        "VG34M",
        "VG54ATT",
        "VG54EU",
        "VG54FN",
        "VG54NA",
        "VG54NAE",
        "VG54NAH",
        "VG55EU",
        "VG55FN",
        "VG55NA",
    ]
    """The model of the gateway installed on the asset.

    Valid values: `AG15`, `AG24`, `AG24EU`, `AG26`, `AG26EU`, `AG41`, `AG41EU`,
    `AG45`, `AG45EU`, `AG46`, `AG46EU`, `AG46P`, `AG46PEU`, `AG51`, `AG51EU`,
    `AG52`, `AG52EU`, `AG53`, `AG53EU`, `IG15`, `IG21`, `IG41`, `IG61`, `SG1`,
    `SG1B`, `SG1G`, `SG1G32`, `SG1x`, `VG32`, `VG33`, `VG34`, `VG34EU`, `VG34FN`,
    `VG34M`, `VG54ATT`, `VG54EU`, `VG54FN`, `VG54NA`, `VG54NAE`, `VG54NAH`,
    `VG55EU`, `VG55FN`, `VG55NA`
    """

    serial: str
    """The serial number of the gateway installed on the asset."""


class DataConditionDetailsRouteStopArrivalVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle"""

    asset_type: Optional[Literal["uncategorized", "trailer", "equipment", "unpowered", "vehicle"]] = FieldInfo(
        alias="assetType", default=None
    )
    """The type of the asset.

    Valid values: `uncategorized`, `trailer`, `equipment`, `unpowered`, `vehicle`
    """

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    gateway: Optional[DataConditionDetailsRouteStopArrivalVehicleGateway] = None
    """A minified gateway object"""

    license_plate: Optional[str] = FieldInfo(alias="licensePlate", default=None)
    """The license plate of the vehicle."""

    name: Optional[str] = None
    """Name of the vehicle"""

    vin: Optional[str] = None
    """The VIN of the vehicle."""


class DataConditionDetailsRouteStopArrival(BaseModel):
    route: DataConditionDetailsRouteStopArrivalRoute

    route_stop_details: DataConditionDetailsRouteStopArrivalRouteStopDetails = FieldInfo(alias="routeStopDetails")
    """A single route stop for a route."""

    time: datetime
    """The timestamp of the route in RFC 3339 format."""

    type: Literal["route tracking"]
    """The type of route update.

    The route tracking updates occur as a route is completed and stops transition
    from one state to another. Currently only Route Tracking updates are supported,
    but this will change in the future when additional types are added. Valid
    values: `route tracking`
    """

    driver: Optional[DataConditionDetailsRouteStopArrivalDriver] = None
    """A minified driver object.

    This object is only returned if the route is assigned to the driver.
    """

    operation: Optional[Literal["stop arrived", "stop departed"]] = None
    """The operation that was performed as part of this route update.

    Valid values: `stop arrived`, `stop departed`
    """

    vehicle: Optional[DataConditionDetailsRouteStopArrivalVehicle] = None
    """A minified vehicle object.

    This object is only returned if the route is assigned to the vehicle.
    """


class DataConditionDetailsRouteStopDepartureRouteSettings(BaseModel):
    route_completion_condition: Optional[Literal["arriveLastStop", "departLastStop"]] = FieldInfo(
        alias="routeCompletionCondition", default=None
    )
    """
    Defaults to 'arriveLastStop' which ends the route upon arriving at the final
    stop. The condition 'departLastStop' ends the route upon departing the last
    stop. If 'arriveLastStop' is set, then the departure time of the final stop
    should not be set. Valid values: `arriveLastStop`, `departLastStop`
    """

    route_starting_condition: Optional[Literal["departFirstStop", "arriveFirstStop"]] = FieldInfo(
        alias="routeStartingCondition", default=None
    )
    """
    Defaults to 'departFirstStop' which starts the route upon departing the first
    stop in the route. The condition 'arriveFirstStop' starts the route upon
    arriving at the first stop in the route. If 'departFirstStop' is set, the
    arrival time of the first stop should not be set. Valid values:
    `departFirstStop`, `arriveFirstStop`
    """


class DataConditionDetailsRouteStopDepartureRouteStopAddress(BaseModel):
    id: str
    """Id of the address"""

    name: str
    """Name of the address"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""


class DataConditionDetailsRouteStopDepartureRouteStopDocument(BaseModel):
    id: str
    """Id of the document"""

    name: Optional[str] = None
    """Name of the document"""


class DataConditionDetailsRouteStopDepartureRouteStopLocationLiveSharingLink(BaseModel):
    live_sharing_url: str = FieldInfo(alias="liveSharingUrl")
    """The shareable URL of the vehicle's location."""

    name: str
    """Name of the Live Sharing Link."""

    expires_at_time: Optional[str] = FieldInfo(alias="expiresAtTime", default=None)
    """Date that this link expires, in RFC 3339 format."""


class DataConditionDetailsRouteStopDepartureRouteStopSingleUseLocation(BaseModel):
    latitude: float
    """The latitude of the location"""

    longitude: float
    """The longitude of the location"""

    address: Optional[str] = None
    """Address of the stop."""


class DataConditionDetailsRouteStopDepartureRouteStop(BaseModel):
    id: str
    """Id of the stop"""

    name: str
    """Name of the stop"""

    state: Literal["unassigned", "scheduled", "en route", "skipped", "arrived", "departed"]
    """The current state of the route stop.

    Valid values: `unassigned`, `scheduled`, `en route`, `skipped`, `arrived`,
    `departed`
    """

    actual_arrival_time: Optional[datetime] = FieldInfo(alias="actualArrivalTime", default=None)
    """Actual arrival time, if it exists, for the route stop in RFC 3339 format."""

    actual_departure_time: Optional[datetime] = FieldInfo(alias="actualDepartureTime", default=None)
    """Actual departure time, if it exists, for the route stop in RFC 3339 format."""

    address: Optional[DataConditionDetailsRouteStopDepartureRouteStopAddress] = None
    """A minified Address object"""

    documents: Optional[List[DataConditionDetailsRouteStopDepartureRouteStopDocument]] = None
    """List of documents associated with the stop."""

    en_route_time: Optional[datetime] = FieldInfo(alias="enRouteTime", default=None)
    """The time the stop became en-route, in RFC 3339 format."""

    eta: Optional[datetime] = None
    """
    Estimated time of arrival, if this stop is currently en-route, in RFC 3339
    format.
    """

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    live_sharing_url: Optional[str] = FieldInfo(alias="liveSharingUrl", default=None)
    """The shareable url of the stop's current status."""

    location_live_sharing_links: Optional[
        List[DataConditionDetailsRouteStopDepartureRouteStopLocationLiveSharingLink]
    ] = FieldInfo(alias="locationLiveSharingLinks", default=None)
    """List of shareable, non-expired 'By Location' Live Sharing Links."""

    notes: Optional[str] = None
    """Notes for the stop"""

    ontime_window_after_arrival_ms: Optional[int] = FieldInfo(alias="ontimeWindowAfterArrivalMs", default=None)
    """
    Specifies the time window (in milliseconds) after a stop's scheduled arrival
    time during which the stop is considered 'on-time'.
    """

    ontime_window_before_arrival_ms: Optional[int] = FieldInfo(alias="ontimeWindowBeforeArrivalMs", default=None)
    """
    Specifies the time window (in milliseconds) before a stop's scheduled arrival
    time during which the stop is considered 'on-time'.
    """

    scheduled_arrival_time: Optional[datetime] = FieldInfo(alias="scheduledArrivalTime", default=None)
    """Scheduled arrival time, if it exists, for the stop in RFC 3339 format."""

    scheduled_departure_time: Optional[datetime] = FieldInfo(alias="scheduledDepartureTime", default=None)
    """Scheduled departure time, if it exists, for the stop in RFC 3339 format."""

    single_use_location: Optional[DataConditionDetailsRouteStopDepartureRouteStopSingleUseLocation] = FieldInfo(
        alias="singleUseLocation", default=None
    )
    """
    This field is used to indicate stops along the route for which an address has
    not been persisted. This field is mutually exclusive with addressId.
    """

    skipped_time: Optional[datetime] = FieldInfo(alias="skippedTime", default=None)
    """Skipped time, if it exists, for the route stop in RFC 3339 format."""


class DataConditionDetailsRouteStopDepartureRoute(BaseModel):
    id: str
    """ID of the route"""

    actual_route_end_time: Optional[datetime] = FieldInfo(alias="actualRouteEndTime", default=None)
    """Actual end time, if it exists, for the route in RFC 3339 format."""

    actual_route_start_time: Optional[datetime] = FieldInfo(alias="actualRouteStartTime", default=None)
    """Actual start time, if it exists, for the route in RFC 3339 format."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Route name"""

    notes: Optional[str] = None
    """Notes for the route"""

    scheduled_route_end_time: Optional[datetime] = FieldInfo(alias="scheduledRouteEndTime", default=None)
    """Scheduled end time, if it exists, for the route in RFC 3339 format."""

    scheduled_route_start_time: Optional[datetime] = FieldInfo(alias="scheduledRouteStartTime", default=None)
    """Scheduled start time, if it exists, for the route in RFC 3339 format."""

    settings: Optional[DataConditionDetailsRouteStopDepartureRouteSettings] = None
    """
    An optional dictionary, only necessary to override the defaults for route start
    and end conditions.
    """

    stops: Optional[List[DataConditionDetailsRouteStopDepartureRouteStop]] = None
    """List of stops along the route"""


class DataConditionDetailsRouteStopDepartureRouteStopDetails(BaseModel):
    id: str
    """Unique identifier for the route stop."""

    state: Literal["unassigned", "scheduled", "en route", "skipped", "arrived", "departed"]
    """The current state of the route stop.

    Valid values: `unassigned`, `scheduled`, `en route`, `skipped`, `arrived`,
    `departed`
    """

    actual_arrival_time: Optional[datetime] = FieldInfo(alias="actualArrivalTime", default=None)
    """Actual arrival time, if it exists, for the route stop in RFC 3339 format."""

    actual_departure_time: Optional[datetime] = FieldInfo(alias="actualDepartureTime", default=None)
    """Actual departure time, if it exists, for the route stop in RFC 3339 format."""

    en_route_time: Optional[datetime] = FieldInfo(alias="enRouteTime", default=None)
    """The time the stop became en-route, in RFC 3339 format."""

    eta: Optional[datetime] = None
    """
    Estimated time of arrival, if this stop is currently en-route, in RFC 3339
    format.
    """

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    live_sharing_url: Optional[str] = FieldInfo(alias="liveSharingUrl", default=None)
    """The shareable url of the stop's current status."""

    skipped_time: Optional[datetime] = FieldInfo(alias="skippedTime", default=None)
    """Skipped time, if it exists, for the route stop in RFC 3339 format."""


class DataConditionDetailsRouteStopDepartureDriver(BaseModel):
    id: str
    """ID of the driver"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the driver"""


class DataConditionDetailsRouteStopDepartureVehicleGateway(BaseModel):
    model: Literal[
        "AG15",
        "AG24",
        "AG24EU",
        "AG26",
        "AG26EU",
        "AG41",
        "AG41EU",
        "AG45",
        "AG45EU",
        "AG46",
        "AG46EU",
        "AG46P",
        "AG46PEU",
        "AG51",
        "AG51EU",
        "AG52",
        "AG52EU",
        "AG53",
        "AG53EU",
        "IG15",
        "IG21",
        "IG41",
        "IG61",
        "SG1",
        "SG1B",
        "SG1G",
        "SG1G32",
        "SG1x",
        "VG32",
        "VG33",
        "VG34",
        "VG34EU",
        "VG34FN",
        "VG34M",
        "VG54ATT",
        "VG54EU",
        "VG54FN",
        "VG54NA",
        "VG54NAE",
        "VG54NAH",
        "VG55EU",
        "VG55FN",
        "VG55NA",
    ]
    """The model of the gateway installed on the asset.

    Valid values: `AG15`, `AG24`, `AG24EU`, `AG26`, `AG26EU`, `AG41`, `AG41EU`,
    `AG45`, `AG45EU`, `AG46`, `AG46EU`, `AG46P`, `AG46PEU`, `AG51`, `AG51EU`,
    `AG52`, `AG52EU`, `AG53`, `AG53EU`, `IG15`, `IG21`, `IG41`, `IG61`, `SG1`,
    `SG1B`, `SG1G`, `SG1G32`, `SG1x`, `VG32`, `VG33`, `VG34`, `VG34EU`, `VG34FN`,
    `VG34M`, `VG54ATT`, `VG54EU`, `VG54FN`, `VG54NA`, `VG54NAE`, `VG54NAH`,
    `VG55EU`, `VG55FN`, `VG55NA`
    """

    serial: str
    """The serial number of the gateway installed on the asset."""


class DataConditionDetailsRouteStopDepartureVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle"""

    asset_type: Optional[Literal["uncategorized", "trailer", "equipment", "unpowered", "vehicle"]] = FieldInfo(
        alias="assetType", default=None
    )
    """The type of the asset.

    Valid values: `uncategorized`, `trailer`, `equipment`, `unpowered`, `vehicle`
    """

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    gateway: Optional[DataConditionDetailsRouteStopDepartureVehicleGateway] = None
    """A minified gateway object"""

    license_plate: Optional[str] = FieldInfo(alias="licensePlate", default=None)
    """The license plate of the vehicle."""

    name: Optional[str] = None
    """Name of the vehicle"""

    vin: Optional[str] = None
    """The VIN of the vehicle."""


class DataConditionDetailsRouteStopDeparture(BaseModel):
    route: DataConditionDetailsRouteStopDepartureRoute

    route_stop_details: DataConditionDetailsRouteStopDepartureRouteStopDetails = FieldInfo(alias="routeStopDetails")
    """A single route stop for a route."""

    time: datetime
    """The timestamp of the route in RFC 3339 format."""

    type: Literal["route tracking"]
    """The type of route update.

    The route tracking updates occur as a route is completed and stops transition
    from one state to another. Currently only Route Tracking updates are supported,
    but this will change in the future when additional types are added. Valid
    values: `route tracking`
    """

    driver: Optional[DataConditionDetailsRouteStopDepartureDriver] = None
    """A minified driver object.

    This object is only returned if the route is assigned to the driver.
    """

    operation: Optional[Literal["stop arrived", "stop departed"]] = None
    """The operation that was performed as part of this route update.

    Valid values: `stop arrived`, `stop departed`
    """

    vehicle: Optional[DataConditionDetailsRouteStopDepartureVehicle] = None
    """A minified vehicle object.

    This object is only returned if the route is assigned to the vehicle.
    """


class DataConditionDetailsRouteStopEtaDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsRouteStopEtaDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsRouteStopEtaDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsRouteStopEtaDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsRouteStopEtaDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsRouteStopEtaTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsRouteStopEtaTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsRouteStopEtaTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsRouteStopEtaTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsRouteStopEtaTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsRouteStopEtaVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsRouteStopEtaVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsRouteStopEtaVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsRouteStopEtaVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsRouteStopEtaVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsRouteStopEtaVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsRouteStopEtaVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsRouteStopEta(BaseModel):
    driver: Optional[DataConditionDetailsRouteStopEtaDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsRouteStopEtaTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsRouteStopEtaVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsScheduledMaintenanceDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsScheduledMaintenanceDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsScheduledMaintenanceDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsScheduledMaintenanceDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsScheduledMaintenanceDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsScheduledMaintenanceTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsScheduledMaintenanceTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsScheduledMaintenanceTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsScheduledMaintenanceTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsScheduledMaintenanceTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsScheduledMaintenanceVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsScheduledMaintenanceVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsScheduledMaintenanceVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsScheduledMaintenanceVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsScheduledMaintenanceVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsScheduledMaintenanceVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsScheduledMaintenanceVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsScheduledMaintenance(BaseModel):
    driver: Optional[DataConditionDetailsScheduledMaintenanceDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsScheduledMaintenanceTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsScheduledMaintenanceVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsScheduledMaintenanceByEngineHoursDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsScheduledMaintenanceByEngineHoursDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsScheduledMaintenanceByEngineHoursDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsScheduledMaintenanceByEngineHoursDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsScheduledMaintenanceByEngineHoursDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsScheduledMaintenanceByEngineHoursTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsScheduledMaintenanceByEngineHoursTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsScheduledMaintenanceByEngineHoursTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsScheduledMaintenanceByEngineHoursTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsScheduledMaintenanceByEngineHoursTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsScheduledMaintenanceByEngineHoursVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsScheduledMaintenanceByEngineHoursVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsScheduledMaintenanceByEngineHoursVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsScheduledMaintenanceByEngineHoursVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsScheduledMaintenanceByEngineHoursVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[
        DataConditionDetailsScheduledMaintenanceByEngineHoursVehicleStaticAssignedDriver
    ] = FieldInfo(alias="staticAssignedDriver", default=None)
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsScheduledMaintenanceByEngineHoursVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsScheduledMaintenanceByEngineHours(BaseModel):
    driver: Optional[DataConditionDetailsScheduledMaintenanceByEngineHoursDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsScheduledMaintenanceByEngineHoursTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsScheduledMaintenanceByEngineHoursVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsScheduledMaintenanceOdometerDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsScheduledMaintenanceOdometerDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsScheduledMaintenanceOdometerDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsScheduledMaintenanceOdometerDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsScheduledMaintenanceOdometerDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsScheduledMaintenanceOdometerTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsScheduledMaintenanceOdometerTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsScheduledMaintenanceOdometerTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsScheduledMaintenanceOdometerTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsScheduledMaintenanceOdometerTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsScheduledMaintenanceOdometerVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsScheduledMaintenanceOdometerVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsScheduledMaintenanceOdometerVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsScheduledMaintenanceOdometerVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsScheduledMaintenanceOdometerVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsScheduledMaintenanceOdometerVehicleStaticAssignedDriver] = (
        FieldInfo(alias="staticAssignedDriver", default=None)
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsScheduledMaintenanceOdometerVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsScheduledMaintenanceOdometer(BaseModel):
    driver: Optional[DataConditionDetailsScheduledMaintenanceOdometerDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsScheduledMaintenanceOdometerTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsScheduledMaintenanceOdometerVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsSevereSpeedingDataVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle"""

    asset_type: Optional[Literal["uncategorized", "trailer", "equipment", "unpowered", "vehicle"]] = FieldInfo(
        alias="assetType", default=None
    )
    """The type of the asset.

    Valid values: `uncategorized`, `trailer`, `equipment`, `unpowered`, `vehicle`
    """

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    license_plate: Optional[str] = FieldInfo(alias="licensePlate", default=None)
    """The license plate of the vehicle."""

    name: Optional[str] = None
    """Name of the vehicle"""

    vehicle_vin: Optional[str] = FieldInfo(alias="vehicleVin", default=None)
    """The VIN of the vehicle."""


class DataConditionDetailsSevereSpeedingData(BaseModel):
    start_time: str = FieldInfo(alias="startTime")
    """
    The speeding start time in RFC 3339 format (Examples: 2019-06-13T19:08:25Z,
    2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    vehicle: DataConditionDetailsSevereSpeedingDataVehicle
    """A vehicle object"""

    trip_start_time: Optional[str] = FieldInfo(alias="tripStartTime", default=None)
    """
    The trip start time in RFC 3339 format (Examples: 2019-06-13T19:08:25Z,
    2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """


class DataConditionDetailsSevereSpeeding(BaseModel):
    data: DataConditionDetailsSevereSpeedingData
    """The start of a severe speeding event"""


class DataConditionDetailsSiteGatewayDisconnectedDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsSiteGatewayDisconnectedDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsSiteGatewayDisconnectedDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsSiteGatewayDisconnectedDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsSiteGatewayDisconnectedDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsSiteGatewayDisconnectedTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsSiteGatewayDisconnectedTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsSiteGatewayDisconnectedTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsSiteGatewayDisconnectedTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsSiteGatewayDisconnectedTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsSiteGatewayDisconnectedVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsSiteGatewayDisconnectedVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsSiteGatewayDisconnectedVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsSiteGatewayDisconnectedVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsSiteGatewayDisconnectedVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsSiteGatewayDisconnectedVehicleStaticAssignedDriver] = (
        FieldInfo(alias="staticAssignedDriver", default=None)
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsSiteGatewayDisconnectedVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsSiteGatewayDisconnected(BaseModel):
    driver: Optional[DataConditionDetailsSiteGatewayDisconnectedDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsSiteGatewayDisconnectedTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsSiteGatewayDisconnectedVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsSpeedDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsSpeedDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsSpeedDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsSpeedDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsSpeedDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsSpeedTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsSpeedTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsSpeedTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsSpeedTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsSpeedTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsSpeedVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsSpeedVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsSpeedVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsSpeedVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsSpeedVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsSpeedVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsSpeedVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsSpeed(BaseModel):
    current_speed_kilometers_per_hour: int = FieldInfo(alias="currentSpeedKilometersPerHour")
    """Current speed of the vehicle in kilometers per hour."""

    min_duration_milliseconds: int = FieldInfo(alias="minDurationMilliseconds")
    """Minimum duration of the current speed in milliseconds."""

    operation: Literal["GREATER", "INSIDE_RANGE", "LESS", "OUTSIDE_RANGE"]
    """Operation of the current and threshold comparison.

    Valid values: `GREATER`, `INSIDE_RANGE`, `LESS`, `OUTSIDE_RANGE`
    """

    threshold_speed_kilometers_per_hour: int = FieldInfo(alias="thresholdSpeedKilometersPerHour")
    """Threshold speed of the vehicle in kilometers per hour."""

    driver: Optional[DataConditionDetailsSpeedDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsSpeedTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsSpeedVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsTamperingDetectedDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsTamperingDetectedDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsTamperingDetectedDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsTamperingDetectedDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsTamperingDetectedDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsTamperingDetectedTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsTamperingDetectedTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsTamperingDetectedTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsTamperingDetectedTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsTamperingDetectedTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsTamperingDetectedVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsTamperingDetectedVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsTamperingDetectedVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsTamperingDetectedVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsTamperingDetectedVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsTamperingDetectedVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsTamperingDetectedVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsTamperingDetected(BaseModel):
    driver: Optional[DataConditionDetailsTamperingDetectedDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsTamperingDetectedTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsTamperingDetectedVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsTireFaultsDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsTireFaultsDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsTireFaultsDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsTireFaultsDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsTireFaultsDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsTireFaultsTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsTireFaultsTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsTireFaultsTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsTireFaultsTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsTireFaultsTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsTireFaultsVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsTireFaultsVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsTireFaultsVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsTireFaultsVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsTireFaultsVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsTireFaultsVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsTireFaultsVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsTireFaults(BaseModel):
    driver: Optional[DataConditionDetailsTireFaultsDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsTireFaultsTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsTireFaultsVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsUnassignedDrivingDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsUnassignedDrivingDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsUnassignedDrivingDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsUnassignedDrivingDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsUnassignedDrivingDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsUnassignedDrivingVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsUnassignedDrivingVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsUnassignedDrivingVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsUnassignedDrivingVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsUnassignedDrivingVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsUnassignedDrivingVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsUnassignedDrivingVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsUnassignedDriving(BaseModel):
    driver: Optional[DataConditionDetailsUnassignedDrivingDriver] = None
    """A driver associated with the alert"""

    vehicle: Optional[DataConditionDetailsUnassignedDrivingVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsVehicleBatteryVoltageDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsVehicleBatteryVoltageDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsVehicleBatteryVoltageDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsVehicleBatteryVoltageDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsVehicleBatteryVoltageDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsVehicleBatteryVoltageTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsVehicleBatteryVoltageTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsVehicleBatteryVoltageTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsVehicleBatteryVoltageTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsVehicleBatteryVoltageTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsVehicleBatteryVoltageVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsVehicleBatteryVoltageVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsVehicleBatteryVoltageVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsVehicleBatteryVoltageVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsVehicleBatteryVoltageVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsVehicleBatteryVoltageVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsVehicleBatteryVoltageVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsVehicleBatteryVoltage(BaseModel):
    driver: Optional[DataConditionDetailsVehicleBatteryVoltageDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsVehicleBatteryVoltageTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsVehicleBatteryVoltageVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsVehicleDefLevelPercentageDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsVehicleDefLevelPercentageDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsVehicleDefLevelPercentageDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsVehicleDefLevelPercentageDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsVehicleDefLevelPercentageDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsVehicleDefLevelPercentageTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsVehicleDefLevelPercentageTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsVehicleDefLevelPercentageTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsVehicleDefLevelPercentageTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsVehicleDefLevelPercentageTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsVehicleDefLevelPercentageVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsVehicleDefLevelPercentageVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsVehicleDefLevelPercentageVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsVehicleDefLevelPercentageVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsVehicleDefLevelPercentageVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsVehicleDefLevelPercentageVehicleStaticAssignedDriver] = (
        FieldInfo(alias="staticAssignedDriver", default=None)
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsVehicleDefLevelPercentageVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsVehicleDefLevelPercentage(BaseModel):
    driver: Optional[DataConditionDetailsVehicleDefLevelPercentageDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsVehicleDefLevelPercentageTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsVehicleDefLevelPercentageVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetailsVehicleDetectedCameraStreamCameraDeviceSiteTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsVehicleDetectedCameraStreamCameraDeviceSite(BaseModel):
    id: str
    """The ID of the site associated with the alert"""

    name: Optional[str] = None
    """The name of the site"""

    tags: Optional[List[DataConditionDetailsVehicleDetectedCameraStreamCameraDeviceSiteTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Site.
    """


class DataConditionDetailsVehicleDetectedCameraStreamCameraDeviceTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsVehicleDetectedCameraStreamCameraDevice(BaseModel):
    id: str
    """The ID of the camera device associated with the alert"""

    name: Optional[str] = None
    """The name of the camera device"""

    sites: Optional[List[DataConditionDetailsVehicleDetectedCameraStreamCameraDeviceSite]] = None
    """The list of sites associated with the camera device."""

    tags: Optional[List[DataConditionDetailsVehicleDetectedCameraStreamCameraDeviceTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the camera device.
    """


class DataConditionDetailsVehicleDetectedCameraStreamTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsVehicleDetectedCameraStream(BaseModel):
    id: str
    """The ID of the camera stream associated with the alert."""

    camera_device: Optional[DataConditionDetailsVehicleDetectedCameraStreamCameraDevice] = FieldInfo(
        alias="cameraDevice", default=None
    )
    """A camera device associated with the alert"""

    name: Optional[str] = None
    """The name of the camera stream."""

    tags: Optional[List[DataConditionDetailsVehicleDetectedCameraStreamTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the camera stream.
    """


class DataConditionDetailsVehicleDetected(BaseModel):
    camera_stream: Optional[DataConditionDetailsVehicleDetectedCameraStream] = FieldInfo(
        alias="cameraStream", default=None
    )
    """A camera stream associated with the alert."""


class DataConditionDetailsVehicleFaultsDriverAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsVehicleFaultsDriverTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsVehicleFaultsDriver(BaseModel):
    id: str
    """The ID of the driver"""

    attributes: Optional[List[DataConditionDetailsVehicleFaultsDriverAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the driver."""

    tags: Optional[List[DataConditionDetailsVehicleFaultsDriverTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the driver.
    """


class DataConditionDetailsVehicleFaultsTrailerAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsVehicleFaultsTrailerTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsVehicleFaultsTrailer(BaseModel):
    id: str
    """The ID of the trailer.

    This is automatically generated when the trailer is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataConditionDetailsVehicleFaultsTrailerAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    tags: Optional[List[DataConditionDetailsVehicleFaultsTrailerTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class DataConditionDetailsVehicleFaultsVehicleAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataConditionDetailsVehicleFaultsVehicleStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataConditionDetailsVehicleFaultsVehicleTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataConditionDetailsVehicleFaultsVehicle(BaseModel):
    id: str
    """The ID of the vehicle."""

    serial: str
    """The serial number of the gateway installed on the asset."""

    attributes: Optional[List[DataConditionDetailsVehicleFaultsVehicleAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """The name of the vehicle."""

    static_assigned_driver: Optional[DataConditionDetailsVehicleFaultsVehicleStaticAssignedDriver] = FieldInfo(
        alias="staticAssignedDriver", default=None
    )
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataConditionDetailsVehicleFaultsVehicleTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the vehicle.
    """


class DataConditionDetailsVehicleFaults(BaseModel):
    driver: Optional[DataConditionDetailsVehicleFaultsDriver] = None
    """A driver associated with the alert"""

    trailer: Optional[DataConditionDetailsVehicleFaultsTrailer] = None
    """A trailer associated with the alert"""

    vehicle: Optional[DataConditionDetailsVehicleFaultsVehicle] = None
    """The vehicle associated with the alert."""


class DataConditionDetails(BaseModel):
    ambient_temperature: Optional[DataConditionDetailsAmbientTemperature] = FieldInfo(
        alias="ambientTemperature", default=None
    )
    """Details specific to Ambient Temperature."""

    camera_connector_disconected: Optional[DataConditionDetailsCameraConnectorDisconected] = FieldInfo(
        alias="cameraConnectorDisconected", default=None
    )
    """Details specific to Camera Connector Disconnected."""

    camera_stream_issue: Optional[DataConditionDetailsCameraStreamIssue] = FieldInfo(
        alias="cameraStreamIssue", default=None
    )
    """Details specific to Camera Stream Issue."""

    cell_signal_loss: Optional[DataConditionDetailsCellSignalLoss] = FieldInfo(alias="cellSignalLoss", default=None)
    """Details specific to Cell Signal Loss."""

    cloud_backup_upload_issue: Optional[DataConditionDetailsCloudBackupUploadIssue] = FieldInfo(
        alias="cloudBackupUploadIssue", default=None
    )
    """Details specific to Cloud Backup Upload Issue."""

    dashcam_disconnected: Optional[DataConditionDetailsDashcamDisconnected] = FieldInfo(
        alias="dashcamDisconnected", default=None
    )
    """Details specific to Dashcam Disconnected."""

    data_input_value: Optional[DataConditionDetailsDataInputValue] = FieldInfo(alias="dataInputValue", default=None)
    """Details specific to Data Input Value."""

    device_movement: Optional[DataConditionDetailsDeviceMovement] = FieldInfo(alias="deviceMovement", default=None)
    """Details specific to Device Movement."""

    device_movement_stopped: Optional[DataConditionDetailsDeviceMovementStopped] = FieldInfo(
        alias="deviceMovementStopped", default=None
    )
    """Details specific to Device Movement Stopped."""

    driver_app_sign_in: Optional[DataConditionDetailsDriverAppSignIn] = FieldInfo(alias="driverAppSignIn", default=None)
    """Details specific to Driver App Sign In."""

    driver_app_sign_out: Optional[DataConditionDetailsDriverAppSignOut] = FieldInfo(
        alias="driverAppSignOut", default=None
    )
    """Details specific to Driver App Sign Out."""

    driver_document_submitted: Optional[DataConditionDetailsDriverDocumentSubmitted] = FieldInfo(
        alias="driverDocumentSubmitted", default=None
    )
    """Details specific to Driver Document Submitted."""

    driver_message_received: Optional[DataConditionDetailsDriverMessageReceived] = FieldInfo(
        alias="driverMessageReceived", default=None
    )
    """Details specific to Driver Message Received."""

    driver_message_sent: Optional[DataConditionDetailsDriverMessageSent] = FieldInfo(
        alias="driverMessageSent", default=None
    )
    """Details specific to Driver Message Sent."""

    driver_recorded: Optional[DataConditionDetailsDriverRecorded] = FieldInfo(alias="driverRecorded", default=None)
    """Details specific to Driver Recorded."""

    dvir_submitted_device: Optional[DataConditionDetailsDvirSubmittedDevice] = FieldInfo(
        alias="dvirSubmittedDevice", default=None
    )
    """Details specific to DVIR Submitted."""

    engine_idle: Optional[DataConditionDetailsEngineIdle] = FieldInfo(alias="engineIdle", default=None)
    """Details specific to Engine Idle."""

    engine_off: Optional[DataConditionDetailsEngineOff] = FieldInfo(alias="engineOff", default=None)
    """Details specific to Engine Off."""

    engine_on: Optional[DataConditionDetailsEngineOn] = FieldInfo(alias="engineOn", default=None)
    """Details specific to Engine On."""

    form_submitted: Optional[DataConditionDetailsFormSubmitted] = FieldInfo(alias="formSubmitted", default=None)
    """Details specific to Form Submitted."""

    fuel_level_percentage: Optional[DataConditionDetailsFuelLevelPercentage] = FieldInfo(
        alias="fuelLevelPercentage", default=None
    )
    """Details specific to Fuel Level Percentage."""

    gateway_disconnected: Optional[DataConditionDetailsGatewayDisconnected] = FieldInfo(
        alias="gatewayDisconnected", default=None
    )
    """Details specific to Gateway Disconnected."""

    gateway_unplugged: Optional[DataConditionDetailsGatewayUnplugged] = FieldInfo(
        alias="gatewayUnplugged", default=None
    )

    geofence_entry: Optional[DataConditionDetailsGeofenceEntry] = FieldInfo(alias="geofenceEntry", default=None)

    geofence_exit: Optional[DataConditionDetailsGeofenceExit] = FieldInfo(alias="geofenceExit", default=None)

    gps_signal_loss: Optional[DataConditionDetailsGpsSignalLoss] = FieldInfo(alias="gpsSignalLoss", default=None)
    """Details specific to GPS Signal Loss."""

    harsh_event: Optional[DataConditionDetailsHarshEvent] = FieldInfo(alias="harshEvent", default=None)
    """Details specific to Harsh Event."""

    hos_violation: Optional[DataConditionDetailsHosViolation] = FieldInfo(alias="hosViolation", default=None)
    """Details specific to Hos Violation."""

    inactivity: Optional[DataConditionDetailsInactivity] = None
    """Details specific to Inactivity."""

    inside_geofence: Optional[DataConditionDetailsInsideGeofence] = FieldInfo(alias="insideGeofence", default=None)
    """Details specific to Inside Geofence."""

    issue_created: Optional[DataConditionDetailsIssueCreated] = FieldInfo(alias="issueCreated", default=None)
    """Details specific to Issue Created."""

    jamming_detected: Optional[DataConditionDetailsJammingDetected] = FieldInfo(alias="jammingDetected", default=None)
    """Details specific to Jamming Detected."""

    motion_detected: Optional[DataConditionDetailsMotionDetected] = FieldInfo(alias="motionDetected", default=None)
    """Details specific to Motion Detected."""

    out_of_route: Optional[DataConditionDetailsOutOfRoute] = FieldInfo(alias="outOfRoute", default=None)
    """Details specific to Out Of Route."""

    outside_geofence: Optional[DataConditionDetailsOutsideGeofence] = FieldInfo(alias="outsideGeofence", default=None)
    """Details specific to Outside Geofence."""

    panic_button: Optional[DataConditionDetailsPanicButton] = FieldInfo(alias="panicButton", default=None)
    """Details specific to Panic Button."""

    person_detected: Optional[DataConditionDetailsPersonDetected] = FieldInfo(alias="personDetected", default=None)
    """Details specific to Person Detected."""

    reefer_temperature: Optional[DataConditionDetailsReeferTemperature] = FieldInfo(
        alias="reeferTemperature", default=None
    )
    """Details specific to Reefer Temperature."""

    route_stop_arrival: Optional[DataConditionDetailsRouteStopArrival] = FieldInfo(
        alias="routeStopArrival", default=None
    )

    route_stop_departure: Optional[DataConditionDetailsRouteStopDeparture] = FieldInfo(
        alias="routeStopDeparture", default=None
    )

    route_stop_eta: Optional[DataConditionDetailsRouteStopEta] = FieldInfo(alias="routeStopETA", default=None)
    """Details specific to Route Stop ETA."""

    scheduled_maintenance: Optional[DataConditionDetailsScheduledMaintenance] = FieldInfo(
        alias="scheduledMaintenance", default=None
    )
    """Details specific to Scheduled Maintenance."""

    scheduled_maintenance_by_engine_hours: Optional[DataConditionDetailsScheduledMaintenanceByEngineHours] = FieldInfo(
        alias="scheduledMaintenanceByEngineHours", default=None
    )
    """Details specific to Scheduled Maintenance By Engine Hours."""

    scheduled_maintenance_odometer: Optional[DataConditionDetailsScheduledMaintenanceOdometer] = FieldInfo(
        alias="scheduledMaintenanceOdometer", default=None
    )
    """Details specific to Scheduled Maintenance By Odometer."""

    severe_speeding: Optional[DataConditionDetailsSevereSpeeding] = FieldInfo(alias="severeSpeeding", default=None)
    """The start of a severe speeding event"""

    site_gateway_disconnected: Optional[DataConditionDetailsSiteGatewayDisconnected] = FieldInfo(
        alias="siteGatewayDisconnected", default=None
    )
    """Details specific to Site Gateway Disconnected."""

    speed: Optional[DataConditionDetailsSpeed] = None
    """Details specific to Speed."""

    tampering_detected: Optional[DataConditionDetailsTamperingDetected] = FieldInfo(
        alias="tamperingDetected", default=None
    )
    """Details specific to Tampering Detected."""

    tire_faults: Optional[DataConditionDetailsTireFaults] = FieldInfo(alias="tireFaults", default=None)
    """Details specific to Tire Faults."""

    unassigned_driving: Optional[DataConditionDetailsUnassignedDriving] = FieldInfo(
        alias="unassignedDriving", default=None
    )
    """Details specific to Unassigned Driving."""

    vehicle_battery_voltage: Optional[DataConditionDetailsVehicleBatteryVoltage] = FieldInfo(
        alias="vehicleBatteryVoltage", default=None
    )
    """Details specific to Vehicle Battery Voltage."""

    vehicle_def_level_percentage: Optional[DataConditionDetailsVehicleDefLevelPercentage] = FieldInfo(
        alias="vehicleDefLevelPercentage", default=None
    )
    """Details specific to Vehicle DEF Level Percentage."""

    vehicle_detected: Optional[DataConditionDetailsVehicleDetected] = FieldInfo(alias="vehicleDetected", default=None)
    """Details specific to Vehicle Detected."""

    vehicle_faults: Optional[DataConditionDetailsVehicleFaults] = FieldInfo(alias="vehicleFaults", default=None)
    """Details specific to Vehicle Faults."""


class DataCondition(BaseModel):
    description: str
    """Descriptive name of the condition."""

    details: DataConditionDetails
    """Object representing the granular details of the condition.

    These details will vary depending on the condition.
    """

    trigger_id: int = FieldInfo(alias="triggerId")
    """Unique identifier describing the type of condition being represented."""


class Data(BaseModel):
    conditions: List[DataCondition]
    """An array of conditions associated with the incident."""

    configuration_id: str = FieldInfo(alias="configurationId")
    """Unique ID of the alert configuration."""

    happened_at_time: str = FieldInfo(alias="happenedAtTime")
    """Time and date that the alert incident occurred in RFC 3339 format."""

    incident_url: str = FieldInfo(alias="incidentUrl")
    """Url of alert incident in the cloud dashboard."""

    is_resolved: bool = FieldInfo(alias="isResolved")
    """Indicates whether the incident is resolved or not."""

    updated_at_time: str = FieldInfo(alias="updatedAtTime")
    """Time and date that the alert incident updated in RFC 3339 format."""

    resolved_at_time: Optional[str] = FieldInfo(alias="resolvedAtTime", default=None)
    """Time and date that the alert incident was resolved in RFC 3339 format."""


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


class IncidentStreamResponse(BaseModel):
    data: List[Data]
    """List of workflow incidents."""

    pagination: Pagination
    """Pagination parameters."""
