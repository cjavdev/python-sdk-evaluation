"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .routessingleuseaddressobjectrequestbody import (
    RoutesSingleUseAddressObjectRequestBody,
    RoutesSingleUseAddressObjectRequestBodyTypedDict,
)
from datetime import datetime
import pydantic
from samsara.types import BaseModel
from typing import Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateRoutesStopRequestObjectRequestBodyTypedDict(TypedDict):
    address_id: NotRequired[str]
    r"""ID of the address. An address [externalId](https://developers.samsara.com/docs/external-ids#using-external-ids) can also be used interchangeably here."""
    external_ids: NotRequired[Dict[str, str]]
    r"""A map of external ids"""
    name: NotRequired[str]
    r"""Name of the stop"""
    notes: NotRequired[str]
    r"""Notes for the stop"""
    ontime_window_after_arrival_ms: NotRequired[int]
    r"""Specifies the time window (in milliseconds) after a stop's scheduled arrival time during which the stop is considered 'on-time'."""
    ontime_window_before_arrival_ms: NotRequired[int]
    r"""Specifies the time window (in milliseconds) before a stop's scheduled arrival time during which the stop is considered 'on-time'."""
    scheduled_arrival_time: NotRequired[datetime]
    r"""This is a required field for all stops EXCEPT the start and end, based on route start and stop settings selected."""
    scheduled_departure_time: NotRequired[datetime]
    r"""This is a required field for all stops EXCEPT the start and end, based on route start and stop settings selected."""
    single_use_location: NotRequired[RoutesSingleUseAddressObjectRequestBodyTypedDict]
    r"""This field is used to indicate stops along the route for which an address has not been persisted. This field is mutually exclusive with addressId."""


class CreateRoutesStopRequestObjectRequestBody(BaseModel):
    address_id: Annotated[Optional[str], pydantic.Field(alias="addressId")] = None
    r"""ID of the address. An address [externalId](https://developers.samsara.com/docs/external-ids#using-external-ids) can also be used interchangeably here."""

    external_ids: Annotated[
        Optional[Dict[str, str]], pydantic.Field(alias="externalIds")
    ] = None
    r"""A map of external ids"""

    name: Optional[str] = None
    r"""Name of the stop"""

    notes: Optional[str] = None
    r"""Notes for the stop"""

    ontime_window_after_arrival_ms: Annotated[
        Optional[int], pydantic.Field(alias="ontimeWindowAfterArrivalMs")
    ] = None
    r"""Specifies the time window (in milliseconds) after a stop's scheduled arrival time during which the stop is considered 'on-time'."""

    ontime_window_before_arrival_ms: Annotated[
        Optional[int], pydantic.Field(alias="ontimeWindowBeforeArrivalMs")
    ] = None
    r"""Specifies the time window (in milliseconds) before a stop's scheduled arrival time during which the stop is considered 'on-time'."""

    scheduled_arrival_time: Annotated[
        Optional[datetime], pydantic.Field(alias="scheduledArrivalTime")
    ] = None
    r"""This is a required field for all stops EXCEPT the start and end, based on route start and stop settings selected."""

    scheduled_departure_time: Annotated[
        Optional[datetime], pydantic.Field(alias="scheduledDepartureTime")
    ] = None
    r"""This is a required field for all stops EXCEPT the start and end, based on route start and stop settings selected."""

    single_use_location: Annotated[
        Optional[RoutesSingleUseAddressObjectRequestBody],
        pydantic.Field(alias="singleUseLocation"),
    ] = None
    r"""This field is used to indicate stops along the route for which an address has not been persisted. This field is mutually exclusive with addressId."""
