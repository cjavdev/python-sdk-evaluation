# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import ifta_detail_create_csv_job_params
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
from ..types.ifta_get_ifta_detail_job_response_body import IftaGetIftaDetailJobResponseBody
from ..types.ifta_create_ifta_detail_job_response_body import IftaCreateIftaDetailJobResponseBody

__all__ = ["IftaDetailsResource", "AsyncIftaDetailsResource"]


class IftaDetailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IftaDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return IftaDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IftaDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return IftaDetailsResourceWithStreamingResponse(self)

    def create_csv_job(
        self,
        *,
        end_hour: str,
        start_hour: str,
        vehicle_ids: str | NotGiven = NOT_GIVEN,
        vehicle_parent_tag_ids: str | NotGiven = NOT_GIVEN,
        vehicle_tag_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IftaCreateIftaDetailJobResponseBody:
        """
        Create a job to generate csv files of IFTA mileage segments.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write IFTA (US)** under the Compliance category
        when creating or editing an API token.
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
          end_hour: An end time in RFC 3339 format. Hour precision and timezones are supported. Any
              minutes or seconds will be truncated down to the nearest hour. Note that the
              most recent 72 hours of data may still be processing and is subject to change
              and latency, so it is not recommended to request data for the most recent 72
              hours. The maximum request duration is 1 month. Limit the number of vehicles to
              1000 when requesting more than 24 hours of data. (Examples:
              2019-06-13T19:00:00Z, 2019-06-13T19:00:00.000Z, OR 2015-09-15T14:00:00-04:00).

          start_hour: A start time in RFC 3339 format. Hour precision and timezones are supported. Any
              minutes or seconds will be truncated down to the nearest hour. Note that the
              most recent 72 hours of data may still be processing and is subject to change
              and latency, so it is not recommended to request data for the most recent 72
              hours. The maximum request duration is 1 month. Limit the number of vehicles to
              1000 when requesting more than 24 hours of data. (Examples:
              2019-06-13T19:00:00Z, 2019-06-13T19:00:00.000Z, OR 2015-09-15T14:00:00-04:00).

          vehicle_ids: A filter on the data based on this comma-separated list of vehicle IDs and
              external IDs. The number of vehicles requested per job shouldn't exceed 5000.
              Example: `vehicleIds: '1234,5678,samsara.vin:1HGBH41JXMN109186'`

          vehicle_parent_tag_ids: A filter on the data based on this comma-separated list of vehicle parent tag
              IDs. The number of vehicles requested per job shouldn't exceed 5000. Example:
              `vehicleParentTagIds: '1234,5678'`

          vehicle_tag_ids: A filter on the data based on this comma-separated list of vehicle tag IDs. The
              number of vehicles requested per job shouldn't exceed 5000. Example:
              `vehicleTagIds: '1234,5678'`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ifta-detail/csv",
            body=maybe_transform(
                {
                    "end_hour": end_hour,
                    "start_hour": start_hour,
                    "vehicle_ids": vehicle_ids,
                    "vehicle_parent_tag_ids": vehicle_parent_tag_ids,
                    "vehicle_tag_ids": vehicle_tag_ids,
                },
                ifta_detail_create_csv_job_params.IftaDetailCreateCsvJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IftaCreateIftaDetailJobResponseBody,
        )

    def retrieve_csv_job(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IftaGetIftaDetailJobResponseBody:
        """
        Get information about an existing IFTA detail job.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read IFTA (US)** under the Compliance category
        when creating or editing an API token.
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/ifta-detail/csv/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IftaGetIftaDetailJobResponseBody,
        )


class AsyncIftaDetailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIftaDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIftaDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIftaDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncIftaDetailsResourceWithStreamingResponse(self)

    async def create_csv_job(
        self,
        *,
        end_hour: str,
        start_hour: str,
        vehicle_ids: str | NotGiven = NOT_GIVEN,
        vehicle_parent_tag_ids: str | NotGiven = NOT_GIVEN,
        vehicle_tag_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IftaCreateIftaDetailJobResponseBody:
        """
        Create a job to generate csv files of IFTA mileage segments.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write IFTA (US)** under the Compliance category
        when creating or editing an API token.
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
          end_hour: An end time in RFC 3339 format. Hour precision and timezones are supported. Any
              minutes or seconds will be truncated down to the nearest hour. Note that the
              most recent 72 hours of data may still be processing and is subject to change
              and latency, so it is not recommended to request data for the most recent 72
              hours. The maximum request duration is 1 month. Limit the number of vehicles to
              1000 when requesting more than 24 hours of data. (Examples:
              2019-06-13T19:00:00Z, 2019-06-13T19:00:00.000Z, OR 2015-09-15T14:00:00-04:00).

          start_hour: A start time in RFC 3339 format. Hour precision and timezones are supported. Any
              minutes or seconds will be truncated down to the nearest hour. Note that the
              most recent 72 hours of data may still be processing and is subject to change
              and latency, so it is not recommended to request data for the most recent 72
              hours. The maximum request duration is 1 month. Limit the number of vehicles to
              1000 when requesting more than 24 hours of data. (Examples:
              2019-06-13T19:00:00Z, 2019-06-13T19:00:00.000Z, OR 2015-09-15T14:00:00-04:00).

          vehicle_ids: A filter on the data based on this comma-separated list of vehicle IDs and
              external IDs. The number of vehicles requested per job shouldn't exceed 5000.
              Example: `vehicleIds: '1234,5678,samsara.vin:1HGBH41JXMN109186'`

          vehicle_parent_tag_ids: A filter on the data based on this comma-separated list of vehicle parent tag
              IDs. The number of vehicles requested per job shouldn't exceed 5000. Example:
              `vehicleParentTagIds: '1234,5678'`

          vehicle_tag_ids: A filter on the data based on this comma-separated list of vehicle tag IDs. The
              number of vehicles requested per job shouldn't exceed 5000. Example:
              `vehicleTagIds: '1234,5678'`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ifta-detail/csv",
            body=await async_maybe_transform(
                {
                    "end_hour": end_hour,
                    "start_hour": start_hour,
                    "vehicle_ids": vehicle_ids,
                    "vehicle_parent_tag_ids": vehicle_parent_tag_ids,
                    "vehicle_tag_ids": vehicle_tag_ids,
                },
                ifta_detail_create_csv_job_params.IftaDetailCreateCsvJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IftaCreateIftaDetailJobResponseBody,
        )

    async def retrieve_csv_job(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IftaGetIftaDetailJobResponseBody:
        """
        Get information about an existing IFTA detail job.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read IFTA (US)** under the Compliance category
        when creating or editing an API token.
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/ifta-detail/csv/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IftaGetIftaDetailJobResponseBody,
        )


class IftaDetailsResourceWithRawResponse:
    def __init__(self, ifta_details: IftaDetailsResource) -> None:
        self._ifta_details = ifta_details

        self.create_csv_job = to_raw_response_wrapper(
            ifta_details.create_csv_job,
        )
        self.retrieve_csv_job = to_raw_response_wrapper(
            ifta_details.retrieve_csv_job,
        )


class AsyncIftaDetailsResourceWithRawResponse:
    def __init__(self, ifta_details: AsyncIftaDetailsResource) -> None:
        self._ifta_details = ifta_details

        self.create_csv_job = async_to_raw_response_wrapper(
            ifta_details.create_csv_job,
        )
        self.retrieve_csv_job = async_to_raw_response_wrapper(
            ifta_details.retrieve_csv_job,
        )


class IftaDetailsResourceWithStreamingResponse:
    def __init__(self, ifta_details: IftaDetailsResource) -> None:
        self._ifta_details = ifta_details

        self.create_csv_job = to_streamed_response_wrapper(
            ifta_details.create_csv_job,
        )
        self.retrieve_csv_job = to_streamed_response_wrapper(
            ifta_details.retrieve_csv_job,
        )


class AsyncIftaDetailsResourceWithStreamingResponse:
    def __init__(self, ifta_details: AsyncIftaDetailsResource) -> None:
        self._ifta_details = ifta_details

        self.create_csv_job = async_to_streamed_response_wrapper(
            ifta_details.create_csv_job,
        )
        self.retrieve_csv_job = async_to_streamed_response_wrapper(
            ifta_details.retrieve_csv_job,
        )
