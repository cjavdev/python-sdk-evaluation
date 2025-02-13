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
from ...types.hos import violation_list_params
from ..._base_client import make_request_options
from ...types.hos.violation_list_response import ViolationListResponse

__all__ = ["ViolationsResource", "AsyncViolationsResource"]


class ViolationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ViolationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return ViolationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ViolationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return ViolationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        driver_ids: List[str] | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        start_time: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        types: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ViolationListResponse:
        """
        Get active Hours of Service violations for the specified drivers.

        The day object time range for a violation is defined by the `driver`'s
        `eldDayStartHour`. This value is configurable per driver.

        The `startTime` and `endTime` parameters indicate the datetime range you'd like
        to retrieve violations for. A violation will be returned if its
        `violationStartTime` falls within this datetime range (inclusive of `startTime`
        and `endTime`)

        **Note:** The following are all the violation types with a short explanation
        about what each of them means: `californiaMealbreakMissed` (Missed California
        Meal Break), `cycleHoursOn` (Cycle Limit), `cycleOffHoursAfterOnDutyHours`
        (Cycle 2 Limit), `dailyDrivingHours` (Daily Driving Limit),
        `dailyOffDutyDeferralAddToDay2Consecutive` (Daily Off-Duty Deferral: Add To Day2
        Consecutive), `dailyOffDutyDeferralNotPartMandatory` (Daily Off-Duty Deferral:
        Not Part Of Mandatory), `dailyOffDutyDeferralTwoDayDrivingLimit` (Daily Off-Duty
        Deferral: 2 Day Driving Limit), `dailyOffDutyDeferralTwoDayOffDuty` (Daily
        Off-Duty Deferral: 2 Day Off Duty), `dailyOffDutyNonResetHours` (Daily Off-Duty
        Time: Non-Reset), `dailyOffDutyTotalHours` (Daily Off-Duty Time),
        `dailyOnDutyHours` (Daily On-Duty Limit), `mandatory24HoursOffDuty` (24 Hours of
        Off Duty required), `restbreakMissed` (Missed Rest Break), `shiftDrivingHours`
        (Shift Driving Limit), `shiftHours` (Shift Duty Limit), `shiftOnDutyHours`
        (Shift On-Duty Limit), `unsubmittedLogs` (Missing Driver Certification)

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read ELD Compliance Settings (US)** under the
        Compliance category when creating or editing an API token.
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
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          driver_ids: A filter on the data based on this comma-separated list of driver IDs and
              externalIds. Example: `driverIds=1234,5678,payroll:4841`

          end_time: An end time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          start_time: A start time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          types:
              A filter on violations data based on the violation type enum. Supported types:
              `NONE, californiaMealbreakMissed, cycleHoursOn, cycleOffHoursAfterOnDutyHours, dailyDrivingHours, dailyOffDutyDeferralAddToDay2Consecutive, dailyOffDutyDeferralNotPartMandatory, dailyOffDutyDeferralTwoDayDrivingLimit, dailyOffDutyDeferralTwoDayOffDuty, dailyOffDutyNonResetHours, dailyOffDutyTotalHours, dailyOnDutyHours, mandatory24HoursOffDuty, restbreakMissed, shiftDrivingHours, shiftHours, shiftOnDutyHours, unsubmittedLogs`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/fleet/hos/violations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "driver_ids": driver_ids,
                        "end_time": end_time,
                        "parent_tag_ids": parent_tag_ids,
                        "start_time": start_time,
                        "tag_ids": tag_ids,
                        "types": types,
                    },
                    violation_list_params.ViolationListParams,
                ),
            ),
            cast_to=ViolationListResponse,
        )


class AsyncViolationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncViolationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncViolationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncViolationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncViolationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        driver_ids: List[str] | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        start_time: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        types: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ViolationListResponse:
        """
        Get active Hours of Service violations for the specified drivers.

        The day object time range for a violation is defined by the `driver`'s
        `eldDayStartHour`. This value is configurable per driver.

        The `startTime` and `endTime` parameters indicate the datetime range you'd like
        to retrieve violations for. A violation will be returned if its
        `violationStartTime` falls within this datetime range (inclusive of `startTime`
        and `endTime`)

        **Note:** The following are all the violation types with a short explanation
        about what each of them means: `californiaMealbreakMissed` (Missed California
        Meal Break), `cycleHoursOn` (Cycle Limit), `cycleOffHoursAfterOnDutyHours`
        (Cycle 2 Limit), `dailyDrivingHours` (Daily Driving Limit),
        `dailyOffDutyDeferralAddToDay2Consecutive` (Daily Off-Duty Deferral: Add To Day2
        Consecutive), `dailyOffDutyDeferralNotPartMandatory` (Daily Off-Duty Deferral:
        Not Part Of Mandatory), `dailyOffDutyDeferralTwoDayDrivingLimit` (Daily Off-Duty
        Deferral: 2 Day Driving Limit), `dailyOffDutyDeferralTwoDayOffDuty` (Daily
        Off-Duty Deferral: 2 Day Off Duty), `dailyOffDutyNonResetHours` (Daily Off-Duty
        Time: Non-Reset), `dailyOffDutyTotalHours` (Daily Off-Duty Time),
        `dailyOnDutyHours` (Daily On-Duty Limit), `mandatory24HoursOffDuty` (24 Hours of
        Off Duty required), `restbreakMissed` (Missed Rest Break), `shiftDrivingHours`
        (Shift Driving Limit), `shiftHours` (Shift Duty Limit), `shiftOnDutyHours`
        (Shift On-Duty Limit), `unsubmittedLogs` (Missing Driver Certification)

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read ELD Compliance Settings (US)** under the
        Compliance category when creating or editing an API token.
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
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          driver_ids: A filter on the data based on this comma-separated list of driver IDs and
              externalIds. Example: `driverIds=1234,5678,payroll:4841`

          end_time: An end time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          start_time: A start time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          types:
              A filter on violations data based on the violation type enum. Supported types:
              `NONE, californiaMealbreakMissed, cycleHoursOn, cycleOffHoursAfterOnDutyHours, dailyDrivingHours, dailyOffDutyDeferralAddToDay2Consecutive, dailyOffDutyDeferralNotPartMandatory, dailyOffDutyDeferralTwoDayDrivingLimit, dailyOffDutyDeferralTwoDayOffDuty, dailyOffDutyNonResetHours, dailyOffDutyTotalHours, dailyOnDutyHours, mandatory24HoursOffDuty, restbreakMissed, shiftDrivingHours, shiftHours, shiftOnDutyHours, unsubmittedLogs`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/fleet/hos/violations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "driver_ids": driver_ids,
                        "end_time": end_time,
                        "parent_tag_ids": parent_tag_ids,
                        "start_time": start_time,
                        "tag_ids": tag_ids,
                        "types": types,
                    },
                    violation_list_params.ViolationListParams,
                ),
            ),
            cast_to=ViolationListResponse,
        )


class ViolationsResourceWithRawResponse:
    def __init__(self, violations: ViolationsResource) -> None:
        self._violations = violations

        self.list = to_raw_response_wrapper(
            violations.list,
        )


class AsyncViolationsResourceWithRawResponse:
    def __init__(self, violations: AsyncViolationsResource) -> None:
        self._violations = violations

        self.list = async_to_raw_response_wrapper(
            violations.list,
        )


class ViolationsResourceWithStreamingResponse:
    def __init__(self, violations: ViolationsResource) -> None:
        self._violations = violations

        self.list = to_streamed_response_wrapper(
            violations.list,
        )


class AsyncViolationsResourceWithStreamingResponse:
    def __init__(self, violations: AsyncViolationsResource) -> None:
        self._violations = violations

        self.list = async_to_streamed_response_wrapper(
            violations.list,
        )
