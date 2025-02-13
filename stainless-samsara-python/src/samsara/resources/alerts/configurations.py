# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ...types.alerts import (
    configuration_list_params,
    configuration_create_params,
    configuration_delete_params,
    configuration_update_params,
)
from ...types.alerts.configuration_list_response import ConfigurationListResponse
from ...types.alerts.configuration_create_response import ConfigurationCreateResponse
from ...types.alerts.configuration_update_response import ConfigurationUpdateResponse

__all__ = ["ConfigurationsResource", "AsyncConfigurationsResource"]


class ConfigurationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return ConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return ConfigurationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        actions: Iterable[configuration_create_params.Action],
        is_enabled: bool,
        name: str,
        scope: configuration_create_params.Scope,
        triggers: Iterable[configuration_create_params.Trigger],
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        operational_settings: configuration_create_params.OperationalSettings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationCreateResponse:
        """
        Creates an alert configuration.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Alerts** under the Alerts category when
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
          actions: An array of actions.

          is_enabled: Whether the alert is enabled or not.

          name: The custom name of the configuration.

          scope: What the triggers are scoped to. These are the objects this alert applies to.

          triggers: An array of triggers.

          external_ids: A map of external ids

          operational_settings: Settings on when the alert should be operational.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/alerts/configurations",
            body=maybe_transform(
                {
                    "actions": actions,
                    "is_enabled": is_enabled,
                    "name": name,
                    "scope": scope,
                    "triggers": triggers,
                    "external_ids": external_ids,
                    "operational_settings": operational_settings,
                },
                configuration_create_params.ConfigurationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigurationCreateResponse,
        )

    def update(
        self,
        *,
        id: str,
        actions: Iterable[configuration_update_params.Action] | NotGiven = NOT_GIVEN,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        is_enabled: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        operational_settings: configuration_update_params.OperationalSettings | NotGiven = NOT_GIVEN,
        scope: configuration_update_params.Scope | NotGiven = NOT_GIVEN,
        triggers: Iterable[configuration_update_params.Trigger] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationUpdateResponse:
        """
        Updates an alert configuration.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Alerts** under the Alerts category when
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
          id: The unqiue Samsara id of the alert configuration.

          actions: An array of actions.

          external_ids: A map of external ids

          is_enabled: Whether the alert is enabled or not.

          name: The custom name of the configuration.

          operational_settings: Settings on when the alert should be operational.

          scope: What the triggers are scoped to. These are the objects this alert applies to.

          triggers: An array of triggers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/alerts/configurations",
            body=maybe_transform(
                {
                    "id": id,
                    "actions": actions,
                    "external_ids": external_ids,
                    "is_enabled": is_enabled,
                    "name": name,
                    "operational_settings": operational_settings,
                    "scope": scope,
                    "triggers": triggers,
                },
                configuration_update_params.ConfigurationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigurationUpdateResponse,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        include_external_ids: bool | NotGiven = NOT_GIVEN,
        status: Literal["all", "enabled", "disabled"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationListResponse:
        """
        Get specified Alert Configurations.

        The following trigger types are API enabled and will show up in the results:
        Vehicle Speed Ambient Temperature Fuel Level (Percentage) Vehicle DEF Level
        (Percentage) Vehicle Battery Gateway Unplugged Dashcam Disconnected Camera
        Connector Disconnected Asset starts moving Inside Geofence Outside Geofence
        Unassigned Driving Driver HOS Violation Vehicle Engine Idle Asset Engine On
        Asset Engine Off Harsh Event Scheduled Maintenance Scheduled Maintenance by
        Odometer Scheduled Maintenance by Engine Hours Out of Route GPS Signal Loss Cell
        Signal Loss Fault Code Tire Faults Gateway Disconnected Panic Button Tampering
        Detected If vehicle is severely speeding (as defined by your organization) DVIR
        Submitted for Asset Driver Document Submitted Driver App Sign In Driver App Sign
        Out Geofence Entry Geofence Exit Route Stop ETA Alert Driver Recorded Scheduled
        Date And Time

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
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
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          ids: Filter by the IDs. Returns all if no ids are provided.

          include_external_ids: Optional boolean indicating whether to return external IDs on supported entities

          status: The status of the alert configuration. Valid values: `all`, `enabled`,
              `disabled`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/alerts/configurations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "ids": ids,
                        "include_external_ids": include_external_ids,
                        "status": status,
                    },
                    configuration_list_params.ConfigurationListParams,
                ),
            ),
            cast_to=ConfigurationListResponse,
        )

    def delete(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an alert configuration.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Alerts** under the Alerts category when
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
          id: The unqiue Samsara id of the alert configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/alerts/configurations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id": id}, configuration_delete_params.ConfigurationDeleteParams),
            ),
            cast_to=NoneType,
        )


class AsyncConfigurationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncConfigurationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        actions: Iterable[configuration_create_params.Action],
        is_enabled: bool,
        name: str,
        scope: configuration_create_params.Scope,
        triggers: Iterable[configuration_create_params.Trigger],
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        operational_settings: configuration_create_params.OperationalSettings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationCreateResponse:
        """
        Creates an alert configuration.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Alerts** under the Alerts category when
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
          actions: An array of actions.

          is_enabled: Whether the alert is enabled or not.

          name: The custom name of the configuration.

          scope: What the triggers are scoped to. These are the objects this alert applies to.

          triggers: An array of triggers.

          external_ids: A map of external ids

          operational_settings: Settings on when the alert should be operational.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/alerts/configurations",
            body=await async_maybe_transform(
                {
                    "actions": actions,
                    "is_enabled": is_enabled,
                    "name": name,
                    "scope": scope,
                    "triggers": triggers,
                    "external_ids": external_ids,
                    "operational_settings": operational_settings,
                },
                configuration_create_params.ConfigurationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigurationCreateResponse,
        )

    async def update(
        self,
        *,
        id: str,
        actions: Iterable[configuration_update_params.Action] | NotGiven = NOT_GIVEN,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        is_enabled: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        operational_settings: configuration_update_params.OperationalSettings | NotGiven = NOT_GIVEN,
        scope: configuration_update_params.Scope | NotGiven = NOT_GIVEN,
        triggers: Iterable[configuration_update_params.Trigger] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationUpdateResponse:
        """
        Updates an alert configuration.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Alerts** under the Alerts category when
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
          id: The unqiue Samsara id of the alert configuration.

          actions: An array of actions.

          external_ids: A map of external ids

          is_enabled: Whether the alert is enabled or not.

          name: The custom name of the configuration.

          operational_settings: Settings on when the alert should be operational.

          scope: What the triggers are scoped to. These are the objects this alert applies to.

          triggers: An array of triggers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/alerts/configurations",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "actions": actions,
                    "external_ids": external_ids,
                    "is_enabled": is_enabled,
                    "name": name,
                    "operational_settings": operational_settings,
                    "scope": scope,
                    "triggers": triggers,
                },
                configuration_update_params.ConfigurationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigurationUpdateResponse,
        )

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        include_external_ids: bool | NotGiven = NOT_GIVEN,
        status: Literal["all", "enabled", "disabled"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationListResponse:
        """
        Get specified Alert Configurations.

        The following trigger types are API enabled and will show up in the results:
        Vehicle Speed Ambient Temperature Fuel Level (Percentage) Vehicle DEF Level
        (Percentage) Vehicle Battery Gateway Unplugged Dashcam Disconnected Camera
        Connector Disconnected Asset starts moving Inside Geofence Outside Geofence
        Unassigned Driving Driver HOS Violation Vehicle Engine Idle Asset Engine On
        Asset Engine Off Harsh Event Scheduled Maintenance Scheduled Maintenance by
        Odometer Scheduled Maintenance by Engine Hours Out of Route GPS Signal Loss Cell
        Signal Loss Fault Code Tire Faults Gateway Disconnected Panic Button Tampering
        Detected If vehicle is severely speeding (as defined by your organization) DVIR
        Submitted for Asset Driver Document Submitted Driver App Sign In Driver App Sign
        Out Geofence Entry Geofence Exit Route Stop ETA Alert Driver Recorded Scheduled
        Date And Time

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
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
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          ids: Filter by the IDs. Returns all if no ids are provided.

          include_external_ids: Optional boolean indicating whether to return external IDs on supported entities

          status: The status of the alert configuration. Valid values: `all`, `enabled`,
              `disabled`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/alerts/configurations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "ids": ids,
                        "include_external_ids": include_external_ids,
                        "status": status,
                    },
                    configuration_list_params.ConfigurationListParams,
                ),
            ),
            cast_to=ConfigurationListResponse,
        )

    async def delete(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an alert configuration.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Alerts** under the Alerts category when
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
          id: The unqiue Samsara id of the alert configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/alerts/configurations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id": id}, configuration_delete_params.ConfigurationDeleteParams),
            ),
            cast_to=NoneType,
        )


