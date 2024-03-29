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

from api_video_python_sdk.type.metadata import Metadata

class RequiredVideoSessionSession(TypedDict):
    pass

class OptionalVideoSessionSession(TypedDict, total=False):
    # The unique identifier for the session that you can use to track what happens during it.
    sessionId: str

    # When the video session started, presented in ISO-8601 format.
    loadedAt: datetime

    # When the video session ended, presented in ISO-8601 format.
    endedAt: datetime

    # A list of key value pairs that you use to provide metadata for your video. These pairs can be made dynamic, allowing you to segment your audience. You can also just use the pairs as another way to tag and categorize your videos.
    metadata: typing.List[Metadata]

class VideoSessionSession(RequiredVideoSessionSession, OptionalVideoSessionSession):
    pass
