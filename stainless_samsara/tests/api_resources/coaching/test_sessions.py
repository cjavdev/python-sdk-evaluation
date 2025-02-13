# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara._utils import parse_datetime
from samsara.types.coaching import SessionStreamResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_stream(self, client: Samsara) -> None:
        session = client.coaching.sessions.stream(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SessionStreamResponse, session, path=["response"])

    @parametrize
    def test_method_stream_with_all_params(self, client: Samsara) -> None:
        session = client.coaching.sessions.stream(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            after="after",
            coach_ids=["string"],
            driver_ids=["string"],
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_coachable_events=True,
            include_external_ids=True,
            session_statuses=["string"],
        )
        assert_matches_type(SessionStreamResponse, session, path=["response"])

    @parametrize
    def test_raw_response_stream(self, client: Samsara) -> None:
        response = client.coaching.sessions.with_raw_response.stream(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionStreamResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_stream(self, client: Samsara) -> None:
        with client.coaching.sessions.with_streaming_response.stream(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionStreamResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_stream(self, async_client: AsyncSamsara) -> None:
        session = await async_client.coaching.sessions.stream(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SessionStreamResponse, session, path=["response"])

    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncSamsara) -> None:
        session = await async_client.coaching.sessions.stream(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            after="after",
            coach_ids=["string"],
            driver_ids=["string"],
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_coachable_events=True,
            include_external_ids=True,
            session_statuses=["string"],
        )
        assert_matches_type(SessionStreamResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncSamsara) -> None:
        response = await async_client.coaching.sessions.with_raw_response.stream(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionStreamResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncSamsara) -> None:
        async with async_client.coaching.sessions.with_streaming_response.stream(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionStreamResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True
