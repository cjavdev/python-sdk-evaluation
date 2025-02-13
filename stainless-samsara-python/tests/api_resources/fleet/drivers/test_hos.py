# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHos:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_duty_status(self, client: Samsara) -> None:
        ho = client.fleet.drivers.hos.duty_status(
            driver_id=0,
            duty_status="ON_DUTY",
        )
        assert ho is None

    @parametrize
    def test_method_duty_status_with_all_params(self, client: Samsara) -> None:
        ho = client.fleet.drivers.hos.duty_status(
            driver_id=0,
            duty_status="ON_DUTY",
            location="Loading dock",
            remark="Beginning On Duty Shift",
            status_change_at_ms=1580834793568,
            vehicle_id=1234,
        )
        assert ho is None

    @parametrize
    def test_raw_response_duty_status(self, client: Samsara) -> None:
        response = client.fleet.drivers.hos.with_raw_response.duty_status(
            driver_id=0,
            duty_status="ON_DUTY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ho = response.parse()
        assert ho is None

    @parametrize
    def test_streaming_response_duty_status(self, client: Samsara) -> None:
        with client.fleet.drivers.hos.with_streaming_response.duty_status(
            driver_id=0,
            duty_status="ON_DUTY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ho = response.parse()
            assert ho is None

        assert cast(Any, response.is_closed) is True


class TestAsyncHos:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_duty_status(self, async_client: AsyncSamsara) -> None:
        ho = await async_client.fleet.drivers.hos.duty_status(
            driver_id=0,
            duty_status="ON_DUTY",
        )
        assert ho is None

    @parametrize
    async def test_method_duty_status_with_all_params(self, async_client: AsyncSamsara) -> None:
        ho = await async_client.fleet.drivers.hos.duty_status(
            driver_id=0,
            duty_status="ON_DUTY",
            location="Loading dock",
            remark="Beginning On Duty Shift",
            status_change_at_ms=1580834793568,
            vehicle_id=1234,
        )
        assert ho is None

    @parametrize
    async def test_raw_response_duty_status(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.drivers.hos.with_raw_response.duty_status(
            driver_id=0,
            duty_status="ON_DUTY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ho = await response.parse()
        assert ho is None

    @parametrize
    async def test_streaming_response_duty_status(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.drivers.hos.with_streaming_response.duty_status(
            driver_id=0,
            duty_status="ON_DUTY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ho = await response.parse()
            assert ho is None

        assert cast(Any, response.is_closed) is True
