# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types import (
    Address,
    AddressListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAddresses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        address = client.addresses.create(
            formatted_address="350 Rhode Island St, San Francisco, CA",
            geofence={},
            name="Samsara HQ",
        )
        assert_matches_type(Address, address, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Samsara) -> None:
        address = client.addresses.create(
            formatted_address="350 Rhode Island St, San Francisco, CA",
            geofence={
                "circle": {
                    "radius_meters": 25,
                    "latitude": 37.765363,
                    "longitude": -122.4029238,
                },
                "polygon": {
                    "vertices": [
                        {
                            "latitude": 37.765363,
                            "longitude": -122.403098,
                        },
                        {
                            "latitude": 38.765363,
                            "longitude": -122.403098,
                        },
                        {
                            "latitude": 37.765363,
                            "longitude": -123.403098,
                        },
                    ]
                },
                "settings": {"show_addresses": True},
            },
            name="Samsara HQ",
            address_types=["yard"],
            contact_ids=["22408"],
            external_ids={
                "maintenanceId": "250020",
                "payrollId": "ABFS18600",
            },
            latitude=37.765363,
            longitude=-122.4029238,
            notes="Hours of operation: 8am - 6pm; Truck entrance on the Rhode Island street side.",
            tag_ids=["3914"],
        )
        assert_matches_type(Address, address, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.addresses.with_raw_response.create(
            formatted_address="350 Rhode Island St, San Francisco, CA",
            geofence={},
            name="Samsara HQ",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = response.parse()
        assert_matches_type(Address, address, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.addresses.with_streaming_response.create(
            formatted_address="350 Rhode Island St, San Francisco, CA",
            geofence={},
            name="Samsara HQ",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = response.parse()
            assert_matches_type(Address, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Samsara) -> None:
        address = client.addresses.retrieve(
            "id",
        )
        assert_matches_type(Address, address, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Samsara) -> None:
        response = client.addresses.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = response.parse()
        assert_matches_type(Address, address, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Samsara) -> None:
        with client.addresses.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = response.parse()
            assert_matches_type(Address, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.addresses.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        address = client.addresses.list()
        assert_matches_type(AddressListResponse, address, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        address = client.addresses.list(
            after="after",
            created_after_time="createdAfterTime",
            limit=1,
            parent_tag_ids=["string"],
            tag_ids=["string"],
        )
        assert_matches_type(AddressListResponse, address, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.addresses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = response.parse()
        assert_matches_type(AddressListResponse, address, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.addresses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = response.parse()
            assert_matches_type(AddressListResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Samsara) -> None:
        address = client.addresses.delete(
            "id",
        )
        assert_matches_type(str, address, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Samsara) -> None:
        response = client.addresses.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = response.parse()
        assert_matches_type(str, address, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Samsara) -> None:
        with client.addresses.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = response.parse()
            assert_matches_type(str, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.addresses.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_modify(self, client: Samsara) -> None:
        address = client.addresses.modify(
            id="id",
        )
        assert_matches_type(Address, address, path=["response"])

    @parametrize
    def test_method_modify_with_all_params(self, client: Samsara) -> None:
        address = client.addresses.modify(
            id="id",
            address_types=["yard"],
            contact_ids=["22408"],
            external_ids={
                "maintenanceId": "250020",
                "payrollId": "ABFS18600",
            },
            formatted_address="350 Rhode Island St, San Francisco, CA",
            geofence={
                "circle": {
                    "radius_meters": 25,
                    "latitude": 37.765363,
                    "longitude": -122.4029238,
                },
                "polygon": {
                    "vertices": [
                        {
                            "latitude": 37.765363,
                            "longitude": -122.403098,
                        },
                        {
                            "latitude": 38.765363,
                            "longitude": -122.403098,
                        },
                        {
                            "latitude": 37.765363,
                            "longitude": -123.403098,
                        },
                    ]
                },
                "settings": {"show_addresses": False},
            },
            latitude=37.765363,
            longitude=-122.4029238,
            name="Samsara HQ",
            notes="Hours of operation: 8am - 6pm; Truck entrance on the Rhode Island street side.",
            tag_ids=["3914"],
        )
        assert_matches_type(Address, address, path=["response"])

    @parametrize
    def test_raw_response_modify(self, client: Samsara) -> None:
        response = client.addresses.with_raw_response.modify(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = response.parse()
        assert_matches_type(Address, address, path=["response"])

    @parametrize
    def test_streaming_response_modify(self, client: Samsara) -> None:
        with client.addresses.with_streaming_response.modify(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = response.parse()
            assert_matches_type(Address, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_modify(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.addresses.with_raw_response.modify(
                id="",
            )


class TestAsyncAddresses:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        address = await async_client.addresses.create(
            formatted_address="350 Rhode Island St, San Francisco, CA",
            geofence={},
            name="Samsara HQ",
        )
        assert_matches_type(Address, address, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSamsara) -> None:
        address = await async_client.addresses.create(
            formatted_address="350 Rhode Island St, San Francisco, CA",
            geofence={
                "circle": {
                    "radius_meters": 25,
                    "latitude": 37.765363,
                    "longitude": -122.4029238,
                },
                "polygon": {
                    "vertices": [
                        {
                            "latitude": 37.765363,
                            "longitude": -122.403098,
                        },
                        {
                            "latitude": 38.765363,
                            "longitude": -122.403098,
                        },
                        {
                            "latitude": 37.765363,
                            "longitude": -123.403098,
                        },
                    ]
                },
                "settings": {"show_addresses": True},
            },
            name="Samsara HQ",
            address_types=["yard"],
            contact_ids=["22408"],
            external_ids={
                "maintenanceId": "250020",
                "payrollId": "ABFS18600",
            },
            latitude=37.765363,
            longitude=-122.4029238,
            notes="Hours of operation: 8am - 6pm; Truck entrance on the Rhode Island street side.",
            tag_ids=["3914"],
        )
        assert_matches_type(Address, address, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.addresses.with_raw_response.create(
            formatted_address="350 Rhode Island St, San Francisco, CA",
            geofence={},
            name="Samsara HQ",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = await response.parse()
        assert_matches_type(Address, address, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.addresses.with_streaming_response.create(
            formatted_address="350 Rhode Island St, San Francisco, CA",
            geofence={},
            name="Samsara HQ",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = await response.parse()
            assert_matches_type(Address, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSamsara) -> None:
        address = await async_client.addresses.retrieve(
            "id",
        )
        assert_matches_type(Address, address, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSamsara) -> None:
        response = await async_client.addresses.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = await response.parse()
        assert_matches_type(Address, address, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSamsara) -> None:
        async with async_client.addresses.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = await response.parse()
            assert_matches_type(Address, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.addresses.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        address = await async_client.addresses.list()
        assert_matches_type(AddressListResponse, address, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        address = await async_client.addresses.list(
            after="after",
            created_after_time="createdAfterTime",
            limit=1,
            parent_tag_ids=["string"],
            tag_ids=["string"],
        )
        assert_matches_type(AddressListResponse, address, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.addresses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = await response.parse()
        assert_matches_type(AddressListResponse, address, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.addresses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = await response.parse()
            assert_matches_type(AddressListResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSamsara) -> None:
        address = await async_client.addresses.delete(
            "id",
        )
        assert_matches_type(str, address, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSamsara) -> None:
        response = await async_client.addresses.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = await response.parse()
        assert_matches_type(str, address, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSamsara) -> None:
        async with async_client.addresses.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = await response.parse()
            assert_matches_type(str, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.addresses.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_modify(self, async_client: AsyncSamsara) -> None:
        address = await async_client.addresses.modify(
            id="id",
        )
        assert_matches_type(Address, address, path=["response"])

    @parametrize
    async def test_method_modify_with_all_params(self, async_client: AsyncSamsara) -> None:
        address = await async_client.addresses.modify(
            id="id",
            address_types=["yard"],
            contact_ids=["22408"],
            external_ids={
                "maintenanceId": "250020",
                "payrollId": "ABFS18600",
            },
            formatted_address="350 Rhode Island St, San Francisco, CA",
            geofence={
                "circle": {
                    "radius_meters": 25,
                    "latitude": 37.765363,
                    "longitude": -122.4029238,
                },
                "polygon": {
                    "vertices": [
                        {
                            "latitude": 37.765363,
                            "longitude": -122.403098,
                        },
                        {
                            "latitude": 38.765363,
                            "longitude": -122.403098,
                        },
                        {
                            "latitude": 37.765363,
                            "longitude": -123.403098,
                        },
                    ]
                },
                "settings": {"show_addresses": False},
            },
            latitude=37.765363,
            longitude=-122.4029238,
            name="Samsara HQ",
            notes="Hours of operation: 8am - 6pm; Truck entrance on the Rhode Island street side.",
            tag_ids=["3914"],
        )
        assert_matches_type(Address, address, path=["response"])

    @parametrize
    async def test_raw_response_modify(self, async_client: AsyncSamsara) -> None:
        response = await async_client.addresses.with_raw_response.modify(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = await response.parse()
        assert_matches_type(Address, address, path=["response"])

    @parametrize
    async def test_streaming_response_modify(self, async_client: AsyncSamsara) -> None:
        async with async_client.addresses.with_streaming_response.modify(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = await response.parse()
            assert_matches_type(Address, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_modify(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.addresses.with_raw_response.modify(
                id="",
            )
