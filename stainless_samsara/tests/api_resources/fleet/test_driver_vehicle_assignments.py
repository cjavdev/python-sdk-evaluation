# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet import (
    DriverVehicleAssignmentListResponse,
    DriverVehicleAssignmentCreateResponse,
    DriverVehicleAssignmentUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDriverVehicleAssignments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        driver_vehicle_assignment = client.fleet.driver_vehicle_assignments.create(
            driver_id="494123",
            vehicle_id="281474978683353",
        )
        assert_matches_type(DriverVehicleAssignmentCreateResponse, driver_vehicle_assignment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Samsara) -> None:
        driver_vehicle_assignment = client.fleet.driver_vehicle_assignments.create(
            driver_id="494123",
            vehicle_id="281474978683353",
            assigned_at_time="2019-06-13T19:08:25Z",
            end_time="2019-06-13T19:08:25Z",
            is_passenger=True,
            metadata={"source_name": "My custom assignment source"},
            start_time="2019-06-13T19:08:25Z",
        )
        assert_matches_type(DriverVehicleAssignmentCreateResponse, driver_vehicle_assignment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.fleet.driver_vehicle_assignments.with_raw_response.create(
            driver_id="494123",
            vehicle_id="281474978683353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_vehicle_assignment = response.parse()
        assert_matches_type(DriverVehicleAssignmentCreateResponse, driver_vehicle_assignment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.fleet.driver_vehicle_assignments.with_streaming_response.create(
            driver_id="494123",
            vehicle_id="281474978683353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_vehicle_assignment = response.parse()
            assert_matches_type(DriverVehicleAssignmentCreateResponse, driver_vehicle_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Samsara) -> None:
        driver_vehicle_assignment = client.fleet.driver_vehicle_assignments.update(
            driver_id="494123",
            start_time="2019-06-13T19:08:25Z",
            vehicle_id="281474978683353",
        )
        assert_matches_type(DriverVehicleAssignmentUpdateResponse, driver_vehicle_assignment, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Samsara) -> None:
        driver_vehicle_assignment = client.fleet.driver_vehicle_assignments.update(
            driver_id="494123",
            start_time="2019-06-13T19:08:25Z",
            vehicle_id="281474978683353",
            assigned_at_time="2019-06-13T19:08:25Z",
            end_time="2019-06-13T19:08:25Z",
            is_passenger=True,
            metadata={"source_name": "My custom assignment source"},
        )
        assert_matches_type(DriverVehicleAssignmentUpdateResponse, driver_vehicle_assignment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Samsara) -> None:
        response = client.fleet.driver_vehicle_assignments.with_raw_response.update(
            driver_id="494123",
            start_time="2019-06-13T19:08:25Z",
            vehicle_id="281474978683353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_vehicle_assignment = response.parse()
        assert_matches_type(DriverVehicleAssignmentUpdateResponse, driver_vehicle_assignment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Samsara) -> None:
        with client.fleet.driver_vehicle_assignments.with_streaming_response.update(
            driver_id="494123",
            start_time="2019-06-13T19:08:25Z",
            vehicle_id="281474978683353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_vehicle_assignment = response.parse()
            assert_matches_type(DriverVehicleAssignmentUpdateResponse, driver_vehicle_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        driver_vehicle_assignment = client.fleet.driver_vehicle_assignments.list(
            filter_by="drivers",
        )
        assert_matches_type(DriverVehicleAssignmentListResponse, driver_vehicle_assignment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        driver_vehicle_assignment = client.fleet.driver_vehicle_assignments.list(
            filter_by="drivers",
            after="after",
            assignment_type="HOS",
            driver_ids=["string"],
            driver_tag_ids="driverTagIds",
            end_time="endTime",
            start_time="startTime",
            vehicle_ids=["string"],
            vehicle_tag_ids="vehicleTagIds",
        )
        assert_matches_type(DriverVehicleAssignmentListResponse, driver_vehicle_assignment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.fleet.driver_vehicle_assignments.with_raw_response.list(
            filter_by="drivers",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_vehicle_assignment = response.parse()
        assert_matches_type(DriverVehicleAssignmentListResponse, driver_vehicle_assignment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.fleet.driver_vehicle_assignments.with_streaming_response.list(
            filter_by="drivers",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_vehicle_assignment = response.parse()
            assert_matches_type(DriverVehicleAssignmentListResponse, driver_vehicle_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Samsara) -> None:
        driver_vehicle_assignment = client.fleet.driver_vehicle_assignments.delete(
            vehicle_id="281474978683353",
        )
        assert driver_vehicle_assignment is None

    @parametrize
    def test_method_delete_with_all_params(self, client: Samsara) -> None:
        driver_vehicle_assignment = client.fleet.driver_vehicle_assignments.delete(
            vehicle_id="281474978683353",
            assigned_at_time="2019-06-13T19:08:25Z",
            end_time="2019-06-13T19:08:25Z",
            is_passenger=True,
            start_time="2019-06-13T19:08:25Z",
        )
        assert driver_vehicle_assignment is None

    @parametrize
    def test_raw_response_delete(self, client: Samsara) -> None:
        response = client.fleet.driver_vehicle_assignments.with_raw_response.delete(
            vehicle_id="281474978683353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_vehicle_assignment = response.parse()
        assert driver_vehicle_assignment is None

    @parametrize
    def test_streaming_response_delete(self, client: Samsara) -> None:
        with client.fleet.driver_vehicle_assignments.with_streaming_response.delete(
            vehicle_id="281474978683353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_vehicle_assignment = response.parse()
            assert driver_vehicle_assignment is None

        assert cast(Any, response.is_closed) is True


class TestAsyncDriverVehicleAssignments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        driver_vehicle_assignment = await async_client.fleet.driver_vehicle_assignments.create(
            driver_id="494123",
            vehicle_id="281474978683353",
        )
        assert_matches_type(DriverVehicleAssignmentCreateResponse, driver_vehicle_assignment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSamsara) -> None:
        driver_vehicle_assignment = await async_client.fleet.driver_vehicle_assignments.create(
            driver_id="494123",
            vehicle_id="281474978683353",
            assigned_at_time="2019-06-13T19:08:25Z",
            end_time="2019-06-13T19:08:25Z",
            is_passenger=True,
            metadata={"source_name": "My custom assignment source"},
            start_time="2019-06-13T19:08:25Z",
        )
        assert_matches_type(DriverVehicleAssignmentCreateResponse, driver_vehicle_assignment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.driver_vehicle_assignments.with_raw_response.create(
            driver_id="494123",
            vehicle_id="281474978683353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_vehicle_assignment = await response.parse()
        assert_matches_type(DriverVehicleAssignmentCreateResponse, driver_vehicle_assignment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.driver_vehicle_assignments.with_streaming_response.create(
            driver_id="494123",
            vehicle_id="281474978683353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_vehicle_assignment = await response.parse()
            assert_matches_type(DriverVehicleAssignmentCreateResponse, driver_vehicle_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncSamsara) -> None:
        driver_vehicle_assignment = await async_client.fleet.driver_vehicle_assignments.update(
            driver_id="494123",
            start_time="2019-06-13T19:08:25Z",
            vehicle_id="281474978683353",
        )
        assert_matches_type(DriverVehicleAssignmentUpdateResponse, driver_vehicle_assignment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSamsara) -> None:
        driver_vehicle_assignment = await async_client.fleet.driver_vehicle_assignments.update(
            driver_id="494123",
            start_time="2019-06-13T19:08:25Z",
            vehicle_id="281474978683353",
            assigned_at_time="2019-06-13T19:08:25Z",
            end_time="2019-06-13T19:08:25Z",
            is_passenger=True,
            metadata={"source_name": "My custom assignment source"},
        )
        assert_matches_type(DriverVehicleAssignmentUpdateResponse, driver_vehicle_assignment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.driver_vehicle_assignments.with_raw_response.update(
            driver_id="494123",
            start_time="2019-06-13T19:08:25Z",
            vehicle_id="281474978683353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_vehicle_assignment = await response.parse()
        assert_matches_type(DriverVehicleAssignmentUpdateResponse, driver_vehicle_assignment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.driver_vehicle_assignments.with_streaming_response.update(
            driver_id="494123",
            start_time="2019-06-13T19:08:25Z",
            vehicle_id="281474978683353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_vehicle_assignment = await response.parse()
            assert_matches_type(DriverVehicleAssignmentUpdateResponse, driver_vehicle_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        driver_vehicle_assignment = await async_client.fleet.driver_vehicle_assignments.list(
            filter_by="drivers",
        )
        assert_matches_type(DriverVehicleAssignmentListResponse, driver_vehicle_assignment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        driver_vehicle_assignment = await async_client.fleet.driver_vehicle_assignments.list(
            filter_by="drivers",
            after="after",
            assignment_type="HOS",
            driver_ids=["string"],
            driver_tag_ids="driverTagIds",
            end_time="endTime",
            start_time="startTime",
            vehicle_ids=["string"],
            vehicle_tag_ids="vehicleTagIds",
        )
        assert_matches_type(DriverVehicleAssignmentListResponse, driver_vehicle_assignment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.driver_vehicle_assignments.with_raw_response.list(
            filter_by="drivers",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_vehicle_assignment = await response.parse()
        assert_matches_type(DriverVehicleAssignmentListResponse, driver_vehicle_assignment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.driver_vehicle_assignments.with_streaming_response.list(
            filter_by="drivers",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_vehicle_assignment = await response.parse()
            assert_matches_type(DriverVehicleAssignmentListResponse, driver_vehicle_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSamsara) -> None:
        driver_vehicle_assignment = await async_client.fleet.driver_vehicle_assignments.delete(
            vehicle_id="281474978683353",
        )
        assert driver_vehicle_assignment is None

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncSamsara) -> None:
        driver_vehicle_assignment = await async_client.fleet.driver_vehicle_assignments.delete(
            vehicle_id="281474978683353",
            assigned_at_time="2019-06-13T19:08:25Z",
            end_time="2019-06-13T19:08:25Z",
            is_passenger=True,
            start_time="2019-06-13T19:08:25Z",
        )
        assert driver_vehicle_assignment is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.driver_vehicle_assignments.with_raw_response.delete(
            vehicle_id="281474978683353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        driver_vehicle_assignment = await response.parse()
        assert driver_vehicle_assignment is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.driver_vehicle_assignments.with_streaming_response.delete(
            vehicle_id="281474978683353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            driver_vehicle_assignment = await response.parse()
            assert driver_vehicle_assignment is None

        assert cast(Any, response.is_closed) is True
