# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet import (
    Driver,
    DriverListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDrivers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        driver = client.fleet.drivers.create(
            name="Susan Jones",
            password="aSecurePassword1234",
            username="SusanJones",
        )
        assert_matches_type(Driver, driver, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Samsara) -> None:
        driver = client.fleet.drivers.create(
            name="Susan Jones",
            password="aSecurePassword1234",
            username="SusanJones",
            attributes=[
                {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "name": "License Certifications",
                    "number_values": [0],
                    "string_values": ["string"],
                }
            ],
            carrier_settings={
                "carrier_name": "Acme Inc.",
                "dot_number": 98231,
                "home_terminal_address": "1234 Pear St., Scranton, PA 62814",
                "home_terminal_name": "Acme Inc.",
                "main_office_address": "1234 Pear St., Scranton, PA 62814",
            },
            current_id_card_code="941767043",
            eld_adverse_weather_exemption_enabled=True,
            eld_big_day_exemption_enabled=True,
            eld_day_start_hour=0,
            eld_exempt=True,
            eld_exempt_reason="Bad driver",
            eld_pc_enabled=True,
            eld_ym_enabled=True,
            external_ids={
                "maintenanceId": "250020",
                "payrollId": "ABFS18600",
            },
            has_driving_features_hidden=True,
            hos_setting={"heavy_haul_exemption_toggle_enabled": True},
            license_number="E1234567",
            license_state="CA",
            locale="us",
            notes="Also goes by the nickname Furious Fred.",
            peer_group_tag_id="peerGroupTagId",
            phone="5558234327",
            static_assigned_vehicle_id="456",
            tachograph_card_number="1000000492436002",
            tag_ids=["147"],
            timezone="America/Los_Angeles",
            us_driver_ruleset_override={
                "cycle": "USA Property (8/70)",
                "restart": "34-hour Restart",
                "restbreak": "Property (off-duty/sleeper)",
                "us_state_to_override": "",
            },
            vehicle_group_tag_id="342417",
            waiting_time_duty_status_enabled=True,
        )
        assert_matches_type(Driver, driver, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.fleet.drivers.with_raw_response.create(
            name="Susan Jones",
            password="aSecurePassword1234",
            username="SusanJones",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver = response.parse()
        assert_matches_type(Driver, driver, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.fleet.drivers.with_streaming_response.create(
            name="Susan Jones",
            password="aSecurePassword1234",
            username="SusanJones",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver = response.parse()
            assert_matches_type(Driver, driver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Samsara) -> None:
        driver = client.fleet.drivers.retrieve(
            "id",
        )
        assert_matches_type(Driver, driver, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Samsara) -> None:
        response = client.fleet.drivers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver = response.parse()
        assert_matches_type(Driver, driver, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Samsara) -> None:
        with client.fleet.drivers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver = response.parse()
            assert_matches_type(Driver, driver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.fleet.drivers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Samsara) -> None:
        driver = client.fleet.drivers.update(
            id="id",
        )
        assert_matches_type(Driver, driver, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Samsara) -> None:
        driver = client.fleet.drivers.update(
            id="id",
            attributes=[
                {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "name": "License Certifications",
                    "number_values": [0],
                    "string_values": ["string"],
                }
            ],
            carrier_settings={
                "carrier_name": "Acme Inc.",
                "dot_number": 98231,
                "home_terminal_address": "1234 Pear St., Scranton, PA 62814",
                "home_terminal_name": "Acme Inc.",
                "main_office_address": "1234 Pear St., Scranton, PA 62814",
            },
            current_id_card_code="941767043",
            deactivated_at_time="2019-05-18T20:27:35Z",
            driver_activation_status="active",
            eld_adverse_weather_exemption_enabled=True,
            eld_big_day_exemption_enabled=True,
            eld_day_start_hour=0,
            eld_exempt=True,
            eld_exempt_reason="Bad driver",
            eld_pc_enabled=True,
            eld_ym_enabled=True,
            external_ids={
                "maintenanceId": "250020",
                "payrollId": "ABFS18600",
            },
            has_driving_features_hidden=True,
            hos_setting={"heavy_haul_exemption_toggle_enabled": True},
            license_number="E1234567",
            license_state="CA",
            locale="us",
            name="Susan Jones",
            notes="Also goes by the nickname Furious Fred.",
            password="aSecurePassword1234",
            peer_group_tag_id="peerGroupTagId",
            phone="5558234327",
            static_assigned_vehicle_id="456",
            tachograph_card_number="1000000492436002",
            tag_ids=["147"],
            timezone="America/Los_Angeles",
            us_driver_ruleset_override={
                "cycle": "USA Property (8/70)",
                "restart": "34-hour Restart",
                "restbreak": "Property (off-duty/sleeper)",
                "us_state_to_override": "",
            },
            username="SusanJones",
            vehicle_group_tag_id="342417",
            waiting_time_duty_status_enabled=True,
        )
        assert_matches_type(Driver, driver, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Samsara) -> None:
        response = client.fleet.drivers.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver = response.parse()
        assert_matches_type(Driver, driver, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Samsara) -> None:
        with client.fleet.drivers.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver = response.parse()
            assert_matches_type(Driver, driver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.fleet.drivers.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        driver = client.fleet.drivers.list()
        assert_matches_type(DriverListResponse, driver, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        driver = client.fleet.drivers.list(
            after="after",
            attribute_value_ids=["string"],
            created_after_time="createdAfterTime",
            driver_activation_status="active",
            limit=1,
            parent_tag_ids=["string"],
            tag_ids=["string"],
            updated_after_time="updatedAfterTime",
        )
        assert_matches_type(DriverListResponse, driver, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.fleet.drivers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver = response.parse()
        assert_matches_type(DriverListResponse, driver, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.fleet.drivers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver = response.parse()
            assert_matches_type(DriverListResponse, driver, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDrivers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        driver = await async_client.fleet.drivers.create(
            name="Susan Jones",
            password="aSecurePassword1234",
            username="SusanJones",
        )
        assert_matches_type(Driver, driver, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSamsara) -> None:
        driver = await async_client.fleet.drivers.create(
            name="Susan Jones",
            password="aSecurePassword1234",
            username="SusanJones",
            attributes=[
                {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "name": "License Certifications",
                    "number_values": [0],
                    "string_values": ["string"],
                }
            ],
            carrier_settings={
                "carrier_name": "Acme Inc.",
                "dot_number": 98231,
                "home_terminal_address": "1234 Pear St., Scranton, PA 62814",
                "home_terminal_name": "Acme Inc.",
                "main_office_address": "1234 Pear St., Scranton, PA 62814",
            },
            current_id_card_code="941767043",
            eld_adverse_weather_exemption_enabled=True,
            eld_big_day_exemption_enabled=True,
            eld_day_start_hour=0,
            eld_exempt=True,
            eld_exempt_reason="Bad driver",
            eld_pc_enabled=True,
            eld_ym_enabled=True,
            external_ids={
                "maintenanceId": "250020",
                "payrollId": "ABFS18600",
            },
            has_driving_features_hidden=True,
            hos_setting={"heavy_haul_exemption_toggle_enabled": True},
            license_number="E1234567",
            license_state="CA",
            locale="us",
            notes="Also goes by the nickname Furious Fred.",
            peer_group_tag_id="peerGroupTagId",
            phone="5558234327",
            static_assigned_vehicle_id="456",
            tachograph_card_number="1000000492436002",
            tag_ids=["147"],
            timezone="America/Los_Angeles",
            us_driver_ruleset_override={
                "cycle": "USA Property (8/70)",
                "restart": "34-hour Restart",
                "restbreak": "Property (off-duty/sleeper)",
                "us_state_to_override": "",
            },
            vehicle_group_tag_id="342417",
            waiting_time_duty_status_enabled=True,
        )
        assert_matches_type(Driver, driver, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.drivers.with_raw_response.create(
            name="Susan Jones",
            password="aSecurePassword1234",
            username="SusanJones",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver = await response.parse()
        assert_matches_type(Driver, driver, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.drivers.with_streaming_response.create(
            name="Susan Jones",
            password="aSecurePassword1234",
            username="SusanJones",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver = await response.parse()
            assert_matches_type(Driver, driver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSamsara) -> None:
        driver = await async_client.fleet.drivers.retrieve(
            "id",
        )
        assert_matches_type(Driver, driver, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.drivers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver = await response.parse()
        assert_matches_type(Driver, driver, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.drivers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver = await response.parse()
            assert_matches_type(Driver, driver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.fleet.drivers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSamsara) -> None:
        driver = await async_client.fleet.drivers.update(
            id="id",
        )
        assert_matches_type(Driver, driver, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSamsara) -> None:
        driver = await async_client.fleet.drivers.update(
            id="id",
            attributes=[
                {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "name": "License Certifications",
                    "number_values": [0],
                    "string_values": ["string"],
                }
            ],
            carrier_settings={
                "carrier_name": "Acme Inc.",
                "dot_number": 98231,
                "home_terminal_address": "1234 Pear St., Scranton, PA 62814",
                "home_terminal_name": "Acme Inc.",
                "main_office_address": "1234 Pear St., Scranton, PA 62814",
            },
            current_id_card_code="941767043",
            deactivated_at_time="2019-05-18T20:27:35Z",
            driver_activation_status="active",
            eld_adverse_weather_exemption_enabled=True,
            eld_big_day_exemption_enabled=True,
            eld_day_start_hour=0,
            eld_exempt=True,
            eld_exempt_reason="Bad driver",
            eld_pc_enabled=True,
            eld_ym_enabled=True,
            external_ids={
                "maintenanceId": "250020",
                "payrollId": "ABFS18600",
            },
            has_driving_features_hidden=True,
            hos_setting={"heavy_haul_exemption_toggle_enabled": True},
            license_number="E1234567",
            license_state="CA",
            locale="us",
            name="Susan Jones",
            notes="Also goes by the nickname Furious Fred.",
            password="aSecurePassword1234",
            peer_group_tag_id="peerGroupTagId",
            phone="5558234327",
            static_assigned_vehicle_id="456",
            tachograph_card_number="1000000492436002",
            tag_ids=["147"],
            timezone="America/Los_Angeles",
            us_driver_ruleset_override={
                "cycle": "USA Property (8/70)",
                "restart": "34-hour Restart",
                "restbreak": "Property (off-duty/sleeper)",
                "us_state_to_override": "",
            },
            username="SusanJones",
            vehicle_group_tag_id="342417",
            waiting_time_duty_status_enabled=True,
        )
        assert_matches_type(Driver, driver, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.drivers.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver = await response.parse()
        assert_matches_type(Driver, driver, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.drivers.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver = await response.parse()
            assert_matches_type(Driver, driver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.fleet.drivers.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        driver = await async_client.fleet.drivers.list()
        assert_matches_type(DriverListResponse, driver, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        driver = await async_client.fleet.drivers.list(
            after="after",
            attribute_value_ids=["string"],
            created_after_time="createdAfterTime",
            driver_activation_status="active",
            limit=1,
            parent_tag_ids=["string"],
            tag_ids=["string"],
            updated_after_time="updatedAfterTime",
        )
        assert_matches_type(DriverListResponse, driver, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.drivers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver = await response.parse()
        assert_matches_type(DriverListResponse, driver, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.drivers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver = await response.parse()
            assert_matches_type(DriverListResponse, driver, path=["response"])

        assert cast(Any, response.is_closed) is True
