# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ..types import (
    attribute_list_params,
    attribute_create_params,
    attribute_delete_params,
    attribute_update_params,
    attribute_retrieve_params,
)
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
from ..types.attribute import Attribute
from ..types.attribute_list_response import AttributeListResponse

__all__ = ["AttributesResource", "AsyncAttributesResource"]


class AttributesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AttributesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AttributesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttributesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AttributesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        attribute_type: Literal["string", "number"],
        attribute_value_quantity: Literal["single", "multi"],
        entity_type: Literal["driver", "asset"],
        name: str,
        entities: Iterable[attribute_create_params.Entity] | NotGiven = NOT_GIVEN,
        number_values: Iterable[float] | NotGiven = NOT_GIVEN,
        string_values: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Attribute:
        """
        Creates a new attribute in the organization.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Attributes** under the Setup &
        Administration category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          attribute_type: Denotes the data type of the attribute's values. Valid values: `string`,
              `number`.

          attribute_value_quantity: Defines whether or not this attribute can be used on the same entity many times
              (with different values). Valid values: `single`, `multi`.

          entity_type: Denotes the type of entity, driver or asset.

          name: Name

          entities: Entities that will be applied to this attribute

          number_values: Number values that can be associated with this attribute

          string_values: String values that can be associated with this attribute

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/attributes",
            body=maybe_transform(
                {
                    "attribute_type": attribute_type,
                    "attribute_value_quantity": attribute_value_quantity,
                    "entity_type": entity_type,
                    "name": name,
                    "entities": entities,
                    "number_values": number_values,
                    "string_values": string_values,
                },
                attribute_create_params.AttributeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Attribute,
        )

    def retrieve(
        self,
        id: str,
        *,
        entity_type: Literal["driver", "asset"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Attribute:
        """
        Fetch an attribute by id, including all of its applications.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Attributes** under the Setup &
        Administration category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          entity_type: Denotes the type of entity, driver or asset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/attributes/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"entity_type": entity_type}, attribute_retrieve_params.AttributeRetrieveParams),
            ),
            cast_to=Attribute,
        )

    def update(
        self,
        id: str,
        *,
        entity_type: Literal["driver", "asset"],
        attribute_type: Literal["string", "number"] | NotGiven = NOT_GIVEN,
        attribute_value_quantity: Literal["single", "multi"] | NotGiven = NOT_GIVEN,
        entities: Iterable[attribute_update_params.Entity] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        number_values: Iterable[float] | NotGiven = NOT_GIVEN,
        string_values: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Attribute:
        """
        Updates an attribute in the organization.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Attributes** under the Setup &
        Administration category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          entity_type: Denotes the type of entity, driver or asset.

          attribute_type: Denotes the data type of the attribute's values. Valid values: `string`,
              `number`.

          attribute_value_quantity: Defines whether or not this attribute can be used on the same entity many times
              (with different values). Denotes the type of entity, driver or asset. Valid
              values: `driver`, `asset`.

          entities: Entities that will be applied to this attribute

          name: Name

          number_values: Number values that can be associated with this attribute

          string_values: String values that can be associated with this attribute

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/attributes/{id}",
            body=maybe_transform(
                {
                    "entity_type": entity_type,
                    "attribute_type": attribute_type,
                    "attribute_value_quantity": attribute_value_quantity,
                    "entities": entities,
                    "name": name,
                    "number_values": number_values,
                    "string_values": string_values,
                },
                attribute_update_params.AttributeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Attribute,
        )

    def list(
        self,
        *,
        entity_type: Literal["driver", "asset"],
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttributeListResponse:
        """
        Fetch all attributes in an organization associated with either drivers or
        assets.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Attributes** under the Setup &
        Administration category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          entity_type: Denotes the type of entity, driver or asset.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          limit: The limit for how many objects will be in the response. Default and max for this
              value is 512 objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/attributes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "entity_type": entity_type,
                        "after": after,
                        "limit": limit,
                    },
                    attribute_list_params.AttributeListParams,
                ),
            ),
            cast_to=AttributeListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        entity_type: Literal["driver", "asset"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Delete an attribute by id, including all of its applications.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Attributes** under the Setup &
        Administration category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          entity_type: Denotes the type of entity, driver or asset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/attributes/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"entity_type": entity_type}, attribute_delete_params.AttributeDeleteParams),
            ),
            cast_to=str,
        )


class AsyncAttributesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAttributesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAttributesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttributesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncAttributesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        attribute_type: Literal["string", "number"],
        attribute_value_quantity: Literal["single", "multi"],
        entity_type: Literal["driver", "asset"],
        name: str,
        entities: Iterable[attribute_create_params.Entity] | NotGiven = NOT_GIVEN,
        number_values: Iterable[float] | NotGiven = NOT_GIVEN,
        string_values: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Attribute:
        """
        Creates a new attribute in the organization.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Attributes** under the Setup &
        Administration category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          attribute_type: Denotes the data type of the attribute's values. Valid values: `string`,
              `number`.

          attribute_value_quantity: Defines whether or not this attribute can be used on the same entity many times
              (with different values). Valid values: `single`, `multi`.

          entity_type: Denotes the type of entity, driver or asset.

          name: Name

          entities: Entities that will be applied to this attribute

          number_values: Number values that can be associated with this attribute

          string_values: String values that can be associated with this attribute

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/attributes",
            body=await async_maybe_transform(
                {
                    "attribute_type": attribute_type,
                    "attribute_value_quantity": attribute_value_quantity,
                    "entity_type": entity_type,
                    "name": name,
                    "entities": entities,
                    "number_values": number_values,
                    "string_values": string_values,
                },
                attribute_create_params.AttributeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Attribute,
        )

    async def retrieve(
        self,
        id: str,
        *,
        entity_type: Literal["driver", "asset"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Attribute:
        """
        Fetch an attribute by id, including all of its applications.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Attributes** under the Setup &
        Administration category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          entity_type: Denotes the type of entity, driver or asset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/attributes/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"entity_type": entity_type}, attribute_retrieve_params.AttributeRetrieveParams
                ),
            ),
            cast_to=Attribute,
        )

    async def update(
        self,
        id: str,
        *,
        entity_type: Literal["driver", "asset"],
        attribute_type: Literal["string", "number"] | NotGiven = NOT_GIVEN,
        attribute_value_quantity: Literal["single", "multi"] | NotGiven = NOT_GIVEN,
        entities: Iterable[attribute_update_params.Entity] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        number_values: Iterable[float] | NotGiven = NOT_GIVEN,
        string_values: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Attribute:
        """
        Updates an attribute in the organization.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Attributes** under the Setup &
        Administration category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          entity_type: Denotes the type of entity, driver or asset.

          attribute_type: Denotes the data type of the attribute's values. Valid values: `string`,
              `number`.

          attribute_value_quantity: Defines whether or not this attribute can be used on the same entity many times
              (with different values). Denotes the type of entity, driver or asset. Valid
              values: `driver`, `asset`.

          entities: Entities that will be applied to this attribute

          name: Name

          number_values: Number values that can be associated with this attribute

          string_values: String values that can be associated with this attribute

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/attributes/{id}",
            body=await async_maybe_transform(
                {
                    "entity_type": entity_type,
                    "attribute_type": attribute_type,
                    "attribute_value_quantity": attribute_value_quantity,
                    "entities": entities,
                    "name": name,
                    "number_values": number_values,
                    "string_values": string_values,
                },
                attribute_update_params.AttributeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Attribute,
        )

    async def list(
        self,
        *,
        entity_type: Literal["driver", "asset"],
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttributeListResponse:
        """
        Fetch all attributes in an organization associated with either drivers or
        assets.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Attributes** under the Setup &
        Administration category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          entity_type: Denotes the type of entity, driver or asset.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          limit: The limit for how many objects will be in the response. Default and max for this
              value is 512 objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/attributes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "entity_type": entity_type,
                        "after": after,
                        "limit": limit,
                    },
                    attribute_list_params.AttributeListParams,
                ),
            ),
            cast_to=AttributeListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        entity_type: Literal["driver", "asset"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Delete an attribute by id, including all of its applications.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Attributes** under the Setup &
        Administration category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          entity_type: Denotes the type of entity, driver or asset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/attributes/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"entity_type": entity_type}, attribute_delete_params.AttributeDeleteParams
                ),
            ),
            cast_to=str,
        )


class AttributesResourceWithRawResponse:
    def __init__(self, attributes: AttributesResource) -> None:
        self._attributes = attributes

        self.create = to_raw_response_wrapper(
            attributes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            attributes.retrieve,
        )
        self.update = to_raw_response_wrapper(
            attributes.update,
        )
        self.list = to_raw_response_wrapper(
            attributes.list,
        )
        self.delete = to_raw_response_wrapper(
            attributes.delete,
        )


class AsyncAttributesResourceWithRawResponse:
    def __init__(self, attributes: AsyncAttributesResource) -> None:
        self._attributes = attributes

        self.create = async_to_raw_response_wrapper(
            attributes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            attributes.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            attributes.update,
        )
        self.list = async_to_raw_response_wrapper(
            attributes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            attributes.delete,
        )


class AttributesResourceWithStreamingResponse:
    def __init__(self, attributes: AttributesResource) -> None:
        self._attributes = attributes

        self.create = to_streamed_response_wrapper(
            attributes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            attributes.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            attributes.update,
        )
        self.list = to_streamed_response_wrapper(
            attributes.list,
        )
        self.delete = to_streamed_response_wrapper(
            attributes.delete,
        )


class AsyncAttributesResourceWithStreamingResponse:
    def __init__(self, attributes: AsyncAttributesResource) -> None:
        self._attributes = attributes

        self.create = async_to_streamed_response_wrapper(
            attributes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            attributes.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            attributes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            attributes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            attributes.delete,
        )
