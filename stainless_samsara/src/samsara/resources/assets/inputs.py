# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

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
from ...types.assets import input_stream_params
from ...types.assets.input_stream_response import InputStreamResponse

__all__ = ["InputsResource", "AsyncInputsResource"]


class InputsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InputsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return InputsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InputsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return InputsResourceWithStreamingResponse(self)

    def stream(
        self,
        *,
        ids: List[str],
        start_time: str,
        type: Literal[
            "auxInput1",
            "auxInput2",
            "auxInput3",
            "auxInput4",
            "auxInput5",
            "auxInput6",
            "auxInput7",
            "auxInput8",
            "auxInput9",
            "auxInput10",
            "auxInput11",
            "auxInput12",
            "auxInput13",
            "analogInput1Voltage",
            "analogInput2Voltage",
            "analogInput1Current",
            "analogInput2Current",
            "batteryVoltage",
        ],
        after: str | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        include_attributes: bool | NotGiven = NOT_GIVEN,
        include_external_ids: bool | NotGiven = NOT_GIVEN,
        include_tags: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InputStreamResponse:
        """
        This endpoint will return data collected from the inputs of your organization's
        assets based on the time parameters passed in. Results are paginated. If you
        include an endTime, the endpoint will return data up until that point. If you
        don’t include an endTime, you can continue to poll the API real-time with the
        pagination cursor that gets returned on every call. The endpoint will only
        return data up until the endTime that has been processed by the server at the
        time of the original request. You will need to request the same [startTime,
        endTime) range again to receive data for assets processed after the original
        request time. This endpoint sorts data by time ascending.

        <b>Rate limit:</b> 10 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Assets** under the Assets category when
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
          ids: Comma-separated list of asset IDs. Limited to 100 ID's for each request.

          start_time: A start time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          type: Input stat type to query for. Valid values: `auxInput1`, `auxInput2`,
              `auxInput3`, `auxInput4`, `auxInput5`, `auxInput6`, `auxInput7`, `auxInput8`,
              `auxInput9`, `auxInput10`, `auxInput11`, `auxInput12`, `auxInput13`,
              `analogInput1Voltage`, `analogInput2Voltage`, `analogInput1Current`,
              `analogInput2Current`, `batteryVoltage`

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          end_time: An end time in RFC 3339 format. Defaults to never if not provided; if not
              provided then pagination will not cease, and a valid pagination cursor will
              always be returned. Millisecond precision and timezones are supported.
              (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          include_attributes: Optional boolean indicating whether to return attributes on supported entities

          include_external_ids: Optional boolean indicating whether to return external IDs on supported entities

          include_tags: Optional boolean indicating whether to return tags on supported entities

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/assets/inputs/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ids": ids,
                        "start_time": start_time,
                        "type": type,
                        "after": after,
                        "end_time": end_time,
                        "include_attributes": include_attributes,
                        "include_external_ids": include_external_ids,
                        "include_tags": include_tags,
                    },
                    input_stream_params.InputStreamParams,
                ),
            ),
            cast_to=InputStreamResponse,
        )


class AsyncInputsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInputsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInputsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInputsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncInputsResourceWithStreamingResponse(self)

    async def stream(
        self,
        *,
        ids: List[str],
        start_time: str,
        type: Literal[
            "auxInput1",
            "auxInput2",
            "auxInput3",
            "auxInput4",
            "auxInput5",
            "auxInput6",
            "auxInput7",
            "auxInput8",
            "auxInput9",
            "auxInput10",
            "auxInput11",
            "auxInput12",
            "auxInput13",
            "analogInput1Voltage",
            "analogInput2Voltage",
            "analogInput1Current",
            "analogInput2Current",
            "batteryVoltage",
        ],
        after: str | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        include_attributes: bool | NotGiven = NOT_GIVEN,
        include_external_ids: bool | NotGiven = NOT_GIVEN,
        include_tags: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InputStreamResponse:
        """
        This endpoint will return data collected from the inputs of your organization's
        assets based on the time parameters passed in. Results are paginated. If you
        include an endTime, the endpoint will return data up until that point. If you
        don’t include an endTime, you can continue to poll the API real-time with the
        pagination cursor that gets returned on every call. The endpoint will only
        return data up until the endTime that has been processed by the server at the
        time of the original request. You will need to request the same [startTime,
        endTime) range again to receive data for assets processed after the original
        request time. This endpoint sorts data by time ascending.

        <b>Rate limit:</b> 10 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Assets** under the Assets category when
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
          ids: Comma-separated list of asset IDs. Limited to 100 ID's for each request.

          start_time: A start time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          type: Input stat type to query for. Valid values: `auxInput1`, `auxInput2`,
              `auxInput3`, `auxInput4`, `auxInput5`, `auxInput6`, `auxInput7`, `auxInput8`,
              `auxInput9`, `auxInput10`, `auxInput11`, `auxInput12`, `auxInput13`,
              `analogInput1Voltage`, `analogInput2Voltage`, `analogInput1Current`,
              `analogInput2Current`, `batteryVoltage`

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          end_time: An end time in RFC 3339 format. Defaults to never if not provided; if not
              provided then pagination will not cease, and a valid pagination cursor will
              always be returned. Millisecond precision and timezones are supported.
              (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          include_attributes: Optional boolean indicating whether to return attributes on supported entities

          include_external_ids: Optional boolean indicating whether to return external IDs on supported entities

          include_tags: Optional boolean indicating whether to return tags on supported entities

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/assets/inputs/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ids": ids,
                        "start_time": start_time,
                        "type": type,
                        "after": after,
                        "end_time": end_time,
                        "include_attributes": include_attributes,
                        "include_external_ids": include_external_ids,
                        "include_tags": include_tags,
                    },
                    input_stream_params.InputStreamParams,
                ),
            ),
            cast_to=InputStreamResponse,
        )


class InputsResourceWithRawResponse:
    def __init__(self, inputs: InputsResource) -> None:
        self._inputs = inputs

        self.stream = to_raw_response_wrapper(
            inputs.stream,
        )


class AsyncInputsResourceWithRawResponse:
    def __init__(self, inputs: AsyncInputsResource) -> None:
        self._inputs = inputs

        self.stream = async_to_raw_response_wrapper(
            inputs.stream,
        )


class InputsResourceWithStreamingResponse:
    def __init__(self, inputs: InputsResource) -> None:
        self._inputs = inputs

        self.stream = to_streamed_response_wrapper(
            inputs.stream,
        )


class AsyncInputsResourceWithStreamingResponse:
    def __init__(self, inputs: AsyncInputsResource) -> None:
        self._inputs = inputs

        self.stream = async_to_streamed_response_wrapper(
            inputs.stream,
        )
