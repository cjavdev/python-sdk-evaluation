# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet.settings import (
    SettingsGetDriverAppSettingsResponseBody,
    SettingsPatchDriverAppSettingsResponseBody,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDriverApp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Samsara) -> None:
        driver_app = client.fleet.settings.driver_app.retrieve()
        assert_matches_type(SettingsGetDriverAppSettingsResponseBody, driver_app, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Samsara) -> None:
        response = client.fleet.settings.driver_app.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_app = response.parse()
        assert_matches_type(SettingsGetDriverAppSettingsResponseBody, driver_app, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Samsara) -> None:
        with client.fleet.settings.driver_app.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_app = response.parse()
            assert_matches_type(SettingsGetDriverAppSettingsResponseBody, driver_app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Samsara) -> None:
        driver_app = client.fleet.settings.driver_app.update()
        assert_matches_type(SettingsPatchDriverAppSettingsResponseBody, driver_app, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Samsara) -> None:
        driver_app = client.fleet.settings.driver_app.update(
            driver_fleet_id="abc-trucking-co",
            gamification=False,
            gamification_config={"anonymize_driver_names": True},
            org_vehicle_search=False,
            trailer_selection=False,
            trailer_selection_config={
                "driver_trailer_creation_enabled": True,
                "max_num_of_trailers_selected": 0,
                "org_trailer_search": True,
            },
        )
        assert_matches_type(SettingsPatchDriverAppSettingsResponseBody, driver_app, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Samsara) -> None:
        response = client.fleet.settings.driver_app.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_app = response.parse()
        assert_matches_type(SettingsPatchDriverAppSettingsResponseBody, driver_app, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Samsara) -> None:
        with client.fleet.settings.driver_app.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_app = response.parse()
            assert_matches_type(SettingsPatchDriverAppSettingsResponseBody, driver_app, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDriverApp:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSamsara) -> None:
        driver_app = await async_client.fleet.settings.driver_app.retrieve()
        assert_matches_type(SettingsGetDriverAppSettingsResponseBody, driver_app, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.settings.driver_app.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_app = await response.parse()
        assert_matches_type(SettingsGetDriverAppSettingsResponseBody, driver_app, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.settings.driver_app.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_app = await response.parse()
            assert_matches_type(SettingsGetDriverAppSettingsResponseBody, driver_app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncSamsara) -> None:
        driver_app = await async_client.fleet.settings.driver_app.update()
        assert_matches_type(SettingsPatchDriverAppSettingsResponseBody, driver_app, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSamsara) -> None:
        driver_app = await async_client.fleet.settings.driver_app.update(
            driver_fleet_id="abc-trucking-co",
            gamification=False,
            gamification_config={"anonymize_driver_names": True},
            org_vehicle_search=False,
            trailer_selection=False,
            trailer_selection_config={
                "driver_trailer_creation_enabled": True,
                "max_num_of_trailers_selected": 0,
                "org_trailer_search": True,
            },
        )
        assert_matches_type(SettingsPatchDriverAppSettingsResponseBody, driver_app, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.settings.driver_app.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_app = await response.parse()
        assert_matches_type(SettingsPatchDriverAppSettingsResponseBody, driver_app, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.settings.driver_app.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_app = await response.parse()
            assert_matches_type(SettingsPatchDriverAppSettingsResponseBody, driver_app, path=["response"])

        assert cast(Any, response.is_closed) is True
