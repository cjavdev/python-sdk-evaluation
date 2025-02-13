# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types import (
    Contact,
    ContactListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        contact = client.contacts.create()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Samsara) -> None:
        contact = client.contacts.create(
            email="jane.jones@yahoo.com",
            first_name="Jane",
            last_name="Jones",
            phone="111-222-3344",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.contacts.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.contacts.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Samsara) -> None:
        contact = client.contacts.retrieve(
            "id",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Samsara) -> None:
        response = client.contacts.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Samsara) -> None:
        with client.contacts.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.contacts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Samsara) -> None:
        contact = client.contacts.update(
            id="id",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Samsara) -> None:
        contact = client.contacts.update(
            id="id",
            email="jane.jones@yahoo.com",
            first_name="Jane",
            last_name="Jones",
            phone="111-222-3344",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Samsara) -> None:
        response = client.contacts.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Samsara) -> None:
        with client.contacts.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.contacts.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        contact = client.contacts.list()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        contact = client.contacts.list(
            after="after",
            limit=1,
        )
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.contacts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.contacts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactListResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Samsara) -> None:
        contact = client.contacts.delete(
            "id",
        )
        assert_matches_type(str, contact, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Samsara) -> None:
        response = client.contacts.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(str, contact, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Samsara) -> None:
        with client.contacts.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(str, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.contacts.with_raw_response.delete(
                "",
            )


class TestAsyncContacts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        contact = await async_client.contacts.create()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSamsara) -> None:
        contact = await async_client.contacts.create(
            email="jane.jones@yahoo.com",
            first_name="Jane",
            last_name="Jones",
            phone="111-222-3344",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.contacts.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.contacts.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSamsara) -> None:
        contact = await async_client.contacts.retrieve(
            "id",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSamsara) -> None:
        response = await async_client.contacts.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSamsara) -> None:
        async with async_client.contacts.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.contacts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSamsara) -> None:
        contact = await async_client.contacts.update(
            id="id",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSamsara) -> None:
        contact = await async_client.contacts.update(
            id="id",
            email="jane.jones@yahoo.com",
            first_name="Jane",
            last_name="Jones",
            phone="111-222-3344",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSamsara) -> None:
        response = await async_client.contacts.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSamsara) -> None:
        async with async_client.contacts.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.contacts.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        contact = await async_client.contacts.list()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        contact = await async_client.contacts.list(
            after="after",
            limit=1,
        )
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.contacts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.contacts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactListResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSamsara) -> None:
        contact = await async_client.contacts.delete(
            "id",
        )
        assert_matches_type(str, contact, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSamsara) -> None:
        response = await async_client.contacts.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(str, contact, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSamsara) -> None:
        async with async_client.contacts.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(str, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.contacts.with_raw_response.delete(
                "",
            )
