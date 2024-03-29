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

from api_video_python_sdk.pydantic.live_stream_session_client import LiveStreamSessionClient
from api_video_python_sdk.pydantic.live_stream_session_device import LiveStreamSessionDevice
from api_video_python_sdk.pydantic.live_stream_session_location import LiveStreamSessionLocation
from api_video_python_sdk.pydantic.live_stream_session_referrer import LiveStreamSessionReferrer
from api_video_python_sdk.pydantic.live_stream_session_session import LiveStreamSessionSession
from api_video_python_sdk.pydantic.video_session_os import VideoSessionOs

class LiveStreamSession(BaseModel):
    session: typing.Optional[LiveStreamSessionSession] = Field(None, alias='session')

    location: typing.Optional[LiveStreamSessionLocation] = Field(None, alias='location')

    referrer: typing.Optional[LiveStreamSessionReferrer] = Field(None, alias='referrer')

    device: typing.Optional[LiveStreamSessionDevice] = Field(None, alias='device')

    os: typing.Optional[VideoSessionOs] = Field(None, alias='os')

    client: typing.Optional[LiveStreamSessionClient] = Field(None, alias='client')
    class Config:
        arbitrary_types_allowed = True
