# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.preview.cameras import MediaRetrievalListUploadedMediaResponseBody

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMedia:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        media = client.preview.cameras.media.list(
            available_after_time="availableAfterTime",
            end_time="endTime",
            inputs=["dashcamRoadFacing"],
            media_types=["image"],
            start_time="startTime",
            trigger_reasons=["api"],
            vehicle_ids="vehicleIds",
        )
        assert_matches_type(MediaRetrievalListUploadedMediaResponseBody, media, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        media = client.preview.cameras.media.list(
            available_after_time="availableAfterTime",
            end_time="endTime",
            inputs=["dashcamRoadFacing"],
            media_types=["image"],
            start_time="startTime",
            trigger_reasons=["api"],
            vehicle_ids="vehicleIds",
            after="after",
        )
        assert_matches_type(MediaRetrievalListUploadedMediaResponseBody, media, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.preview.cameras.media.with_raw_response.list(
            available_after_time="availableAfterTime",
            end_time="endTime",
            inputs=["dashcamRoadFacing"],
            media_types=["image"],
            start_time="startTime",
            trigger_reasons=["api"],
            vehicle_ids="vehicleIds",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaRetrievalListUploadedMediaResponseBody, media, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.preview.cameras.media.with_streaming_response.list(
            available_after_time="availableAfterTime",
            end_time="endTime",
            inputs=["dashcamRoadFacing"],
            media_types=["image"],
            start_time="startTime",
            trigger_reasons=["api"],
            vehicle_ids="vehicleIds",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaRetrievalListUploadedMediaResponseBody, media, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMedia:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        media = await async_client.preview.cameras.media.list(
            available_after_time="availableAfterTime",
            end_time="endTime",
            inputs=["dashcamRoadFacing"],
            media_types=["image"],
            start_time="startTime",
            trigger_reasons=["api"],
            vehicle_ids="vehicleIds",
        )
        assert_matches_type(MediaRetrievalListUploadedMediaResponseBody, media, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        media = await async_client.preview.cameras.media.list(
            available_after_time="availableAfterTime",
            end_time="endTime",
            inputs=["dashcamRoadFacing"],
            media_types=["image"],
            start_time="startTime",
            trigger_reasons=["api"],
            vehicle_ids="vehicleIds",
            after="after",
        )
        assert_matches_type(MediaRetrievalListUploadedMediaResponseBody, media, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.preview.cameras.media.with_raw_response.list(
            available_after_time="availableAfterTime",
            end_time="endTime",
            inputs=["dashcamRoadFacing"],
            media_types=["image"],
            start_time="startTime",
            trigger_reasons=["api"],
            vehicle_ids="vehicleIds",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaRetrievalListUploadedMediaResponseBody, media, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.preview.cameras.media.with_streaming_response.list(
            available_after_time="availableAfterTime",
            end_time="endTime",
            inputs=["dashcamRoadFacing"],
            media_types=["image"],
            start_time="startTime",
            trigger_reasons=["api"],
            vehicle_ids="vehicleIds",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaRetrievalListUploadedMediaResponseBody, media, path=["response"])

        assert cast(Any, response.is_closed) is True
