# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.alerts import incident_stream_params
from ...types.alerts.incident_stream_response import IncidentStreamResponse

__all__ = ["IncidentsResource", "AsyncIncidentsResource"]


class IncidentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IncidentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return IncidentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IncidentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return IncidentsResourceWithStreamingResponse(self)

    def stream(
        self,
        *,
        configuration_ids: List[str],
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IncidentStreamResponse:
        """
        Get Alert Incidents for specific Alert Configurations over a specified period of
        time.

        <b>Rate limit:</b> 10 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Alerts** under the Alerts category when
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
          configuration_ids: Required array of alert configuration ids to return incident data for.

          start_time: Required RFC 3339 timestamp that indicates when to begin receiving data. This
              will be based on updatedAtTime.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          end_time: Optional RFC 3339 timestamp to stop receiving data. Defaults to now if not
              provided. This will be based on updatedAtTime.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/alerts/incidents/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "configuration_ids": configuration_ids,
                        "start_time": start_time,
                        "after": after,
                        "end_time": end_time,
                    },
                    incident_stream_params.IncidentStreamParams,
                ),
            ),
            cast_to=IncidentStreamResponse,
        )


class AsyncIncidentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIncidentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIncidentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIncidentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncIncidentsResourceWithStreamingResponse(self)

    async def stream(
        self,
        *,
        configuration_ids: List[str],
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IncidentStreamResponse:
        """
        Get Alert Incidents for specific Alert Configurations over a specified period of
        time.

        <b>Rate limit:</b> 10 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Alerts** under the Alerts category when
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
          configuration_ids: Required array of alert configuration ids to return incident data for.

          start_time: Required RFC 3339 timestamp that indicates when to begin receiving data. This
              will be based on updatedAtTime.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          end_time: Optional RFC 3339 timestamp to stop receiving data. Defaults to now if not
              provided. This will be based on updatedAtTime.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/alerts/incidents/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "configuration_ids": configuration_ids,
                        "start_time": start_time,
                        "after": after,
                        "end_time": end_time,
                    },
                    incident_stream_params.IncidentStreamParams,
                ),
            ),
            cast_to=IncidentStreamResponse,
        )


class IncidentsResourceWithRawResponse:
    def __init__(self, incidents: IncidentsResource) -> None:
        self._incidents = incidents

        self.stream = to_raw_response_wrapper(
            incidents.stream,
        )


class AsyncIncidentsResourceWithRawResponse:
    def __init__(self, incidents: AsyncIncidentsResource) -> None:
        self._incidents = incidents

        self.stream = async_to_raw_response_wrapper(
            incidents.stream,
        )


class IncidentsResourceWithStreamingResponse:
    def __init__(self, incidents: IncidentsResource) -> None:
        self._incidents = incidents

        self.stream = to_streamed_response_wrapper(
            incidents.stream,
        )


class AsyncIncidentsResourceWithStreamingResponse:
    def __init__(self, incidents: AsyncIncidentsResource) -> None:
        self._incidents = incidents

        self.stream = async_to_streamed_response_wrapper(
            incidents.stream,
        )
