# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.beta.aemp import FleetListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFleet:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        fleet = client.beta.aemp.fleet.list(
            "pageNumber",
        )
        assert_matches_type(FleetListResponse, fleet, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.beta.aemp.fleet.with_raw_response.list(
            "pageNumber",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fleet = response.parse()
        assert_matches_type(FleetListResponse, fleet, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.beta.aemp.fleet.with_streaming_response.list(
            "pageNumber",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fleet = response.parse()
            assert_matches_type(FleetListResponse, fleet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_number` but received ''"):
            client.beta.aemp.fleet.with_raw_response.list(
                "",
            )


class TestAsyncFleet:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        fleet = await async_client.beta.aemp.fleet.list(
            "pageNumber",
        )
        assert_matches_type(FleetListResponse, fleet, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.beta.aemp.fleet.with_raw_response.list(
            "pageNumber",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fleet = await response.parse()
        assert_matches_type(FleetListResponse, fleet, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.beta.aemp.fleet.with_streaming_response.list(
            "pageNumber",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fleet = await response.parse()
            assert_matches_type(FleetListResponse, fleet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_number` but received ''"):
            await async_client.beta.aemp.fleet.with_raw_response.list(
                "",
            )
