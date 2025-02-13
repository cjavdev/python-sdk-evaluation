# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types import (
    DriverTrailerAssignmentListResponse,
    DriverTrailerAssignmentCreateResponse,
    DriverTrailerAssignmentUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDriverTrailerAssignments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        driver_trailer_assignment = client.driver_trailer_assignments.create(
            driver_id="494123",
            trailer_id="12345",
        )
        assert_matches_type(DriverTrailerAssignmentCreateResponse, driver_trailer_assignment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Samsara) -> None:
        driver_trailer_assignment = client.driver_trailer_assignments.create(
            driver_id="494123",
            trailer_id="12345",
            start_time="2019-06-13T19:08:25Z",
        )
        assert_matches_type(DriverTrailerAssignmentCreateResponse, driver_trailer_assignment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.driver_trailer_assignments.with_raw_response.create(
            driver_id="494123",
            trailer_id="12345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_trailer_assignment = response.parse()
        assert_matches_type(DriverTrailerAssignmentCreateResponse, driver_trailer_assignment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.driver_trailer_assignments.with_streaming_response.create(
            driver_id="494123",
            trailer_id="12345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_trailer_assignment = response.parse()
            assert_matches_type(DriverTrailerAssignmentCreateResponse, driver_trailer_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Samsara) -> None:
        driver_trailer_assignment = client.driver_trailer_assignments.update(
            id="id",
            end_time="2019-06-13T19:08:25Z",
        )
        assert_matches_type(DriverTrailerAssignmentUpdateResponse, driver_trailer_assignment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Samsara) -> None:
        response = client.driver_trailer_assignments.with_raw_response.update(
            id="id",
            end_time="2019-06-13T19:08:25Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_trailer_assignment = response.parse()
        assert_matches_type(DriverTrailerAssignmentUpdateResponse, driver_trailer_assignment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Samsara) -> None:
        with client.driver_trailer_assignments.with_streaming_response.update(
            id="id",
            end_time="2019-06-13T19:08:25Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_trailer_assignment = response.parse()
            assert_matches_type(DriverTrailerAssignmentUpdateResponse, driver_trailer_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        driver_trailer_assignment = client.driver_trailer_assignments.list(
            driver_ids=["string"],
        )
        assert_matches_type(DriverTrailerAssignmentListResponse, driver_trailer_assignment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        driver_trailer_assignment = client.driver_trailer_assignments.list(
            driver_ids=["string"],
            after="after",
            include_external_ids=True,
        )
        assert_matches_type(DriverTrailerAssignmentListResponse, driver_trailer_assignment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.driver_trailer_assignments.with_raw_response.list(
            driver_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_trailer_assignment = response.parse()
        assert_matches_type(DriverTrailerAssignmentListResponse, driver_trailer_assignment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.driver_trailer_assignments.with_streaming_response.list(
            driver_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_trailer_assignment = response.parse()
            assert_matches_type(DriverTrailerAssignmentListResponse, driver_trailer_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDriverTrailerAssignments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        driver_trailer_assignment = await async_client.driver_trailer_assignments.create(
            driver_id="494123",
            trailer_id="12345",
        )
        assert_matches_type(DriverTrailerAssignmentCreateResponse, driver_trailer_assignment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSamsara) -> None:
        driver_trailer_assignment = await async_client.driver_trailer_assignments.create(
            driver_id="494123",
            trailer_id="12345",
            start_time="2019-06-13T19:08:25Z",
        )
        assert_matches_type(DriverTrailerAssignmentCreateResponse, driver_trailer_assignment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.driver_trailer_assignments.with_raw_response.create(
            driver_id="494123",
            trailer_id="12345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_trailer_assignment = await response.parse()
        assert_matches_type(DriverTrailerAssignmentCreateResponse, driver_trailer_assignment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.driver_trailer_assignments.with_streaming_response.create(
            driver_id="494123",
            trailer_id="12345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_trailer_assignment = await response.parse()
            assert_matches_type(DriverTrailerAssignmentCreateResponse, driver_trailer_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncSamsara) -> None:
        driver_trailer_assignment = await async_client.driver_trailer_assignments.update(
            id="id",
            end_time="2019-06-13T19:08:25Z",
        )
        assert_matches_type(DriverTrailerAssignmentUpdateResponse, driver_trailer_assignment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSamsara) -> None:
        response = await async_client.driver_trailer_assignments.with_raw_response.update(
            id="id",
            end_time="2019-06-13T19:08:25Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_trailer_assignment = await response.parse()
        assert_matches_type(DriverTrailerAssignmentUpdateResponse, driver_trailer_assignment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSamsara) -> None:
        async with async_client.driver_trailer_assignments.with_streaming_response.update(
            id="id",
            end_time="2019-06-13T19:08:25Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_trailer_assignment = await response.parse()
            assert_matches_type(DriverTrailerAssignmentUpdateResponse, driver_trailer_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        driver_trailer_assignment = await async_client.driver_trailer_assignments.list(
            driver_ids=["string"],
        )
        assert_matches_type(DriverTrailerAssignmentListResponse, driver_trailer_assignment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        driver_trailer_assignment = await async_client.driver_trailer_assignments.list(
            driver_ids=["string"],
            after="after",
            include_external_ids=True,
        )
        assert_matches_type(DriverTrailerAssignmentListResponse, driver_trailer_assignment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.driver_trailer_assignments.with_raw_response.list(
            driver_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_trailer_assignment = await response.parse()
        assert_matches_type(DriverTrailerAssignmentListResponse, driver_trailer_assignment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.driver_trailer_assignments.with_streaming_response.list(
            driver_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_trailer_assignment = await response.parse()
            assert_matches_type(DriverTrailerAssignmentListResponse, driver_trailer_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True
