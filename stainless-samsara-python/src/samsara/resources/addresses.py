# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal

import httpx

from ..types import address_list_params, address_create_params, address_modify_params
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
from ..types.address import Address
from ..types.address_list_response import AddressListResponse

__all__ = ["AddressesResource", "AsyncAddressesResource"]


class AddressesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AddressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AddressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AddressesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        formatted_address: str,
        geofence: address_create_params.Geofence,
        name: str,
        address_types: List[Literal["yard", "shortHaul", "workforceSite", "riskZone", "industrialSite", "alertsOnly"]]
        | NotGiven = NOT_GIVEN,
        contact_ids: List[str] | NotGiven = NOT_GIVEN,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        latitude: float | NotGiven = NOT_GIVEN,
        longitude: float | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Address:
        """
        Creates a new address in the organization.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Addresses** under the Addresses category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          formatted_address: The full street address for this address/geofence, as it might be recognized by
              Google Maps.

          geofence: The geofence that defines this address and its bounds. This can either be a
              circle or a polygon, but not both.

          name: Name of the address.

          address_types: Reporting location type associated with the address (used for ELD reporting
              purposes). Valid values: `yard`, `shortHaul`, `workforceSite`, `riskZone`,
              `industrialSite`, `alertsOnly`.

          contact_ids: An array of Contact IDs associated with this Address.

          external_ids: The [external IDs](https://developers.samsara.com/docs/external-ids) for the
              given object.

          latitude: Latitude of the address. Will be geocoded from `formattedAddress` if not
              provided.

          longitude: Longitude of the address. Will be geocoded from `formattedAddress` if not
              provided.

          notes: Notes about the address.

          tag_ids: An array of IDs of tags to associate with this address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/addresses",
            body=maybe_transform(
                {
                    "formatted_address": formatted_address,
                    "geofence": geofence,
                    "name": name,
                    "address_types": address_types,
                    "contact_ids": contact_ids,
                    "external_ids": external_ids,
                    "latitude": latitude,
                    "longitude": longitude,
                    "notes": notes,
                    "tag_ids": tag_ids,
                },
                address_create_params.AddressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Address,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Address:
        """
        Returns a specific address.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Addresses** under the Addresses category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/addresses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Address,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        created_after_time: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressListResponse:
        """
        Returns a list of all addresses in an organization.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Addresses** under the Addresses category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          created_after_time: A filter on data to have a created at time after or equal to this specified time
              in RFC 3339 format. Millisecond precision and timezones are supported.
              (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          limit: The limit for how many objects will be in the response. Default and max for this
              value is 512 objects.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/addresses",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "created_after_time": created_after_time,
                        "limit": limit,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                    },
                    address_list_params.AddressListParams,
                ),
            ),
            cast_to=AddressListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Delete a specific address.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Addresses** under the Addresses category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/addresses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def modify(
        self,
        id: str,
        *,
        address_types: List[Literal["yard", "shortHaul", "workforceSite", "riskZone", "industrialSite", "alertsOnly"]]
        | NotGiven = NOT_GIVEN,
        contact_ids: List[str] | NotGiven = NOT_GIVEN,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        formatted_address: str | NotGiven = NOT_GIVEN,
        geofence: address_modify_params.Geofence | NotGiven = NOT_GIVEN,
        latitude: float | NotGiven = NOT_GIVEN,
        longitude: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Address:
        """
        Update a specific address.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Addresses** under the Addresses category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          address_types: Reporting location type associated with the address (used for ELD reporting
              purposes). Valid values: `yard`, `shortHaul`, `workforceSite`, `riskZone`,
              `industrialSite`, `alertsOnly`.

          contact_ids: An array of Contact IDs associated with this Address.

          external_ids: The [external IDs](https://developers.samsara.com/docs/external-ids) for the
              given object.

          formatted_address: The full street address for this address/geofence, as it might be recognized by
              Google Maps.

          geofence: The geofence that defines this address and its bounds. This can either be a
              circle or a polygon, but not both.

          latitude: Latitude of the address. Will be geocoded from `formattedAddress` if not
              provided.

          longitude: Longitude of the address. Will be geocoded from `formattedAddress` if not
              provided.

          name: Name of the address.

          notes: Notes about the address.

          tag_ids: An array of IDs of tags to associate with this address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/addresses/{id}",
            body=maybe_transform(
                {
                    "address_types": address_types,
                    "contact_ids": contact_ids,
                    "external_ids": external_ids,
                    "formatted_address": formatted_address,
                    "geofence": geofence,
                    "latitude": latitude,
                    "longitude": longitude,
                    "name": name,
                    "notes": notes,
                    "tag_ids": tag_ids,
                },
                address_modify_params.AddressModifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Address,
        )


class AsyncAddressesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAddressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAddressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncAddressesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        formatted_address: str,
        geofence: address_create_params.Geofence,
        name: str,
        address_types: List[Literal["yard", "shortHaul", "workforceSite", "riskZone", "industrialSite", "alertsOnly"]]
        | NotGiven = NOT_GIVEN,
        contact_ids: List[str] | NotGiven = NOT_GIVEN,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        latitude: float | NotGiven = NOT_GIVEN,
        longitude: float | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Address:
        """
        Creates a new address in the organization.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Addresses** under the Addresses category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          formatted_address: The full street address for this address/geofence, as it might be recognized by
              Google Maps.

          geofence: The geofence that defines this address and its bounds. This can either be a
              circle or a polygon, but not both.

          name: Name of the address.

          address_types: Reporting location type associated with the address (used for ELD reporting
              purposes). Valid values: `yard`, `shortHaul`, `workforceSite`, `riskZone`,
              `industrialSite`, `alertsOnly`.

          contact_ids: An array of Contact IDs associated with this Address.

          external_ids: The [external IDs](https://developers.samsara.com/docs/external-ids) for the
              given object.

          latitude: Latitude of the address. Will be geocoded from `formattedAddress` if not
              provided.

          longitude: Longitude of the address. Will be geocoded from `formattedAddress` if not
              provided.

          notes: Notes about the address.

          tag_ids: An array of IDs of tags to associate with this address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/addresses",
            body=await async_maybe_transform(
                {
                    "formatted_address": formatted_address,
                    "geofence": geofence,
                    "name": name,
                    "address_types": address_types,
                    "contact_ids": contact_ids,
                    "external_ids": external_ids,
                    "latitude": latitude,
                    "longitude": longitude,
                    "notes": notes,
                    "tag_ids": tag_ids,
                },
                address_create_params.AddressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Address,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Address:
        """
        Returns a specific address.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Addresses** under the Addresses category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/addresses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Address,
        )

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        created_after_time: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressListResponse:
        """
        Returns a list of all addresses in an organization.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Addresses** under the Addresses category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          created_after_time: A filter on data to have a created at time after or equal to this specified time
              in RFC 3339 format. Millisecond precision and timezones are supported.
              (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          limit: The limit for how many objects will be in the response. Default and max for this
              value is 512 objects.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/addresses",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "created_after_time": created_after_time,
                        "limit": limit,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                    },
                    address_list_params.AddressListParams,
                ),
            ),
            cast_to=AddressListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Delete a specific address.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Addresses** under the Addresses category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/addresses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def modify(
        self,
        id: str,
        *,
        address_types: List[Literal["yard", "shortHaul", "workforceSite", "riskZone", "industrialSite", "alertsOnly"]]
        | NotGiven = NOT_GIVEN,
        contact_ids: List[str] | NotGiven = NOT_GIVEN,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        formatted_address: str | NotGiven = NOT_GIVEN,
        geofence: address_modify_params.Geofence | NotGiven = NOT_GIVEN,
        latitude: float | NotGiven = NOT_GIVEN,
        longitude: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Address:
        """
        Update a specific address.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Addresses** under the Addresses category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          address_types: Reporting location type associated with the address (used for ELD reporting
              purposes). Valid values: `yard`, `shortHaul`, `workforceSite`, `riskZone`,
              `industrialSite`, `alertsOnly`.

          contact_ids: An array of Contact IDs associated with this Address.

          external_ids: The [external IDs](https://developers.samsara.com/docs/external-ids) for the
              given object.

          formatted_address: The full street address for this address/geofence, as it might be recognized by
              Google Maps.

          geofence: The geofence that defines this address and its bounds. This can either be a
              circle or a polygon, but not both.

          latitude: Latitude of the address. Will be geocoded from `formattedAddress` if not
              provided.

          longitude: Longitude of the address. Will be geocoded from `formattedAddress` if not
              provided.

          name: Name of the address.

          notes: Notes about the address.

          tag_ids: An array of IDs of tags to associate with this address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/addresses/{id}",
            body=await async_maybe_transform(
                {
                    "address_types": address_types,
                    "contact_ids": contact_ids,
                    "external_ids": external_ids,
                    "formatted_address": formatted_address,
                    "geofence": geofence,
                    "latitude": latitude,
                    "longitude": longitude,
                    "name": name,
                    "notes": notes,
                    "tag_ids": tag_ids,
                },
                address_modify_params.AddressModifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Address,
        )


class AddressesResourceWithRawResponse:
    def __init__(self, addresses: AddressesResource) -> None:
        self._addresses = addresses

        self.create = to_raw_response_wrapper(
            addresses.create,
        )
        self.retrieve = to_raw_response_wrapper(
            addresses.retrieve,
        )
        self.list = to_raw_response_wrapper(
            addresses.list,
        )
        self.delete = to_raw_response_wrapper(
            addresses.delete,
        )
        self.modify = to_raw_response_wrapper(
            addresses.modify,
        )


class AsyncAddressesResourceWithRawResponse:
    def __init__(self, addresses: AsyncAddressesResource) -> None:
        self._addresses = addresses

        self.create = async_to_raw_response_wrapper(
            addresses.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            addresses.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            addresses.list,
        )
        self.delete = async_to_raw_response_wrapper(
            addresses.delete,
        )
        self.modify = async_to_raw_response_wrapper(
            addresses.modify,
        )


class AddressesResourceWithStreamingResponse:
    def __init__(self, addresses: AddressesResource) -> None:
        self._addresses = addresses

        self.create = to_streamed_response_wrapper(
            addresses.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            addresses.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            addresses.list,
        )
        self.delete = to_streamed_response_wrapper(
            addresses.delete,
        )
        self.modify = to_streamed_response_wrapper(
            addresses.modify,
        )


class AsyncAddressesResourceWithStreamingResponse:
    def __init__(self, addresses: AsyncAddressesResource) -> None:
        self._addresses = addresses

        self.create = async_to_streamed_response_wrapper(
            addresses.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            addresses.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            addresses.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            addresses.delete,
        )
        self.modify = async_to_streamed_response_wrapper(
            addresses.modify,
        )
