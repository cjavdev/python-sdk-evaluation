# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet.defects import HistoryListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHistory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        history = client.fleet.defects.history.list(
            end_time="endTime",
            start_time="startTime",
        )
        assert_matches_type(HistoryListResponse, history, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        history = client.fleet.defects.history.list(
            end_time="endTime",
            start_time="startTime",
            after="after",
            is_resolved=True,
            limit=1,
        )
        assert_matches_type(HistoryListResponse, history, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.fleet.defects.history.with_raw_response.list(
            end_time="endTime",
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert_matches_type(HistoryListResponse, history, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.fleet.defects.history.with_streaming_response.list(
            end_time="endTime",
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = response.parse()
            assert_matches_type(HistoryListResponse, history, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHistory:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        history = await async_client.fleet.defects.history.list(
            end_time="endTime",
            start_time="startTime",
        )
        assert_matches_type(HistoryListResponse, history, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        history = await async_client.fleet.defects.history.list(
            end_time="endTime",
            start_time="startTime",
            after="after",
            is_resolved=True,
            limit=1,
        )
        assert_matches_type(HistoryListResponse, history, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.defects.history.with_raw_response.list(
            end_time="endTime",
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert_matches_type(HistoryListResponse, history, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.defects.history.with_streaming_response.list(
            end_time="endTime",
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert_matches_type(HistoryListResponse, history, path=["response"])

        assert cast(Any, response.is_closed) is True
