"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from samsara.types import BaseModel
from typing_extensions import TypedDict


class TrainingLearnerObjectResponseBodyType(str, Enum):
    r"""The type of the polymorphic user.  Valid values: `driver`"""

    DRIVER = "driver"


class TrainingLearnerObjectResponseBodyTypedDict(TypedDict):
    r"""Learner that is associated with the training assignment. Only driver learners are supported currently."""

    id: str
    r"""ID of the polymorphic user."""
    type: TrainingLearnerObjectResponseBodyType
    r"""The type of the polymorphic user.  Valid values: `driver`"""


class TrainingLearnerObjectResponseBody(BaseModel):
    r"""Learner that is associated with the training assignment. Only driver learners are supported currently."""

    id: str
    r"""ID of the polymorphic user."""

    type: TrainingLearnerObjectResponseBodyType
    r"""The type of the polymorphic user.  Valid values: `driver`"""
