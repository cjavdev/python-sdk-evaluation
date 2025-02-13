# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.sensors import HistoryCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHistory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        history = client.sensors.history.create(
            end_ms=1462881998034,
            series=[
                {
                    "field": "ambientTemperature",
                    "widget_id": 1,
                }
            ],
            start_ms=1462878398034,
            step_ms=3600000,
        )
        assert_matches_type(HistoryCreateResponse, history, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Samsara) -> None:
        history = client.sensors.history.create(
            end_ms=1462881998034,
            series=[
                {
                    "field": "ambientTemperature",
                    "widget_id": 1,
                }
            ],
            start_ms=1462878398034,
            step_ms=3600000,
            fill_missing="withNull",
        )
        assert_matches_type(HistoryCreateResponse, history, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.sensors.history.with_raw_response.create(
            end_ms=1462881998034,
            series=[
                {
                    "field": "ambientTemperature",
                    "widget_id": 1,
                }
            ],
            start_ms=1462878398034,
            step_ms=3600000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert_matches_type(HistoryCreateResponse, history, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.sensors.history.with_streaming_response.create(
            end_ms=1462881998034,
            series=[
                {
                    "field": "ambientTemperature",
                    "widget_id": 1,
                }
            ],
            start_ms=1462878398034,
            step_ms=3600000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = response.parse()
            assert_matches_type(HistoryCreateResponse, history, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHistory:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        history = await async_client.sensors.history.create(
            end_ms=1462881998034,
            series=[
                {
                    "field": "ambientTemperature",
                    "widget_id": 1,
                }
            ],
            start_ms=1462878398034,
            step_ms=3600000,
        )
        assert_matches_type(HistoryCreateResponse, history, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSamsara) -> None:
        history = await async_client.sensors.history.create(
            end_ms=1462881998034,
            series=[
                {
                    "field": "ambientTemperature",
                    "widget_id": 1,
                }
            ],
            start_ms=1462878398034,
            step_ms=3600000,
            fill_missing="withNull",
        )
        assert_matches_type(HistoryCreateResponse, history, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.sensors.history.with_raw_response.create(
            end_ms=1462881998034,
            series=[
                {
                    "field": "ambientTemperature",
                    "widget_id": 1,
                }
            ],
            start_ms=1462878398034,
            step_ms=3600000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert_matches_type(HistoryCreateResponse, history, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.sensors.history.with_streaming_response.create(
            end_ms=1462881998034,
            series=[
                {
                    "field": "ambientTemperature",
                    "widget_id": 1,
                }
            ],
            start_ms=1462878398034,
            step_ms=3600000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert_matches_type(HistoryCreateResponse, history, path=["response"])

        assert cast(Any, response.is_closed) is True
