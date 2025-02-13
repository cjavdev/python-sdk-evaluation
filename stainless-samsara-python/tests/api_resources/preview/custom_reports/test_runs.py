# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara._utils import parse_datetime
from samsara.types.preview.custom_reports import (
    CustomReportsGetCustomReportRunsResponseBody,
    CustomReportsPostCustomReportRunResponseBody,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        run = client.preview.custom_reports.runs.create(
            custom_report_id="4f71fd67-54f0-41de-991c-ee1e031134d1",
            end_time=parse_datetime("2019-06-13T21:08:25Z"),
            start_time=parse_datetime("2019-06-13T19:08:25Z"),
        )
        assert_matches_type(CustomReportsPostCustomReportRunResponseBody, run, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Samsara) -> None:
        run = client.preview.custom_reports.runs.create(
            custom_report_id="4f71fd67-54f0-41de-991c-ee1e031134d1",
            end_time=parse_datetime("2019-06-13T21:08:25Z"),
            start_time=parse_datetime("2019-06-13T19:08:25Z"),
            attribute_value_ids=["19abdecf-54f0-41de-991c-ee1e031134d1", "ab83dfce-54f0-41de-991c-ee1e031134d2"],
            tag_ids=[48923049, 198349],
        )
        assert_matches_type(CustomReportsPostCustomReportRunResponseBody, run, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.preview.custom_reports.runs.with_raw_response.create(
            custom_report_id="4f71fd67-54f0-41de-991c-ee1e031134d1",
            end_time=parse_datetime("2019-06-13T21:08:25Z"),
            start_time=parse_datetime("2019-06-13T19:08:25Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(CustomReportsPostCustomReportRunResponseBody, run, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.preview.custom_reports.runs.with_streaming_response.create(
            custom_report_id="4f71fd67-54f0-41de-991c-ee1e031134d1",
            end_time=parse_datetime("2019-06-13T21:08:25Z"),
            start_time=parse_datetime("2019-06-13T19:08:25Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(CustomReportsPostCustomReportRunResponseBody, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        run = client.preview.custom_reports.runs.list()
        assert_matches_type(CustomReportsGetCustomReportRunsResponseBody, run, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        run = client.preview.custom_reports.runs.list(
            after="after",
            custom_report_ids=["string"],
            ids=["string"],
        )
        assert_matches_type(CustomReportsGetCustomReportRunsResponseBody, run, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.preview.custom_reports.runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(CustomReportsGetCustomReportRunsResponseBody, run, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.preview.custom_reports.runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(CustomReportsGetCustomReportRunsResponseBody, run, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        run = await async_client.preview.custom_reports.runs.create(
            custom_report_id="4f71fd67-54f0-41de-991c-ee1e031134d1",
            end_time=parse_datetime("2019-06-13T21:08:25Z"),
            start_time=parse_datetime("2019-06-13T19:08:25Z"),
        )
        assert_matches_type(CustomReportsPostCustomReportRunResponseBody, run, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSamsara) -> None:
        run = await async_client.preview.custom_reports.runs.create(
            custom_report_id="4f71fd67-54f0-41de-991c-ee1e031134d1",
            end_time=parse_datetime("2019-06-13T21:08:25Z"),
            start_time=parse_datetime("2019-06-13T19:08:25Z"),
            attribute_value_ids=["19abdecf-54f0-41de-991c-ee1e031134d1", "ab83dfce-54f0-41de-991c-ee1e031134d2"],
            tag_ids=[48923049, 198349],
        )
        assert_matches_type(CustomReportsPostCustomReportRunResponseBody, run, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.preview.custom_reports.runs.with_raw_response.create(
            custom_report_id="4f71fd67-54f0-41de-991c-ee1e031134d1",
            end_time=parse_datetime("2019-06-13T21:08:25Z"),
            start_time=parse_datetime("2019-06-13T19:08:25Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(CustomReportsPostCustomReportRunResponseBody, run, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.preview.custom_reports.runs.with_streaming_response.create(
            custom_report_id="4f71fd67-54f0-41de-991c-ee1e031134d1",
            end_time=parse_datetime("2019-06-13T21:08:25Z"),
            start_time=parse_datetime("2019-06-13T19:08:25Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(CustomReportsPostCustomReportRunResponseBody, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        run = await async_client.preview.custom_reports.runs.list()
        assert_matches_type(CustomReportsGetCustomReportRunsResponseBody, run, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        run = await async_client.preview.custom_reports.runs.list(
            after="after",
            custom_report_ids=["string"],
            ids=["string"],
        )
        assert_matches_type(CustomReportsGetCustomReportRunsResponseBody, run, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.preview.custom_reports.runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(CustomReportsGetCustomReportRunsResponseBody, run, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.preview.custom_reports.runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(CustomReportsGetCustomReportRunsResponseBody, run, path=["response"])

        assert cast(Any, response.is_closed) is True
