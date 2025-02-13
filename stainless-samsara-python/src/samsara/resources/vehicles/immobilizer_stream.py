# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.vehicles import immobilizer_stream_list_params
from ...types.fleet.vehicles.engine_immobilizer_get_engine_immobilizer_states_response_body import (
    EngineImmobilizerGetEngineImmobilizerStatesResponseBody,
)

__all__ = ["ImmobilizerStreamResource", "AsyncImmobilizerStreamResource"]


class ImmobilizerStreamResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ImmobilizerStreamResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return ImmobilizerStreamResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImmobilizerStreamResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return ImmobilizerStreamResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        start_time: str,
        vehicle_ids: str,
        after: str | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EngineImmobilizerGetEngineImmobilizerStatesResponseBody:
        """Get the engine immobilizer states of the queried vehicles.

        If a vehicle has
        never had an engine immobilizer connected, there won't be any state returned for
        that vehicle.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Vehicle Immobilization** under the Vehicles
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
          start_time: A start time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          vehicle_ids: A filter on the data based on this comma-separated list of vehicle IDs and
              externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          end_time: An end time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/fleet/vehicles/immobilizer/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "vehicle_ids": vehicle_ids,
                        "after": after,
                        "end_time": end_time,
                    },
                    immobilizer_stream_list_params.ImmobilizerStreamListParams,
                ),
            ),
            cast_to=EngineImmobilizerGetEngineImmobilizerStatesResponseBody,
        )


class AsyncImmobilizerStreamResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncImmobilizerStreamResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncImmobilizerStreamResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImmobilizerStreamResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncImmobilizerStreamResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        start_time: str,
        vehicle_ids: str,
        after: str | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EngineImmobilizerGetEngineImmobilizerStatesResponseBody:
        """Get the engine immobilizer states of the queried vehicles.

        If a vehicle has
        never had an engine immobilizer connected, there won't be any state returned for
        that vehicle.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Vehicle Immobilization** under the Vehicles
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
          start_time: A start time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          vehicle_ids: A filter on the data based on this comma-separated list of vehicle IDs and
              externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          end_time: An end time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/fleet/vehicles/immobilizer/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_time": start_time,
                        "vehicle_ids": vehicle_ids,
                        "after": after,
                        "end_time": end_time,
                    },
                    immobilizer_stream_list_params.ImmobilizerStreamListParams,
                ),
            ),
            cast_to=EngineImmobilizerGetEngineImmobilizerStatesResponseBody,
        )


class ImmobilizerStreamResourceWithRawResponse:
    def __init__(self, immobilizer_stream: ImmobilizerStreamResource) -> None:
        self._immobilizer_stream = immobilizer_stream

        self.list = to_raw_response_wrapper(
            immobilizer_stream.list,
        )


class AsyncImmobilizerStreamResourceWithRawResponse:
    def __init__(self, immobilizer_stream: AsyncImmobilizerStreamResource) -> None:
        self._immobilizer_stream = immobilizer_stream

        self.list = async_to_raw_response_wrapper(
            immobilizer_stream.list,
        )


class ImmobilizerStreamResourceWithStreamingResponse:
    def __init__(self, immobilizer_stream: ImmobilizerStreamResource) -> None:
        self._immobilizer_stream = immobilizer_stream

        self.list = to_streamed_response_wrapper(
            immobilizer_stream.list,
        )


class AsyncImmobilizerStreamResourceWithStreamingResponse:
    def __init__(self, immobilizer_stream: AsyncImmobilizerStreamResource) -> None:
        self._immobilizer_stream = immobilizer_stream

        self.list = async_to_streamed_response_wrapper(
            immobilizer_stream.list,
        )
