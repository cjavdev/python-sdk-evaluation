# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CarrierProposedAssignmentListResponse", "Data", "DataDriver", "DataTrailer", "DataVehicle", "Pagination"]


class DataDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """
    The [external IDs](https://developers.samsara.com/docs/external-ids) for the
    given object.
    """

    name: Optional[str] = None
    """Name of the driver."""


class DataTrailer(BaseModel):
    id: Optional[str] = None
    """ID of the trailer."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """
    The [external IDs](https://developers.samsara.com/docs/external-ids) for the
    given object.
    """

    name: Optional[str] = None
    """Name of the trailer."""


class DataVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="ExternalIds", default=None)
    """
    The [external IDs](https://developers.samsara.com/docs/external-ids) for the
    given object.
    """

    name: Optional[str] = None
    """Name of the vehicle."""


class Data(BaseModel):
    id: str
    """Samsara ID for the assignment."""

    active_time: str = FieldInfo(alias="activeTime")
    """
    Time after which this assignment will be active and visible to the driver on the
    mobile app. Not setting it makes it active now. UTC timestamp in RFC 3339
    format. Example: `2020-01-27T07:06:25Z`.
    """

    accepted_time: Optional[str] = FieldInfo(alias="acceptedTime", default=None)
    """Time when the driver accepted this assignment in the mobile app.

    Will be omitted if the driver hasn't accepted this assignment. RFC 3339 format.
    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    driver: Optional[DataDriver] = None

    first_seen_time: Optional[str] = FieldInfo(alias="firstSeenTime", default=None)
    """Time when the driver first saw this assignment in the mobile app.

    Will be omitted if the driver hasn't seen this assignment yet. RFC 3339 format.
    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    rejected_time: Optional[str] = FieldInfo(alias="rejectedTime", default=None)
    """Time when the driver rejected this assignment in the mobile app.

    Will be omitted if the driver hasn't rejected this assignment. RFC 3339 format.
    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    shipping_docs: Optional[str] = FieldInfo(alias="shippingDocs", default=None)
    """Shipping Documents that this assignment will propose to the driver."""

    trailers: Optional[List[DataTrailer]] = None
    """Trailers that this assignment will propose to the driver."""

    vehicle: Optional[DataVehicle] = None


class Pagination(BaseModel):
    end_cursor: str = FieldInfo(alias="endCursor")
    """Cursor identifier representing the last element in the response.

    This value should be used in conjunction with a subsequent request's 'after'
    query parameter. This may be an empty string if there are no more pages left to
    view.
    """

    has_next_page: bool = FieldInfo(alias="hasNextPage")
    """
    True if there are more pages of results immediately available after this
    endCursor.
    """


class CarrierProposedAssignmentListResponse(BaseModel):
    data: List[Data]
    """A list of carrier-proposed assignments"""

    pagination: Pagination
    """Pagination parameters."""
