# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.hos import (
    DailyLogListResponse,
    HosDailyLogsUpdateShippingDocsResponseBody,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDailyLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        daily_log = client.hos.daily_logs.list()
        assert_matches_type(DailyLogListResponse, daily_log, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        daily_log = client.hos.daily_logs.list(
            after="after",
            driver_activation_status="active",
            driver_ids=["string"],
            end_date="endDate",
            expand="vehicle",
            parent_tag_ids="parentTagIds",
            start_date="startDate",
            tag_ids="tagIds",
        )
        assert_matches_type(DailyLogListResponse, daily_log, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.hos.daily_logs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        daily_log = response.parse()
        assert_matches_type(DailyLogListResponse, daily_log, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.hos.daily_logs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            daily_log = response.parse()
            assert_matches_type(DailyLogListResponse, daily_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_log_metadata(self, client: Samsara) -> None:
        daily_log = client.hos.daily_logs.update_log_metadata(
            driver_id="driverID",
            hos_date="hosDate",
            shipping_docs="ShippingID1, ShippingID2",
        )
        assert_matches_type(HosDailyLogsUpdateShippingDocsResponseBody, daily_log, path=["response"])

    @parametrize
    def test_raw_response_update_log_metadata(self, client: Samsara) -> None:
        response = client.hos.daily_logs.with_raw_response.update_log_metadata(
            driver_id="driverID",
            hos_date="hosDate",
            shipping_docs="ShippingID1, ShippingID2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        daily_log = response.parse()
        assert_matches_type(HosDailyLogsUpdateShippingDocsResponseBody, daily_log, path=["response"])

    @parametrize
    def test_streaming_response_update_log_metadata(self, client: Samsara) -> None:
        with client.hos.daily_logs.with_streaming_response.update_log_metadata(
            driver_id="driverID",
            hos_date="hosDate",
            shipping_docs="ShippingID1, ShippingID2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            daily_log = response.parse()
            assert_matches_type(HosDailyLogsUpdateShippingDocsResponseBody, daily_log, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDailyLogs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        daily_log = await async_client.hos.daily_logs.list()
        assert_matches_type(DailyLogListResponse, daily_log, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        daily_log = await async_client.hos.daily_logs.list(
            after="after",
            driver_activation_status="active",
            driver_ids=["string"],
            end_date="endDate",
            expand="vehicle",
            parent_tag_ids="parentTagIds",
            start_date="startDate",
            tag_ids="tagIds",
        )
        assert_matches_type(DailyLogListResponse, daily_log, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.hos.daily_logs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        daily_log = await response.parse()
        assert_matches_type(DailyLogListResponse, daily_log, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.hos.daily_logs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            daily_log = await response.parse()
            assert_matches_type(DailyLogListResponse, daily_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_log_metadata(self, async_client: AsyncSamsara) -> None:
        daily_log = await async_client.hos.daily_logs.update_log_metadata(
            driver_id="driverID",
            hos_date="hosDate",
            shipping_docs="ShippingID1, ShippingID2",
        )
        assert_matches_type(HosDailyLogsUpdateShippingDocsResponseBody, daily_log, path=["response"])

    @parametrize
    async def test_raw_response_update_log_metadata(self, async_client: AsyncSamsara) -> None:
        response = await async_client.hos.daily_logs.with_raw_response.update_log_metadata(
            driver_id="driverID",
            hos_date="hosDate",
            shipping_docs="ShippingID1, ShippingID2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        daily_log = await response.parse()
        assert_matches_type(HosDailyLogsUpdateShippingDocsResponseBody, daily_log, path=["response"])

    @parametrize
    async def test_streaming_response_update_log_metadata(self, async_client: AsyncSamsara) -> None:
        async with async_client.hos.daily_logs.with_streaming_response.update_log_metadata(
            driver_id="driverID",
            hos_date="hosDate",
            shipping_docs="ShippingID1, ShippingID2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            daily_log = await response.parse()
            assert_matches_type(HosDailyLogsUpdateShippingDocsResponseBody, daily_log, path=["response"])

        assert cast(Any, response.is_closed) is True
