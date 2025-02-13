# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types import ListUserRolesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserRoles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        user_role = client.user_roles.list()
        assert_matches_type(ListUserRolesResponse, user_role, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        user_role = client.user_roles.list(
            after="after",
            limit=1,
        )
        assert_matches_type(ListUserRolesResponse, user_role, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.user_roles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_role = response.parse()
        assert_matches_type(ListUserRolesResponse, user_role, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.user_roles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_role = response.parse()
            assert_matches_type(ListUserRolesResponse, user_role, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUserRoles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        user_role = await async_client.user_roles.list()
        assert_matches_type(ListUserRolesResponse, user_role, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        user_role = await async_client.user_roles.list(
            after="after",
            limit=1,
        )
        assert_matches_type(ListUserRolesResponse, user_role, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.user_roles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_role = await response.parse()
        assert_matches_type(ListUserRolesResponse, user_role, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.user_roles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_role = await response.parse()
            assert_matches_type(ListUserRolesResponse, user_role, path=["response"])

        assert cast(Any, response.is_closed) is True
