# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal

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
from .data_outputs import (
    DataOutputsResource,
    AsyncDataOutputsResource,
    DataOutputsResourceWithRawResponse,
    AsyncDataOutputsResourceWithRawResponse,
    DataOutputsResourceWithStreamingResponse,
    AsyncDataOutputsResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.industrial import asset_list_params, asset_create_params, asset_update_params
from ....types.industrial.inline_response_200 import InlineResponse200
from ....types.industrial.list_industrial_assets_response import ListIndustrialAssetsResponse

__all__ = ["AssetsResource", "AsyncAssetsResource"]


class AssetsResource(SyncAPIResource):
    @cached_property
    def data_outputs(self) -> DataOutputsResource:
        return DataOutputsResource(self._client)

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
        name: str,
        custom_metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        location: asset_create_params.Location | NotGiven = NOT_GIVEN,
        location_data_input_id: str | NotGiven = NOT_GIVEN,
        location_type: Literal["point", "address", "dataInput"] | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        running_status_data_input_id: str | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InlineResponse200:
        """
        Create an asset with optional configuration parameters.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Equipment** under the Equipment category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          name: The name of the asset.

          custom_metadata: The custom fields of an asset.

          location: For locationType "point", latitude and longitude are required. For "address",
              formattedAddress must be provided, and lat/long can be optionally included for
              displaying a dot on the assets map. For "dataInput", this object should not be
              passed in.

          location_data_input_id: Required if locationType is "dataInput". Specifies the id of a location data
              input which will determine the asset's location. **The data input will be moved
              to the new asset.**

          location_type: The format of the location. This field is required if a location is provided.
              Valid values: `point`, `address`, `dataInput`.

          parent_id: The id of the parent asset that the asset belongs to.

          running_status_data_input_id: The asset's isRunning status will be true when the associated data input's value
              is 1. Data input cannot be of location format. **The data input will be moved to
              the new asset.**

          tag_ids: The ids of the tags that the asset should belong to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/industrial/assets",
            body=maybe_transform(
                {
                    "name": name,
                    "custom_metadata": custom_metadata,
                    "location": location,
                    "location_data_input_id": location_data_input_id,
                    "location_type": location_type,
                    "parent_id": parent_id,
                    "running_status_data_input_id": running_status_data_input_id,
                    "tag_ids": tag_ids,
                },
                asset_create_params.AssetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InlineResponse200,
        )

    def update(
        self,
        id: str,
        *,
        custom_metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        location: asset_update_params.Location | NotGiven = NOT_GIVEN,
        location_data_input_id: str | NotGiven = NOT_GIVEN,
        location_type: Literal["point", "address", "dataInput"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        running_status_data_input_id: str | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InlineResponse200:
        """Update an existing asset.

        Only the provided fields will be updated.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Equipment** under the Equipment category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          custom_metadata: The custom fields of an asset.

          location: For locationType "point", latitude and longitude are required. For "address",
              formattedAddress must be provided, and lat/long can be optionally included for
              displaying a dot on the assets map. For "dataInput", this object should not be
              passed in.

          location_data_input_id: Required if locationType is "dataInput". Specifies the id of a location data
              input which will determine the asset's location. The data input must be in the
              asset.

          location_type: The format of the location. This field is required if a location is provided.
              Valid values: `point`, `address`, `dataInput`.

          name: The name of the asset.

          parent_id: The id of the parent asset that the asset belongs to. Pass in an empty string to
              remove the child from the parent.

          running_status_data_input_id: The asset's isRunning status will be true when the associated data input's value
              is 1. Data input cannot be of location format. The data input must be in the
              asset.

          tag_ids: The ids of the tags that the asset should belong to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/industrial/assets/{id}",
            body=maybe_transform(
                {
                    "custom_metadata": custom_metadata,
                    "location": location,
                    "location_data_input_id": location_data_input_id,
                    "location_type": location_type,
                    "name": name,
                    "parent_id": parent_id,
                    "running_status_data_input_id": running_status_data_input_id,
                    "tag_ids": tag_ids,
                },
                asset_update_params.AssetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InlineResponse200,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        asset_ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListIndustrialAssetsResponse:
        """
        List all assets in the organization.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Equipment** under the Equipment category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          asset_ids:
              A comma-separated list of industrial asset UUIDs. Example:
              `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`

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
            "/industrial/assets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "asset_ids": asset_ids,
                        "limit": limit,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                    },
                    asset_list_params.AssetListParams,
                ),
            ),
            cast_to=ListIndustrialAssetsResponse,
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
        Delete asset.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Equipment** under the Equipment category
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
            f"/industrial/assets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncAssetsResource(AsyncAPIResource):
    @cached_property
    def data_outputs(self) -> AsyncDataOutputsResource:
        return AsyncDataOutputsResource(self._client)

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
        name: str,
        custom_metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        location: asset_create_params.Location | NotGiven = NOT_GIVEN,
        location_data_input_id: str | NotGiven = NOT_GIVEN,
        location_type: Literal["point", "address", "dataInput"] | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        running_status_data_input_id: str | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InlineResponse200:
        """
        Create an asset with optional configuration parameters.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Equipment** under the Equipment category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          name: The name of the asset.

          custom_metadata: The custom fields of an asset.

          location: For locationType "point", latitude and longitude are required. For "address",
              formattedAddress must be provided, and lat/long can be optionally included for
              displaying a dot on the assets map. For "dataInput", this object should not be
              passed in.

          location_data_input_id: Required if locationType is "dataInput". Specifies the id of a location data
              input which will determine the asset's location. **The data input will be moved
              to the new asset.**

          location_type: The format of the location. This field is required if a location is provided.
              Valid values: `point`, `address`, `dataInput`.

          parent_id: The id of the parent asset that the asset belongs to.

          running_status_data_input_id: The asset's isRunning status will be true when the associated data input's value
              is 1. Data input cannot be of location format. **The data input will be moved to
              the new asset.**

          tag_ids: The ids of the tags that the asset should belong to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/industrial/assets",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "custom_metadata": custom_metadata,
                    "location": location,
                    "location_data_input_id": location_data_input_id,
                    "location_type": location_type,
                    "parent_id": parent_id,
                    "running_status_data_input_id": running_status_data_input_id,
                    "tag_ids": tag_ids,
                },
                asset_create_params.AssetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InlineResponse200,
        )

    async def update(
        self,
        id: str,
        *,
        custom_metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        location: asset_update_params.Location | NotGiven = NOT_GIVEN,
        location_data_input_id: str | NotGiven = NOT_GIVEN,
        location_type: Literal["point", "address", "dataInput"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        running_status_data_input_id: str | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InlineResponse200:
        """Update an existing asset.

        Only the provided fields will be updated.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Equipment** under the Equipment category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          custom_metadata: The custom fields of an asset.

          location: For locationType "point", latitude and longitude are required. For "address",
              formattedAddress must be provided, and lat/long can be optionally included for
              displaying a dot on the assets map. For "dataInput", this object should not be
              passed in.

          location_data_input_id: Required if locationType is "dataInput". Specifies the id of a location data
              input which will determine the asset's location. The data input must be in the
              asset.

          location_type: The format of the location. This field is required if a location is provided.
              Valid values: `point`, `address`, `dataInput`.

          name: The name of the asset.

          parent_id: The id of the parent asset that the asset belongs to. Pass in an empty string to
              remove the child from the parent.

          running_status_data_input_id: The asset's isRunning status will be true when the associated data input's value
              is 1. Data input cannot be of location format. The data input must be in the
              asset.

          tag_ids: The ids of the tags that the asset should belong to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/industrial/assets/{id}",
            body=await async_maybe_transform(
                {
                    "custom_metadata": custom_metadata,
                    "location": location,
                    "location_data_input_id": location_data_input_id,
                    "location_type": location_type,
                    "name": name,
                    "parent_id": parent_id,
                    "running_status_data_input_id": running_status_data_input_id,
                    "tag_ids": tag_ids,
                },
                asset_update_params.AssetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InlineResponse200,
        )

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        asset_ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListIndustrialAssetsResponse:
        """
        List all assets in the organization.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Equipment** under the Equipment category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          asset_ids:
              A comma-separated list of industrial asset UUIDs. Example:
              `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`

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
            "/industrial/assets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "asset_ids": asset_ids,
                        "limit": limit,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                    },
                    asset_list_params.AssetListParams,
                ),
            ),
            cast_to=ListIndustrialAssetsResponse,
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
        Delete asset.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Equipment** under the Equipment category
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
            f"/industrial/assets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
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
    def data_outputs(self) -> DataOutputsResourceWithRawResponse:
        return DataOutputsResourceWithRawResponse(self._assets.data_outputs)


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
    def data_outputs(self) -> AsyncDataOutputsResourceWithRawResponse:
        return AsyncDataOutputsResourceWithRawResponse(self._assets.data_outputs)


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
    def data_outputs(self) -> DataOutputsResourceWithStreamingResponse:
        return DataOutputsResourceWithStreamingResponse(self._assets.data_outputs)


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
    def data_outputs(self) -> AsyncDataOutputsResourceWithStreamingResponse:
        return AsyncDataOutputsResourceWithStreamingResponse(self._assets.data_outputs)
