# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.alerts import (
    ConfigurationListResponse,
    ConfigurationCreateResponse,
    ConfigurationUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigurations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        configuration = client.alerts.configurations.create(
            actions=[{"action_type_id": 1}],
            is_enabled=True,
            name="My Harsh Event Alert",
            scope={"all": False},
            triggers=[{"trigger_type_id": 1000}],
        )
        assert_matches_type(ConfigurationCreateResponse, configuration, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Samsara) -> None:
        configuration = client.alerts.configurations.create(
            actions=[
                {
                    "action_type_id": 1,
                    "action_params": {
                        "driver_app_notification": {
                            "in_app_notification_options": {
                                "is_enabled": True,
                                "can_dictate_alert_title": False,
                                "can_play_alert_sound": False,
                                "custom_text": "Custom text",
                            },
                            "push_notification_options": {"is_enabled": True},
                        },
                        "recipients": [
                            {
                                "type": "user",
                                "contact_id": "1234",
                                "notification_types": ["push", "sms", "email"],
                                "role_id": "67004a16-be3c-4ef6-a51b-1c45a2c27a92",
                                "user_id": "1234",
                            }
                        ],
                        "webhooks": {
                            "webhook_ids": ["123", "123", "123"],
                            "payload_type": "legacy",
                        },
                    },
                }
            ],
            is_enabled=True,
            name="My Harsh Event Alert",
            scope={
                "all": False,
                "assets": [
                    {
                        "asset_id": "12443",
                        "asset_type": "uncategorized",
                    }
                ],
                "drivers": [{"driver_id": "12434"}],
                "tags": [
                    {
                        "id": "3914",
                        "name": "East Coast",
                        "parent_tag_id": "4815",
                    }
                ],
                "widgets": [{"widget_id": "12434"}],
            },
            triggers=[
                {
                    "trigger_type_id": 1000,
                    "trigger_params": {
                        "ambient_temperature": {
                            "min_duration_milliseconds": 600000,
                            "operation": "GREATER",
                            "temperature_celcius": 60,
                            "cargo_is_full": True,
                            "doors_are_closed": True,
                        },
                        "cell_signal_loss": {"min_duration_milliseconds": 600000},
                        "def_level": {
                            "def_level_percent": 100,
                            "min_duration_milliseconds": 600000,
                            "operation": "GREATER",
                        },
                        "device_movement": {"min_duration_milliseconds": 600000},
                        "document_submitted": {
                            "template_ids": [
                                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            ]
                        },
                        "dvir_submitted_device": {
                            "dvir_min_duration_milliseconds": 600000,
                            "dvir_submission_types": [
                                "SAFE_NO_DEFECTS",
                                "SAFE_WITH_DEFECTS",
                                "UNSAFE",
                                "SAFE_NO_DEFECTS",
                            ],
                        },
                        "engine_idle": {"min_duration_milliseconds": 600000},
                        "engine_off": {"min_duration_milliseconds": 600000},
                        "engine_on": {"min_duration_milliseconds": 600000},
                        "fuel_level": {
                            "fuel_level_percent": 20,
                            "min_duration_milliseconds": 600000,
                            "operation": "LESS",
                        },
                        "gateway_disconnected": {"min_duration_milliseconds": 3600000},
                        "gateway_unplugged": {"min_duration_milliseconds": 600000},
                        "geofence_entry": {
                            "location": {
                                "address_ids": [
                                    "Ipsam doloremque.",
                                    "Quisquam rerum dolorum et unde.",
                                    "In culpa voluptas ab.",
                                    "Repellendus vel fugit iure.",
                                ],
                                "address_types": ["alertsOnly", "industrialSite"],
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
                                        }
                                    ],
                                },
                                "tag_ids": ["4815", "4815", "4815"],
                            }
                        },
                        "geofence_exit": {
                            "location": {
                                "address_ids": [
                                    "Ipsam doloremque.",
                                    "Quisquam rerum dolorum et unde.",
                                    "In culpa voluptas ab.",
                                    "Repellendus vel fugit iure.",
                                ],
                                "address_types": ["alertsOnly", "industrialSite"],
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
                                        }
                                    ],
                                },
                                "tag_ids": ["4815", "4815", "4815"],
                            }
                        },
                        "gps_signal_loss": {"min_duration_milliseconds": 600000},
                        "harsh_event": {"types": ["haAccel", "haBraking", "haCameraMisaligned", "haCrash"]},
                        "hos_violation": {
                            "max_until_violation_milliseconds": 600000,
                            "violation": "CaliforniaMealbreakMissed",
                        },
                        "inside_geofence": {
                            "location": {
                                "address_ids": [
                                    "Ipsam doloremque.",
                                    "Quisquam rerum dolorum et unde.",
                                    "In culpa voluptas ab.",
                                    "Repellendus vel fugit iure.",
                                ],
                                "address_types": ["alertsOnly", "industrialSite"],
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
                                        }
                                    ],
                                },
                                "tag_ids": ["4815", "4815", "4815"],
                            },
                            "min_duration_milliseconds": 600000,
                        },
                        "out_of_route": {
                            "max_off_route_meters": 100,
                            "min_duration_milliseconds": 600000,
                        },
                        "outside_geofence": {
                            "location": {
                                "address_ids": [
                                    "Ipsam doloremque.",
                                    "Quisquam rerum dolorum et unde.",
                                    "In culpa voluptas ab.",
                                    "Repellendus vel fugit iure.",
                                ],
                                "address_types": ["alertsOnly", "industrialSite"],
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
                                        }
                                    ],
                                },
                                "tag_ids": ["4815", "4815", "4815"],
                            },
                            "min_duration_milliseconds": 600000,
                        },
                        "panic_button": {"is_filtering_out_power_loss": True},
                        "route_stop_estimated_arrival": {
                            "alert_before_arrival_milliseconds": 300000,
                            "location": {
                                "address_ids": [
                                    "Ipsam doloremque.",
                                    "Quisquam rerum dolorum et unde.",
                                    "In culpa voluptas ab.",
                                    "Repellendus vel fugit iure.",
                                ],
                                "address_types": ["alertsOnly", "industrialSite"],
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
                                        }
                                    ],
                                },
                                "tag_ids": ["4815", "4815", "4815"],
                            },
                            "has_live_share_link": True,
                            "is_alert_on_route_stop_only": True,
                        },
                        "scheduled_maintenance": {
                            "due_in_days": 10,
                            "schedule_id": "123",
                        },
                        "scheduled_maintenance_by_engine_hours": {
                            "due_in_hours": 5000,
                            "schedule_id": "123",
                        },
                        "scheduled_maintenance_odometer": {
                            "due_in_meters": 5000,
                            "schedule_id": "123",
                        },
                        "speed": {
                            "min_duration_milliseconds": 600000,
                            "operation": "GREATER",
                            "speed_kilometers_per_hour": 120,
                        },
                        "tire_fault_code": {
                            "manufacturer": "MANUFACTURER_BENDIX",
                            "has_cautionary_tire_fault_codes": True,
                            "has_critical_tire_fault_codes": True,
                            "specific_tire_fault_codes": [
                                "TIRE_ALERT_ACROSS_AXLE_FAULT",
                                "TIRE_ALERT_EXTREME_OVER_PRESSURE",
                                "TIRE_ALERT_EXTREME_UNDER_PRESSURE",
                                "TIRE_ALERT_INVALID",
                            ],
                        },
                        "unassigned_driving": {"min_duration_milliseconds": 600000},
                        "vehicle_battery_voltage": {
                            "battery_volts": 100,
                            "min_duration_milliseconds": 600000,
                            "operation": "GREATER",
                        },
                        "vehicle_fault_code": {
                            "has_any_amber_warning_lamp_codes": True,
                            "has_any_fault_codes": True,
                            "has_any_malfunction_indicator_lamp_codes": True,
                            "has_any_protection_lamp_codes": True,
                            "has_any_red_stop_lamp_codes": True,
                            "has_any_trailer_abs_lamp_codes": True,
                            "specific_fault_codes": [
                                {
                                    "fault_code": "1067",
                                    "type": "INVALID_FAULT_CODE_TYPE",
                                }
                            ],
                        },
                    },
                }
            ],
            external_ids={"foo": "string"},
            operational_settings={
                "time_ranges": [
                    {
                        "days_of_week": ["FRIDAY", "MONDAY"],
                        "end_time": "20:00",
                        "start_time": "11:00",
                        "timezone": "America/Los_Angeles",
                    }
                ],
                "time_range_type": "activeBetween",
            },
        )
        assert_matches_type(ConfigurationCreateResponse, configuration, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.alerts.configurations.with_raw_response.create(
            actions=[{"action_type_id": 1}],
            is_enabled=True,
            name="My Harsh Event Alert",
            scope={"all": False},
            triggers=[{"trigger_type_id": 1000}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(ConfigurationCreateResponse, configuration, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.alerts.configurations.with_streaming_response.create(
            actions=[{"action_type_id": 1}],
            is_enabled=True,
            name="My Harsh Event Alert",
            scope={"all": False},
            triggers=[{"trigger_type_id": 1000}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(ConfigurationCreateResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Samsara) -> None:
        configuration = client.alerts.configurations.update(
            id="e1c5dffc-c7b7-47b0-a778-6a65de638abf",
        )
        assert_matches_type(ConfigurationUpdateResponse, configuration, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Samsara) -> None:
        configuration = client.alerts.configurations.update(
            id="e1c5dffc-c7b7-47b0-a778-6a65de638abf",
            actions=[
                {
                    "action_type_id": 1,
                    "action_params": {
                        "driver_app_notification": {
                            "in_app_notification_options": {
                                "is_enabled": True,
                                "can_dictate_alert_title": False,
                                "can_play_alert_sound": False,
                                "custom_text": "Custom text",
                            },
                            "push_notification_options": {"is_enabled": True},
                        },
                        "recipients": [
                            {
                                "type": "user",
                                "contact_id": "1234",
                                "notification_types": ["push", "sms", "email"],
                                "role_id": "67004a16-be3c-4ef6-a51b-1c45a2c27a92",
                                "user_id": "1234",
                            }
                        ],
                        "webhooks": {
                            "webhook_ids": ["123", "123", "123"],
                            "payload_type": "legacy",
                        },
                    },
                }
            ],
            external_ids={"foo": "string"},
            is_enabled=True,
            name="My Harsh Event Alert",
            operational_settings={
                "time_ranges": [
                    {
                        "days_of_week": ["FRIDAY", "MONDAY"],
                        "end_time": "20:00",
                        "start_time": "11:00",
                        "timezone": "America/Los_Angeles",
                    }
                ],
                "time_range_type": "activeBetween",
            },
            scope={
                "all": False,
                "assets": [
                    {
                        "asset_id": "12443",
                        "asset_type": "uncategorized",
                    }
                ],
                "drivers": [{"driver_id": "12434"}],
                "tags": [
                    {
                        "id": "3914",
                        "name": "East Coast",
                        "parent_tag_id": "4815",
                    }
                ],
                "widgets": [{"widget_id": "12434"}],
            },
            triggers=[
                {
                    "trigger_type_id": 1000,
                    "trigger_params": {
                        "ambient_temperature": {
                            "min_duration_milliseconds": 600000,
                            "operation": "GREATER",
                            "temperature_celcius": 60,
                            "cargo_is_full": True,
                            "doors_are_closed": True,
                        },
                        "cell_signal_loss": {"min_duration_milliseconds": 600000},
                        "def_level": {
                            "def_level_percent": 100,
                            "min_duration_milliseconds": 600000,
                            "operation": "GREATER",
                        },
                        "device_movement": {"min_duration_milliseconds": 600000},
                        "document_submitted": {
                            "template_ids": [
                                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            ]
                        },
                        "dvir_submitted_device": {
                            "dvir_min_duration_milliseconds": 600000,
                            "dvir_submission_types": [
                                "SAFE_NO_DEFECTS",
                                "SAFE_WITH_DEFECTS",
                                "UNSAFE",
                                "SAFE_NO_DEFECTS",
                            ],
                        },
                        "engine_idle": {"min_duration_milliseconds": 600000},
                        "engine_off": {"min_duration_milliseconds": 600000},
                        "engine_on": {"min_duration_milliseconds": 600000},
                        "fuel_level": {
                            "fuel_level_percent": 20,
                            "min_duration_milliseconds": 600000,
                            "operation": "LESS",
                        },
                        "gateway_disconnected": {"min_duration_milliseconds": 3600000},
                        "gateway_unplugged": {"min_duration_milliseconds": 600000},
                        "geofence_entry": {
                            "location": {
                                "address_ids": [
                                    "Ipsam doloremque.",
                                    "Quisquam rerum dolorum et unde.",
                                    "In culpa voluptas ab.",
                                    "Repellendus vel fugit iure.",
                                ],
                                "address_types": ["alertsOnly", "industrialSite"],
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
                                        }
                                    ],
                                },
                                "tag_ids": ["4815", "4815", "4815"],
                            }
                        },
                        "geofence_exit": {
                            "location": {
                                "address_ids": [
                                    "Ipsam doloremque.",
                                    "Quisquam rerum dolorum et unde.",
                                    "In culpa voluptas ab.",
                                    "Repellendus vel fugit iure.",
                                ],
                                "address_types": ["alertsOnly", "industrialSite"],
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
                                        }
                                    ],
                                },
                                "tag_ids": ["4815", "4815", "4815"],
                            }
                        },
                        "gps_signal_loss": {"min_duration_milliseconds": 600000},
                        "harsh_event": {"types": ["haAccel", "haBraking", "haCameraMisaligned", "haCrash"]},
                        "hos_violation": {
                            "max_until_violation_milliseconds": 600000,
                            "violation": "CaliforniaMealbreakMissed",
                        },
                        "inside_geofence": {
                            "location": {
                                "address_ids": [
                                    "Ipsam doloremque.",
                                    "Quisquam rerum dolorum et unde.",
                                    "In culpa voluptas ab.",
                                    "Repellendus vel fugit iure.",
                                ],
                                "address_types": ["alertsOnly", "industrialSite"],
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
                                        }
                                    ],
                                },
                                "tag_ids": ["4815", "4815", "4815"],
                            },
                            "min_duration_milliseconds": 600000,
                        },
                        "out_of_route": {
                            "max_off_route_meters": 100,
                            "min_duration_milliseconds": 600000,
                        },
                        "outside_geofence": {
                            "location": {
                                "address_ids": [
                                    "Ipsam doloremque.",
                                    "Quisquam rerum dolorum et unde.",
                                    "In culpa voluptas ab.",
                                    "Repellendus vel fugit iure.",
                                ],
                                "address_types": ["alertsOnly", "industrialSite"],
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
                                        }
                                    ],
                                },
                                "tag_ids": ["4815", "4815", "4815"],
                            },
                            "min_duration_milliseconds": 600000,
                        },
                        "panic_button": {"is_filtering_out_power_loss": True},
                        "route_stop_estimated_arrival": {
                            "alert_before_arrival_milliseconds": 300000,
                            "location": {
                                "address_ids": [
                                    "Ipsam doloremque.",
                                    "Quisquam rerum dolorum et unde.",
                                    "In culpa voluptas ab.",
                                    "Repellendus vel fugit iure.",
                                ],
                                "address_types": ["alertsOnly", "industrialSite"],
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
                                        }
                                    ],
                                },
                                "tag_ids": ["4815", "4815", "4815"],
                            },
                            "has_live_share_link": True,
                            "is_alert_on_route_stop_only": True,
                        },
                        "scheduled_maintenance": {
                            "due_in_days": 10,
                            "schedule_id": "123",
                        },
                        "scheduled_maintenance_by_engine_hours": {
                            "due_in_hours": 5000,
                            "schedule_id": "123",
                        },
                        "scheduled_maintenance_odometer": {
                            "due_in_meters": 5000,
                            "schedule_id": "123",
                        },
                        "speed": {
                            "min_duration_milliseconds": 600000,
                            "operation": "GREATER",
                            "speed_kilometers_per_hour": 120,
                        },
                        "tire_fault_code": {
                            "manufacturer": "MANUFACTURER_BENDIX",
                            "has_cautionary_tire_fault_codes": True,
                            "has_critical_tire_fault_codes": True,
                            "specific_tire_fault_codes": [
                                "TIRE_ALERT_ACROSS_AXLE_FAULT",
                                "TIRE_ALERT_EXTREME_OVER_PRESSURE",
                                "TIRE_ALERT_EXTREME_UNDER_PRESSURE",
                                "TIRE_ALERT_INVALID",
                            ],
                        },
                        "unassigned_driving": {"min_duration_milliseconds": 600000},
                        "vehicle_battery_voltage": {
                            "battery_volts": 100,
                            "min_duration_milliseconds": 600000,
                            "operation": "GREATER",
                        },
                        "vehicle_fault_code": {
                            "has_any_amber_warning_lamp_codes": True,
                            "has_any_fault_codes": True,
                            "has_any_malfunction_indicator_lamp_codes": True,
                            "has_any_protection_lamp_codes": True,
                            "has_any_red_stop_lamp_codes": True,
                            "has_any_trailer_abs_lamp_codes": True,
                            "specific_fault_codes": [
                                {
                                    "fault_code": "1067",
                                    "type": "INVALID_FAULT_CODE_TYPE",
                                }
                            ],
                        },
                    },
                }
            ],
        )
        assert_matches_type(ConfigurationUpdateResponse, configuration, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Samsara) -> None:
        response = client.alerts.configurations.with_raw_response.update(
            id="e1c5dffc-c7b7-47b0-a778-6a65de638abf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(ConfigurationUpdateResponse, configuration, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Samsara) -> None:
        with client.alerts.configurations.with_streaming_response.update(
            id="e1c5dffc-c7b7-47b0-a778-6a65de638abf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(ConfigurationUpdateResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        configuration = client.alerts.configurations.list()
        assert_matches_type(ConfigurationListResponse, configuration, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        configuration = client.alerts.configurations.list(
            after="after",
            ids=["string"],
            include_external_ids=True,
            status="all",
        )
        assert_matches_type(ConfigurationListResponse, configuration, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.alerts.configurations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(ConfigurationListResponse, configuration, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.alerts.configurations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(ConfigurationListResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Samsara) -> None:
        configuration = client.alerts.configurations.delete(
            id="id",
        )
        assert configuration is None

    @parametrize
    def test_raw_response_delete(self, client: Samsara) -> None:
        response = client.alerts.configurations.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert configuration is None

    @parametrize
    def test_streaming_response_delete(self, client: Samsara) -> None:
        with client.alerts.configurations.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert configuration is None

        assert cast(Any, response.is_closed) is True


class TestAsyncConfigurations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        configuration = await async_client.alerts.configurations.create(
            actions=[{"action_type_id": 1}],
            is_enabled=True,
            name="My Harsh Event Alert",
            scope={"all": False},
            triggers=[{"trigger_type_id": 1000}],
        )
        assert_matches_type(ConfigurationCreateResponse, configuration, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSamsara) -> None:
        configuration = await async_client.alerts.configurations.create(
            actions=[
                {
                    "action_type_id": 1,
                    "action_params": {
                        "driver_app_notification": {
                            "in_app_notification_options": {
                                "is_enabled": True,
                                "can_dictate_alert_title": False,
                                "can_play_alert_sound": False,
                                "custom_text": "Custom text",
                            },
                            "push_notification_options": {"is_enabled": True},
                        },
                        "recipients": [
                            {
                                "type": "user",
                                "contact_id": "1234",
                                "notification_types": ["push", "sms", "email"],
                                "role_id": "67004a16-be3c-4ef6-a51b-1c45a2c27a92",
                                "user_id": "1234",
                            }
                        ],
                        "webhooks": {
                            "webhook_ids": ["123", "123", "123"],
                            "payload_type": "legacy",
                        },
                    },
                }
            ],
            is_enabled=True,
            name="My Harsh Event Alert",
            scope={
                "all": False,
                "assets": [
                    {
                        "asset_id": "12443",
                        "asset_type": "uncategorized",
                    }
                ],
                "drivers": [{"driver_id": "12434"}],
                "tags": [
                    {
                        "id": "3914",
                        "name": "East Coast",
                        "parent_tag_id": "4815",
                    }
                ],
                "widgets": [{"widget_id": "12434"}],
            },
            triggers=[
                {
                    "trigger_type_id": 1000,
                    "trigger_params": {
                        "ambient_temperature": {
                            "min_duration_milliseconds": 600000,
                            "operation": "GREATER",
                            "temperature_celcius": 60,
                            "cargo_is_full": True,
                            "doors_are_closed": True,
                        },
                        "cell_signal_loss": {"min_duration_milliseconds": 600000},
                        "def_level": {
                            "def_level_percent": 100,
                            "min_duration_milliseconds": 600000,
                            "operation": "GREATER",
                        },
                        "device_movement": {"min_duration_milliseconds": 600000},
                        "document_submitted": {
                            "template_ids": [
                                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            ]
                        },
                        "dvir_submitted_device": {
                            "dvir_min_duration_milliseconds": 600000,
                            "dvir_submission_types": [
                                "SAFE_NO_DEFECTS",
                                "SAFE_WITH_DEFECTS",
                                "UNSAFE",
                                "SAFE_NO_DEFECTS",
                            ],
                        },
                        "engine_idle": {"min_duration_milliseconds": 600000},
                        "engine_off": {"min_duration_milliseconds": 600000},
                        "engine_on": {"min_duration_milliseconds": 600000},
                        "fuel_level": {
                            "fuel_level_percent": 20,
                            "min_duration_milliseconds": 600000,
                            "operation": "LESS",
                        },
                        "gateway_disconnected": {"min_duration_milliseconds": 3600000},
                        "gateway_unplugged": {"min_duration_milliseconds": 600000},
                        "geofence_entry": {
                            "location": {
                                "address_ids": [
                                    "Ipsam doloremque.",
                                    "Quisquam rerum dolorum et unde.",
                                    "In culpa voluptas ab.",
                                    "Repellendus vel fugit iure.",
                                ],
                                "address_types": ["alertsOnly", "industrialSite"],
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
                                        }
                                    ],
                                },
                                "tag_ids": ["4815", "4815", "4815"],
                            }
                        },
                        "geofence_exit": {
                            "location": {
                                "address_ids": [
                                    "Ipsam doloremque.",
                                    "Quisquam rerum dolorum et unde.",
                                    "In culpa voluptas ab.",
                                    "Repellendus vel fugit iure.",
                                ],
                                "address_types": ["alertsOnly", "industrialSite"],
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
                                        }
                                    ],
                                },
                                "tag_ids": ["4815", "4815", "4815"],
                            }
                        },
                        "gps_signal_loss": {"min_duration_milliseconds": 600000},
                        "harsh_event": {"types": ["haAccel", "haBraking", "haCameraMisaligned", "haCrash"]},
                        "hos_violation": {
                            "max_until_violation_milliseconds": 600000,
                            "violation": "CaliforniaMealbreakMissed",
                        },
                        "inside_geofence": {
                            "location": {
                                "address_ids": [
                                    "Ipsam doloremque.",
                                    "Quisquam rerum dolorum et unde.",
                                    "In culpa voluptas ab.",
                                    "Repellendus vel fugit iure.",
                                ],
                                "address_types": ["alertsOnly", "industrialSite"],
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
                                        }
                                    ],
                                },
                                "tag_ids": ["4815", "4815", "4815"],
                            },
                            "min_duration_milliseconds": 600000,
                        },
                        "out_of_route": {
                            "max_off_route_meters": 100,
                            "min_duration_milliseconds": 600000,
                        },
                        "outside_geofence": {
                            "location": {
                                "address_ids": [
                                    "Ipsam doloremque.",
                                    "Quisquam rerum dolorum et unde.",
                                    "In culpa voluptas ab.",
                                    "Repellendus vel fugit iure.",
                                ],
                                "address_types": ["alertsOnly", "industrialSite"],
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
                                        }
                                    ],
                                },
                                "tag_ids": ["4815", "4815", "4815"],
                            },
                            "min_duration_milliseconds": 600000,
                        },
                        "panic_button": {"is_filtering_out_power_loss": True},
                        "route_stop_estimated_arrival": {
                            "alert_before_arrival_milliseconds": 300000,
                            "location": {
                                "address_ids": [
                                    "Ipsam doloremque.",
                                    "Quisquam rerum dolorum et unde.",
                                    "In culpa voluptas ab.",
                                    "Repellendus vel fugit iure.",
                                ],
                                "address_types": ["alertsOnly", "industrialSite"],
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
                                        }
                                    ],
                                },
                                "tag_ids": ["4815", "4815", "4815"],
                            },
                            "has_live_share_link": True,
                            "is_alert_on_route_stop_only": True,
                        },
                        "scheduled_maintenance": {
                            "due_in_days": 10,
                            "schedule_id": "123",
                        },
                        "scheduled_maintenance_by_engine_hours": {
                            "due_in_hours": 5000,
                            "schedule_id": "123",
                        },
                        "scheduled_maintenance_odometer": {
                            "due_in_meters": 5000,
                            "schedule_id": "123",
                        },
                        "speed": {
                            "min_duration_milliseconds": 600000,
                            "operation": "GREATER",
                            "speed_kilometers_per_hour": 120,
                        },
                        "tire_fault_code": {
                            "manufacturer": "MANUFACTURER_BENDIX",
                            "has_cautionary_tire_fault_codes": True,
                            "has_critical_tire_fault_codes": True,
                            "specific_tire_fault_codes": [
                                "TIRE_ALERT_ACROSS_AXLE_FAULT",
                                "TIRE_ALERT_EXTREME_OVER_PRESSURE",
                                "TIRE_ALERT_EXTREME_UNDER_PRESSURE",
                                "TIRE_ALERT_INVALID",
                            ],
                        },
                        "unassigned_driving": {"min_duration_milliseconds": 600000},
                        "vehicle_battery_voltage": {
                            "battery_volts": 100,
                            "min_duration_milliseconds": 600000,
                            "operation": "GREATER",
                        },
                        "vehicle_fault_code": {
                            "has_any_amber_warning_lamp_codes": True,
                            "has_any_fault_codes": True,
                            "has_any_malfunction_indicator_lamp_codes": True,
                            "has_any_protection_lamp_codes": True,
                            "has_any_red_stop_lamp_codes": True,
                            "has_any_trailer_abs_lamp_codes": True,
                            "specific_fault_codes": [
                                {
                                    "fault_code": "1067",
                                    "type": "INVALID_FAULT_CODE_TYPE",
                                }
                            ],
                        },
                    },
                }
            ],
            external_ids={"foo": "string"},
            operational_settings={
                "time_ranges": [
                    {
                        "days_of_week": ["FRIDAY", "MONDAY"],
                        "end_time": "20:00",
                        "start_time": "11:00",
                        "timezone": "America/Los_Angeles",
                    }
                ],
                "time_range_type": "activeBetween",
            },
        )
        assert_matches_type(ConfigurationCreateResponse, configuration, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.alerts.configurations.with_raw_response.create(
            actions=[{"action_type_id": 1}],
            is_enabled=True,
            name="My Harsh Event Alert",
            scope={"all": False},
            triggers=[{"trigger_type_id": 1000}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(ConfigurationCreateResponse, configuration, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.alerts.configurations.with_streaming_response.create(
            actions=[{"action_type_id": 1}],
            is_enabled=True,
            name="My Harsh Event Alert",
            scope={"all": False},
            triggers=[{"trigger_type_id": 1000}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(ConfigurationCreateResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncSamsara) -> None:
        configuration = await async_client.alerts.configurations.update(
            id="e1c5dffc-c7b7-47b0-a778-6a65de638abf",
        )
        assert_matches_type(ConfigurationUpdateResponse, configuration, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSamsara) -> None:
        configuration = await async_client.alerts.configurations.update(
            id="e1c5dffc-c7b7-47b0-a778-6a65de638abf",
            actions=[
                {
                    "action_type_id": 1,
                    "action_params": {
                        "driver_app_notification": {
                            "in_app_notification_options": {
                                "is_enabled": True,
                                "can_dictate_alert_title": False,
                                "can_play_alert_sound": False,
                                "custom_text": "Custom text",
                            },
                            "push_notification_options": {"is_enabled": True},
                        },
                        "recipients": [
                            {
                                "type": "user",
                                "contact_id": "1234",
                                "notification_types": ["push", "sms", "email"],
                                "role_id": "67004a16-be3c-4ef6-a51b-1c45a2c27a92",
                                "user_id": "1234",
                            }
                        ],
                        "webhooks": {
                            "webhook_ids": ["123", "123", "123"],
                            "payload_type": "legacy",
                        },
                    },
                }
            ],
            external_ids={"foo": "string"},
            is_enabled=True,
            name="My Harsh Event Alert",
            operational_settings={
                "time_ranges": [
                    {
                        "days_of_week": ["FRIDAY", "MONDAY"],
                        "end_time": "20:00",
                        "start_time": "11:00",
                        "timezone": "America/Los_Angeles",
                    }
                ],
                "time_range_type": "activeBetween",
            },
            scope={
                "all": False,
                "assets": [
                    {
                        "asset_id": "12443",
                        "asset_type": "uncategorized",
                    }
                ],
                "drivers": [{"driver_id": "12434"}],
                "tags": [
                    {
                        "id": "3914",
                        "name": "East Coast",
                        "parent_tag_id": "4815",
                    }
                ],
                "widgets": [{"widget_id": "12434"}],
            },
            triggers=[
                {
                    "trigger_type_id": 1000,
                    "trigger_params": {
                        "ambient_temperature": {
                            "min_duration_milliseconds": 600000,
                            "operation": "GREATER",
                            "temperature_celcius": 60,
                            "cargo_is_full": True,
                            "doors_are_closed": True,
                        },
                        "cell_signal_loss": {"min_duration_milliseconds": 600000},
                        "def_level": {
                            "def_level_percent": 100,
                            "min_duration_milliseconds": 600000,
                            "operation": "GREATER",
                        },
                        "device_movement": {"min_duration_milliseconds": 600000},
                        "document_submitted": {
                            "template_ids": [
                                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            ]
                        },
                        "dvir_submitted_device": {
                            "dvir_min_duration_milliseconds": 600000,
                            "dvir_submission_types": [
                                "SAFE_NO_DEFECTS",
                                "SAFE_WITH_DEFECTS",
                                "UNSAFE",
                                "SAFE_NO_DEFECTS",
                            ],
                        },
                        "engine_idle": {"min_duration_milliseconds": 600000},
                        "engine_off": {"min_duration_milliseconds": 600000},
                        "engine_on": {"min_duration_milliseconds": 600000},
                        "fuel_level": {
                            "fuel_level_percent": 20,
                            "min_duration_milliseconds": 600000,
                            "operation": "LESS",
                        },
                        "gateway_disconnected": {"min_duration_milliseconds": 3600000},
                        "gateway_unplugged": {"min_duration_milliseconds": 600000},
                        "geofence_entry": {
                            "location": {
                                "address_ids": [
                                    "Ipsam doloremque.",
                                    "Quisquam rerum dolorum et unde.",
                                    "In culpa voluptas ab.",
                                    "Repellendus vel fugit iure.",
                                ],
                                "address_types": ["alertsOnly", "industrialSite"],
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
                                        }
                                    ],
                                },
                                "tag_ids": ["4815", "4815", "4815"],
                            }
                        },
                        "geofence_exit": {
                            "location": {
                                "address_ids": [
                                    "Ipsam doloremque.",
                                    "Quisquam rerum dolorum et unde.",
                                    "In culpa voluptas ab.",
                                    "Repellendus vel fugit iure.",
                                ],
                                "address_types": ["alertsOnly", "industrialSite"],
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
                                        }
                                    ],
                                },
                                "tag_ids": ["4815", "4815", "4815"],
                            }
                        },
                        "gps_signal_loss": {"min_duration_milliseconds": 600000},
                        "harsh_event": {"types": ["haAccel", "haBraking", "haCameraMisaligned", "haCrash"]},
                        "hos_violation": {
                            "max_until_violation_milliseconds": 600000,
                            "violation": "CaliforniaMealbreakMissed",
                        },
                        "inside_geofence": {
                            "location": {
                                "address_ids": [
                                    "Ipsam doloremque.",
                                    "Quisquam rerum dolorum et unde.",
                                    "In culpa voluptas ab.",
                                    "Repellendus vel fugit iure.",
                                ],
                                "address_types": ["alertsOnly", "industrialSite"],
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
                                        }
                                    ],
                                },
                                "tag_ids": ["4815", "4815", "4815"],
                            },
                            "min_duration_milliseconds": 600000,
                        },
                        "out_of_route": {
                            "max_off_route_meters": 100,
                            "min_duration_milliseconds": 600000,
                        },
                        "outside_geofence": {
                            "location": {
                                "address_ids": [
                                    "Ipsam doloremque.",
                                    "Quisquam rerum dolorum et unde.",
                                    "In culpa voluptas ab.",
                                    "Repellendus vel fugit iure.",
                                ],
                                "address_types": ["alertsOnly", "industrialSite"],
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
                                        }
                                    ],
                                },
                                "tag_ids": ["4815", "4815", "4815"],
                            },
                            "min_duration_milliseconds": 600000,
                        },
                        "panic_button": {"is_filtering_out_power_loss": True},
                        "route_stop_estimated_arrival": {
                            "alert_before_arrival_milliseconds": 300000,
                            "location": {
                                "address_ids": [
                                    "Ipsam doloremque.",
                                    "Quisquam rerum dolorum et unde.",
                                    "In culpa voluptas ab.",
                                    "Repellendus vel fugit iure.",
                                ],
                                "address_types": ["alertsOnly", "industrialSite"],
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
                                        }
                                    ],
                                },
                                "tag_ids": ["4815", "4815", "4815"],
                            },
                            "has_live_share_link": True,
                            "is_alert_on_route_stop_only": True,
                        },
                        "scheduled_maintenance": {
                            "due_in_days": 10,
                            "schedule_id": "123",
                        },
                        "scheduled_maintenance_by_engine_hours": {
                            "due_in_hours": 5000,
                            "schedule_id": "123",
                        },
                        "scheduled_maintenance_odometer": {
                            "due_in_meters": 5000,
                            "schedule_id": "123",
                        },
                        "speed": {
                            "min_duration_milliseconds": 600000,
                            "operation": "GREATER",
                            "speed_kilometers_per_hour": 120,
                        },
                        "tire_fault_code": {
                            "manufacturer": "MANUFACTURER_BENDIX",
                            "has_cautionary_tire_fault_codes": True,
                            "has_critical_tire_fault_codes": True,
                            "specific_tire_fault_codes": [
                                "TIRE_ALERT_ACROSS_AXLE_FAULT",
                                "TIRE_ALERT_EXTREME_OVER_PRESSURE",
                                "TIRE_ALERT_EXTREME_UNDER_PRESSURE",
                                "TIRE_ALERT_INVALID",
                            ],
                        },
                        "unassigned_driving": {"min_duration_milliseconds": 600000},
                        "vehicle_battery_voltage": {
                            "battery_volts": 100,
                            "min_duration_milliseconds": 600000,
                            "operation": "GREATER",
                        },
                        "vehicle_fault_code": {
                            "has_any_amber_warning_lamp_codes": True,
                            "has_any_fault_codes": True,
                            "has_any_malfunction_indicator_lamp_codes": True,
                            "has_any_protection_lamp_codes": True,
                            "has_any_red_stop_lamp_codes": True,
                            "has_any_trailer_abs_lamp_codes": True,
                            "specific_fault_codes": [
                                {
                                    "fault_code": "1067",
                                    "type": "INVALID_FAULT_CODE_TYPE",
                                }
                            ],
                        },
                    },
                }
            ],
        )
        assert_matches_type(ConfigurationUpdateResponse, configuration, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSamsara) -> None:
        response = await async_client.alerts.configurations.with_raw_response.update(
            id="e1c5dffc-c7b7-47b0-a778-6a65de638abf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(ConfigurationUpdateResponse, configuration, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSamsara) -> None:
        async with async_client.alerts.configurations.with_streaming_response.update(
            id="e1c5dffc-c7b7-47b0-a778-6a65de638abf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(ConfigurationUpdateResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        configuration = await async_client.alerts.configurations.list()
        assert_matches_type(ConfigurationListResponse, configuration, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        configuration = await async_client.alerts.configurations.list(
            after="after",
            ids=["string"],
            include_external_ids=True,
            status="all",
        )
        assert_matches_type(ConfigurationListResponse, configuration, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.alerts.configurations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(ConfigurationListResponse, configuration, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.alerts.configurations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(ConfigurationListResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSamsara) -> None:
        configuration = await async_client.alerts.configurations.delete(
            id="id",
        )
        assert configuration is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSamsara) -> None:
        response = await async_client.alerts.configurations.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert configuration is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSamsara) -> None:
        async with async_client.alerts.configurations.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert configuration is None

        assert cast(Any, response.is_closed) is True
