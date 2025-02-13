# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.beta.fleet import EquipmentUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEquipment:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Samsara) -> None:
        equipment = client.beta.fleet.equipment.update(
            path_id="id",
        )
        assert_matches_type(EquipmentUpdateResponse, equipment, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Samsara) -> None:
        equipment = client.beta.fleet.equipment.update(
            path_id="id",
            body_id="494123",
            attributes=[
                {
                    "id": "494123",
                    "name": "Compliance/ELD",
                    "number_values": [867, 5309],
                    "string_values": ["HQ", "Leased"],
                }
            ],
            engine_hours=1234,
            equipment_serial_number="8V8WD530FLN016251",
            external_ids={"foo": "string"},
            name="Equipment-123",
            notes="These are my equipment notes",
            odometer_meters=1234,
            tag_ids=["Porro dolor provident consequatur est.", "Aperiam consequatur laborum magnam illum a veniam."],
        )
        assert_matches_type(EquipmentUpdateResponse, equipment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Samsara) -> None:
        response = client.beta.fleet.equipment.with_raw_response.update(
            path_id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = response.parse()
        assert_matches_type(EquipmentUpdateResponse, equipment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Samsara) -> None:
        with client.beta.fleet.equipment.with_streaming_response.update(
            path_id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = response.parse()
            assert_matches_type(EquipmentUpdateResponse, equipment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.beta.fleet.equipment.with_raw_response.update(
                path_id="",
                body_id="",
            )


class TestAsyncEquipment:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncSamsara) -> None:
        equipment = await async_client.beta.fleet.equipment.update(
            path_id="id",
        )
        assert_matches_type(EquipmentUpdateResponse, equipment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSamsara) -> None:
        equipment = await async_client.beta.fleet.equipment.update(
            path_id="id",
            body_id="494123",
            attributes=[
                {
                    "id": "494123",
                    "name": "Compliance/ELD",
                    "number_values": [867, 5309],
                    "string_values": ["HQ", "Leased"],
                }
            ],
            engine_hours=1234,
            equipment_serial_number="8V8WD530FLN016251",
            external_ids={"foo": "string"},
            name="Equipment-123",
            notes="These are my equipment notes",
            odometer_meters=1234,
            tag_ids=["Porro dolor provident consequatur est.", "Aperiam consequatur laborum magnam illum a veniam."],
        )
        assert_matches_type(EquipmentUpdateResponse, equipment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSamsara) -> None:
        response = await async_client.beta.fleet.equipment.with_raw_response.update(
            path_id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment = await response.parse()
        assert_matches_type(EquipmentUpdateResponse, equipment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSamsara) -> None:
        async with async_client.beta.fleet.equipment.with_streaming_response.update(
            path_id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment = await response.parse()
            assert_matches_type(EquipmentUpdateResponse, equipment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.beta.fleet.equipment.with_raw_response.update(
                path_id="",
                body_id="",
            )
