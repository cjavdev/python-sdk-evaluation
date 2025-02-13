# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.beta.aemp.fleet_list_response import FleetListResponse

__all__ = ["FleetResource", "AsyncFleetResource"]


class FleetResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FleetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return FleetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FleetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return FleetResourceWithStreamingResponse(self)

    def list(
        self,
        page_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FleetListResponse:
        """
        Get a list of equipment following the AEMP ISO 15143-3 standard.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read AEMP** under the Equipment category when
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not page_number:
            raise ValueError(f"Expected a non-empty value for `page_number` but received {page_number!r}")
        return self._get(
            f"/beta/aemp/Fleet/{page_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FleetListResponse,
        )


class AsyncFleetResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFleetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFleetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFleetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncFleetResourceWithStreamingResponse(self)

    async def list(
        self,
        page_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FleetListResponse:
        """
        Get a list of equipment following the AEMP ISO 15143-3 standard.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read AEMP** under the Equipment category when
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not page_number:
            raise ValueError(f"Expected a non-empty value for `page_number` but received {page_number!r}")
        return await self._get(
            f"/beta/aemp/Fleet/{page_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FleetListResponse,
        )


class FleetResourceWithRawResponse:
    def __init__(self, fleet: FleetResource) -> None:
        self._fleet = fleet

        self.list = to_raw_response_wrapper(
            fleet.list,
        )


class AsyncFleetResourceWithRawResponse:
    def __init__(self, fleet: AsyncFleetResource) -> None:
        self._fleet = fleet

        self.list = async_to_raw_response_wrapper(
            fleet.list,
        )


class FleetResourceWithStreamingResponse:
    def __init__(self, fleet: FleetResource) -> None:
        self._fleet = fleet

        self.list = to_streamed_response_wrapper(
            fleet.list,
        )


class AsyncFleetResourceWithStreamingResponse:
    def __init__(self, fleet: AsyncFleetResource) -> None:
        self._fleet = fleet

        self.list = async_to_streamed_response_wrapper(
            fleet.list,
        )
