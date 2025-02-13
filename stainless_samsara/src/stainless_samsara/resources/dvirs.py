# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import dvir_stream_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.dvir_stream_response import DvirStreamResponse

__all__ = ["DvirsResource", "AsyncDvirsResource"]


class DvirsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DvirsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return DvirsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DvirsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return DvirsResourceWithStreamingResponse(self)

    def stream(
        self,
        *,
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        include_external_ids: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        safety_status: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DvirStreamResponse:
        """
        Returns a history/feed of changed DVIRs by updatedAtTime between startTime and
        endTime parameters. In case of missing `endTime` parameter it will return a
        never ending stream of data.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read DVIRs** under the Maintenance category when
        creating or editing an API token.
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
          start_time: Required RFC 3339 timestamp to begin the feed or history by `updatedAtTime` at
              `startTime`.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          end_time: Optional RFC 3339 timestamp. If not provided then the endpoint behaves as an
              unending feed of changes.

          include_external_ids: Optional boolean indicating whether to return external IDs on supported entities

          limit: The limit for how many objects will be in the response. Default and max for this
              value is 200 objects.

          safety_status: Optional list of safety statuses. Valid values: [safe, unsafe, resolved]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/dvirs/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "after": after,
                        "end_time": end_time,
                        "include_external_ids": include_external_ids,
                        "limit": limit,
                        "safety_status": safety_status,
                    },
                    dvir_stream_params.DvirStreamParams,
                ),
            ),
            cast_to=DvirStreamResponse,
        )


class AsyncDvirsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDvirsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDvirsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDvirsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncDvirsResourceWithStreamingResponse(self)

    async def stream(
        self,
        *,
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        include_external_ids: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        safety_status: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DvirStreamResponse:
        """
        Returns a history/feed of changed DVIRs by updatedAtTime between startTime and
        endTime parameters. In case of missing `endTime` parameter it will return a
        never ending stream of data.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read DVIRs** under the Maintenance category when
        creating or editing an API token.
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
          start_time: Required RFC 3339 timestamp to begin the feed or history by `updatedAtTime` at
              `startTime`.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          end_time: Optional RFC 3339 timestamp. If not provided then the endpoint behaves as an
              unending feed of changes.

          include_external_ids: Optional boolean indicating whether to return external IDs on supported entities

          limit: The limit for how many objects will be in the response. Default and max for this
              value is 200 objects.

          safety_status: Optional list of safety statuses. Valid values: [safe, unsafe, resolved]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/dvirs/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_time": start_time,
                        "after": after,
                        "end_time": end_time,
                        "include_external_ids": include_external_ids,
                        "limit": limit,
                        "safety_status": safety_status,
                    },
                    dvir_stream_params.DvirStreamParams,
                ),
            ),
            cast_to=DvirStreamResponse,
        )


class DvirsResourceWithRawResponse:
    def __init__(self, dvirs: DvirsResource) -> None:
        self._dvirs = dvirs

        self.stream = to_raw_response_wrapper(
            dvirs.stream,
        )


class AsyncDvirsResourceWithRawResponse:
    def __init__(self, dvirs: AsyncDvirsResource) -> None:
        self._dvirs = dvirs

        self.stream = async_to_raw_response_wrapper(
            dvirs.stream,
        )


class DvirsResourceWithStreamingResponse:
    def __init__(self, dvirs: DvirsResource) -> None:
        self._dvirs = dvirs

        self.stream = to_streamed_response_wrapper(
            dvirs.stream,
        )


class AsyncDvirsResourceWithStreamingResponse:
    def __init__(self, dvirs: AsyncDvirsResource) -> None:
        self._dvirs = dvirs

        self.stream = async_to_streamed_response_wrapper(
            dvirs.stream,
        )
