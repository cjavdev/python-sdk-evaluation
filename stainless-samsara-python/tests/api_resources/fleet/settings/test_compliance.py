# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet.settings import (
    SettingsGetComplianceSettingsResponseBody,
    SettingsPatchComplianceSettingsResponseBody,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompliance:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Samsara) -> None:
        compliance = client.fleet.settings.compliance.retrieve()
        assert_matches_type(SettingsGetComplianceSettingsResponseBody, compliance, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Samsara) -> None:
        response = client.fleet.settings.compliance.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compliance = response.parse()
        assert_matches_type(SettingsGetComplianceSettingsResponseBody, compliance, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Samsara) -> None:
        with client.fleet.settings.compliance.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compliance = response.parse()
            assert_matches_type(SettingsGetComplianceSettingsResponseBody, compliance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Samsara) -> None:
        compliance = client.fleet.settings.compliance.update()
        assert_matches_type(SettingsPatchComplianceSettingsResponseBody, compliance, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Samsara) -> None:
        compliance = client.fleet.settings.compliance.update(
            allow_unregulated_vehicles_enabled=False,
            canada_hos_enabled=True,
            carrier_name="ABC Trucking",
            dot_number=12345678,
            driver_auto_duty_enabled=True,
            edit_certified_logs_enabled=False,
            force_manual_location_for_duty_status_changes_enabled=False,
            force_review_unassigned_hos_enabled=False,
            main_office_formatted_address="123 Main Street",
            persistent_duty_status_enabled=True,
        )
        assert_matches_type(SettingsPatchComplianceSettingsResponseBody, compliance, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Samsara) -> None:
        response = client.fleet.settings.compliance.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compliance = response.parse()
        assert_matches_type(SettingsPatchComplianceSettingsResponseBody, compliance, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Samsara) -> None:
        with client.fleet.settings.compliance.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compliance = response.parse()
            assert_matches_type(SettingsPatchComplianceSettingsResponseBody, compliance, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompliance:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSamsara) -> None:
        compliance = await async_client.fleet.settings.compliance.retrieve()
        assert_matches_type(SettingsGetComplianceSettingsResponseBody, compliance, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.settings.compliance.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compliance = await response.parse()
        assert_matches_type(SettingsGetComplianceSettingsResponseBody, compliance, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.settings.compliance.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compliance = await response.parse()
            assert_matches_type(SettingsGetComplianceSettingsResponseBody, compliance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncSamsara) -> None:
        compliance = await async_client.fleet.settings.compliance.update()
        assert_matches_type(SettingsPatchComplianceSettingsResponseBody, compliance, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSamsara) -> None:
        compliance = await async_client.fleet.settings.compliance.update(
            allow_unregulated_vehicles_enabled=False,
            canada_hos_enabled=True,
            carrier_name="ABC Trucking",
            dot_number=12345678,
            driver_auto_duty_enabled=True,
            edit_certified_logs_enabled=False,
            force_manual_location_for_duty_status_changes_enabled=False,
            force_review_unassigned_hos_enabled=False,
            main_office_formatted_address="123 Main Street",
            persistent_duty_status_enabled=True,
        )
        assert_matches_type(SettingsPatchComplianceSettingsResponseBody, compliance, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.settings.compliance.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compliance = await response.parse()
        assert_matches_type(SettingsPatchComplianceSettingsResponseBody, compliance, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.settings.compliance.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compliance = await response.parse()
            assert_matches_type(SettingsPatchComplianceSettingsResponseBody, compliance, path=["response"])

        assert cast(Any, response.is_closed) is True
