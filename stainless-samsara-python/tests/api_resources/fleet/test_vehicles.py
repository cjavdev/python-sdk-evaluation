# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet import VehicleResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVehicles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Samsara) -> None:
        vehicle = client.fleet.vehicles.retrieve(
            "id",
        )
        assert_matches_type(VehicleResponse, vehicle, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Samsara) -> None:
        response = client.fleet.vehicles.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vehicle = response.parse()
        assert_matches_type(VehicleResponse, vehicle, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Samsara) -> None:
        with client.fleet.vehicles.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vehicle = response.parse()
            assert_matches_type(VehicleResponse, vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.fleet.vehicles.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Samsara) -> None:
        vehicle = client.fleet.vehicles.update(
            id="id",
        )
        assert_matches_type(VehicleResponse, vehicle, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Samsara) -> None:
        vehicle = client.fleet.vehicles.update(
            id="id",
            attributes=[
                {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "name": "License Certifications",
                    "number_values": [0],
                    "string_values": ["string"],
                }
            ],
            aux_input_type1="none",
            aux_input_type10="none",
            aux_input_type11="none",
            aux_input_type12="none",
            aux_input_type13="none",
            aux_input_type2="none",
            aux_input_type3="none",
            aux_input_type4="none",
            aux_input_type5="none",
            aux_input_type6="none",
            aux_input_type7="none",
            aux_input_type8="none",
            aux_input_type9="none",
            engine_hours=10943,
            external_ids={
                "maintenanceId": "250020",
                "payrollId": "ABFS18600",
            },
            gateway_serial="ABCD-123-XYZ",
            gross_vehicle_weight={
                "unit": "lb",
                "weight": 1000,
            },
            harsh_acceleration_setting_type="passengerCar",
            license_plate="XHK1234",
            name="Truck A7",
            notes="These are notes about this given vehicle.",
            odometer_meters=9182,
            static_assigned_driver_id="123",
            tag_ids=["321"],
            vehicle_regulation_mode="regulated",
            vehicle_type="truck",
            vin="1FUJA6BD31LJ09646",
        )
        assert_matches_type(VehicleResponse, vehicle, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Samsara) -> None:
        response = client.fleet.vehicles.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vehicle = response.parse()
        assert_matches_type(VehicleResponse, vehicle, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Samsara) -> None:
        with client.fleet.vehicles.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vehicle = response.parse()
            assert_matches_type(VehicleResponse, vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.fleet.vehicles.with_raw_response.update(
                id="",
            )


class TestAsyncVehicles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSamsara) -> None:
        vehicle = await async_client.fleet.vehicles.retrieve(
            "id",
        )
        assert_matches_type(VehicleResponse, vehicle, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.vehicles.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vehicle = await response.parse()
        assert_matches_type(VehicleResponse, vehicle, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.vehicles.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vehicle = await response.parse()
            assert_matches_type(VehicleResponse, vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.fleet.vehicles.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSamsara) -> None:
        vehicle = await async_client.fleet.vehicles.update(
            id="id",
        )
        assert_matches_type(VehicleResponse, vehicle, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSamsara) -> None:
        vehicle = await async_client.fleet.vehicles.update(
            id="id",
            attributes=[
                {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "name": "License Certifications",
                    "number_values": [0],
                    "string_values": ["string"],
                }
            ],
            aux_input_type1="none",
            aux_input_type10="none",
            aux_input_type11="none",
            aux_input_type12="none",
            aux_input_type13="none",
            aux_input_type2="none",
            aux_input_type3="none",
            aux_input_type4="none",
            aux_input_type5="none",
            aux_input_type6="none",
            aux_input_type7="none",
            aux_input_type8="none",
            aux_input_type9="none",
            engine_hours=10943,
            external_ids={
                "maintenanceId": "250020",
                "payrollId": "ABFS18600",
            },
            gateway_serial="ABCD-123-XYZ",
            gross_vehicle_weight={
                "unit": "lb",
                "weight": 1000,
            },
            harsh_acceleration_setting_type="passengerCar",
            license_plate="XHK1234",
            name="Truck A7",
            notes="These are notes about this given vehicle.",
            odometer_meters=9182,
            static_assigned_driver_id="123",
            tag_ids=["321"],
            vehicle_regulation_mode="regulated",
            vehicle_type="truck",
            vin="1FUJA6BD31LJ09646",
        )
        assert_matches_type(VehicleResponse, vehicle, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.vehicles.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vehicle = await response.parse()
        assert_matches_type(VehicleResponse, vehicle, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.vehicles.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vehicle = await response.parse()
            assert_matches_type(VehicleResponse, vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.fleet.vehicles.with_raw_response.update(
                id="",
            )
