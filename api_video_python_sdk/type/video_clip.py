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


class RequiredVideoClip(TypedDict):
    pass

class OptionalVideoClip(TypedDict, total=False):
    # The timestamp that defines the beginning of the video clip you want to create. The value must follow the `HH:MM:SS` format.
    startTimecode: str

    # The timestamp that defines the end of the video clip you want to create. The value must follow the `HH:MM:SS` format.
    endTimecode: str

class VideoClip(RequiredVideoClip, OptionalVideoClip):
    pass
