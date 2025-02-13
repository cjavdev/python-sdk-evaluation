"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .alertobjectonvifcamerastreamresponsebody import (
    AlertObjectOnvifCameraStreamResponseBody,
    AlertObjectOnvifCameraStreamResponseBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class MotionDetectedResponseBodyTypedDict(TypedDict):
    r"""Details specific to Motion Detected."""

    camera_stream: NotRequired[AlertObjectOnvifCameraStreamResponseBodyTypedDict]
    r"""A camera stream associated with the alert."""


class MotionDetectedResponseBody(BaseModel):
    r"""Details specific to Motion Detected."""

    camera_stream: Annotated[
        Optional[AlertObjectOnvifCameraStreamResponseBody],
        pydantic.Field(alias="cameraStream"),
    ] = None
    r"""A camera stream associated with the alert."""
