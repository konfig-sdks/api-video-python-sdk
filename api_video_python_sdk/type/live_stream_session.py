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

from api_video_python_sdk.type.live_stream_session_client import LiveStreamSessionClient
from api_video_python_sdk.type.live_stream_session_device import LiveStreamSessionDevice
from api_video_python_sdk.type.live_stream_session_location import LiveStreamSessionLocation
from api_video_python_sdk.type.live_stream_session_referrer import LiveStreamSessionReferrer
from api_video_python_sdk.type.live_stream_session_session import LiveStreamSessionSession
from api_video_python_sdk.type.video_session_os import VideoSessionOs

class RequiredLiveStreamSession(TypedDict):
    pass

class OptionalLiveStreamSession(TypedDict, total=False):
    session: LiveStreamSessionSession

    location: LiveStreamSessionLocation

    referrer: LiveStreamSessionReferrer

    device: LiveStreamSessionDevice

    os: VideoSessionOs

    client: LiveStreamSessionClient

class LiveStreamSession(RequiredLiveStreamSession, OptionalLiveStreamSession):
    pass