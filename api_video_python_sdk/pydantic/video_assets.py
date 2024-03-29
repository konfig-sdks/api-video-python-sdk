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


class VideoAssets(BaseModel):
    # This is the manifest URL. For HTTP Live Streaming (HLS), when a HLS video stream is initiated, the first file to download is the manifest. This file has the extension M3U8, and provides the video player with information about the various bitrates available for streaming.
    hls: typing.Optional[str] = Field(None, alias='hls')

    # Code to use video from a third party website
    iframe: typing.Optional[str] = Field(None, alias='iframe')

    # Raw url of the player.
    player: typing.Optional[str] = Field(None, alias='player')

    # Poster of the video.
    thumbnail: typing.Optional[str] = Field(None, alias='thumbnail')

    # Available only if mp4Support is enabled. Raw mp4 url.
    mp4: typing.Optional[str] = Field(None, alias='mp4')
    class Config:
        arbitrary_types_allowed = True
