# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types import DefectTypeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDefectTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        defect_type = client.defect_types.list()
        assert_matches_type(DefectTypeListResponse, defect_type, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        defect_type = client.defect_types.list(
            after="after",
            ids=["string"],
            limit=1,
        )
        assert_matches_type(DefectTypeListResponse, defect_type, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.defect_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        defect_type = response.parse()
        assert_matches_type(DefectTypeListResponse, defect_type, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.defect_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            defect_type = response.parse()
            assert_matches_type(DefectTypeListResponse, defect_type, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDefectTypes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        defect_type = await async_client.defect_types.list()
        assert_matches_type(DefectTypeListResponse, defect_type, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        defect_type = await async_client.defect_types.list(
            after="after",
            ids=["string"],
            limit=1,
        )
        assert_matches_type(DefectTypeListResponse, defect_type, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.defect_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        defect_type = await response.parse()
        assert_matches_type(DefectTypeListResponse, defect_type, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.defect_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            defect_type = await response.parse()
            assert_matches_type(DefectTypeListResponse, defect_type, path=["response"])

        assert cast(Any, response.is_closed) is True
