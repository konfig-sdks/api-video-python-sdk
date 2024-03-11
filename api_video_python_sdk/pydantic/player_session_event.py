# coding: utf-8

"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel


class PlayerSessionEvent(BaseModel):
    # Possible values are: ready, play, pause, resume, seek.backward, seek.forward, end
    type: typing.Optional[str] = Field(None, alias='type')

    # When an event occurred, presented in ISO-8601 format.
    emitted_at: typing.Optional[datetime] = Field(None, alias='emittedAt')

    at: typing.Optional[int] = Field(None, alias='at')

    from_: typing.Optional[int] = Field(None, alias='from')

    to: typing.Optional[int] = Field(None, alias='to')
    class Config:
        arbitrary_types_allowed = True