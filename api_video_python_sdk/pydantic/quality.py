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


class Quality(BaseModel):
    # The type of video (hls or mp4).
    type: typing.Optional[Literal["hls", "mp4"]] = Field(None, alias='type')

    # The quality of the video you have, in pixels. Choices include 360p, 480p, 720p, 1080p, and 2160p.
    quality: typing.Optional[Literal["240p", "360p", "480p", "720p", "1080p", "2160p"]] = Field(None, alias='quality')

    # The status of your video. Statuses include waiting - the video is waiting to be encoded. encoding - the video is in the process of being encoded. encoded - the video was successfully encoded. failed - the video failed to be encoded.
    status: typing.Optional[Literal["waiting", "encoding", "encoded", "failed"]] = Field(None, alias='status')
    class Config:
        arbitrary_types_allowed = True
