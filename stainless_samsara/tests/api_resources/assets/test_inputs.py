# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.assets import InputStreamResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInputs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_stream(self, client: Samsara) -> None:
        input = client.assets.inputs.stream(
            ids=["string"],
            start_time="startTime",
            type="auxInput1",
        )
        assert_matches_type(InputStreamResponse, input, path=["response"])

    @parametrize
    def test_method_stream_with_all_params(self, client: Samsara) -> None:
        input = client.assets.inputs.stream(
            ids=["string"],
            start_time="startTime",
            type="auxInput1",
            after="after",
            end_time="endTime",
            include_attributes=True,
            include_external_ids=True,
            include_tags=True,
        )
        assert_matches_type(InputStreamResponse, input, path=["response"])

    @parametrize
    def test_raw_response_stream(self, client: Samsara) -> None:
        response = client.assets.inputs.with_raw_response.stream(
            ids=["string"],
            start_time="startTime",
            type="auxInput1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        input = response.parse()
        assert_matches_type(InputStreamResponse, input, path=["response"])

    @parametrize
    def test_streaming_response_stream(self, client: Samsara) -> None:
        with client.assets.inputs.with_streaming_response.stream(
            ids=["string"],
            start_time="startTime",
            type="auxInput1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            input = response.parse()
            assert_matches_type(InputStreamResponse, input, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInputs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_stream(self, async_client: AsyncSamsara) -> None:
        input = await async_client.assets.inputs.stream(
            ids=["string"],
            start_time="startTime",
            type="auxInput1",
        )
        assert_matches_type(InputStreamResponse, input, path=["response"])

    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncSamsara) -> None:
        input = await async_client.assets.inputs.stream(
            ids=["string"],
            start_time="startTime",
            type="auxInput1",
            after="after",
            end_time="endTime",
            include_attributes=True,
            include_external_ids=True,
            include_tags=True,
        )
        assert_matches_type(InputStreamResponse, input, path=["response"])

    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncSamsara) -> None:
        response = await async_client.assets.inputs.with_raw_response.stream(
            ids=["string"],
            start_time="startTime",
            type="auxInput1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        input = await response.parse()
        assert_matches_type(InputStreamResponse, input, path=["response"])

    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncSamsara) -> None:
        async with async_client.assets.inputs.with_streaming_response.stream(
            ids=["string"],
            start_time="startTime",
            type="auxInput1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            input = await response.parse()
            assert_matches_type(InputStreamResponse, input, path=["response"])

        assert cast(Any, response.is_closed) is True
