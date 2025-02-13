# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.preview.cameras import media_list_params
from ....types.preview.cameras.media_retrieval_list_uploaded_media_response_body import (
    MediaRetrievalListUploadedMediaResponseBody,
)

__all__ = ["MediaResource", "AsyncMediaResource"]


class MediaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MediaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return MediaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MediaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return MediaResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        available_after_time: str,
        end_time: str,
        inputs: List[Literal["dashcamRoadFacing", "dashcamDriverFacing", "analog"]],
        media_types: List[Literal["image"]],
        start_time: str,
        trigger_reasons: List[
            Literal["api", "panicButton", "periodicStill", "tripEndStill", "tripStartStill", "videoRetrieval"]
        ],
        vehicle_ids: str,
        after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MediaRetrievalListUploadedMediaResponseBody:
        """
        This endpoint returns a list of all uploaded media (video and still images)
        matching query parameters. Additional media can be retrieved with the
        [Create a media retrieval request](https://developers.samsara.com/reference/postmediaretrieval)
        endpoint, and they will be included in the list after they are uploaded. Urls
        provided by this endpoint expire in 8 hours.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Preview** under the category when creating
        or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Endpoints in this section are in Preview. These APIs are not functional and are
        instead for soliciting feedback from our API users on the intended design of
        this API. Additionally, it is not guaranteed that we will be releasing an
        endpoint included in this section to production. This means that developers
        should **NOT** rely on these APIs to build business critical applications

        - Samsara may change the structure of a preview API's interface without
          versioning or any notice to API users.

        - When an endpoint becomes generally available, it will be announced in the API
          [changelog](https://developers.samsara.com/changelog).

          **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
          as feedback in our
          <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
          form</a>. If you encountered an issue or noticed inaccuracies in the API
          documentation, please
          <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to
          our support team.

        Args:
          available_after_time: A timestamp in RFC 3339 format that can act as a cursor to track which media has
              previously been retrieved; only media whose availableAtTime comes after this
              parameter will be returned. Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00

          end_time: An end time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          inputs: A list of desired camera inputs for which to return captured media. If empty,
              media for all available inputs will be returned.

          media_types: A list of desired media types for which to return captured media. If empty,
              media for all available media types will be returned.

          start_time: A start time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          trigger_reasons: A list of desired trigger reasons for which to return captured media. If empty,
              media for all available trigger reasons will be returned.

          vehicle_ids: A filter on the data based on this comma-separated list of vehicle IDs and
              externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/preview/cameras/media",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "available_after_time": available_after_time,
                        "end_time": end_time,
                        "inputs": inputs,
                        "media_types": media_types,
                        "start_time": start_time,
                        "trigger_reasons": trigger_reasons,
                        "vehicle_ids": vehicle_ids,
                        "after": after,
                    },
                    media_list_params.MediaListParams,
                ),
            ),
            cast_to=MediaRetrievalListUploadedMediaResponseBody,
        )


class AsyncMediaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMediaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMediaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMediaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncMediaResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        available_after_time: str,
        end_time: str,
        inputs: List[Literal["dashcamRoadFacing", "dashcamDriverFacing", "analog"]],
        media_types: List[Literal["image"]],
        start_time: str,
        trigger_reasons: List[
            Literal["api", "panicButton", "periodicStill", "tripEndStill", "tripStartStill", "videoRetrieval"]
        ],
        vehicle_ids: str,
        after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MediaRetrievalListUploadedMediaResponseBody:
        """
        This endpoint returns a list of all uploaded media (video and still images)
        matching query parameters. Additional media can be retrieved with the
        [Create a media retrieval request](https://developers.samsara.com/reference/postmediaretrieval)
        endpoint, and they will be included in the list after they are uploaded. Urls
        provided by this endpoint expire in 8 hours.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Preview** under the category when creating
        or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Endpoints in this section are in Preview. These APIs are not functional and are
        instead for soliciting feedback from our API users on the intended design of
        this API. Additionally, it is not guaranteed that we will be releasing an
        endpoint included in this section to production. This means that developers
        should **NOT** rely on these APIs to build business critical applications

        - Samsara may change the structure of a preview API's interface without
          versioning or any notice to API users.

        - When an endpoint becomes generally available, it will be announced in the API
          [changelog](https://developers.samsara.com/changelog).

          **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
          as feedback in our
          <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
          form</a>. If you encountered an issue or noticed inaccuracies in the API
          documentation, please
          <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to
          our support team.

        Args:
          available_after_time: A timestamp in RFC 3339 format that can act as a cursor to track which media has
              previously been retrieved; only media whose availableAtTime comes after this
              parameter will be returned. Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00

          end_time: An end time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          inputs: A list of desired camera inputs for which to return captured media. If empty,
              media for all available inputs will be returned.

          media_types: A list of desired media types for which to return captured media. If empty,
              media for all available media types will be returned.

          start_time: A start time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          trigger_reasons: A list of desired trigger reasons for which to return captured media. If empty,
              media for all available trigger reasons will be returned.

          vehicle_ids: A filter on the data based on this comma-separated list of vehicle IDs and
              externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/preview/cameras/media",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "available_after_time": available_after_time,
                        "end_time": end_time,
                        "inputs": inputs,
                        "media_types": media_types,
                        "start_time": start_time,
                        "trigger_reasons": trigger_reasons,
                        "vehicle_ids": vehicle_ids,
                        "after": after,
                    },
                    media_list_params.MediaListParams,
                ),
            ),
            cast_to=MediaRetrievalListUploadedMediaResponseBody,
        )


class MediaResourceWithRawResponse:
    def __init__(self, media: MediaResource) -> None:
        self._media = media

        self.list = to_raw_response_wrapper(
            media.list,
        )


class AsyncMediaResourceWithRawResponse:
    def __init__(self, media: AsyncMediaResource) -> None:
        self._media = media

        self.list = async_to_raw_response_wrapper(
            media.list,
        )


class MediaResourceWithStreamingResponse:
    def __init__(self, media: MediaResource) -> None:
        self._media = media

        self.list = to_streamed_response_wrapper(
            media.list,
        )


class AsyncMediaResourceWithStreamingResponse:
    def __init__(self, media: AsyncMediaResource) -> None:
        self._media = media

        self.list = async_to_streamed_response_wrapper(
            media.list,
        )
