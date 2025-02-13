# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet.reports import DriversFuelEnergyListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDriversFuelEnergy:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        drivers_fuel_energy = client.fleet.reports.drivers_fuel_energy.list(
            end_date="endDate",
            start_date="startDate",
        )
        assert_matches_type(DriversFuelEnergyListResponse, drivers_fuel_energy, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        drivers_fuel_energy = client.fleet.reports.drivers_fuel_energy.list(
            end_date="endDate",
            start_date="startDate",
            after="after",
            driver_ids=["string"],
            parent_tag_ids="parentTagIds",
            tag_ids="tagIds",
        )
        assert_matches_type(DriversFuelEnergyListResponse, drivers_fuel_energy, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.fleet.reports.drivers_fuel_energy.with_raw_response.list(
            end_date="endDate",
            start_date="startDate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drivers_fuel_energy = response.parse()
        assert_matches_type(DriversFuelEnergyListResponse, drivers_fuel_energy, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.fleet.reports.drivers_fuel_energy.with_streaming_response.list(
            end_date="endDate",
            start_date="startDate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drivers_fuel_energy = response.parse()
            assert_matches_type(DriversFuelEnergyListResponse, drivers_fuel_energy, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDriversFuelEnergy:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        drivers_fuel_energy = await async_client.fleet.reports.drivers_fuel_energy.list(
            end_date="endDate",
            start_date="startDate",
        )
        assert_matches_type(DriversFuelEnergyListResponse, drivers_fuel_energy, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        drivers_fuel_energy = await async_client.fleet.reports.drivers_fuel_energy.list(
            end_date="endDate",
            start_date="startDate",
            after="after",
            driver_ids=["string"],
            parent_tag_ids="parentTagIds",
            tag_ids="tagIds",
        )
        assert_matches_type(DriversFuelEnergyListResponse, drivers_fuel_energy, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.reports.drivers_fuel_energy.with_raw_response.list(
            end_date="endDate",
            start_date="startDate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drivers_fuel_energy = await response.parse()
        assert_matches_type(DriversFuelEnergyListResponse, drivers_fuel_energy, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.reports.drivers_fuel_energy.with_streaming_response.list(
            end_date="endDate",
            start_date="startDate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drivers_fuel_energy = await response.parse()
            assert_matches_type(DriversFuelEnergyListResponse, drivers_fuel_energy, path=["response"])

        assert cast(Any, response.is_closed) is True
