# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet import InlineResponse200_4

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMaintenance:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        maintenance = client.maintenance.list()
        assert_matches_type(InlineResponse200_4, maintenance, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.maintenance.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maintenance = response.parse()
        assert_matches_type(InlineResponse200_4, maintenance, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.maintenance.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maintenance = response.parse()
            assert_matches_type(InlineResponse200_4, maintenance, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMaintenance:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        maintenance = await async_client.maintenance.list()
        assert_matches_type(InlineResponse200_4, maintenance, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.maintenance.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maintenance = await response.parse()
        assert_matches_type(InlineResponse200_4, maintenance, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.maintenance.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maintenance = await response.parse()
            assert_matches_type(InlineResponse200_4, maintenance, path=["response"])

        assert cast(Any, response.is_closed) is True
