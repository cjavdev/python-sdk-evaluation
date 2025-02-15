"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing_extensions import Annotated, TypedDict


class TinyWidgetObjectResponseBodyTypedDict(TypedDict):
    r"""Widget to be tracked."""

    widget_id: str
    r"""ID of the widget."""


class TinyWidgetObjectResponseBody(BaseModel):
    r"""Widget to be tracked."""

    widget_id: Annotated[str, pydantic.Field(alias="widgetId")]
    r"""ID of the widget."""
