# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal

import httpx

from .inputs import (
    InputsResource,
    AsyncInputsResource,
    InputsResourceWithRawResponse,
    AsyncInputsResourceWithRawResponse,
    InputsResourceWithStreamingResponse,
    AsyncInputsResourceWithStreamingResponse,
)
from ...types import asset_list_params, asset_create_params, asset_delete_params, asset_update_params
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
from .location_and_speed import (
    LocationAndSpeedResource,
    AsyncLocationAndSpeedResource,
    LocationAndSpeedResourceWithRawResponse,
    AsyncLocationAndSpeedResourceWithRawResponse,
    LocationAndSpeedResourceWithStreamingResponse,
    AsyncLocationAndSpeedResourceWithStreamingResponse,
)
from ...types.asset_list_response import AssetListResponse
from ...types.asset_create_response import AssetCreateResponse
from ...types.asset_update_response import AssetUpdateResponse

__all__ = ["AssetsResource", "AsyncAssetsResource"]


class AssetsResource(SyncAPIResource):
    @cached_property
    def inputs(self) -> InputsResource:
        return InputsResource(self._client)

    @cached_property
    def location_and_speed(self) -> LocationAndSpeedResource:
        return LocationAndSpeedResource(self._client)

    @cached_property
    def with_raw_response(self) -> AssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AssetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        license_plate: str | NotGiven = NOT_GIVEN,
        make: str | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        regulation_mode: Literal["mixed", "regulated", "unregulated"] | NotGiven = NOT_GIVEN,
        serial_number: str | NotGiven = NOT_GIVEN,
        type: Literal["uncategorized", "trailer", "equipment", "unpowered", "vehicle"] | NotGiven = NOT_GIVEN,
        vin: str | NotGiven = NOT_GIVEN,
        year: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetCreateResponse:
        """
        Create a new asset.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Assets** under the Assets category when
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
          external_ids: A map of external ids

          license_plate: The license plate of the asset.

          make: The manufacturer of the asset. (If a VIN is entered and the system detects it is
              registered to a different manufacturer than provided an error will be returned).

          model: The manufacturer model of the asset. (If a VIN is entered and the system detects
              it is registered to a different model than provided an error will be returned).

          name: The human-readable name of the asset. This is set by a fleet administrator and
              will appear in both Samsara’s cloud dashboard as well as the Samsara Driver
              mobile app. By default, this name is the serial number of the Samsara Asset
              Gateway. It can be set or updated through the Samsara Dashboard or through the
              API at any time.

          notes: These are generic notes about the asset. Can be set or updated through the
              Samsara Dashboard or the API at any time.

          regulation_mode: Whether or not the asset is regulated, unregulated (non-CMV), or a mixed use
              unregulated asset. Primarily used with vehicles. Valid values: `mixed`,
              `regulated`, `unregulated`

          serial_number: The serial number of the asset.

          type: The operational context in which the asset interacts with the Samsara system.
              Examples: Vehicle (eg: truck, bus...), Trailer (eg: dry van, reefer,
              flatbed...), Powered Equipment (eg: dozer, crane...), Unpowered Equipment (eg:
              container, dumpster...), or Uncategorized. Valid values: `uncategorized`,
              `trailer`, `equipment`, `unpowered`, `vehicle`

          vin: The vehicle identification number of the asset.

          year: The year of manufacture of the asset. (If a VIN is entered and the system
              detects it is registered to a different year than provided an error will be
              returned).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/assets",
            body=maybe_transform(
                {
                    "external_ids": external_ids,
                    "license_plate": license_plate,
                    "make": make,
                    "model": model,
                    "name": name,
                    "notes": notes,
                    "regulation_mode": regulation_mode,
                    "serial_number": serial_number,
                    "type": type,
                    "vin": vin,
                    "year": year,
                },
                asset_create_params.AssetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetCreateResponse,
        )

    def update(
        self,
        *,
        id: str,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        license_plate: str | NotGiven = NOT_GIVEN,
        make: str | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        regulation_mode: Literal["mixed", "regulated", "unregulated"] | NotGiven = NOT_GIVEN,
        serial_number: str | NotGiven = NOT_GIVEN,
        type: Literal["uncategorized", "trailer", "equipment", "unpowered", "vehicle"] | NotGiven = NOT_GIVEN,
        vin: str | NotGiven = NOT_GIVEN,
        year: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetUpdateResponse:
        """
        Update an existing asset.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Assets** under the Assets category when
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
          id: A filter selecting a single asset by id.

          external_ids: A map of external ids

          license_plate: The license plate of the asset.

          make: The manufacturer of the asset. (If a VIN is entered and the system detects it is
              registered to a different manufacturer than provided an error will be returned).

          model: The manufacturer model of the asset. (If a VIN is entered and the system detects
              it is registered to a different model than provided an error will be returned).

          name: The human-readable name of the asset. This is set by a fleet administrator and
              will appear in both Samsara’s cloud dashboard as well as the Samsara Driver
              mobile app. By default, this name is the serial number of the Samsara Asset
              Gateway. It can be set or updated through the Samsara Dashboard or through the
              API at any time.

          notes: These are generic notes about the asset. Can be set or updated through the
              Samsara Dashboard or the API at any time.

          regulation_mode: Whether or not the asset is regulated, unregulated (non-CMV), or a mixed use
              unregulated asset. Primarily used with vehicles. Valid values: `mixed`,
              `regulated`, `unregulated`

          serial_number: The serial number of the asset.

          type: The operational context in which the asset interacts with the Samsara system.
              Examples: Vehicle (eg: truck, bus...), Trailer (eg: dry van, reefer,
              flatbed...), Powered Equipment (eg: dozer, crane...), Unpowered Equipment (eg:
              container, dumpster...), or Uncategorized. Valid values: `uncategorized`,
              `trailer`, `equipment`, `unpowered`, `vehicle`

          vin: The vehicle identification number of the asset.

          year: The year of manufacture of the asset. (If a VIN is entered and the system
              detects it is registered to a different year than provided an error will be
              returned).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/assets",
            body=maybe_transform(
                {
                    "external_ids": external_ids,
                    "license_plate": license_plate,
                    "make": make,
                    "model": model,
                    "name": name,
                    "notes": notes,
                    "regulation_mode": regulation_mode,
                    "serial_number": serial_number,
                    "type": type,
                    "vin": vin,
                    "year": year,
                },
                asset_update_params.AssetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id": id}, asset_update_params.AssetUpdateParams),
            ),
            cast_to=AssetUpdateResponse,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        attribute_value_ids: str | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        include_external_ids: bool | NotGiven = NOT_GIVEN,
        include_tags: bool | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        type: Literal["uncategorized", "trailer", "equipment", "unpowered", "vehicle"] | NotGiven = NOT_GIVEN,
        updated_after_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetListResponse:
        """List all assets.

        Up to 300 assets will be returned per page.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
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
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          attribute_value_ids: A filter on the data based on this comma-separated list of attribute value IDs.
              Only entities associated with ALL of the referenced values will be returned
              (i.e. the intersection of the sets of entities with each value). Example:
              `attributeValueIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`

          ids: A filter on the data based on this comma-separated list of asset IDs and
              External IDs.

          include_external_ids: Optional boolean indicating whether to return external IDs on supported entities

          include_tags: Optional boolean indicating whether to return tags on supported entities

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          type: The operational context in which the asset interacts with the Samsara system.
              Examples: Vehicle (eg: truck, bus...), Trailer (eg: dry van, reefer,
              flatbed...), Powered Equipment (eg: dozer, crane...), Unpowered Equipment (eg:
              container, dumpster...), or Uncategorized. Valid values: `uncategorized`,
              `trailer`, `equipment`, `unpowered`, `vehicle`

          updated_after_time: A filter on data to have an updated at time after or equal to this specified
              time in RFC 3339 format. Millisecond precision and timezones are supported.
              (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/assets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "attribute_value_ids": attribute_value_ids,
                        "ids": ids,
                        "include_external_ids": include_external_ids,
                        "include_tags": include_tags,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                        "type": type,
                        "updated_after_time": updated_after_time,
                    },
                    asset_list_params.AssetListParams,
                ),
            ),
            cast_to=AssetListResponse,
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
        Delete an existing asset.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Assets** under the Assets category when
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
          id: A filter selecting a single asset by id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/assets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id": id}, asset_delete_params.AssetDeleteParams),
            ),
            cast_to=NoneType,
        )


class AsyncAssetsResource(AsyncAPIResource):
    @cached_property
    def inputs(self) -> AsyncInputsResource:
        return AsyncInputsResource(self._client)

    @cached_property
    def location_and_speed(self) -> AsyncLocationAndSpeedResource:
        return AsyncLocationAndSpeedResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncAssetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        license_plate: str | NotGiven = NOT_GIVEN,
        make: str | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        regulation_mode: Literal["mixed", "regulated", "unregulated"] | NotGiven = NOT_GIVEN,
        serial_number: str | NotGiven = NOT_GIVEN,
        type: Literal["uncategorized", "trailer", "equipment", "unpowered", "vehicle"] | NotGiven = NOT_GIVEN,
        vin: str | NotGiven = NOT_GIVEN,
        year: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetCreateResponse:
        """
        Create a new asset.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Assets** under the Assets category when
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
          external_ids: A map of external ids

          license_plate: The license plate of the asset.

          make: The manufacturer of the asset. (If a VIN is entered and the system detects it is
              registered to a different manufacturer than provided an error will be returned).

          model: The manufacturer model of the asset. (If a VIN is entered and the system detects
              it is registered to a different model than provided an error will be returned).

          name: The human-readable name of the asset. This is set by a fleet administrator and
              will appear in both Samsara’s cloud dashboard as well as the Samsara Driver
              mobile app. By default, this name is the serial number of the Samsara Asset
              Gateway. It can be set or updated through the Samsara Dashboard or through the
              API at any time.

          notes: These are generic notes about the asset. Can be set or updated through the
              Samsara Dashboard or the API at any time.

          regulation_mode: Whether or not the asset is regulated, unregulated (non-CMV), or a mixed use
              unregulated asset. Primarily used with vehicles. Valid values: `mixed`,
              `regulated`, `unregulated`

          serial_number: The serial number of the asset.

          type: The operational context in which the asset interacts with the Samsara system.
              Examples: Vehicle (eg: truck, bus...), Trailer (eg: dry van, reefer,
              flatbed...), Powered Equipment (eg: dozer, crane...), Unpowered Equipment (eg:
              container, dumpster...), or Uncategorized. Valid values: `uncategorized`,
              `trailer`, `equipment`, `unpowered`, `vehicle`

          vin: The vehicle identification number of the asset.

          year: The year of manufacture of the asset. (If a VIN is entered and the system
              detects it is registered to a different year than provided an error will be
              returned).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/assets",
            body=await async_maybe_transform(
                {
                    "external_ids": external_ids,
                    "license_plate": license_plate,
                    "make": make,
                    "model": model,
                    "name": name,
                    "notes": notes,
                    "regulation_mode": regulation_mode,
                    "serial_number": serial_number,
                    "type": type,
                    "vin": vin,
                    "year": year,
                },
                asset_create_params.AssetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetCreateResponse,
        )

    async def update(
        self,
        *,
        id: str,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        license_plate: str | NotGiven = NOT_GIVEN,
        make: str | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        regulation_mode: Literal["mixed", "regulated", "unregulated"] | NotGiven = NOT_GIVEN,
        serial_number: str | NotGiven = NOT_GIVEN,
        type: Literal["uncategorized", "trailer", "equipment", "unpowered", "vehicle"] | NotGiven = NOT_GIVEN,
        vin: str | NotGiven = NOT_GIVEN,
        year: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetUpdateResponse:
        """
        Update an existing asset.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Assets** under the Assets category when
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
          id: A filter selecting a single asset by id.

          external_ids: A map of external ids

          license_plate: The license plate of the asset.

          make: The manufacturer of the asset. (If a VIN is entered and the system detects it is
              registered to a different manufacturer than provided an error will be returned).

          model: The manufacturer model of the asset. (If a VIN is entered and the system detects
              it is registered to a different model than provided an error will be returned).

          name: The human-readable name of the asset. This is set by a fleet administrator and
              will appear in both Samsara’s cloud dashboard as well as the Samsara Driver
              mobile app. By default, this name is the serial number of the Samsara Asset
              Gateway. It can be set or updated through the Samsara Dashboard or through the
              API at any time.

          notes: These are generic notes about the asset. Can be set or updated through the
              Samsara Dashboard or the API at any time.

          regulation_mode: Whether or not the asset is regulated, unregulated (non-CMV), or a mixed use
              unregulated asset. Primarily used with vehicles. Valid values: `mixed`,
              `regulated`, `unregulated`

          serial_number: The serial number of the asset.

          type: The operational context in which the asset interacts with the Samsara system.
              Examples: Vehicle (eg: truck, bus...), Trailer (eg: dry van, reefer,
              flatbed...), Powered Equipment (eg: dozer, crane...), Unpowered Equipment (eg:
              container, dumpster...), or Uncategorized. Valid values: `uncategorized`,
              `trailer`, `equipment`, `unpowered`, `vehicle`

          vin: The vehicle identification number of the asset.

          year: The year of manufacture of the asset. (If a VIN is entered and the system
              detects it is registered to a different year than provided an error will be
              returned).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/assets",
            body=await async_maybe_transform(
                {
                    "external_ids": external_ids,
                    "license_plate": license_plate,
                    "make": make,
                    "model": model,
                    "name": name,
                    "notes": notes,
                    "regulation_mode": regulation_mode,
                    "serial_number": serial_number,
                    "type": type,
                    "vin": vin,
                    "year": year,
                },
                asset_update_params.AssetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id": id}, asset_update_params.AssetUpdateParams),
            ),
            cast_to=AssetUpdateResponse,
        )

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        attribute_value_ids: str | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        include_external_ids: bool | NotGiven = NOT_GIVEN,
        include_tags: bool | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        type: Literal["uncategorized", "trailer", "equipment", "unpowered", "vehicle"] | NotGiven = NOT_GIVEN,
        updated_after_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetListResponse:
        """List all assets.

        Up to 300 assets will be returned per page.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
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
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          attribute_value_ids: A filter on the data based on this comma-separated list of attribute value IDs.
              Only entities associated with ALL of the referenced values will be returned
              (i.e. the intersection of the sets of entities with each value). Example:
              `attributeValueIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`

          ids: A filter on the data based on this comma-separated list of asset IDs and
              External IDs.

          include_external_ids: Optional boolean indicating whether to return external IDs on supported entities

          include_tags: Optional boolean indicating whether to return tags on supported entities

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          type: The operational context in which the asset interacts with the Samsara system.
              Examples: Vehicle (eg: truck, bus...), Trailer (eg: dry van, reefer,
              flatbed...), Powered Equipment (eg: dozer, crane...), Unpowered Equipment (eg:
              container, dumpster...), or Uncategorized. Valid values: `uncategorized`,
              `trailer`, `equipment`, `unpowered`, `vehicle`

          updated_after_time: A filter on data to have an updated at time after or equal to this specified
              time in RFC 3339 format. Millisecond precision and timezones are supported.
              (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/assets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "attribute_value_ids": attribute_value_ids,
                        "ids": ids,
                        "include_external_ids": include_external_ids,
                        "include_tags": include_tags,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                        "type": type,
                        "updated_after_time": updated_after_time,
                    },
                    asset_list_params.AssetListParams,
                ),
            ),
            cast_to=AssetListResponse,
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
        Delete an existing asset.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Assets** under the Assets category when
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
          id: A filter selecting a single asset by id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/assets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id": id}, asset_delete_params.AssetDeleteParams),
            ),
            cast_to=NoneType,
        )


class AssetsResourceWithRawResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.create = to_raw_response_wrapper(
            assets.create,
        )
        self.update = to_raw_response_wrapper(
            assets.update,
        )
        self.list = to_raw_response_wrapper(
            assets.list,
        )
        self.delete = to_raw_response_wrapper(
            assets.delete,
        )

    @cached_property
    def inputs(self) -> InputsResourceWithRawResponse:
        return InputsResourceWithRawResponse(self._assets.inputs)

    @cached_property
    def location_and_speed(self) -> LocationAndSpeedResourceWithRawResponse:
        return LocationAndSpeedResourceWithRawResponse(self._assets.location_and_speed)


class AsyncAssetsResourceWithRawResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.create = async_to_raw_response_wrapper(
            assets.create,
        )
        self.update = async_to_raw_response_wrapper(
            assets.update,
        )
        self.list = async_to_raw_response_wrapper(
            assets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            assets.delete,
        )

    @cached_property
    def inputs(self) -> AsyncInputsResourceWithRawResponse:
        return AsyncInputsResourceWithRawResponse(self._assets.inputs)

    @cached_property
    def location_and_speed(self) -> AsyncLocationAndSpeedResourceWithRawResponse:
        return AsyncLocationAndSpeedResourceWithRawResponse(self._assets.location_and_speed)


class AssetsResourceWithStreamingResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.create = to_streamed_response_wrapper(
            assets.create,
        )
        self.update = to_streamed_response_wrapper(
            assets.update,
        )
        self.list = to_streamed_response_wrapper(
            assets.list,
        )
        self.delete = to_streamed_response_wrapper(
            assets.delete,
        )

    @cached_property
    def inputs(self) -> InputsResourceWithStreamingResponse:
        return InputsResourceWithStreamingResponse(self._assets.inputs)

    @cached_property
    def location_and_speed(self) -> LocationAndSpeedResourceWithStreamingResponse:
        return LocationAndSpeedResourceWithStreamingResponse(self._assets.location_and_speed)


class AsyncAssetsResourceWithStreamingResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.create = async_to_streamed_response_wrapper(
            assets.create,
        )
        self.update = async_to_streamed_response_wrapper(
            assets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            assets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            assets.delete,
        )

    @cached_property
    def inputs(self) -> AsyncInputsResourceWithStreamingResponse:
        return AsyncInputsResourceWithStreamingResponse(self._assets.inputs)

    @cached_property
    def location_and_speed(self) -> AsyncLocationAndSpeedResourceWithStreamingResponse:
        return AsyncLocationAndSpeedResourceWithStreamingResponse(self._assets.location_and_speed)
