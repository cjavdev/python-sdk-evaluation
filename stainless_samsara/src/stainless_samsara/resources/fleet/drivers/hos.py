# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ....types.fleet.drivers import ho_duty_status_params

__all__ = ["HosResource", "AsyncHosResource"]


class HosResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return HosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return HosResourceWithStreamingResponse(self)

    def duty_status(
        self,
        driver_id: int,
        *,
        duty_status: str,
        location: str | NotGiven = NOT_GIVEN,
        remark: str | NotGiven = NOT_GIVEN,
        status_change_at_ms: float | NotGiven = NOT_GIVEN,
        vehicle_id: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        <n class="warning">
        <nh>
        <i class="fa fa-exclamation-circle"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Set an individual driver’s current duty status to 'On Duty' or 'Off Duty'.

        To ensure compliance with the ELD Mandate, only authenticated drivers can make
        direct duty status changes on their own logbook. Any system external to the
        Samsara Driver App using this endpoint to trigger duty status changes must
        ensure that such changes are only triggered directly by the driver in question
        and that the driver has been properly authenticated. This endpoint should not be
        used to algorithmically trigger duty status changes nor should it be used by
        personnel besides the driver to trigger duty status changes on the driver’s
        behalf. Carriers and their drivers are ultimately responsible for maintaining
        accurate logs and should confirm that their use of the endpoint is compliant
        with the ELD Mandate.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write ELD Hours of Service (US)** under the
        Compliance category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          duty_status: Duty status to set the driver to. The only supported values are 'ON_DUTY' and
              'OFF_DUTY'.

          location: Location to associate the duty status change with.

          remark: Remark to associate the duty status change with.

          status_change_at_ms: Timestamp that the duty status will begin at specified in milliseconds UNIX
              time. Defaults to the current time if left blank. This can only be set to up to
              8 hours in the past.

          vehicle_id: Vehicle ID to associate the duty status change with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/v1/fleet/drivers/{driver_id}/hos/duty_status",
            body=maybe_transform(
                {
                    "duty_status": duty_status,
                    "location": location,
                    "remark": remark,
                    "status_change_at_ms": status_change_at_ms,
                    "vehicle_id": vehicle_id,
                },
                ho_duty_status_params.HoDutyStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncHosResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncHosResourceWithStreamingResponse(self)

    async def duty_status(
        self,
        driver_id: int,
        *,
        duty_status: str,
        location: str | NotGiven = NOT_GIVEN,
        remark: str | NotGiven = NOT_GIVEN,
        status_change_at_ms: float | NotGiven = NOT_GIVEN,
        vehicle_id: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        <n class="warning">
        <nh>
        <i class="fa fa-exclamation-circle"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Set an individual driver’s current duty status to 'On Duty' or 'Off Duty'.

        To ensure compliance with the ELD Mandate, only authenticated drivers can make
        direct duty status changes on their own logbook. Any system external to the
        Samsara Driver App using this endpoint to trigger duty status changes must
        ensure that such changes are only triggered directly by the driver in question
        and that the driver has been properly authenticated. This endpoint should not be
        used to algorithmically trigger duty status changes nor should it be used by
        personnel besides the driver to trigger duty status changes on the driver’s
        behalf. Carriers and their drivers are ultimately responsible for maintaining
        accurate logs and should confirm that their use of the endpoint is compliant
        with the ELD Mandate.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write ELD Hours of Service (US)** under the
        Compliance category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          duty_status: Duty status to set the driver to. The only supported values are 'ON_DUTY' and
              'OFF_DUTY'.

          location: Location to associate the duty status change with.

          remark: Remark to associate the duty status change with.

          status_change_at_ms: Timestamp that the duty status will begin at specified in milliseconds UNIX
              time. Defaults to the current time if left blank. This can only be set to up to
              8 hours in the past.

          vehicle_id: Vehicle ID to associate the duty status change with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/v1/fleet/drivers/{driver_id}/hos/duty_status",
            body=await async_maybe_transform(
                {
                    "duty_status": duty_status,
                    "location": location,
                    "remark": remark,
                    "status_change_at_ms": status_change_at_ms,
                    "vehicle_id": vehicle_id,
                },
                ho_duty_status_params.HoDutyStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class HosResourceWithRawResponse:
    def __init__(self, hos: HosResource) -> None:
        self._hos = hos

        self.duty_status = to_raw_response_wrapper(
            hos.duty_status,
        )


class AsyncHosResourceWithRawResponse:
    def __init__(self, hos: AsyncHosResource) -> None:
        self._hos = hos

        self.duty_status = async_to_raw_response_wrapper(
            hos.duty_status,
        )


class HosResourceWithStreamingResponse:
    def __init__(self, hos: HosResource) -> None:
        self._hos = hos

        self.duty_status = to_streamed_response_wrapper(
            hos.duty_status,
        )


class AsyncHosResourceWithStreamingResponse:
    def __init__(self, hos: AsyncHosResource) -> None:
        self._hos = hos

        self.duty_status = async_to_streamed_response_wrapper(
            hos.duty_status,
        )
