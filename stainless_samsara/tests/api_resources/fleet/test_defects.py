# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet import DefectUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDefects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Samsara) -> None:
        defect = client.fleet.defects.update(
            id="id",
        )
        assert_matches_type(DefectUpdateResponse, defect, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Samsara) -> None:
        defect = client.fleet.defects.update(
            id="id",
            is_resolved=True,
            mechanic_notes="Extremely large oddly shaped hole in passenger side window.",
            resolved_at_time="2020-01-27T07:06:25Z",
            resolved_by={
                "id": "11",
                "type": "mechanic",
            },
        )
        assert_matches_type(DefectUpdateResponse, defect, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Samsara) -> None:
        response = client.fleet.defects.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        defect = response.parse()
        assert_matches_type(DefectUpdateResponse, defect, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Samsara) -> None:
        with client.fleet.defects.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            defect = response.parse()
            assert_matches_type(DefectUpdateResponse, defect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.fleet.defects.with_raw_response.update(
                id="",
            )


class TestAsyncDefects:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncSamsara) -> None:
        defect = await async_client.fleet.defects.update(
            id="id",
        )
        assert_matches_type(DefectUpdateResponse, defect, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSamsara) -> None:
        defect = await async_client.fleet.defects.update(
            id="id",
            is_resolved=True,
            mechanic_notes="Extremely large oddly shaped hole in passenger side window.",
            resolved_at_time="2020-01-27T07:06:25Z",
            resolved_by={
                "id": "11",
                "type": "mechanic",
            },
        )
        assert_matches_type(DefectUpdateResponse, defect, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.defects.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        defect = await response.parse()
        assert_matches_type(DefectUpdateResponse, defect, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.defects.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            defect = await response.parse()
            assert_matches_type(DefectUpdateResponse, defect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.fleet.defects.with_raw_response.update(
                id="",
            )
