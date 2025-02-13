# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet.safety_events import SafetyEventsGetSafetyActivityEventFeedResponseBody

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuditLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_feed(self, client: Samsara) -> None:
        audit_log = client.fleet.safety_events.audit_logs.feed()
        assert_matches_type(SafetyEventsGetSafetyActivityEventFeedResponseBody, audit_log, path=["response"])

    @parametrize
    def test_method_feed_with_all_params(self, client: Samsara) -> None:
        audit_log = client.fleet.safety_events.audit_logs.feed(
            after="after",
            start_time="startTime",
        )
        assert_matches_type(SafetyEventsGetSafetyActivityEventFeedResponseBody, audit_log, path=["response"])

    @parametrize
    def test_raw_response_feed(self, client: Samsara) -> None:
        response = client.fleet.safety_events.audit_logs.with_raw_response.feed()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = response.parse()
        assert_matches_type(SafetyEventsGetSafetyActivityEventFeedResponseBody, audit_log, path=["response"])

    @parametrize
    def test_streaming_response_feed(self, client: Samsara) -> None:
        with client.fleet.safety_events.audit_logs.with_streaming_response.feed() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = response.parse()
            assert_matches_type(SafetyEventsGetSafetyActivityEventFeedResponseBody, audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuditLogs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_feed(self, async_client: AsyncSamsara) -> None:
        audit_log = await async_client.fleet.safety_events.audit_logs.feed()
        assert_matches_type(SafetyEventsGetSafetyActivityEventFeedResponseBody, audit_log, path=["response"])

    @parametrize
    async def test_method_feed_with_all_params(self, async_client: AsyncSamsara) -> None:
        audit_log = await async_client.fleet.safety_events.audit_logs.feed(
            after="after",
            start_time="startTime",
        )
        assert_matches_type(SafetyEventsGetSafetyActivityEventFeedResponseBody, audit_log, path=["response"])

    @parametrize
    async def test_raw_response_feed(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.safety_events.audit_logs.with_raw_response.feed()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = await response.parse()
        assert_matches_type(SafetyEventsGetSafetyActivityEventFeedResponseBody, audit_log, path=["response"])

    @parametrize
    async def test_streaming_response_feed(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.safety_events.audit_logs.with_streaming_response.feed() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = await response.parse()
            assert_matches_type(SafetyEventsGetSafetyActivityEventFeedResponseBody, audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True
