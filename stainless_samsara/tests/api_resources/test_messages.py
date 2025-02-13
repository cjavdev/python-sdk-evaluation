# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet import InlineResponse200_5, InlineResponse200_6

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        message = client.messages.create(
            driver_ids=[111, 222, 333],
            text="This is a message.",
        )
        assert_matches_type(InlineResponse200_6, message, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.messages.with_raw_response.create(
            driver_ids=[111, 222, 333],
            text="This is a message.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(InlineResponse200_6, message, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.messages.with_streaming_response.create(
            driver_ids=[111, 222, 333],
            text="This is a message.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(InlineResponse200_6, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        message = client.messages.list()
        assert_matches_type(InlineResponse200_5, message, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        message = client.messages.list(
            duration_ms=0,
            end_ms=0,
        )
        assert_matches_type(InlineResponse200_5, message, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.messages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(InlineResponse200_5, message, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.messages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(InlineResponse200_5, message, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        message = await async_client.messages.create(
            driver_ids=[111, 222, 333],
            text="This is a message.",
        )
        assert_matches_type(InlineResponse200_6, message, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.messages.with_raw_response.create(
            driver_ids=[111, 222, 333],
            text="This is a message.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(InlineResponse200_6, message, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.messages.with_streaming_response.create(
            driver_ids=[111, 222, 333],
            text="This is a message.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(InlineResponse200_6, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        message = await async_client.messages.list()
        assert_matches_type(InlineResponse200_5, message, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        message = await async_client.messages.list(
            duration_ms=0,
            end_ms=0,
        )
        assert_matches_type(InlineResponse200_5, message, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.messages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(InlineResponse200_5, message, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.messages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(InlineResponse200_5, message, path=["response"])

        assert cast(Any, response.is_closed) is True
