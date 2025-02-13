# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .assets.assets import (
    AssetsResource,
    AsyncAssetsResource,
    AssetsResourceWithRawResponse,
    AsyncAssetsResourceWithRawResponse,
    AssetsResourceWithStreamingResponse,
    AsyncAssetsResourceWithStreamingResponse,
)
from .vision.vision import (
    VisionResource,
    AsyncVisionResource,
    VisionResourceWithRawResponse,
    AsyncVisionResourceWithRawResponse,
    VisionResourceWithStreamingResponse,
    AsyncVisionResourceWithStreamingResponse,
)
from .data_inputs.data_inputs import (
    DataInputsResource,
    AsyncDataInputsResource,
    DataInputsResourceWithRawResponse,
    AsyncDataInputsResourceWithRawResponse,
    DataInputsResourceWithStreamingResponse,
    AsyncDataInputsResourceWithStreamingResponse,
)

__all__ = ["IndustrialResource", "AsyncIndustrialResource"]


class IndustrialResource(SyncAPIResource):
    @cached_property
    def assets(self) -> AssetsResource:
        return AssetsResource(self._client)

    @cached_property
    def data_inputs(self) -> DataInputsResource:
        return DataInputsResource(self._client)

    @cached_property
    def vision(self) -> VisionResource:
        return VisionResource(self._client)

    @cached_property
    def with_raw_response(self) -> IndustrialResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return IndustrialResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndustrialResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return IndustrialResourceWithStreamingResponse(self)


class AsyncIndustrialResource(AsyncAPIResource):
    @cached_property
    def assets(self) -> AsyncAssetsResource:
        return AsyncAssetsResource(self._client)

    @cached_property
    def data_inputs(self) -> AsyncDataInputsResource:
        return AsyncDataInputsResource(self._client)

    @cached_property
    def vision(self) -> AsyncVisionResource:
        return AsyncVisionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIndustrialResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIndustrialResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndustrialResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncIndustrialResourceWithStreamingResponse(self)


class IndustrialResourceWithRawResponse:
    def __init__(self, industrial: IndustrialResource) -> None:
        self._industrial = industrial

    @cached_property
    def assets(self) -> AssetsResourceWithRawResponse:
        return AssetsResourceWithRawResponse(self._industrial.assets)

    @cached_property
    def data_inputs(self) -> DataInputsResourceWithRawResponse:
        return DataInputsResourceWithRawResponse(self._industrial.data_inputs)

    @cached_property
    def vision(self) -> VisionResourceWithRawResponse:
        return VisionResourceWithRawResponse(self._industrial.vision)


class AsyncIndustrialResourceWithRawResponse:
    def __init__(self, industrial: AsyncIndustrialResource) -> None:
        self._industrial = industrial

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithRawResponse:
        return AsyncAssetsResourceWithRawResponse(self._industrial.assets)

    @cached_property
    def data_inputs(self) -> AsyncDataInputsResourceWithRawResponse:
        return AsyncDataInputsResourceWithRawResponse(self._industrial.data_inputs)

    @cached_property
    def vision(self) -> AsyncVisionResourceWithRawResponse:
        return AsyncVisionResourceWithRawResponse(self._industrial.vision)


class IndustrialResourceWithStreamingResponse:
    def __init__(self, industrial: IndustrialResource) -> None:
        self._industrial = industrial

    @cached_property
    def assets(self) -> AssetsResourceWithStreamingResponse:
        return AssetsResourceWithStreamingResponse(self._industrial.assets)

    @cached_property
    def data_inputs(self) -> DataInputsResourceWithStreamingResponse:
        return DataInputsResourceWithStreamingResponse(self._industrial.data_inputs)

    @cached_property
    def vision(self) -> VisionResourceWithStreamingResponse:
        return VisionResourceWithStreamingResponse(self._industrial.vision)


class AsyncIndustrialResourceWithStreamingResponse:
    def __init__(self, industrial: AsyncIndustrialResource) -> None:
        self._industrial = industrial

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithStreamingResponse:
        return AsyncAssetsResourceWithStreamingResponse(self._industrial.assets)

    @cached_property
    def data_inputs(self) -> AsyncDataInputsResourceWithStreamingResponse:
        return AsyncDataInputsResourceWithStreamingResponse(self._industrial.data_inputs)

    @cached_property
    def vision(self) -> AsyncVisionResourceWithStreamingResponse:
        return AsyncVisionResourceWithStreamingResponse(self._industrial.vision)
