# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types import (
    IssuesGetIssuesResponseBody,
    IssuesPatchIssueResponseBody,
    IssuesGetIssuesStreamResponseBody,
)
from samsara._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIssues:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Samsara) -> None:
        issue = client.issues.update(
            id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
        )
        assert_matches_type(IssuesPatchIssueResponseBody, issue, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Samsara) -> None:
        issue = client.issues.update(
            id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
            assigned_to={
                "id": "938172",
                "type": "user",
            },
            due_date=parse_datetime("2019-06-13T19:08:25Z"),
            external_ids={"foo": "string"},
            status="open",
        )
        assert_matches_type(IssuesPatchIssueResponseBody, issue, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Samsara) -> None:
        response = client.issues.with_raw_response.update(
            id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        issue = response.parse()
        assert_matches_type(IssuesPatchIssueResponseBody, issue, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Samsara) -> None:
        with client.issues.with_streaming_response.update(
            id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            issue = response.parse()
            assert_matches_type(IssuesPatchIssueResponseBody, issue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        issue = client.issues.list(
            ids=["string"],
        )
        assert_matches_type(IssuesGetIssuesResponseBody, issue, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        issue = client.issues.list(
            ids=["string"],
            include=["string"],
        )
        assert_matches_type(IssuesGetIssuesResponseBody, issue, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.issues.with_raw_response.list(
            ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        issue = response.parse()
        assert_matches_type(IssuesGetIssuesResponseBody, issue, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.issues.with_streaming_response.list(
            ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            issue = response.parse()
            assert_matches_type(IssuesGetIssuesResponseBody, issue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_stream(self, client: Samsara) -> None:
        issue = client.issues.stream(
            start_time="startTime",
        )
        assert_matches_type(IssuesGetIssuesStreamResponseBody, issue, path=["response"])

    @parametrize
    def test_method_stream_with_all_params(self, client: Samsara) -> None:
        issue = client.issues.stream(
            start_time="startTime",
            after="after",
            asset_ids=["string"],
            end_time="endTime",
            include=["string"],
            status=["string"],
        )
        assert_matches_type(IssuesGetIssuesStreamResponseBody, issue, path=["response"])

    @parametrize
    def test_raw_response_stream(self, client: Samsara) -> None:
        response = client.issues.with_raw_response.stream(
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        issue = response.parse()
        assert_matches_type(IssuesGetIssuesStreamResponseBody, issue, path=["response"])

    @parametrize
    def test_streaming_response_stream(self, client: Samsara) -> None:
        with client.issues.with_streaming_response.stream(
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            issue = response.parse()
            assert_matches_type(IssuesGetIssuesStreamResponseBody, issue, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIssues:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncSamsara) -> None:
        issue = await async_client.issues.update(
            id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
        )
        assert_matches_type(IssuesPatchIssueResponseBody, issue, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSamsara) -> None:
        issue = await async_client.issues.update(
            id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
            assigned_to={
                "id": "938172",
                "type": "user",
            },
            due_date=parse_datetime("2019-06-13T19:08:25Z"),
            external_ids={"foo": "string"},
            status="open",
        )
        assert_matches_type(IssuesPatchIssueResponseBody, issue, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSamsara) -> None:
        response = await async_client.issues.with_raw_response.update(
            id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        issue = await response.parse()
        assert_matches_type(IssuesPatchIssueResponseBody, issue, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSamsara) -> None:
        async with async_client.issues.with_streaming_response.update(
            id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            issue = await response.parse()
            assert_matches_type(IssuesPatchIssueResponseBody, issue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        issue = await async_client.issues.list(
            ids=["string"],
        )
        assert_matches_type(IssuesGetIssuesResponseBody, issue, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        issue = await async_client.issues.list(
            ids=["string"],
            include=["string"],
        )
        assert_matches_type(IssuesGetIssuesResponseBody, issue, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.issues.with_raw_response.list(
            ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        issue = await response.parse()
        assert_matches_type(IssuesGetIssuesResponseBody, issue, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.issues.with_streaming_response.list(
            ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            issue = await response.parse()
            assert_matches_type(IssuesGetIssuesResponseBody, issue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_stream(self, async_client: AsyncSamsara) -> None:
        issue = await async_client.issues.stream(
            start_time="startTime",
        )
        assert_matches_type(IssuesGetIssuesStreamResponseBody, issue, path=["response"])

    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncSamsara) -> None:
        issue = await async_client.issues.stream(
            start_time="startTime",
            after="after",
            asset_ids=["string"],
            end_time="endTime",
            include=["string"],
            status=["string"],
        )
        assert_matches_type(IssuesGetIssuesStreamResponseBody, issue, path=["response"])

    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncSamsara) -> None:
        response = await async_client.issues.with_raw_response.stream(
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        issue = await response.parse()
        assert_matches_type(IssuesGetIssuesStreamResponseBody, issue, path=["response"])

    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncSamsara) -> None:
        async with async_client.issues.with_streaming_response.stream(
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            issue = await response.parse()
            assert_matches_type(IssuesGetIssuesStreamResponseBody, issue, path=["response"])

        assert cast(Any, response.is_closed) is True
