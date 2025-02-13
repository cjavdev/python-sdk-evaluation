# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types import (
    IftaGetIftaDetailJobResponseBody,
    IftaCreateIftaDetailJobResponseBody,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIftaDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_csv_job(self, client: Samsara) -> None:
        ifta_detail = client.ifta_details.create_csv_job(
            end_hour="2019-06-13T19:00:00Z",
            start_hour="2019-06-13T19:00:00Z",
        )
        assert_matches_type(IftaCreateIftaDetailJobResponseBody, ifta_detail, path=["response"])

    @parametrize
    def test_method_create_csv_job_with_all_params(self, client: Samsara) -> None:
        ifta_detail = client.ifta_details.create_csv_job(
            end_hour="2019-06-13T19:00:00Z",
            start_hour="2019-06-13T19:00:00Z",
            vehicle_ids="1234,5678,samsara.vin:1HGBH41JXMN109186",
            vehicle_parent_tag_ids="1234,5678",
            vehicle_tag_ids="1234,5678",
        )
        assert_matches_type(IftaCreateIftaDetailJobResponseBody, ifta_detail, path=["response"])

    @parametrize
    def test_raw_response_create_csv_job(self, client: Samsara) -> None:
        response = client.ifta_details.with_raw_response.create_csv_job(
            end_hour="2019-06-13T19:00:00Z",
            start_hour="2019-06-13T19:00:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ifta_detail = response.parse()
        assert_matches_type(IftaCreateIftaDetailJobResponseBody, ifta_detail, path=["response"])

    @parametrize
    def test_streaming_response_create_csv_job(self, client: Samsara) -> None:
        with client.ifta_details.with_streaming_response.create_csv_job(
            end_hour="2019-06-13T19:00:00Z",
            start_hour="2019-06-13T19:00:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ifta_detail = response.parse()
            assert_matches_type(IftaCreateIftaDetailJobResponseBody, ifta_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_csv_job(self, client: Samsara) -> None:
        ifta_detail = client.ifta_details.retrieve_csv_job(
            "id",
        )
        assert_matches_type(IftaGetIftaDetailJobResponseBody, ifta_detail, path=["response"])

    @parametrize
    def test_raw_response_retrieve_csv_job(self, client: Samsara) -> None:
        response = client.ifta_details.with_raw_response.retrieve_csv_job(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ifta_detail = response.parse()
        assert_matches_type(IftaGetIftaDetailJobResponseBody, ifta_detail, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_csv_job(self, client: Samsara) -> None:
        with client.ifta_details.with_streaming_response.retrieve_csv_job(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ifta_detail = response.parse()
            assert_matches_type(IftaGetIftaDetailJobResponseBody, ifta_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_csv_job(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ifta_details.with_raw_response.retrieve_csv_job(
                "",
            )


class TestAsyncIftaDetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_csv_job(self, async_client: AsyncSamsara) -> None:
        ifta_detail = await async_client.ifta_details.create_csv_job(
            end_hour="2019-06-13T19:00:00Z",
            start_hour="2019-06-13T19:00:00Z",
        )
        assert_matches_type(IftaCreateIftaDetailJobResponseBody, ifta_detail, path=["response"])

    @parametrize
    async def test_method_create_csv_job_with_all_params(self, async_client: AsyncSamsara) -> None:
        ifta_detail = await async_client.ifta_details.create_csv_job(
            end_hour="2019-06-13T19:00:00Z",
            start_hour="2019-06-13T19:00:00Z",
            vehicle_ids="1234,5678,samsara.vin:1HGBH41JXMN109186",
            vehicle_parent_tag_ids="1234,5678",
            vehicle_tag_ids="1234,5678",
        )
        assert_matches_type(IftaCreateIftaDetailJobResponseBody, ifta_detail, path=["response"])

    @parametrize
    async def test_raw_response_create_csv_job(self, async_client: AsyncSamsara) -> None:
        response = await async_client.ifta_details.with_raw_response.create_csv_job(
            end_hour="2019-06-13T19:00:00Z",
            start_hour="2019-06-13T19:00:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ifta_detail = await response.parse()
        assert_matches_type(IftaCreateIftaDetailJobResponseBody, ifta_detail, path=["response"])

    @parametrize
    async def test_streaming_response_create_csv_job(self, async_client: AsyncSamsara) -> None:
        async with async_client.ifta_details.with_streaming_response.create_csv_job(
            end_hour="2019-06-13T19:00:00Z",
            start_hour="2019-06-13T19:00:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ifta_detail = await response.parse()
            assert_matches_type(IftaCreateIftaDetailJobResponseBody, ifta_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_csv_job(self, async_client: AsyncSamsara) -> None:
        ifta_detail = await async_client.ifta_details.retrieve_csv_job(
            "id",
        )
        assert_matches_type(IftaGetIftaDetailJobResponseBody, ifta_detail, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_csv_job(self, async_client: AsyncSamsara) -> None:
        response = await async_client.ifta_details.with_raw_response.retrieve_csv_job(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ifta_detail = await response.parse()
        assert_matches_type(IftaGetIftaDetailJobResponseBody, ifta_detail, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_csv_job(self, async_client: AsyncSamsara) -> None:
        async with async_client.ifta_details.with_streaming_response.retrieve_csv_job(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ifta_detail = await response.parse()
            assert_matches_type(IftaGetIftaDetailJobResponseBody, ifta_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_csv_job(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ifta_details.with_raw_response.retrieve_csv_job(
                "",
            )
