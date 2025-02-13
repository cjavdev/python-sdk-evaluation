# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara._utils import parse_datetime
from samsara.types.beta.fleet import DriverEfficiencyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDrivers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_efficiency(self, client: Samsara) -> None:
        driver = client.beta.fleet.drivers.efficiency()
        assert_matches_type(DriverEfficiencyResponse, driver, path=["response"])

    @parametrize
    def test_method_efficiency_with_all_params(self, client: Samsara) -> None:
        driver = client.beta.fleet.drivers.efficiency(
            after="after",
            driver_activation_status="active",
            driver_ids=["string"],
            driver_parent_tag_ids=["string"],
            driver_tag_ids=["string"],
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DriverEfficiencyResponse, driver, path=["response"])

    @parametrize
    def test_raw_response_efficiency(self, client: Samsara) -> None:
        response = client.beta.fleet.drivers.with_raw_response.efficiency()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver = response.parse()
        assert_matches_type(DriverEfficiencyResponse, driver, path=["response"])

    @parametrize
    def test_streaming_response_efficiency(self, client: Samsara) -> None:
        with client.beta.fleet.drivers.with_streaming_response.efficiency() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver = response.parse()
            assert_matches_type(DriverEfficiencyResponse, driver, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDrivers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_efficiency(self, async_client: AsyncSamsara) -> None:
        driver = await async_client.beta.fleet.drivers.efficiency()
        assert_matches_type(DriverEfficiencyResponse, driver, path=["response"])

    @parametrize
    async def test_method_efficiency_with_all_params(self, async_client: AsyncSamsara) -> None:
        driver = await async_client.beta.fleet.drivers.efficiency(
            after="after",
            driver_activation_status="active",
            driver_ids=["string"],
            driver_parent_tag_ids=["string"],
            driver_tag_ids=["string"],
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DriverEfficiencyResponse, driver, path=["response"])

    @parametrize
    async def test_raw_response_efficiency(self, async_client: AsyncSamsara) -> None:
        response = await async_client.beta.fleet.drivers.with_raw_response.efficiency()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver = await response.parse()
        assert_matches_type(DriverEfficiencyResponse, driver, path=["response"])

    @parametrize
    async def test_streaming_response_efficiency(self, async_client: AsyncSamsara) -> None:
        async with async_client.beta.fleet.drivers.with_streaming_response.efficiency() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver = await response.parse()
            assert_matches_type(DriverEfficiencyResponse, driver, path=["response"])

        assert cast(Any, response.is_closed) is True
