# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet.vehicles import VehiclesDriverAssignmentsGetVehiclesDriverAssignmentsResponseBody

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDriverAssignments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        driver_assignment = client.vehicles.driver_assignments.list()
        assert_matches_type(
            VehiclesDriverAssignmentsGetVehiclesDriverAssignmentsResponseBody, driver_assignment, path=["response"]
        )

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        driver_assignment = client.vehicles.driver_assignments.list(
            after="after",
            end_time="endTime",
            parent_tag_ids="parentTagIds",
            start_time="startTime",
            tag_ids="tagIds",
            vehicle_ids="vehicleIds",
        )
        assert_matches_type(
            VehiclesDriverAssignmentsGetVehiclesDriverAssignmentsResponseBody, driver_assignment, path=["response"]
        )

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.vehicles.driver_assignments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_assignment = response.parse()
        assert_matches_type(
            VehiclesDriverAssignmentsGetVehiclesDriverAssignmentsResponseBody, driver_assignment, path=["response"]
        )

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.vehicles.driver_assignments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_assignment = response.parse()
            assert_matches_type(
                VehiclesDriverAssignmentsGetVehiclesDriverAssignmentsResponseBody, driver_assignment, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncDriverAssignments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        driver_assignment = await async_client.vehicles.driver_assignments.list()
        assert_matches_type(
            VehiclesDriverAssignmentsGetVehiclesDriverAssignmentsResponseBody, driver_assignment, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        driver_assignment = await async_client.vehicles.driver_assignments.list(
            after="after",
            end_time="endTime",
            parent_tag_ids="parentTagIds",
            start_time="startTime",
            tag_ids="tagIds",
            vehicle_ids="vehicleIds",
        )
        assert_matches_type(
            VehiclesDriverAssignmentsGetVehiclesDriverAssignmentsResponseBody, driver_assignment, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.vehicles.driver_assignments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_assignment = await response.parse()
        assert_matches_type(
            VehiclesDriverAssignmentsGetVehiclesDriverAssignmentsResponseBody, driver_assignment, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.vehicles.driver_assignments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_assignment = await response.parse()
            assert_matches_type(
                VehiclesDriverAssignmentsGetVehiclesDriverAssignmentsResponseBody, driver_assignment, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
