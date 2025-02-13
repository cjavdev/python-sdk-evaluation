# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types import DefectStreamResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDefects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_stream(self, client: Samsara) -> None:
        defect = client.defects.stream(
            start_time="startTime",
        )
        assert_matches_type(DefectStreamResponse, defect, path=["response"])

    @parametrize
    def test_method_stream_with_all_params(self, client: Samsara) -> None:
        defect = client.defects.stream(
            start_time="startTime",
            after="after",
            end_time="endTime",
            include_external_ids=True,
            is_resolved=True,
            limit=1,
        )
        assert_matches_type(DefectStreamResponse, defect, path=["response"])

    @parametrize
    def test_raw_response_stream(self, client: Samsara) -> None:
        response = client.defects.with_raw_response.stream(
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        defect = response.parse()
        assert_matches_type(DefectStreamResponse, defect, path=["response"])

    @parametrize
    def test_streaming_response_stream(self, client: Samsara) -> None:
        with client.defects.with_streaming_response.stream(
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            defect = response.parse()
            assert_matches_type(DefectStreamResponse, defect, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDefects:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_stream(self, async_client: AsyncSamsara) -> None:
        defect = await async_client.defects.stream(
            start_time="startTime",
        )
        assert_matches_type(DefectStreamResponse, defect, path=["response"])

    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncSamsara) -> None:
        defect = await async_client.defects.stream(
            start_time="startTime",
            after="after",
            end_time="endTime",
            include_external_ids=True,
            is_resolved=True,
            limit=1,
        )
        assert_matches_type(DefectStreamResponse, defect, path=["response"])

    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncSamsara) -> None:
        response = await async_client.defects.with_raw_response.stream(
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        defect = await response.parse()
        assert_matches_type(DefectStreamResponse, defect, path=["response"])

    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncSamsara) -> None:
        async with async_client.defects.with_streaming_response.stream(
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            defect = await response.parse()
            assert_matches_type(DefectStreamResponse, defect, path=["response"])

        assert cast(Any, response.is_closed) is True
