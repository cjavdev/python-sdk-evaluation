# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types import (
    Attribute,
    AttributeListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAttributes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        attribute = client.attributes.create(
            attribute_type="string",
            attribute_value_quantity="single",
            entity_type="driver",
            name="License Certifications",
        )
        assert_matches_type(Attribute, attribute, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Samsara) -> None:
        attribute = client.attributes.create(
            attribute_type="string",
            attribute_value_quantity="single",
            entity_type="driver",
            name="License Certifications",
            entities=[
                {
                    "entity_id": "entityId",
                    "external_ids": {
                        "maintenanceId": "250020",
                        "payrollId": "ABFS18600",
                    },
                    "number_values": [0],
                    "string_values": ["string"],
                }
            ],
            number_values=[0],
            string_values=["string"],
        )
        assert_matches_type(Attribute, attribute, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.attributes.with_raw_response.create(
            attribute_type="string",
            attribute_value_quantity="single",
            entity_type="driver",
            name="License Certifications",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(Attribute, attribute, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.attributes.with_streaming_response.create(
            attribute_type="string",
            attribute_value_quantity="single",
            entity_type="driver",
            name="License Certifications",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(Attribute, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Samsara) -> None:
        attribute = client.attributes.retrieve(
            id="id",
            entity_type="driver",
        )
        assert_matches_type(Attribute, attribute, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Samsara) -> None:
        response = client.attributes.with_raw_response.retrieve(
            id="id",
            entity_type="driver",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(Attribute, attribute, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Samsara) -> None:
        with client.attributes.with_streaming_response.retrieve(
            id="id",
            entity_type="driver",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(Attribute, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.attributes.with_raw_response.retrieve(
                id="",
                entity_type="driver",
            )

    @parametrize
    def test_method_update(self, client: Samsara) -> None:
        attribute = client.attributes.update(
            id="id",
            entity_type="driver",
        )
        assert_matches_type(Attribute, attribute, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Samsara) -> None:
        attribute = client.attributes.update(
            id="id",
            entity_type="driver",
            attribute_type="string",
            attribute_value_quantity="single",
            entities=[
                {
                    "entity_id": "entityId",
                    "external_ids": {
                        "maintenanceId": "250020",
                        "payrollId": "ABFS18600",
                    },
                    "number_values": [0],
                    "string_values": ["string"],
                }
            ],
            name="License Certifications",
            number_values=[0],
            string_values=["string"],
        )
        assert_matches_type(Attribute, attribute, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Samsara) -> None:
        response = client.attributes.with_raw_response.update(
            id="id",
            entity_type="driver",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(Attribute, attribute, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Samsara) -> None:
        with client.attributes.with_streaming_response.update(
            id="id",
            entity_type="driver",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(Attribute, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.attributes.with_raw_response.update(
                id="",
                entity_type="driver",
            )

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        attribute = client.attributes.list(
            entity_type="driver",
        )
        assert_matches_type(AttributeListResponse, attribute, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        attribute = client.attributes.list(
            entity_type="driver",
            after="after",
            limit=1,
        )
        assert_matches_type(AttributeListResponse, attribute, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.attributes.with_raw_response.list(
            entity_type="driver",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeListResponse, attribute, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.attributes.with_streaming_response.list(
            entity_type="driver",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeListResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Samsara) -> None:
        attribute = client.attributes.delete(
            id="id",
            entity_type="driver",
        )
        assert_matches_type(str, attribute, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Samsara) -> None:
        response = client.attributes.with_raw_response.delete(
            id="id",
            entity_type="driver",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(str, attribute, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Samsara) -> None:
        with client.attributes.with_streaming_response.delete(
            id="id",
            entity_type="driver",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(str, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.attributes.with_raw_response.delete(
                id="",
                entity_type="driver",
            )


class TestAsyncAttributes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        attribute = await async_client.attributes.create(
            attribute_type="string",
            attribute_value_quantity="single",
            entity_type="driver",
            name="License Certifications",
        )
        assert_matches_type(Attribute, attribute, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSamsara) -> None:
        attribute = await async_client.attributes.create(
            attribute_type="string",
            attribute_value_quantity="single",
            entity_type="driver",
            name="License Certifications",
            entities=[
                {
                    "entity_id": "entityId",
                    "external_ids": {
                        "maintenanceId": "250020",
                        "payrollId": "ABFS18600",
                    },
                    "number_values": [0],
                    "string_values": ["string"],
                }
            ],
            number_values=[0],
            string_values=["string"],
        )
        assert_matches_type(Attribute, attribute, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.attributes.with_raw_response.create(
            attribute_type="string",
            attribute_value_quantity="single",
            entity_type="driver",
            name="License Certifications",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(Attribute, attribute, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.attributes.with_streaming_response.create(
            attribute_type="string",
            attribute_value_quantity="single",
            entity_type="driver",
            name="License Certifications",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(Attribute, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSamsara) -> None:
        attribute = await async_client.attributes.retrieve(
            id="id",
            entity_type="driver",
        )
        assert_matches_type(Attribute, attribute, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSamsara) -> None:
        response = await async_client.attributes.with_raw_response.retrieve(
            id="id",
            entity_type="driver",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(Attribute, attribute, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSamsara) -> None:
        async with async_client.attributes.with_streaming_response.retrieve(
            id="id",
            entity_type="driver",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(Attribute, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.attributes.with_raw_response.retrieve(
                id="",
                entity_type="driver",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSamsara) -> None:
        attribute = await async_client.attributes.update(
            id="id",
            entity_type="driver",
        )
        assert_matches_type(Attribute, attribute, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSamsara) -> None:
        attribute = await async_client.attributes.update(
            id="id",
            entity_type="driver",
            attribute_type="string",
            attribute_value_quantity="single",
            entities=[
                {
                    "entity_id": "entityId",
                    "external_ids": {
                        "maintenanceId": "250020",
                        "payrollId": "ABFS18600",
                    },
                    "number_values": [0],
                    "string_values": ["string"],
                }
            ],
            name="License Certifications",
            number_values=[0],
            string_values=["string"],
        )
        assert_matches_type(Attribute, attribute, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSamsara) -> None:
        response = await async_client.attributes.with_raw_response.update(
            id="id",
            entity_type="driver",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(Attribute, attribute, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSamsara) -> None:
        async with async_client.attributes.with_streaming_response.update(
            id="id",
            entity_type="driver",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(Attribute, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.attributes.with_raw_response.update(
                id="",
                entity_type="driver",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        attribute = await async_client.attributes.list(
            entity_type="driver",
        )
        assert_matches_type(AttributeListResponse, attribute, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        attribute = await async_client.attributes.list(
            entity_type="driver",
            after="after",
            limit=1,
        )
        assert_matches_type(AttributeListResponse, attribute, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.attributes.with_raw_response.list(
            entity_type="driver",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeListResponse, attribute, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.attributes.with_streaming_response.list(
            entity_type="driver",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeListResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSamsara) -> None:
        attribute = await async_client.attributes.delete(
            id="id",
            entity_type="driver",
        )
        assert_matches_type(str, attribute, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSamsara) -> None:
        response = await async_client.attributes.with_raw_response.delete(
            id="id",
            entity_type="driver",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(str, attribute, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSamsara) -> None:
        async with async_client.attributes.with_streaming_response.delete(
            id="id",
            entity_type="driver",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(str, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.attributes.with_raw_response.delete(
                id="",
                entity_type="driver",
            )
