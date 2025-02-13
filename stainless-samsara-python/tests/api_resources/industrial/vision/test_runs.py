# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.industrial.vision import (
    RunListResponse,
    RunRetrieveResponse,
    RunRetrievebycameraResponse,
    RunRetrievebycameraprogramResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Samsara) -> None:
        run = client.industrial.vision.runs.retrieve(
            camera_id=0,
        )
        assert_matches_type(RunRetrieveResponse, run, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Samsara) -> None:
        run = client.industrial.vision.runs.retrieve(
            camera_id=0,
            include="include",
            limit=0,
            program_id=0,
            started_at_ms=0,
        )
        assert_matches_type(RunRetrieveResponse, run, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Samsara) -> None:
        response = client.industrial.vision.runs.with_raw_response.retrieve(
            camera_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunRetrieveResponse, run, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Samsara) -> None:
        with client.industrial.vision.runs.with_streaming_response.retrieve(
            camera_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunRetrieveResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        run = client.industrial.vision.runs.list(
            duration_ms=0,
        )
        assert_matches_type(RunListResponse, run, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        run = client.industrial.vision.runs.list(
            duration_ms=0,
            end_ms=0,
        )
        assert_matches_type(RunListResponse, run, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.industrial.vision.runs.with_raw_response.list(
            duration_ms=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunListResponse, run, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.industrial.vision.runs.with_streaming_response.list(
            duration_ms=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunListResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrievebycamera(self, client: Samsara) -> None:
        run = client.industrial.vision.runs.retrievebycamera(
            camera_id=0,
            duration_ms=0,
        )
        assert_matches_type(RunRetrievebycameraResponse, run, path=["response"])

    @parametrize
    def test_method_retrievebycamera_with_all_params(self, client: Samsara) -> None:
        run = client.industrial.vision.runs.retrievebycamera(
            camera_id=0,
            duration_ms=0,
            end_ms=0,
        )
        assert_matches_type(RunRetrievebycameraResponse, run, path=["response"])

    @parametrize
    def test_raw_response_retrievebycamera(self, client: Samsara) -> None:
        response = client.industrial.vision.runs.with_raw_response.retrievebycamera(
            camera_id=0,
            duration_ms=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunRetrievebycameraResponse, run, path=["response"])

    @parametrize
    def test_streaming_response_retrievebycamera(self, client: Samsara) -> None:
        with client.industrial.vision.runs.with_streaming_response.retrievebycamera(
            camera_id=0,
            duration_ms=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunRetrievebycameraResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrievebycameraprogram(self, client: Samsara) -> None:
        run = client.industrial.vision.runs.retrievebycameraprogram(
            started_at_ms=0,
            camera_id=0,
            program_id=0,
        )
        assert_matches_type(RunRetrievebycameraprogramResponse, run, path=["response"])

    @parametrize
    def test_method_retrievebycameraprogram_with_all_params(self, client: Samsara) -> None:
        run = client.industrial.vision.runs.retrievebycameraprogram(
            started_at_ms=0,
            camera_id=0,
            program_id=0,
            include="include",
        )
        assert_matches_type(RunRetrievebycameraprogramResponse, run, path=["response"])

    @parametrize
    def test_raw_response_retrievebycameraprogram(self, client: Samsara) -> None:
        response = client.industrial.vision.runs.with_raw_response.retrievebycameraprogram(
            started_at_ms=0,
            camera_id=0,
            program_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunRetrievebycameraprogramResponse, run, path=["response"])

    @parametrize
    def test_streaming_response_retrievebycameraprogram(self, client: Samsara) -> None:
        with client.industrial.vision.runs.with_streaming_response.retrievebycameraprogram(
            started_at_ms=0,
            camera_id=0,
            program_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunRetrievebycameraprogramResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSamsara) -> None:
        run = await async_client.industrial.vision.runs.retrieve(
            camera_id=0,
        )
        assert_matches_type(RunRetrieveResponse, run, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSamsara) -> None:
        run = await async_client.industrial.vision.runs.retrieve(
            camera_id=0,
            include="include",
            limit=0,
            program_id=0,
            started_at_ms=0,
        )
        assert_matches_type(RunRetrieveResponse, run, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSamsara) -> None:
        response = await async_client.industrial.vision.runs.with_raw_response.retrieve(
            camera_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunRetrieveResponse, run, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSamsara) -> None:
        async with async_client.industrial.vision.runs.with_streaming_response.retrieve(
            camera_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunRetrieveResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        run = await async_client.industrial.vision.runs.list(
            duration_ms=0,
        )
        assert_matches_type(RunListResponse, run, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        run = await async_client.industrial.vision.runs.list(
            duration_ms=0,
            end_ms=0,
        )
        assert_matches_type(RunListResponse, run, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.industrial.vision.runs.with_raw_response.list(
            duration_ms=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunListResponse, run, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.industrial.vision.runs.with_streaming_response.list(
            duration_ms=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunListResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrievebycamera(self, async_client: AsyncSamsara) -> None:
        run = await async_client.industrial.vision.runs.retrievebycamera(
            camera_id=0,
            duration_ms=0,
        )
        assert_matches_type(RunRetrievebycameraResponse, run, path=["response"])

    @parametrize
    async def test_method_retrievebycamera_with_all_params(self, async_client: AsyncSamsara) -> None:
        run = await async_client.industrial.vision.runs.retrievebycamera(
            camera_id=0,
            duration_ms=0,
            end_ms=0,
        )
        assert_matches_type(RunRetrievebycameraResponse, run, path=["response"])

    @parametrize
    async def test_raw_response_retrievebycamera(self, async_client: AsyncSamsara) -> None:
        response = await async_client.industrial.vision.runs.with_raw_response.retrievebycamera(
            camera_id=0,
            duration_ms=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunRetrievebycameraResponse, run, path=["response"])

    @parametrize
    async def test_streaming_response_retrievebycamera(self, async_client: AsyncSamsara) -> None:
        async with async_client.industrial.vision.runs.with_streaming_response.retrievebycamera(
            camera_id=0,
            duration_ms=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunRetrievebycameraResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrievebycameraprogram(self, async_client: AsyncSamsara) -> None:
        run = await async_client.industrial.vision.runs.retrievebycameraprogram(
            started_at_ms=0,
            camera_id=0,
            program_id=0,
        )
        assert_matches_type(RunRetrievebycameraprogramResponse, run, path=["response"])

    @parametrize
    async def test_method_retrievebycameraprogram_with_all_params(self, async_client: AsyncSamsara) -> None:
        run = await async_client.industrial.vision.runs.retrievebycameraprogram(
            started_at_ms=0,
            camera_id=0,
            program_id=0,
            include="include",
        )
        assert_matches_type(RunRetrievebycameraprogramResponse, run, path=["response"])

    @parametrize
    async def test_raw_response_retrievebycameraprogram(self, async_client: AsyncSamsara) -> None:
        response = await async_client.industrial.vision.runs.with_raw_response.retrievebycameraprogram(
            started_at_ms=0,
            camera_id=0,
            program_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunRetrievebycameraprogramResponse, run, path=["response"])

    @parametrize
    async def test_streaming_response_retrievebycameraprogram(self, async_client: AsyncSamsara) -> None:
        async with async_client.industrial.vision.runs.with_streaming_response.retrievebycameraprogram(
            started_at_ms=0,
            camera_id=0,
            program_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunRetrievebycameraprogramResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True
