# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types import V1HosAuthenticationLogsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHosAuthenticationLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        hos_authentication_log = client.hos_authentication_logs.list(
            driver_id=0,
            end_ms=0,
            start_ms=0,
        )
        assert_matches_type(V1HosAuthenticationLogsResponse, hos_authentication_log, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.hos_authentication_logs.with_raw_response.list(
            driver_id=0,
            end_ms=0,
            start_ms=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hos_authentication_log = response.parse()
        assert_matches_type(V1HosAuthenticationLogsResponse, hos_authentication_log, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.hos_authentication_logs.with_streaming_response.list(
            driver_id=0,
            end_ms=0,
            start_ms=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hos_authentication_log = response.parse()
            assert_matches_type(V1HosAuthenticationLogsResponse, hos_authentication_log, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHosAuthenticationLogs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        hos_authentication_log = await async_client.hos_authentication_logs.list(
            driver_id=0,
            end_ms=0,
            start_ms=0,
        )
        assert_matches_type(V1HosAuthenticationLogsResponse, hos_authentication_log, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.hos_authentication_logs.with_raw_response.list(
            driver_id=0,
            end_ms=0,
            start_ms=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hos_authentication_log = await response.parse()
        assert_matches_type(V1HosAuthenticationLogsResponse, hos_authentication_log, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.hos_authentication_logs.with_streaming_response.list(
            driver_id=0,
            end_ms=0,
            start_ms=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hos_authentication_log = await response.parse()
            assert_matches_type(V1HosAuthenticationLogsResponse, hos_authentication_log, path=["response"])

        assert cast(Any, response.is_closed) is True
