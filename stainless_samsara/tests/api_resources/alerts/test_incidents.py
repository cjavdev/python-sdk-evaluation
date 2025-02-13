# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.alerts import IncidentStreamResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIncidents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_stream(self, client: Samsara) -> None:
        incident = client.alerts.incidents.stream(
            configuration_ids=["string"],
            start_time="startTime",
        )
        assert_matches_type(IncidentStreamResponse, incident, path=["response"])

    @parametrize
    def test_method_stream_with_all_params(self, client: Samsara) -> None:
        incident = client.alerts.incidents.stream(
            configuration_ids=["string"],
            start_time="startTime",
            after="after",
            end_time="endTime",
        )
        assert_matches_type(IncidentStreamResponse, incident, path=["response"])

    @parametrize
    def test_raw_response_stream(self, client: Samsara) -> None:
        response = client.alerts.incidents.with_raw_response.stream(
            configuration_ids=["string"],
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incident = response.parse()
        assert_matches_type(IncidentStreamResponse, incident, path=["response"])

    @parametrize
    def test_streaming_response_stream(self, client: Samsara) -> None:
        with client.alerts.incidents.with_streaming_response.stream(
            configuration_ids=["string"],
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incident = response.parse()
            assert_matches_type(IncidentStreamResponse, incident, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIncidents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_stream(self, async_client: AsyncSamsara) -> None:
        incident = await async_client.alerts.incidents.stream(
            configuration_ids=["string"],
            start_time="startTime",
        )
        assert_matches_type(IncidentStreamResponse, incident, path=["response"])

    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncSamsara) -> None:
        incident = await async_client.alerts.incidents.stream(
            configuration_ids=["string"],
            start_time="startTime",
            after="after",
            end_time="endTime",
        )
        assert_matches_type(IncidentStreamResponse, incident, path=["response"])

    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncSamsara) -> None:
        response = await async_client.alerts.incidents.with_raw_response.stream(
            configuration_ids=["string"],
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incident = await response.parse()
        assert_matches_type(IncidentStreamResponse, incident, path=["response"])

    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncSamsara) -> None:
        async with async_client.alerts.incidents.with_streaming_response.stream(
            configuration_ids=["string"],
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incident = await response.parse()
            assert_matches_type(IncidentStreamResponse, incident, path=["response"])

        assert cast(Any, response.is_closed) is True
