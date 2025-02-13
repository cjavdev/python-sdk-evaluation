# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.beta.fleet.trailers import (
    StatFeedResponse,
    StatListResponse,
    StatHistoryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        stat = client.beta.fleet.trailers.stats.list(
            types="types",
        )
        assert_matches_type(StatListResponse, stat, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        stat = client.beta.fleet.trailers.stats.list(
            types="types",
            after="after",
            parent_tag_ids="parentTagIds",
            tag_ids="tagIds",
            time="time",
            trailer_ids="trailerIds",
        )
        assert_matches_type(StatListResponse, stat, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.beta.fleet.trailers.stats.with_raw_response.list(
            types="types",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = response.parse()
        assert_matches_type(StatListResponse, stat, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.beta.fleet.trailers.stats.with_streaming_response.list(
            types="types",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = response.parse()
            assert_matches_type(StatListResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_feed(self, client: Samsara) -> None:
        stat = client.beta.fleet.trailers.stats.feed(
            types="types",
        )
        assert_matches_type(StatFeedResponse, stat, path=["response"])

    @parametrize
    def test_method_feed_with_all_params(self, client: Samsara) -> None:
        stat = client.beta.fleet.trailers.stats.feed(
            types="types",
            after="after",
            decorations="decorations",
            parent_tag_ids="parentTagIds",
            tag_ids="tagIds",
            trailer_ids="trailerIds",
        )
        assert_matches_type(StatFeedResponse, stat, path=["response"])

    @parametrize
    def test_raw_response_feed(self, client: Samsara) -> None:
        response = client.beta.fleet.trailers.stats.with_raw_response.feed(
            types="types",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = response.parse()
        assert_matches_type(StatFeedResponse, stat, path=["response"])

    @parametrize
    def test_streaming_response_feed(self, client: Samsara) -> None:
        with client.beta.fleet.trailers.stats.with_streaming_response.feed(
            types="types",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = response.parse()
            assert_matches_type(StatFeedResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_history(self, client: Samsara) -> None:
        stat = client.beta.fleet.trailers.stats.history(
            end_time="endTime",
            start_time="startTime",
            types="types",
        )
        assert_matches_type(StatHistoryResponse, stat, path=["response"])

    @parametrize
    def test_method_history_with_all_params(self, client: Samsara) -> None:
        stat = client.beta.fleet.trailers.stats.history(
            end_time="endTime",
            start_time="startTime",
            types="types",
            after="after",
            decorations="decorations",
            parent_tag_ids="parentTagIds",
            tag_ids="tagIds",
            trailer_ids="trailerIds",
        )
        assert_matches_type(StatHistoryResponse, stat, path=["response"])

    @parametrize
    def test_raw_response_history(self, client: Samsara) -> None:
        response = client.beta.fleet.trailers.stats.with_raw_response.history(
            end_time="endTime",
            start_time="startTime",
            types="types",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = response.parse()
        assert_matches_type(StatHistoryResponse, stat, path=["response"])

    @parametrize
    def test_streaming_response_history(self, client: Samsara) -> None:
        with client.beta.fleet.trailers.stats.with_streaming_response.history(
            end_time="endTime",
            start_time="startTime",
            types="types",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = response.parse()
            assert_matches_type(StatHistoryResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStats:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        stat = await async_client.beta.fleet.trailers.stats.list(
            types="types",
        )
        assert_matches_type(StatListResponse, stat, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        stat = await async_client.beta.fleet.trailers.stats.list(
            types="types",
            after="after",
            parent_tag_ids="parentTagIds",
            tag_ids="tagIds",
            time="time",
            trailer_ids="trailerIds",
        )
        assert_matches_type(StatListResponse, stat, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.beta.fleet.trailers.stats.with_raw_response.list(
            types="types",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = await response.parse()
        assert_matches_type(StatListResponse, stat, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.beta.fleet.trailers.stats.with_streaming_response.list(
            types="types",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = await response.parse()
            assert_matches_type(StatListResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_feed(self, async_client: AsyncSamsara) -> None:
        stat = await async_client.beta.fleet.trailers.stats.feed(
            types="types",
        )
        assert_matches_type(StatFeedResponse, stat, path=["response"])

    @parametrize
    async def test_method_feed_with_all_params(self, async_client: AsyncSamsara) -> None:
        stat = await async_client.beta.fleet.trailers.stats.feed(
            types="types",
            after="after",
            decorations="decorations",
            parent_tag_ids="parentTagIds",
            tag_ids="tagIds",
            trailer_ids="trailerIds",
        )
        assert_matches_type(StatFeedResponse, stat, path=["response"])

    @parametrize
    async def test_raw_response_feed(self, async_client: AsyncSamsara) -> None:
        response = await async_client.beta.fleet.trailers.stats.with_raw_response.feed(
            types="types",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = await response.parse()
        assert_matches_type(StatFeedResponse, stat, path=["response"])

    @parametrize
    async def test_streaming_response_feed(self, async_client: AsyncSamsara) -> None:
        async with async_client.beta.fleet.trailers.stats.with_streaming_response.feed(
            types="types",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = await response.parse()
            assert_matches_type(StatFeedResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_history(self, async_client: AsyncSamsara) -> None:
        stat = await async_client.beta.fleet.trailers.stats.history(
            end_time="endTime",
            start_time="startTime",
            types="types",
        )
        assert_matches_type(StatHistoryResponse, stat, path=["response"])

    @parametrize
    async def test_method_history_with_all_params(self, async_client: AsyncSamsara) -> None:
        stat = await async_client.beta.fleet.trailers.stats.history(
            end_time="endTime",
            start_time="startTime",
            types="types",
            after="after",
            decorations="decorations",
            parent_tag_ids="parentTagIds",
            tag_ids="tagIds",
            trailer_ids="trailerIds",
        )
        assert_matches_type(StatHistoryResponse, stat, path=["response"])

    @parametrize
    async def test_raw_response_history(self, async_client: AsyncSamsara) -> None:
        response = await async_client.beta.fleet.trailers.stats.with_raw_response.history(
            end_time="endTime",
            start_time="startTime",
            types="types",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = await response.parse()
        assert_matches_type(StatHistoryResponse, stat, path=["response"])

    @parametrize
    async def test_streaming_response_history(self, async_client: AsyncSamsara) -> None:
        async with async_client.beta.fleet.trailers.stats.with_streaming_response.history(
            end_time="endTime",
            start_time="startTime",
            types="types",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = await response.parse()
            assert_matches_type(StatHistoryResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True
