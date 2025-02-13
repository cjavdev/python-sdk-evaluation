# Alerts
(*alerts*)

## Overview

### Available Operations

* [delete_configurations](#delete_configurations) - Delete alert configurations.
* [get_configurations](#get_configurations) - Get Alert Configurations.
* [patch_configurations](#patch_configurations) - Update alert configurations.
* [post_configurations](#post_configurations) - Create alert configurations.
* [get_incidents](#get_incidents) - Get Alert Incidents.

## delete_configurations

Delete an alert configuration.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Alerts** under the Alerts category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.alerts.delete_configurations(id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The unqiue Samsara id of the alert configuration.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AlertsDeleteConfigurationsBadRequestErrorResponseBody](../../models/alertsdeleteconfigurationsbadrequesterrorresponsebody.md)**

### Errors

| Error Type                                                           | Status Code                                                          | Content Type                                                         |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| models.AlertsDeleteConfigurationsUnauthorizedErrorResponseBody       | 401                                                                  | application/json                                                     |
| models.AlertsDeleteConfigurationsNotFoundErrorResponseBody           | 404                                                                  | application/json                                                     |
| models.AlertsDeleteConfigurationsMethodNotAllowedErrorResponseBody   | 405                                                                  | application/json                                                     |
| models.AlertsDeleteConfigurationsTooManyRequestsErrorResponseBody    | 429                                                                  | application/json                                                     |
| models.AlertsDeleteConfigurationsInternalServerErrorResponseBody     | 500                                                                  | application/json                                                     |
| models.AlertsDeleteConfigurationsNotImplementedErrorResponseBody     | 501                                                                  | application/json                                                     |
| models.AlertsDeleteConfigurationsBadGatewayErrorResponseBody         | 502                                                                  | application/json                                                     |
| models.AlertsDeleteConfigurationsServiceUnavailableErrorResponseBody | 503                                                                  | application/json                                                     |
| models.AlertsDeleteConfigurationsGatewayTimeoutErrorResponseBody     | 504                                                                  | application/json                                                     |
| models.APIError                                                      | 4XX, 5XX                                                             | \*/\*                                                                |

## get_configurations

Get specified Alert Configurations.

The following trigger types are API enabled and will show up in the results:
Vehicle Speed
Ambient Temperature
Fuel Level (Percentage)
Vehicle DEF Level (Percentage)
Vehicle Battery
Gateway Unplugged
Dashcam Disconnected
Camera Connector Disconnected
Asset starts moving
Inside Geofence
Outside Geofence
Unassigned Driving
Driver HOS Violation
Vehicle Engine Idle
Asset Engine On
Asset Engine Off
Harsh Event
Scheduled Maintenance
Scheduled Maintenance by Odometer
Scheduled Maintenance by Engine Hours
Out of Route
GPS Signal Loss
Cell Signal Loss
Fault Code
Tire Faults
Gateway Disconnected
Panic Button
Tampering Detected
If vehicle is severely speeding (as defined by your organization)
DVIR Submitted for Asset
Driver Document Submitted
Driver App Sign In
Driver App Sign Out
Geofence Entry
Geofence Exit
Route Stop ETA Alert
Driver Recorded
Scheduled Date And Time
Training Assignment Due Soon
Training Assignment Past Due

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Alerts** under the Alerts category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.alerts.get_configurations()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                       | Type                                                                                                                                                                                                            | Required                                                                                                                                                                                                        | Description                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ids`                                                                                                                                                                                                           | List[*str*]                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                              | Filter by the IDs. Returns all if no ids are provided.                                                                                                                                                          |
| `status`                                                                                                                                                                                                        | [Optional[models.QueryParamStatus]](../../models/queryparamstatus.md)                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                              | The status of the alert configuration.  Valid values: `all`, `enabled`, `disabled`                                                                                                                              |
| `after`                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              |  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. |
| `include_external_ids`                                                                                                                                                                                          | *Optional[bool]*                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Optional boolean indicating whether to return external IDs on supported entities                                                                                                                                |
| `retries`                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                             |

### Response

**[models.GetConfigurationsResponse](../../models/getconfigurationsresponse.md)**

### Errors

| Error Type                                                        | Status Code                                                       | Content Type                                                      |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| models.AlertsGetConfigurationsUnauthorizedErrorResponseBody       | 401                                                               | application/json                                                  |
| models.AlertsGetConfigurationsNotFoundErrorResponseBody           | 404                                                               | application/json                                                  |
| models.AlertsGetConfigurationsMethodNotAllowedErrorResponseBody   | 405                                                               | application/json                                                  |
| models.AlertsGetConfigurationsTooManyRequestsErrorResponseBody    | 429                                                               | application/json                                                  |
| models.AlertsGetConfigurationsInternalServerErrorResponseBody     | 500                                                               | application/json                                                  |
| models.AlertsGetConfigurationsNotImplementedErrorResponseBody     | 501                                                               | application/json                                                  |
| models.AlertsGetConfigurationsBadGatewayErrorResponseBody         | 502                                                               | application/json                                                  |
| models.AlertsGetConfigurationsServiceUnavailableErrorResponseBody | 503                                                               | application/json                                                  |
| models.AlertsGetConfigurationsGatewayTimeoutErrorResponseBody     | 504                                                               | application/json                                                  |
| models.APIError                                                   | 4XX, 5XX                                                          | \*/\*                                                             |

## patch_configurations

Updates an alert configuration.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Alerts** under the Alerts category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
import samsara
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.alerts.patch_configurations(id="e1c5dffc-c7b7-47b0-a778-6a65de638abf", actions=[
        {
            "action_type_id": 1,
            "action_params": {
                "driver_app_notification": {
                    "in_app_notification_options": {
                        "custom_text": "Custom text",
                    },
                    "push_notification_options": {},
                },
                "recipients": [
                    {
                        "type": samsara.RecipientObjectRequestBodyType.USER,
                        "contact_id": "1234",
                        "notification_types": [
                            samsara.RecipientObjectRequestBodyNotificationTypes.SMS,
                        ],
                        "role_id": "67004a16-be3c-4ef6-a51b-1c45a2c27a92",
                        "user_id": "1234",
                    },
                    {
                        "type": samsara.RecipientObjectRequestBodyType.USER,
                        "contact_id": "1234",
                        "notification_types": [
                            samsara.RecipientObjectRequestBodyNotificationTypes.SMS,
                        ],
                        "role_id": "67004a16-be3c-4ef6-a51b-1c45a2c27a92",
                        "user_id": "1234",
                    },
                    {
                        "type": samsara.RecipientObjectRequestBodyType.USER,
                        "contact_id": "1234",
                        "notification_types": [
                            samsara.RecipientObjectRequestBodyNotificationTypes.SMS,
                        ],
                        "role_id": "67004a16-be3c-4ef6-a51b-1c45a2c27a92",
                        "user_id": "1234",
                    },
                ],
                "webhooks": {
                    "webhook_ids": [
                        "123",
                    ],
                },
            },
        },
        {
            "action_type_id": 1,
            "action_params": {
                "driver_app_notification": {
                    "in_app_notification_options": {
                        "custom_text": "Custom text",
                    },
                    "push_notification_options": {},
                },
                "recipients": [
                    {
                        "type": samsara.RecipientObjectRequestBodyType.USER,
                        "contact_id": "1234",
                        "notification_types": [
                            samsara.RecipientObjectRequestBodyNotificationTypes.SMS,
                        ],
                        "role_id": "67004a16-be3c-4ef6-a51b-1c45a2c27a92",
                        "user_id": "1234",
                    },
                ],
                "webhooks": {
                    "webhook_ids": [
                        "123",
                    ],
                },
            },
        },
    ], is_enabled=True, name="My Harsh Event Alert", operational_settings={
        "time_range_type": samsara.OperationalSettingsObjectRequestBodyTimeRangeType.ACTIVE_BETWEEN,
        "time_ranges": [
            {
                "days_of_week": [
                    samsara.TimeRangeObjectRequestBodyDaysOfWeek.THURSDAY,
                ],
                "end_time": "20:00",
                "start_time": "11:00",
                "timezone": "America/Los_Angeles",
            },
        ],
    }, scope={
        "all": True,
        "assets": [
            {
                "asset_id": "12443",
            },
            {
                "asset_id": "12443",
            },
        ],
        "drivers": [
            {
                "driver_id": "12434",
            },
            {
                "driver_id": "12434",
            },
        ],
        "tags": [
            {
                "id": "3914",
                "name": "East Coast",
                "parent_tag_id": "4815",
            },
        ],
        "widgets": [
            {
                "widget_id": "12434",
            },
            {
                "widget_id": "12434",
            },
        ],
    }, triggers=[
        samsara.WorkflowTriggerObjectRequestBody(
            trigger_type_id=1000,
            trigger_params=samsara.TriggerParamsObjectRequestBody(
                ambient_temperature={
                    "min_duration_milliseconds": 600000,
                    "operation": samsara.AmbientTemperatureDetailsObjectRequestBodyOperation.GREATER,
                    "temperature_celcius": 60,
                    "cargo_is_full": True,
                    "doors_are_closed": True,
                },
                cell_signal_loss={
                    "min_duration_milliseconds": 600000,
                },
                def_level={
                    "def_level_percent": 100,
                    "min_duration_milliseconds": 600000,
                    "operation": samsara.DefLevelTriggerDetailsObjectRequestBodyOperation.GREATER,
                },
                device_movement={
                    "min_duration_milliseconds": 600000,
                },
                document_submitted={
                    "template_ids": [
                        "23b78345-d098-3k4j-1pk3-4k5j6938j289",
                        "23b78345-d098-3k4j-1pk3-4k5j6938j289",
                    ],
                },
                dvir_submitted_device={
                    "dvir_min_duration_milliseconds": 600000,
                    "dvir_submission_types": [
                        samsara.DVIRSubmittedDeviceTriggerDetailsObjectRequestBodyDVIRSubmissionTypes.SAFE_WITH_DEFECTS,
                    ],
                },
                engine_idle={
                    "min_duration_milliseconds": 600000,
                },
                engine_off={
                    "min_duration_milliseconds": 600000,
                },
                engine_on={
                    "min_duration_milliseconds": 600000,
                },
                fuel_level={
                    "fuel_level_percent": 20,
                    "min_duration_milliseconds": 600000,
                    "operation": samsara.FuelLevelTriggerDetailsObjectRequestBodyOperation.LESS,
                },
                gateway_disconnected={
                    "min_duration_milliseconds": 3600000,
                },
                gateway_unplugged={
                    "min_duration_milliseconds": 600000,
                },
                geofence_entry={
                    "location": {
                        "address_ids": [
                            "Rerum consectetur ut et.",
                        ],
                        "address_types": [
                            samsara.LocationObjectRequestBodyAddressTypes.RISK_ZONE,
                        ],
                        "circle": {
                            "name": "My Geofence Cirlce",
                            "radius_meters": 23,
                            "latitude": 37.7749,
                            "longitude": 137.7749,
                        },
                        "polygon": {
                            "name": "My Geofence Polygon",
                            "vertices": [
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                            ],
                        },
                        "tag_ids": [
                            "4815",
                        ],
                    },
                },
                geofence_exit={
                    "location": {
                        "address_ids": [
                            "Rerum consectetur ut et.",
                        ],
                        "address_types": [
                            samsara.LocationObjectRequestBodyAddressTypes.RISK_ZONE,
                        ],
                        "circle": {
                            "name": "My Geofence Cirlce",
                            "radius_meters": 23,
                            "latitude": 37.7749,
                            "longitude": 137.7749,
                        },
                        "polygon": {
                            "name": "My Geofence Polygon",
                            "vertices": [
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                            ],
                        },
                        "tag_ids": [
                            "4815",
                        ],
                    },
                },
                gps_signal_loss={
                    "min_duration_milliseconds": 600000,
                },
                harsh_event={
                    "types": [
                        samsara.HarshEventTriggerDetailsObjectRequestBodyTypes.HA_DRINK_POLICY,
                    ],
                },
                hos_violation={
                    "max_until_violation_milliseconds": 600000,
                    "violation": samsara.HOSViolationTriggerDetailsObjectRequestBodyViolation.CALIFORNIA_MEALBREAK_MISSED,
                },
                inside_geofence={
                    "location": {
                        "address_ids": [
                            "Rerum consectetur ut et.",
                        ],
                        "address_types": [
                            samsara.LocationObjectRequestBodyAddressTypes.RISK_ZONE,
                        ],
                        "circle": {
                            "name": "My Geofence Cirlce",
                            "radius_meters": 23,
                            "latitude": 37.7749,
                            "longitude": 137.7749,
                        },
                        "polygon": {
                            "name": "My Geofence Polygon",
                            "vertices": [
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                            ],
                        },
                        "tag_ids": [
                            "4815",
                        ],
                    },
                    "min_duration_milliseconds": 600000,
                },
                out_of_route={
                    "max_off_route_meters": 100,
                    "min_duration_milliseconds": 600000,
                },
                outside_geofence={
                    "location": {
                        "address_ids": [
                            "Rerum consectetur ut et.",
                        ],
                        "address_types": [
                            samsara.LocationObjectRequestBodyAddressTypes.RISK_ZONE,
                        ],
                        "circle": {
                            "name": "My Geofence Cirlce",
                            "radius_meters": 23,
                            "latitude": 37.7749,
                            "longitude": 137.7749,
                        },
                        "polygon": {
                            "name": "My Geofence Polygon",
                            "vertices": [
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                            ],
                        },
                        "tag_ids": [
                            "4815",
                        ],
                    },
                    "min_duration_milliseconds": 600000,
                },
                panic_button={
                    "is_filtering_out_power_loss": True,
                },
                route_stop_estimated_arrival={
                    "alert_before_arrival_milliseconds": 300000,
                    "location": {
                        "address_ids": [
                            "Rerum consectetur ut et.",
                        ],
                        "address_types": [
                            samsara.LocationObjectRequestBodyAddressTypes.RISK_ZONE,
                        ],
                        "circle": {
                            "name": "My Geofence Cirlce",
                            "radius_meters": 23,
                            "latitude": 37.7749,
                            "longitude": 137.7749,
                        },
                        "polygon": {
                            "name": "My Geofence Polygon",
                            "vertices": [
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                            ],
                        },
                        "tag_ids": [
                            "4815",
                        ],
                    },
                    "has_live_share_link": True,
                    "is_alert_on_route_stop_only": True,
                },
                scheduled_maintenance={
                    "due_in_days": 10,
                    "schedule_id": "123",
                },
                scheduled_maintenance_by_engine_hours={
                    "due_in_hours": 5000,
                    "schedule_id": "123",
                },
                scheduled_maintenance_odometer={
                    "due_in_meters": 5000,
                    "schedule_id": "123",
                },
                speed={
                    "min_duration_milliseconds": 600000,
                    "operation": samsara.SpeedTriggerDetailsObjectRequestBodyOperation.GREATER,
                    "speed_kilometers_per_hour": 120,
                },
                tire_fault_code={
                    "manufacturer": samsara.TireFaultCodeDetailsObjectRequestBodyManufacturer.MANUFACTURER_BENDIX,
                    "has_cautionary_tire_fault_codes": True,
                    "has_critical_tire_fault_codes": True,
                    "specific_tire_fault_codes": [
                        samsara.TireFaultCodeDetailsObjectRequestBodySpecificTireFaultCodes.TIRE_ALERT_ACROSS_AXLE_FAULT,
                    ],
                },
                training_assignment_near_due_date={
                    "condition_units": samsara.TrainingAssignmentNearDueDateTriggerDetailsObjectRequestBodyConditionUnits.DAYS,
                    "condition_value": 1,
                    "timezone": "America/Los_Angeles",
                    "assignment_groups": [
                        {
                            "assignment_group_type": samsara.TrainingAssignmentNearDueDateTriggerAssignmentGroupObjectRequestBodyAssignmentGroupType.CATEGORY,
                            "assignment_group_uuid": "0732ac5e-dc72-429f-9661-e50394e97d47",
                        },
                        {
                            "assignment_group_type": samsara.TrainingAssignmentNearDueDateTriggerAssignmentGroupObjectRequestBodyAssignmentGroupType.CATEGORY,
                            "assignment_group_uuid": "53504316-a3ca-4322-9aba-6ae363d498e1",
                        },
                    ],
                },
                unassigned_driving={
                    "min_duration_milliseconds": 600000,
                },
                vehicle_battery_voltage={
                    "battery_volts": 100,
                    "min_duration_milliseconds": 600000,
                    "operation": samsara.VehicleBatterVoltageDetailsObjectRequestBodyOperation.GREATER,
                },
                vehicle_fault_code={
                    "has_any_amber_warning_lamp_codes": True,
                    "has_any_fault_codes": True,
                    "has_any_malfunction_indicator_lamp_codes": True,
                    "has_any_protection_lamp_codes": True,
                    "has_any_red_stop_lamp_codes": True,
                    "has_any_trailer_abs_lamp_codes": True,
                    "specific_fault_codes": [
                        {
                            "fault_code": "1067",
                            "type": samsara.SpecificVehicleFaultCodeObjectRequestBodyType.J1939_SPN,
                        },
                        {
                            "fault_code": "1067",
                            "type": samsara.SpecificVehicleFaultCodeObjectRequestBodyType.J1939_SPN,
                        },
                        {
                            "fault_code": "1067",
                            "type": samsara.SpecificVehicleFaultCodeObjectRequestBodyType.J1939_SPN,
                        },
                    ],
                },
            ),
        ),
        samsara.WorkflowTriggerObjectRequestBody(
            trigger_type_id=1000,
            trigger_params=samsara.TriggerParamsObjectRequestBody(
                ambient_temperature={
                    "min_duration_milliseconds": 600000,
                    "operation": samsara.AmbientTemperatureDetailsObjectRequestBodyOperation.GREATER,
                    "temperature_celcius": 60,
                    "cargo_is_full": True,
                    "doors_are_closed": True,
                },
                cell_signal_loss={
                    "min_duration_milliseconds": 600000,
                },
                def_level={
                    "def_level_percent": 100,
                    "min_duration_milliseconds": 600000,
                    "operation": samsara.DefLevelTriggerDetailsObjectRequestBodyOperation.GREATER,
                },
                device_movement={
                    "min_duration_milliseconds": 600000,
                },
                document_submitted={
                    "template_ids": [
                        "23b78345-d098-3k4j-1pk3-4k5j6938j289",
                        "23b78345-d098-3k4j-1pk3-4k5j6938j289",
                    ],
                },
                dvir_submitted_device={
                    "dvir_min_duration_milliseconds": 600000,
                    "dvir_submission_types": [
                        samsara.DVIRSubmittedDeviceTriggerDetailsObjectRequestBodyDVIRSubmissionTypes.SAFE_WITH_DEFECTS,
                    ],
                },
                engine_idle={
                    "min_duration_milliseconds": 600000,
                },
                engine_off={
                    "min_duration_milliseconds": 600000,
                },
                engine_on={
                    "min_duration_milliseconds": 600000,
                },
                fuel_level={
                    "fuel_level_percent": 20,
                    "min_duration_milliseconds": 600000,
                    "operation": samsara.FuelLevelTriggerDetailsObjectRequestBodyOperation.LESS,
                },
                gateway_disconnected={
                    "min_duration_milliseconds": 3600000,
                },
                gateway_unplugged={
                    "min_duration_milliseconds": 600000,
                },
                geofence_entry={
                    "location": {
                        "address_ids": [
                            "Rerum consectetur ut et.",
                        ],
                        "address_types": [
                            samsara.LocationObjectRequestBodyAddressTypes.RISK_ZONE,
                        ],
                        "circle": {
                            "name": "My Geofence Cirlce",
                            "radius_meters": 23,
                            "latitude": 37.7749,
                            "longitude": 137.7749,
                        },
                        "polygon": {
                            "name": "My Geofence Polygon",
                            "vertices": [
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                            ],
                        },
                        "tag_ids": [
                            "4815",
                        ],
                    },
                },
                geofence_exit={
                    "location": {
                        "address_ids": [
                            "Rerum consectetur ut et.",
                        ],
                        "address_types": [
                            samsara.LocationObjectRequestBodyAddressTypes.RISK_ZONE,
                        ],
                        "circle": {
                            "name": "My Geofence Cirlce",
                            "radius_meters": 23,
                            "latitude": 37.7749,
                            "longitude": 137.7749,
                        },
                        "polygon": {
                            "name": "My Geofence Polygon",
                            "vertices": [
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                            ],
                        },
                        "tag_ids": [
                            "4815",
                        ],
                    },
                },
                gps_signal_loss={
                    "min_duration_milliseconds": 600000,
                },
                harsh_event={
                    "types": [
                        samsara.HarshEventTriggerDetailsObjectRequestBodyTypes.HA_DRINK_POLICY,
                    ],
                },
                hos_violation={
                    "max_until_violation_milliseconds": 600000,
                    "violation": samsara.HOSViolationTriggerDetailsObjectRequestBodyViolation.CALIFORNIA_MEALBREAK_MISSED,
                },
                inside_geofence={
                    "location": {
                        "address_ids": [
                            "Rerum consectetur ut et.",
                        ],
                        "address_types": [
                            samsara.LocationObjectRequestBodyAddressTypes.RISK_ZONE,
                        ],
                        "circle": {
                            "name": "My Geofence Cirlce",
                            "radius_meters": 23,
                            "latitude": 37.7749,
                            "longitude": 137.7749,
                        },
                        "polygon": {
                            "name": "My Geofence Polygon",
                            "vertices": [
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                            ],
                        },
                        "tag_ids": [
                            "4815",
                        ],
                    },
                    "min_duration_milliseconds": 600000,
                },
                out_of_route={
                    "max_off_route_meters": 100,
                    "min_duration_milliseconds": 600000,
                },
                outside_geofence={
                    "location": {
                        "address_ids": [
                            "Rerum consectetur ut et.",
                        ],
                        "address_types": [
                            samsara.LocationObjectRequestBodyAddressTypes.RISK_ZONE,
                        ],
                        "circle": {
                            "name": "My Geofence Cirlce",
                            "radius_meters": 23,
                            "latitude": 37.7749,
                            "longitude": 137.7749,
                        },
                        "polygon": {
                            "name": "My Geofence Polygon",
                            "vertices": [
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                            ],
                        },
                        "tag_ids": [
                            "4815",
                        ],
                    },
                    "min_duration_milliseconds": 600000,
                },
                panic_button={
                    "is_filtering_out_power_loss": True,
                },
                route_stop_estimated_arrival={
                    "alert_before_arrival_milliseconds": 300000,
                    "location": {
                        "address_ids": [
                            "Rerum consectetur ut et.",
                        ],
                        "address_types": [
                            samsara.LocationObjectRequestBodyAddressTypes.RISK_ZONE,
                        ],
                        "circle": {
                            "name": "My Geofence Cirlce",
                            "radius_meters": 23,
                            "latitude": 37.7749,
                            "longitude": 137.7749,
                        },
                        "polygon": {
                            "name": "My Geofence Polygon",
                            "vertices": [
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                            ],
                        },
                        "tag_ids": [
                            "4815",
                        ],
                    },
                    "has_live_share_link": True,
                    "is_alert_on_route_stop_only": True,
                },
                scheduled_maintenance={
                    "due_in_days": 10,
                    "schedule_id": "123",
                },
                scheduled_maintenance_by_engine_hours={
                    "due_in_hours": 5000,
                    "schedule_id": "123",
                },
                scheduled_maintenance_odometer={
                    "due_in_meters": 5000,
                    "schedule_id": "123",
                },
                speed={
                    "min_duration_milliseconds": 600000,
                    "operation": samsara.SpeedTriggerDetailsObjectRequestBodyOperation.GREATER,
                    "speed_kilometers_per_hour": 120,
                },
                tire_fault_code={
                    "manufacturer": samsara.TireFaultCodeDetailsObjectRequestBodyManufacturer.MANUFACTURER_BENDIX,
                    "has_cautionary_tire_fault_codes": True,
                    "has_critical_tire_fault_codes": True,
                    "specific_tire_fault_codes": [
                        samsara.TireFaultCodeDetailsObjectRequestBodySpecificTireFaultCodes.TIRE_ALERT_ACROSS_AXLE_FAULT,
                    ],
                },
                training_assignment_near_due_date={
                    "condition_units": samsara.TrainingAssignmentNearDueDateTriggerDetailsObjectRequestBodyConditionUnits.DAYS,
                    "condition_value": 1,
                    "timezone": "America/Los_Angeles",
                    "assignment_groups": [
                        {
                            "assignment_group_type": samsara.TrainingAssignmentNearDueDateTriggerAssignmentGroupObjectRequestBodyAssignmentGroupType.CATEGORY,
                            "assignment_group_uuid": "15bcd442-9dae-45d1-b552-6eb2821a33c0",
                        },
                        {
                            "assignment_group_type": samsara.TrainingAssignmentNearDueDateTriggerAssignmentGroupObjectRequestBodyAssignmentGroupType.CATEGORY,
                            "assignment_group_uuid": "dd4d6ecf-2ad6-4ec9-8b35-a215c0933ba6",
                        },
                    ],
                },
                unassigned_driving={
                    "min_duration_milliseconds": 600000,
                },
                vehicle_battery_voltage={
                    "battery_volts": 100,
                    "min_duration_milliseconds": 600000,
                    "operation": samsara.VehicleBatterVoltageDetailsObjectRequestBodyOperation.GREATER,
                },
                vehicle_fault_code={
                    "has_any_amber_warning_lamp_codes": True,
                    "has_any_fault_codes": True,
                    "has_any_malfunction_indicator_lamp_codes": True,
                    "has_any_protection_lamp_codes": True,
                    "has_any_red_stop_lamp_codes": True,
                    "has_any_trailer_abs_lamp_codes": True,
                    "specific_fault_codes": [
                        {
                            "fault_code": "1067",
                            "type": samsara.SpecificVehicleFaultCodeObjectRequestBodyType.J1939_SPN,
                        },
                    ],
                },
            ),
        ),
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   | Example                                                                                                       |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                          | *str*                                                                                                         | :heavy_check_mark:                                                                                            | The unqiue Samsara id of the alert configuration.                                                             | e1c5dffc-c7b7-47b0-a778-6a65de638abf                                                                          |
| `actions`                                                                                                     | List[[models.ActionObjectRequestBody](../../models/actionobjectrequestbody.md)]                               | :heavy_minus_sign:                                                                                            | An array of actions.                                                                                          |                                                                                                               |
| `external_ids`                                                                                                | Dict[str, *str*]                                                                                              | :heavy_minus_sign:                                                                                            | A map of external ids                                                                                         |                                                                                                               |
| `is_enabled`                                                                                                  | *Optional[bool]*                                                                                              | :heavy_minus_sign:                                                                                            | Whether the alert is enabled or not.                                                                          | true                                                                                                          |
| `name`                                                                                                        | *Optional[str]*                                                                                               | :heavy_minus_sign:                                                                                            | The custom name of the configuration.                                                                         | My Harsh Event Alert                                                                                          |
| `operational_settings`                                                                                        | [Optional[models.OperationalSettingsObjectRequestBody]](../../models/operationalsettingsobjectrequestbody.md) | :heavy_minus_sign:                                                                                            | Settings on when the alert should be operational.                                                             |                                                                                                               |
| `scope`                                                                                                       | [Optional[models.ScopeObjectRequestBody]](../../models/scopeobjectrequestbody.md)                             | :heavy_minus_sign:                                                                                            | What the triggers are scoped to. These are the objects this alert applies to.                                 |                                                                                                               |
| `triggers`                                                                                                    | List[[models.WorkflowTriggerObjectRequestBody](../../models/workflowtriggerobjectrequestbody.md)]             | :heavy_minus_sign:                                                                                            | An array of triggers.                                                                                         |                                                                                                               |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |                                                                                                               |

### Response

**[models.PatchConfigurationsResponse](../../models/patchconfigurationsresponse.md)**

### Errors

| Error Type                                                          | Status Code                                                         | Content Type                                                        |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| models.AlertsPatchConfigurationsUnauthorizedErrorResponseBody       | 401                                                                 | application/json                                                    |
| models.AlertsPatchConfigurationsNotFoundErrorResponseBody           | 404                                                                 | application/json                                                    |
| models.AlertsPatchConfigurationsMethodNotAllowedErrorResponseBody   | 405                                                                 | application/json                                                    |
| models.AlertsPatchConfigurationsTooManyRequestsErrorResponseBody    | 429                                                                 | application/json                                                    |
| models.AlertsPatchConfigurationsInternalServerErrorResponseBody     | 500                                                                 | application/json                                                    |
| models.AlertsPatchConfigurationsNotImplementedErrorResponseBody     | 501                                                                 | application/json                                                    |
| models.AlertsPatchConfigurationsBadGatewayErrorResponseBody         | 502                                                                 | application/json                                                    |
| models.AlertsPatchConfigurationsServiceUnavailableErrorResponseBody | 503                                                                 | application/json                                                    |
| models.AlertsPatchConfigurationsGatewayTimeoutErrorResponseBody     | 504                                                                 | application/json                                                    |
| models.APIError                                                     | 4XX, 5XX                                                            | \*/\*                                                               |

## post_configurations

Creates an alert configuration.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Alerts** under the Alerts category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
import samsara
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.alerts.post_configurations(actions=[
        {
            "action_type_id": 1,
            "action_params": {
                "driver_app_notification": {
                    "in_app_notification_options": {
                        "custom_text": "Custom text",
                    },
                    "push_notification_options": {},
                },
                "recipients": [
                    {
                        "type": samsara.RecipientObjectRequestBodyType.USER,
                        "contact_id": "1234",
                        "notification_types": [
                            samsara.RecipientObjectRequestBodyNotificationTypes.SMS,
                        ],
                        "role_id": "67004a16-be3c-4ef6-a51b-1c45a2c27a92",
                        "user_id": "1234",
                    },
                ],
                "webhooks": {
                    "webhook_ids": [
                        "123",
                    ],
                },
            },
        },
    ], name="My Harsh Event Alert", scope={
        "all": True,
        "assets": [
            {
                "asset_id": "12443",
            },
            {
                "asset_id": "12443",
            },
            {
                "asset_id": "12443",
            },
        ],
        "drivers": [
            {
                "driver_id": "12434",
            },
            {
                "driver_id": "12434",
            },
        ],
        "tags": [
            {
                "id": "3914",
                "name": "East Coast",
                "parent_tag_id": "4815",
            },
        ],
        "widgets": [
            {
                "widget_id": "12434",
            },
        ],
    }, triggers=[
        samsara.WorkflowTriggerObjectRequestBody(
            trigger_type_id=1000,
            trigger_params=samsara.TriggerParamsObjectRequestBody(
                ambient_temperature={
                    "min_duration_milliseconds": 600000,
                    "operation": samsara.AmbientTemperatureDetailsObjectRequestBodyOperation.GREATER,
                    "temperature_celcius": 60,
                    "cargo_is_full": True,
                    "doors_are_closed": True,
                },
                cell_signal_loss={
                    "min_duration_milliseconds": 600000,
                },
                def_level={
                    "def_level_percent": 100,
                    "min_duration_milliseconds": 600000,
                    "operation": samsara.DefLevelTriggerDetailsObjectRequestBodyOperation.GREATER,
                },
                device_movement={
                    "min_duration_milliseconds": 600000,
                },
                document_submitted={
                    "template_ids": [
                        "23b78345-d098-3k4j-1pk3-4k5j6938j289",
                        "23b78345-d098-3k4j-1pk3-4k5j6938j289",
                    ],
                },
                dvir_submitted_device={
                    "dvir_min_duration_milliseconds": 600000,
                    "dvir_submission_types": [
                        samsara.DVIRSubmittedDeviceTriggerDetailsObjectRequestBodyDVIRSubmissionTypes.SAFE_WITH_DEFECTS,
                    ],
                },
                engine_idle={
                    "min_duration_milliseconds": 600000,
                },
                engine_off={
                    "min_duration_milliseconds": 600000,
                },
                engine_on={
                    "min_duration_milliseconds": 600000,
                },
                fuel_level={
                    "fuel_level_percent": 20,
                    "min_duration_milliseconds": 600000,
                    "operation": samsara.FuelLevelTriggerDetailsObjectRequestBodyOperation.LESS,
                },
                gateway_disconnected={
                    "min_duration_milliseconds": 3600000,
                },
                gateway_unplugged={
                    "min_duration_milliseconds": 600000,
                },
                geofence_entry={
                    "location": {
                        "address_ids": [
                            "Rerum consectetur ut et.",
                        ],
                        "address_types": [
                            samsara.LocationObjectRequestBodyAddressTypes.RISK_ZONE,
                        ],
                        "circle": {
                            "name": "My Geofence Cirlce",
                            "radius_meters": 23,
                            "latitude": 37.7749,
                            "longitude": 137.7749,
                        },
                        "polygon": {
                            "name": "My Geofence Polygon",
                            "vertices": [
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                            ],
                        },
                        "tag_ids": [
                            "4815",
                        ],
                    },
                },
                geofence_exit={
                    "location": {
                        "address_ids": [
                            "Rerum consectetur ut et.",
                        ],
                        "address_types": [
                            samsara.LocationObjectRequestBodyAddressTypes.RISK_ZONE,
                        ],
                        "circle": {
                            "name": "My Geofence Cirlce",
                            "radius_meters": 23,
                            "latitude": 37.7749,
                            "longitude": 137.7749,
                        },
                        "polygon": {
                            "name": "My Geofence Polygon",
                            "vertices": [
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                            ],
                        },
                        "tag_ids": [
                            "4815",
                        ],
                    },
                },
                gps_signal_loss={
                    "min_duration_milliseconds": 600000,
                },
                harsh_event={
                    "types": [
                        samsara.HarshEventTriggerDetailsObjectRequestBodyTypes.HA_DRINK_POLICY,
                    ],
                },
                hos_violation={
                    "max_until_violation_milliseconds": 600000,
                    "violation": samsara.HOSViolationTriggerDetailsObjectRequestBodyViolation.CALIFORNIA_MEALBREAK_MISSED,
                },
                inside_geofence={
                    "location": {
                        "address_ids": [
                            "Rerum consectetur ut et.",
                        ],
                        "address_types": [
                            samsara.LocationObjectRequestBodyAddressTypes.RISK_ZONE,
                        ],
                        "circle": {
                            "name": "My Geofence Cirlce",
                            "radius_meters": 23,
                            "latitude": 37.7749,
                            "longitude": 137.7749,
                        },
                        "polygon": {
                            "name": "My Geofence Polygon",
                            "vertices": [
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                            ],
                        },
                        "tag_ids": [
                            "4815",
                        ],
                    },
                    "min_duration_milliseconds": 600000,
                },
                out_of_route={
                    "max_off_route_meters": 100,
                    "min_duration_milliseconds": 600000,
                },
                outside_geofence={
                    "location": {
                        "address_ids": [
                            "Rerum consectetur ut et.",
                        ],
                        "address_types": [
                            samsara.LocationObjectRequestBodyAddressTypes.RISK_ZONE,
                        ],
                        "circle": {
                            "name": "My Geofence Cirlce",
                            "radius_meters": 23,
                            "latitude": 37.7749,
                            "longitude": 137.7749,
                        },
                        "polygon": {
                            "name": "My Geofence Polygon",
                            "vertices": [
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                            ],
                        },
                        "tag_ids": [
                            "4815",
                        ],
                    },
                    "min_duration_milliseconds": 600000,
                },
                panic_button={
                    "is_filtering_out_power_loss": True,
                },
                route_stop_estimated_arrival={
                    "alert_before_arrival_milliseconds": 300000,
                    "location": {
                        "address_ids": [
                            "Rerum consectetur ut et.",
                        ],
                        "address_types": [
                            samsara.LocationObjectRequestBodyAddressTypes.RISK_ZONE,
                        ],
                        "circle": {
                            "name": "My Geofence Cirlce",
                            "radius_meters": 23,
                            "latitude": 37.7749,
                            "longitude": 137.7749,
                        },
                        "polygon": {
                            "name": "My Geofence Polygon",
                            "vertices": [
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                                {
                                    "latitude": 37.7749,
                                    "longitude": 137.7749,
                                },
                            ],
                        },
                        "tag_ids": [
                            "4815",
                        ],
                    },
                    "has_live_share_link": True,
                    "is_alert_on_route_stop_only": True,
                },
                scheduled_maintenance={
                    "due_in_days": 10,
                    "schedule_id": "123",
                },
                scheduled_maintenance_by_engine_hours={
                    "due_in_hours": 5000,
                    "schedule_id": "123",
                },
                scheduled_maintenance_odometer={
                    "due_in_meters": 5000,
                    "schedule_id": "123",
                },
                speed={
                    "min_duration_milliseconds": 600000,
                    "operation": samsara.SpeedTriggerDetailsObjectRequestBodyOperation.GREATER,
                    "speed_kilometers_per_hour": 120,
                },
                tire_fault_code={
                    "manufacturer": samsara.TireFaultCodeDetailsObjectRequestBodyManufacturer.MANUFACTURER_BENDIX,
                    "has_cautionary_tire_fault_codes": True,
                    "has_critical_tire_fault_codes": True,
                    "specific_tire_fault_codes": [
                        samsara.TireFaultCodeDetailsObjectRequestBodySpecificTireFaultCodes.TIRE_ALERT_ACROSS_AXLE_FAULT,
                    ],
                },
                training_assignment_near_due_date={
                    "condition_units": samsara.TrainingAssignmentNearDueDateTriggerDetailsObjectRequestBodyConditionUnits.DAYS,
                    "condition_value": 1,
                    "timezone": "America/Los_Angeles",
                    "assignment_groups": [
                        {
                            "assignment_group_type": samsara.TrainingAssignmentNearDueDateTriggerAssignmentGroupObjectRequestBodyAssignmentGroupType.CATEGORY,
                            "assignment_group_uuid": "8417c184-3208-4288-a8d9-9efd23370b8a",
                        },
                        {
                            "assignment_group_type": samsara.TrainingAssignmentNearDueDateTriggerAssignmentGroupObjectRequestBodyAssignmentGroupType.CATEGORY,
                            "assignment_group_uuid": "84d4d6ec-a736-40fc-90b2-be72614440b4",
                        },
                    ],
                },
                unassigned_driving={
                    "min_duration_milliseconds": 600000,
                },
                vehicle_battery_voltage={
                    "battery_volts": 100,
                    "min_duration_milliseconds": 600000,
                    "operation": samsara.VehicleBatterVoltageDetailsObjectRequestBodyOperation.GREATER,
                },
                vehicle_fault_code={
                    "has_any_amber_warning_lamp_codes": True,
                    "has_any_fault_codes": True,
                    "has_any_malfunction_indicator_lamp_codes": True,
                    "has_any_protection_lamp_codes": True,
                    "has_any_red_stop_lamp_codes": True,
                    "has_any_trailer_abs_lamp_codes": True,
                    "specific_fault_codes": [
                        {
                            "fault_code": "1067",
                            "type": samsara.SpecificVehicleFaultCodeObjectRequestBodyType.J1939_SPN,
                        },
                    ],
                },
            ),
        ),
    ], operational_settings={
        "time_range_type": samsara.OperationalSettingsObjectRequestBodyTimeRangeType.ACTIVE_BETWEEN,
        "time_ranges": [

        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   | Example                                                                                                       |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `actions`                                                                                                     | List[[models.ActionObjectRequestBody](../../models/actionobjectrequestbody.md)]                               | :heavy_check_mark:                                                                                            | An array of actions.                                                                                          |                                                                                                               |
| `name`                                                                                                        | *str*                                                                                                         | :heavy_check_mark:                                                                                            | The custom name of the configuration.                                                                         | My Harsh Event Alert                                                                                          |
| `scope`                                                                                                       | [models.ScopeObjectRequestBody](../../models/scopeobjectrequestbody.md)                                       | :heavy_check_mark:                                                                                            | What the triggers are scoped to. These are the objects this alert applies to.                                 |                                                                                                               |
| `triggers`                                                                                                    | List[[models.WorkflowTriggerObjectRequestBody](../../models/workflowtriggerobjectrequestbody.md)]             | :heavy_check_mark:                                                                                            | An array of triggers.                                                                                         |                                                                                                               |
| `external_ids`                                                                                                | Dict[str, *str*]                                                                                              | :heavy_minus_sign:                                                                                            | A map of external ids                                                                                         |                                                                                                               |
| `is_enabled`                                                                                                  | *Optional[bool]*                                                                                              | :heavy_minus_sign:                                                                                            | Whether the alert is enabled or not.                                                                          | true                                                                                                          |
| `operational_settings`                                                                                        | [Optional[models.OperationalSettingsObjectRequestBody]](../../models/operationalsettingsobjectrequestbody.md) | :heavy_minus_sign:                                                                                            | Settings on when the alert should be operational.                                                             |                                                                                                               |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |                                                                                                               |

### Response

**[models.PostConfigurationsResponse](../../models/postconfigurationsresponse.md)**

### Errors

| Error Type                                                         | Status Code                                                        | Content Type                                                       |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| models.AlertsPostConfigurationsUnauthorizedErrorResponseBody       | 401                                                                | application/json                                                   |
| models.AlertsPostConfigurationsNotFoundErrorResponseBody           | 404                                                                | application/json                                                   |
| models.AlertsPostConfigurationsMethodNotAllowedErrorResponseBody   | 405                                                                | application/json                                                   |
| models.AlertsPostConfigurationsTooManyRequestsErrorResponseBody    | 429                                                                | application/json                                                   |
| models.AlertsPostConfigurationsInternalServerErrorResponseBody     | 500                                                                | application/json                                                   |
| models.AlertsPostConfigurationsNotImplementedErrorResponseBody     | 501                                                                | application/json                                                   |
| models.AlertsPostConfigurationsBadGatewayErrorResponseBody         | 502                                                                | application/json                                                   |
| models.AlertsPostConfigurationsServiceUnavailableErrorResponseBody | 503                                                                | application/json                                                   |
| models.AlertsPostConfigurationsGatewayTimeoutErrorResponseBody     | 504                                                                | application/json                                                   |
| models.APIError                                                    | 4XX, 5XX                                                           | \*/\*                                                              |

## get_incidents

Get Alert Incidents for specific Alert Configurations over a specified period of time.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Alerts** under the Alerts category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

### Example Usage

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.alerts.get_incidents(start_time="<value>", configuration_ids=[
        "<value>",
        "<value>",
        "<value>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                       | Type                                                                                                                                                                                                            | Required                                                                                                                                                                                                        | Description                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                                                                                                    | *str*                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                              | Required RFC 3339 timestamp that indicates when to begin receiving data. This will be based on updatedAtTime.                                                                                                   |
| `configuration_ids`                                                                                                                                                                                             | List[*str*]                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                              | Required array of alert configuration ids to return incident data for.                                                                                                                                          |
| `end_time`                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              | Optional RFC 3339 timestamp to stop receiving data. Defaults to now if not provided. This will be based on updatedAtTime.                                                                                       |
| `after`                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                              |  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. |
| `retries`                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                             |

### Response

**[models.GetIncidentsResponse](../../models/getincidentsresponse.md)**

### Errors

| Error Type                                                   | Status Code                                                  | Content Type                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| models.AlertsGetIncidentsUnauthorizedErrorResponseBody       | 401                                                          | application/json                                             |
| models.AlertsGetIncidentsNotFoundErrorResponseBody           | 404                                                          | application/json                                             |
| models.AlertsGetIncidentsMethodNotAllowedErrorResponseBody   | 405                                                          | application/json                                             |
| models.AlertsGetIncidentsTooManyRequestsErrorResponseBody    | 429                                                          | application/json                                             |
| models.AlertsGetIncidentsInternalServerErrorResponseBody     | 500                                                          | application/json                                             |
| models.AlertsGetIncidentsNotImplementedErrorResponseBody     | 501                                                          | application/json                                             |
| models.AlertsGetIncidentsBadGatewayErrorResponseBody         | 502                                                          | application/json                                             |
| models.AlertsGetIncidentsServiceUnavailableErrorResponseBody | 503                                                          | application/json                                             |
| models.AlertsGetIncidentsGatewayTimeoutErrorResponseBody     | 504                                                          | application/json                                             |
| models.APIError                                              | 4XX, 5XX                                                     | \*/\*                                                        |