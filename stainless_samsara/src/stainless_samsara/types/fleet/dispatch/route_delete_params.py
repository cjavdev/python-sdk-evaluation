# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RouteDeleteParams"]


class RouteDeleteParams(TypedDict, total=False):
    apply_to_future_routes: bool
    """This is only for a recurring route.

    If set to true, delete all following runs of the route. If set to false, only
    delete the current route.
    """
