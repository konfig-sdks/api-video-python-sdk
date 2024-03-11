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


class LiveStreamAssets(BaseModel):
    # The http live streaming (HLS) link for your live video stream.
    hls: typing.Optional[str] = Field(None, alias='hls')

    # The embed code for the iframe containing your live video stream.
    iframe: typing.Optional[str] = Field(None, alias='iframe')

    # A link to the video player that is playing your live stream.
    player: typing.Optional[str] = Field(None, alias='player')

    # A link to the thumbnail for your video.
    thumbnail: typing.Optional[str] = Field(None, alias='thumbnail')
    class Config:
        arbitrary_types_allowed = True