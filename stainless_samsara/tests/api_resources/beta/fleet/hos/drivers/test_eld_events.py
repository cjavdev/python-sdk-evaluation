# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.beta.fleet.hos.drivers import EldEventListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEldEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        eld_event = client.beta.fleet.hos.drivers.eld_events.list(
            end_time="endTime",
            start_time="startTime",
        )
        assert_matches_type(EldEventListResponse, eld_event, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        eld_event = client.beta.fleet.hos.drivers.eld_events.list(
            end_time="endTime",
            start_time="startTime",
            after="after",
            driver_activation_status="active",
            driver_ids=["string"],
            limit=1,
            parent_tag_ids="parentTagIds",
            tag_ids="tagIds",
        )
        assert_matches_type(EldEventListResponse, eld_event, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.beta.fleet.hos.drivers.eld_events.with_raw_response.list(
            end_time="endTime",
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eld_event = response.parse()
        assert_matches_type(EldEventListResponse, eld_event, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.beta.fleet.hos.drivers.eld_events.with_streaming_response.list(
            end_time="endTime",
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eld_event = response.parse()
            assert_matches_type(EldEventListResponse, eld_event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEldEvents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        eld_event = await async_client.beta.fleet.hos.drivers.eld_events.list(
            end_time="endTime",
            start_time="startTime",
        )
        assert_matches_type(EldEventListResponse, eld_event, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        eld_event = await async_client.beta.fleet.hos.drivers.eld_events.list(
            end_time="endTime",
            start_time="startTime",
            after="after",
            driver_activation_status="active",
            driver_ids=["string"],
            limit=1,
            parent_tag_ids="parentTagIds",
            tag_ids="tagIds",
        )
        assert_matches_type(EldEventListResponse, eld_event, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.beta.fleet.hos.drivers.eld_events.with_raw_response.list(
            end_time="endTime",
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eld_event = await response.parse()
        assert_matches_type(EldEventListResponse, eld_event, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.beta.fleet.hos.drivers.eld_events.with_streaming_response.list(
            end_time="endTime",
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eld_event = await response.parse()
            assert_matches_type(EldEventListResponse, eld_event, path=["response"])

        assert cast(Any, response.is_closed) is True
