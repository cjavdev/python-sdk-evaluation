# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.beta.fleet.vehicles import immobilizer_update_params

__all__ = ["ImmobilizerResource", "AsyncImmobilizerResource"]


class ImmobilizerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ImmobilizerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return ImmobilizerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImmobilizerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return ImmobilizerResourceWithStreamingResponse(self)

    def update(
        self,
        id: int,
        *,
        relay_states: Iterable[immobilizer_update_params.RelayState],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Update the engine immobilizer state of a vehicle.

        This requires an engine
        immobilizer to be installed on the vehicle gateway.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Vehicle Immobilization** under the Vehicles
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
          relay_states: A list of relay states. If a relay is omitted, its state won't be updated. If
              the list is empty, a 400 bad request status code will be returned. If there are
              multiple states for the same relay, a 400 bad request status code will be
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/beta/fleet/vehicles/{id}/immobilizer",
            body=maybe_transform({"relay_states": relay_states}, immobilizer_update_params.ImmobilizerUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncImmobilizerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncImmobilizerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncImmobilizerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImmobilizerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncImmobilizerResourceWithStreamingResponse(self)

    async def update(
        self,
        id: int,
        *,
        relay_states: Iterable[immobilizer_update_params.RelayState],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Update the engine immobilizer state of a vehicle.

        This requires an engine
        immobilizer to be installed on the vehicle gateway.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Vehicle Immobilization** under the Vehicles
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
          relay_states: A list of relay states. If a relay is omitted, its state won't be updated. If
              the list is empty, a 400 bad request status code will be returned. If there are
              multiple states for the same relay, a 400 bad request status code will be
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/beta/fleet/vehicles/{id}/immobilizer",
            body=await async_maybe_transform(
                {"relay_states": relay_states}, immobilizer_update_params.ImmobilizerUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ImmobilizerResourceWithRawResponse:
    def __init__(self, immobilizer: ImmobilizerResource) -> None:
        self._immobilizer = immobilizer

        self.update = to_raw_response_wrapper(
            immobilizer.update,
        )


class AsyncImmobilizerResourceWithRawResponse:
    def __init__(self, immobilizer: AsyncImmobilizerResource) -> None:
        self._immobilizer = immobilizer

        self.update = async_to_raw_response_wrapper(
            immobilizer.update,
        )


class ImmobilizerResourceWithStreamingResponse:
    def __init__(self, immobilizer: ImmobilizerResource) -> None:
        self._immobilizer = immobilizer

        self.update = to_streamed_response_wrapper(
            immobilizer.update,
        )


class AsyncImmobilizerResourceWithStreamingResponse:
    def __init__(self, immobilizer: AsyncImmobilizerResource) -> None:
        self._immobilizer = immobilizer

        self.update = async_to_streamed_response_wrapper(
            immobilizer.update,
        )
