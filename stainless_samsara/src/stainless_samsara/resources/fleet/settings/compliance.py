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
from ....types.fleet.settings import compliance_update_params
from ....types.fleet.settings.settings_get_compliance_settings_response_body import (
    SettingsGetComplianceSettingsResponseBody,
)
from ....types.fleet.settings.settings_patch_compliance_settings_response_body import (
    SettingsPatchComplianceSettingsResponseBody,
)

__all__ = ["ComplianceResource", "AsyncComplianceResource"]


class ComplianceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ComplianceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return ComplianceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ComplianceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return ComplianceResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingsGetComplianceSettingsResponseBody:
        """
        Get organization's compliance settings, including carrier name, office address,
        and DOT number

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
        """
        return self._get(
            "/fleet/settings/compliance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsGetComplianceSettingsResponseBody,
        )

    def update(
        self,
        *,
        allow_unregulated_vehicles_enabled: bool | NotGiven = NOT_GIVEN,
        canada_hos_enabled: bool | NotGiven = NOT_GIVEN,
        carrier_name: str | NotGiven = NOT_GIVEN,
        dot_number: int | NotGiven = NOT_GIVEN,
        driver_auto_duty_enabled: bool | NotGiven = NOT_GIVEN,
        edit_certified_logs_enabled: bool | NotGiven = NOT_GIVEN,
        force_manual_location_for_duty_status_changes_enabled: bool | NotGiven = NOT_GIVEN,
        force_review_unassigned_hos_enabled: bool | NotGiven = NOT_GIVEN,
        main_office_formatted_address: str | NotGiven = NOT_GIVEN,
        persistent_duty_status_enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingsPatchComplianceSettingsResponseBody:
        """
        Update organization's compliance settings, including carrier name, office
        address, and DOT number

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write ELD Compliance Settings (US)** under the
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
          allow_unregulated_vehicles_enabled: [deprecated] Allow Unregulated Vehicles. This setting is deprecated as all
              organizations can now mark vehicles as unregulated.

          canada_hos_enabled: Enable Canada HOS

          carrier_name: Carrier Name / Principal Place of Business Name

          dot_number: Carrier US DOT Number

          driver_auto_duty_enabled: Enable Driver Auto-Duty

          edit_certified_logs_enabled: Drivers Can Edit Certified Log

          force_manual_location_for_duty_status_changes_enabled: Force Manual Location For Duty Status Changes

          force_review_unassigned_hos_enabled: Force Review of Unassigned HOS

          main_office_formatted_address: Main Office Address / Principal Place of Businesss Address

          persistent_duty_status_enabled: Persistent Duty Status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/fleet/settings/compliance",
            body=maybe_transform(
                {
                    "allow_unregulated_vehicles_enabled": allow_unregulated_vehicles_enabled,
                    "canada_hos_enabled": canada_hos_enabled,
                    "carrier_name": carrier_name,
                    "dot_number": dot_number,
                    "driver_auto_duty_enabled": driver_auto_duty_enabled,
                    "edit_certified_logs_enabled": edit_certified_logs_enabled,
                    "force_manual_location_for_duty_status_changes_enabled": force_manual_location_for_duty_status_changes_enabled,
                    "force_review_unassigned_hos_enabled": force_review_unassigned_hos_enabled,
                    "main_office_formatted_address": main_office_formatted_address,
                    "persistent_duty_status_enabled": persistent_duty_status_enabled,
                },
                compliance_update_params.ComplianceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsPatchComplianceSettingsResponseBody,
        )


class AsyncComplianceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncComplianceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncComplianceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncComplianceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncComplianceResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingsGetComplianceSettingsResponseBody:
        """
        Get organization's compliance settings, including carrier name, office address,
        and DOT number

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
        """
        return await self._get(
            "/fleet/settings/compliance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsGetComplianceSettingsResponseBody,
        )

    async def update(
        self,
        *,
        allow_unregulated_vehicles_enabled: bool | NotGiven = NOT_GIVEN,
        canada_hos_enabled: bool | NotGiven = NOT_GIVEN,
        carrier_name: str | NotGiven = NOT_GIVEN,
        dot_number: int | NotGiven = NOT_GIVEN,
        driver_auto_duty_enabled: bool | NotGiven = NOT_GIVEN,
        edit_certified_logs_enabled: bool | NotGiven = NOT_GIVEN,
        force_manual_location_for_duty_status_changes_enabled: bool | NotGiven = NOT_GIVEN,
        force_review_unassigned_hos_enabled: bool | NotGiven = NOT_GIVEN,
        main_office_formatted_address: str | NotGiven = NOT_GIVEN,
        persistent_duty_status_enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingsPatchComplianceSettingsResponseBody:
        """
        Update organization's compliance settings, including carrier name, office
        address, and DOT number

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write ELD Compliance Settings (US)** under the
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
          allow_unregulated_vehicles_enabled: [deprecated] Allow Unregulated Vehicles. This setting is deprecated as all
              organizations can now mark vehicles as unregulated.

          canada_hos_enabled: Enable Canada HOS

          carrier_name: Carrier Name / Principal Place of Business Name

          dot_number: Carrier US DOT Number

          driver_auto_duty_enabled: Enable Driver Auto-Duty

          edit_certified_logs_enabled: Drivers Can Edit Certified Log

          force_manual_location_for_duty_status_changes_enabled: Force Manual Location For Duty Status Changes

          force_review_unassigned_hos_enabled: Force Review of Unassigned HOS

          main_office_formatted_address: Main Office Address / Principal Place of Businesss Address

          persistent_duty_status_enabled: Persistent Duty Status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/fleet/settings/compliance",
            body=await async_maybe_transform(
                {
                    "allow_unregulated_vehicles_enabled": allow_unregulated_vehicles_enabled,
                    "canada_hos_enabled": canada_hos_enabled,
                    "carrier_name": carrier_name,
                    "dot_number": dot_number,
                    "driver_auto_duty_enabled": driver_auto_duty_enabled,
                    "edit_certified_logs_enabled": edit_certified_logs_enabled,
                    "force_manual_location_for_duty_status_changes_enabled": force_manual_location_for_duty_status_changes_enabled,
                    "force_review_unassigned_hos_enabled": force_review_unassigned_hos_enabled,
                    "main_office_formatted_address": main_office_formatted_address,
                    "persistent_duty_status_enabled": persistent_duty_status_enabled,
                },
                compliance_update_params.ComplianceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsPatchComplianceSettingsResponseBody,
        )


class ComplianceResourceWithRawResponse:
    def __init__(self, compliance: ComplianceResource) -> None:
        self._compliance = compliance

        self.retrieve = to_raw_response_wrapper(
            compliance.retrieve,
        )
        self.update = to_raw_response_wrapper(
            compliance.update,
        )


class AsyncComplianceResourceWithRawResponse:
    def __init__(self, compliance: AsyncComplianceResource) -> None:
        self._compliance = compliance

        self.retrieve = async_to_raw_response_wrapper(
            compliance.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            compliance.update,
        )


class ComplianceResourceWithStreamingResponse:
    def __init__(self, compliance: ComplianceResource) -> None:
        self._compliance = compliance

        self.retrieve = to_streamed_response_wrapper(
            compliance.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            compliance.update,
        )


class AsyncComplianceResourceWithStreamingResponse:
    def __init__(self, compliance: AsyncComplianceResource) -> None:
        self._compliance = compliance

        self.retrieve = async_to_streamed_response_wrapper(
            compliance.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            compliance.update,
        )
