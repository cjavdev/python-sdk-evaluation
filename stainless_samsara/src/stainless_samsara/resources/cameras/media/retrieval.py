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
from ....types.cameras.media import retrieval_create_params, retrieval_retrieve_params
from ....types.cameras.media.retrieval_create_response import RetrievalCreateResponse
from ....types.cameras.media.retrieval_retrieve_response import RetrievalRetrieveResponse

__all__ = ["RetrievalResource", "AsyncRetrievalResource"]


class RetrievalResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RetrievalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return RetrievalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetrievalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return RetrievalResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        inputs: List[Literal["dashcamRoadFacing", "dashcamDriverFacing", "analog"]],
        start_time: str,
        vehicle_id: str,
        end_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RetrievalCreateResponse:
        """
        This endpoint creates an asynchronous request to upload certain media from a
        device. Currently, only images can be requested for timestamps when there's high
        resolution footage stored on the device, even if low resolution footage exists
        on the device during that timestamp. Other types of media (e.g. videos,
        hyperlapse) are planned to be supported in the future. If a device is offline,
        the requested media will be uploaded once it comes back online. Quota limits for
        media requests will be enforced in GA, but not in closed beta.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Media Retrieval** under the Safety &
        Cameras category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        Args:
          inputs: A list of desired camera inputs for which to capture media. Only media with
              valid inputs (e.g. device has that input stream and device was recording at the
              time) will be uploaded. An empty list is invalid.

          start_time: A start time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          vehicle_id: Vehicle ID for which to initiate media capture. Examples: 1234

          end_time: An end time in RFC 3339 format. If same as startTime or not specified, an image
              will be captured at startTime. If specified, must be equal to or after startTime
              and no more than 60 seconds after startTime. (Examples: 2019-06-13T19:08:55Z,
              2019-06-13T19:08:55.455Z, OR 2015-09-15T14:00:42-04:00).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cameras/media/retrieval",
            body=maybe_transform(
                {
                    "inputs": inputs,
                    "start_time": start_time,
                    "vehicle_id": vehicle_id,
                    "end_time": end_time,
                },
                retrieval_create_params.RetrievalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetrievalCreateResponse,
        )

    def retrieve(
        self,
        *,
        retrieval_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RetrievalRetrieveResponse:
        """
        This endpoint returns media information corresponding to a retrieval ID.
        Retrieval IDs are associated to prior
        [media retrieval requests](https://developers.samsara.com/reference/postmediaretrieval).
        Urls provided by this endpoint expire in 8 hours.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Media Retrieval** under the Safety & Cameras
        category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        Args:
          retrieval_id:
              Retrieval ID associated with this media capture request. Examples:
              2308cec4-82e0-46f1-8b3c-a3592e5cc21e

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cameras/media/retrieval",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"retrieval_id": retrieval_id}, retrieval_retrieve_params.RetrievalRetrieveParams
                ),
            ),
            cast_to=RetrievalRetrieveResponse,
        )


class AsyncRetrievalResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRetrievalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRetrievalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetrievalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncRetrievalResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        inputs: List[Literal["dashcamRoadFacing", "dashcamDriverFacing", "analog"]],
        start_time: str,
        vehicle_id: str,
        end_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RetrievalCreateResponse:
        """
        This endpoint creates an asynchronous request to upload certain media from a
        device. Currently, only images can be requested for timestamps when there's high
        resolution footage stored on the device, even if low resolution footage exists
        on the device during that timestamp. Other types of media (e.g. videos,
        hyperlapse) are planned to be supported in the future. If a device is offline,
        the requested media will be uploaded once it comes back online. Quota limits for
        media requests will be enforced in GA, but not in closed beta.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Media Retrieval** under the Safety &
        Cameras category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        Args:
          inputs: A list of desired camera inputs for which to capture media. Only media with
              valid inputs (e.g. device has that input stream and device was recording at the
              time) will be uploaded. An empty list is invalid.

          start_time: A start time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          vehicle_id: Vehicle ID for which to initiate media capture. Examples: 1234

          end_time: An end time in RFC 3339 format. If same as startTime or not specified, an image
              will be captured at startTime. If specified, must be equal to or after startTime
              and no more than 60 seconds after startTime. (Examples: 2019-06-13T19:08:55Z,
              2019-06-13T19:08:55.455Z, OR 2015-09-15T14:00:42-04:00).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cameras/media/retrieval",
            body=await async_maybe_transform(
                {
                    "inputs": inputs,
                    "start_time": start_time,
                    "vehicle_id": vehicle_id,
                    "end_time": end_time,
                },
                retrieval_create_params.RetrievalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetrievalCreateResponse,
        )

    async def retrieve(
        self,
        *,
        retrieval_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RetrievalRetrieveResponse:
        """
        This endpoint returns media information corresponding to a retrieval ID.
        Retrieval IDs are associated to prior
        [media retrieval requests](https://developers.samsara.com/reference/postmediaretrieval).
        Urls provided by this endpoint expire in 8 hours.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Media Retrieval** under the Safety & Cameras
        category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        Args:
          retrieval_id:
              Retrieval ID associated with this media capture request. Examples:
              2308cec4-82e0-46f1-8b3c-a3592e5cc21e

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cameras/media/retrieval",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"retrieval_id": retrieval_id}, retrieval_retrieve_params.RetrievalRetrieveParams
                ),
            ),
            cast_to=RetrievalRetrieveResponse,
        )


class RetrievalResourceWithRawResponse:
    def __init__(self, retrieval: RetrievalResource) -> None:
        self._retrieval = retrieval

        self.create = to_raw_response_wrapper(
            retrieval.create,
        )
        self.retrieve = to_raw_response_wrapper(
            retrieval.retrieve,
        )


class AsyncRetrievalResourceWithRawResponse:
    def __init__(self, retrieval: AsyncRetrievalResource) -> None:
        self._retrieval = retrieval

        self.create = async_to_raw_response_wrapper(
            retrieval.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            retrieval.retrieve,
        )


class RetrievalResourceWithStreamingResponse:
    def __init__(self, retrieval: RetrievalResource) -> None:
        self._retrieval = retrieval

        self.create = to_streamed_response_wrapper(
            retrieval.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            retrieval.retrieve,
        )


class AsyncRetrievalResourceWithStreamingResponse:
    def __init__(self, retrieval: AsyncRetrievalResource) -> None:
        self._retrieval = retrieval

        self.create = async_to_streamed_response_wrapper(
            retrieval.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            retrieval.retrieve,
        )