class ConfigurationsResourceWithRawResponse:
    def __init__(self, configurations: ConfigurationsResource) -> None:
        self._configurations = configurations

        self.create = to_raw_response_wrapper(
            configurations.create,
        )
        self.update = to_raw_response_wrapper(
            configurations.update,
        )
        self.list = to_raw_response_wrapper(
            configurations.list,
        )
        self.delete = to_raw_response_wrapper(
            configurations.delete,
        )


class AsyncConfigurationsResourceWithRawResponse:
    def __init__(self, configurations: AsyncConfigurationsResource) -> None:
        self._configurations = configurations

        self.create = async_to_raw_response_wrapper(
            configurations.create,
        )
        self.update = async_to_raw_response_wrapper(
            configurations.update,
        )
        self.list = async_to_raw_response_wrapper(
            configurations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            configurations.delete,
        )


class ConfigurationsResourceWithStreamingResponse:
    def __init__(self, configurations: ConfigurationsResource) -> None:
        self._configurations = configurations

        self.create = to_streamed_response_wrapper(
            configurations.create,
        )
        self.update = to_streamed_response_wrapper(
            configurations.update,
        )
        self.list = to_streamed_response_wrapper(
            configurations.list,
        )
        self.delete = to_streamed_response_wrapper(
            configurations.delete,
        )


class AsyncConfigurationsResourceWithStreamingResponse:
    def __init__(self, configurations: AsyncConfigurationsResource) -> None:
        self._configurations = configurations

        self.create = async_to_streamed_response_wrapper(
            configurations.create,
        )
        self.update = async_to_streamed_response_wrapper(
            configurations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            configurations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            configurations.delete,
        )
