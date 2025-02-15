# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ....types.industrial.assets import data_output_update_params
from ....types.industrial.assets.asset_data_outputs_patch_asset_data_outputs_response_body import (
    AssetDataOutputsPatchAssetDataOutputsResponseBody,
)

__all__ = ["DataOutputsResource", "AsyncDataOutputsResource"]


class DataOutputsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DataOutputsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return DataOutputsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataOutputsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return DataOutputsResourceWithStreamingResponse(self)

    def update(
        self,
        id: str,
        *,
        values: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetDataOutputsPatchAssetDataOutputsResponseBody:
        """Writes values to multiple data outputs on an asset simultaneously.

        Only the
        provided data outputs will be updated.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Equipment Statistics** under the Equipment
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
          values: A map of data output IDs to values. All data outputs must belong to the same
              asset. Only the specified IDs will be written to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/industrial/assets/{id}/data-outputs",
            body=maybe_transform({"values": values}, data_output_update_params.DataOutputUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetDataOutputsPatchAssetDataOutputsResponseBody,
        )


class AsyncDataOutputsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDataOutputsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDataOutputsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataOutputsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncDataOutputsResourceWithStreamingResponse(self)

    async def update(
        self,
        id: str,
        *,
        values: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetDataOutputsPatchAssetDataOutputsResponseBody:
        """Writes values to multiple data outputs on an asset simultaneously.

        Only the
        provided data outputs will be updated.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Equipment Statistics** under the Equipment
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
          values: A map of data output IDs to values. All data outputs must belong to the same
              asset. Only the specified IDs will be written to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/industrial/assets/{id}/data-outputs",
            body=await async_maybe_transform({"values": values}, data_output_update_params.DataOutputUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetDataOutputsPatchAssetDataOutputsResponseBody,
        )


class DataOutputsResourceWithRawResponse:
    def __init__(self, data_outputs: DataOutputsResource) -> None:
        self._data_outputs = data_outputs

        self.update = to_raw_response_wrapper(
            data_outputs.update,
        )


class AsyncDataOutputsResourceWithRawResponse:
    def __init__(self, data_outputs: AsyncDataOutputsResource) -> None:
        self._data_outputs = data_outputs

        self.update = async_to_raw_response_wrapper(
            data_outputs.update,
        )


class DataOutputsResourceWithStreamingResponse:
    def __init__(self, data_outputs: DataOutputsResource) -> None:
        self._data_outputs = data_outputs

        self.update = to_streamed_response_wrapper(
            data_outputs.update,
        )


class AsyncDataOutputsResourceWithStreamingResponse:
    def __init__(self, data_outputs: AsyncDataOutputsResource) -> None:
        self._data_outputs = data_outputs

        self.update = async_to_streamed_response_wrapper(
            data_outputs.update,
        )
