# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.coaching import (
    DriverCoachAssignmentListResponse,
    DriverCoachAssignmentUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDriverCoachAssignments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Samsara) -> None:
        driver_coach_assignment = client.coaching.driver_coach_assignments.update(
            driver_id="driverId",
        )
        assert_matches_type(DriverCoachAssignmentUpdateResponse, driver_coach_assignment, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Samsara) -> None:
        driver_coach_assignment = client.coaching.driver_coach_assignments.update(
            driver_id="driverId",
            coach_id="coachId",
        )
        assert_matches_type(DriverCoachAssignmentUpdateResponse, driver_coach_assignment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Samsara) -> None:
        response = client.coaching.driver_coach_assignments.with_raw_response.update(
            driver_id="driverId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_coach_assignment = response.parse()
        assert_matches_type(DriverCoachAssignmentUpdateResponse, driver_coach_assignment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Samsara) -> None:
        with client.coaching.driver_coach_assignments.with_streaming_response.update(
            driver_id="driverId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_coach_assignment = response.parse()
            assert_matches_type(DriverCoachAssignmentUpdateResponse, driver_coach_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        driver_coach_assignment = client.coaching.driver_coach_assignments.list()
        assert_matches_type(DriverCoachAssignmentListResponse, driver_coach_assignment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        driver_coach_assignment = client.coaching.driver_coach_assignments.list(
            after="after",
            coach_ids=["string"],
            driver_ids=["string"],
            include_external_ids=True,
        )
        assert_matches_type(DriverCoachAssignmentListResponse, driver_coach_assignment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.coaching.driver_coach_assignments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_coach_assignment = response.parse()
        assert_matches_type(DriverCoachAssignmentListResponse, driver_coach_assignment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.coaching.driver_coach_assignments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_coach_assignment = response.parse()
            assert_matches_type(DriverCoachAssignmentListResponse, driver_coach_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDriverCoachAssignments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncSamsara) -> None:
        driver_coach_assignment = await async_client.coaching.driver_coach_assignments.update(
            driver_id="driverId",
        )
        assert_matches_type(DriverCoachAssignmentUpdateResponse, driver_coach_assignment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSamsara) -> None:
        driver_coach_assignment = await async_client.coaching.driver_coach_assignments.update(
            driver_id="driverId",
            coach_id="coachId",
        )
        assert_matches_type(DriverCoachAssignmentUpdateResponse, driver_coach_assignment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSamsara) -> None:
        response = await async_client.coaching.driver_coach_assignments.with_raw_response.update(
            driver_id="driverId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_coach_assignment = await response.parse()
        assert_matches_type(DriverCoachAssignmentUpdateResponse, driver_coach_assignment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSamsara) -> None:
        async with async_client.coaching.driver_coach_assignments.with_streaming_response.update(
            driver_id="driverId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_coach_assignment = await response.parse()
            assert_matches_type(DriverCoachAssignmentUpdateResponse, driver_coach_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        driver_coach_assignment = await async_client.coaching.driver_coach_assignments.list()
        assert_matches_type(DriverCoachAssignmentListResponse, driver_coach_assignment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        driver_coach_assignment = await async_client.coaching.driver_coach_assignments.list(
            after="after",
            coach_ids=["string"],
            driver_ids=["string"],
            include_external_ids=True,
        )
        assert_matches_type(DriverCoachAssignmentListResponse, driver_coach_assignment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.coaching.driver_coach_assignments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_coach_assignment = await response.parse()
        assert_matches_type(DriverCoachAssignmentListResponse, driver_coach_assignment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.coaching.driver_coach_assignments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_coach_assignment = await response.parse()
            assert_matches_type(DriverCoachAssignmentListResponse, driver_coach_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True
