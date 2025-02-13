# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
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
from ....types.fleet import defect_update_params
from ...._base_client import make_request_options
from ....types.fleet.defect_update_response import DefectUpdateResponse

__all__ = ["DefectsResource", "AsyncDefectsResource"]


class DefectsResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> DefectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return DefectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DefectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return DefectsResourceWithStreamingResponse(self)

    def update(
        self,
        id: str,
        *,
        is_resolved: bool | NotGiven = NOT_GIVEN,
        mechanic_notes: str | NotGiven = NOT_GIVEN,
        resolved_at_time: str | NotGiven = NOT_GIVEN,
        resolved_by: defect_update_params.ResolvedBy | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DefectUpdateResponse:
        """Updates a given defect.

        Can be used to resolve a defect by marking its
        `isResolved` field to `true`.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Defects** under the Maintenance category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          is_resolved: Resolves the defect. Must be `true`.

          mechanic_notes: The mechanics notes on the defect.

          resolved_at_time: Time when defect was resolved. Defaults to now if not provided. UTC timestamp in
              RFC 3339 format. Example: `2020-01-27T07:06:25Z`.

          resolved_by: Information about the user who is resolving a defect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/fleet/defects/{id}",
            body=maybe_transform(
                {
                    "is_resolved": is_resolved,
                    "mechanic_notes": mechanic_notes,
                    "resolved_at_time": resolved_at_time,
                    "resolved_by": resolved_by,
                },
                defect_update_params.DefectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DefectUpdateResponse,
        )


class AsyncDefectsResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDefectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDefectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDefectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncDefectsResourceWithStreamingResponse(self)

    async def update(
        self,
        id: str,
        *,
        is_resolved: bool | NotGiven = NOT_GIVEN,
        mechanic_notes: str | NotGiven = NOT_GIVEN,
        resolved_at_time: str | NotGiven = NOT_GIVEN,
        resolved_by: defect_update_params.ResolvedBy | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DefectUpdateResponse:
        """Updates a given defect.

        Can be used to resolve a defect by marking its
        `isResolved` field to `true`.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Defects** under the Maintenance category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          is_resolved: Resolves the defect. Must be `true`.

          mechanic_notes: The mechanics notes on the defect.

          resolved_at_time: Time when defect was resolved. Defaults to now if not provided. UTC timestamp in
              RFC 3339 format. Example: `2020-01-27T07:06:25Z`.

          resolved_by: Information about the user who is resolving a defect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/fleet/defects/{id}",
            body=await async_maybe_transform(
                {
                    "is_resolved": is_resolved,
                    "mechanic_notes": mechanic_notes,
                    "resolved_at_time": resolved_at_time,
                    "resolved_by": resolved_by,
                },
                defect_update_params.DefectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DefectUpdateResponse,
        )


class DefectsResourceWithRawResponse:
    def __init__(self, defects: DefectsResource) -> None:
        self._defects = defects

        self.update = to_raw_response_wrapper(
            defects.update,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._defects.history)


class AsyncDefectsResourceWithRawResponse:
    def __init__(self, defects: AsyncDefectsResource) -> None:
        self._defects = defects

        self.update = async_to_raw_response_wrapper(
            defects.update,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._defects.history)


class DefectsResourceWithStreamingResponse:
    def __init__(self, defects: DefectsResource) -> None:
        self._defects = defects

        self.update = to_streamed_response_wrapper(
            defects.update,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._defects.history)


class AsyncDefectsResourceWithStreamingResponse:
    def __init__(self, defects: AsyncDefectsResource) -> None:
        self._defects = defects

        self.update = async_to_streamed_response_wrapper(
            defects.update,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._defects.history)
