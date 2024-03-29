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

from api_video_python_sdk.type.video_session_client import VideoSessionClient
from api_video_python_sdk.type.video_session_device import VideoSessionDevice
from api_video_python_sdk.type.video_session_location import VideoSessionLocation
from api_video_python_sdk.type.video_session_os import VideoSessionOs
from api_video_python_sdk.type.video_session_referrer import VideoSessionReferrer
from api_video_python_sdk.type.video_session_session import VideoSessionSession

class RequiredVideoSession(TypedDict):
    pass

class OptionalVideoSession(TypedDict, total=False):
    session: VideoSessionSession

    location: VideoSessionLocation

    referrer: VideoSessionReferrer

    device: VideoSessionDevice

    os: VideoSessionOs

    client: VideoSessionClient

class VideoSession(RequiredVideoSession, OptionalVideoSession):
    pass
