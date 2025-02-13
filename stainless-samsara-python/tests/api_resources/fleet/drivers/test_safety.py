# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet.drivers import V1DriverSafetyScoreResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSafety:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_score(self, client: Samsara) -> None:
        safety = client.fleet.drivers.safety.score(
            driver_id=0,
            end_ms=0,
            start_ms=0,
        )
        assert_matches_type(V1DriverSafetyScoreResponse, safety, path=["response"])

    @parametrize
    def test_raw_response_score(self, client: Samsara) -> None:
        response = client.fleet.drivers.safety.with_raw_response.score(
            driver_id=0,
            end_ms=0,
            start_ms=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        safety = response.parse()
        assert_matches_type(V1DriverSafetyScoreResponse, safety, path=["response"])

    @parametrize
    def test_streaming_response_score(self, client: Samsara) -> None:
        with client.fleet.drivers.safety.with_streaming_response.score(
            driver_id=0,
            end_ms=0,
            start_ms=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            safety = response.parse()
            assert_matches_type(V1DriverSafetyScoreResponse, safety, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSafety:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_score(self, async_client: AsyncSamsara) -> None:
        safety = await async_client.fleet.drivers.safety.score(
            driver_id=0,
            end_ms=0,
            start_ms=0,
        )
        assert_matches_type(V1DriverSafetyScoreResponse, safety, path=["response"])

    @parametrize
    async def test_raw_response_score(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.drivers.safety.with_raw_response.score(
            driver_id=0,
            end_ms=0,
            start_ms=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        safety = await response.parse()
        assert_matches_type(V1DriverSafetyScoreResponse, safety, path=["response"])

    @parametrize
    async def test_streaming_response_score(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.drivers.safety.with_streaming_response.score(
            driver_id=0,
            end_ms=0,
            start_ms=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            safety = await response.parse()
            assert_matches_type(V1DriverSafetyScoreResponse, safety, path=["response"])

        assert cast(Any, response.is_closed) is True
