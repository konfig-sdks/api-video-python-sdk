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


class RequiredVideoWatermark(TypedDict):
    pass

class OptionalVideoWatermark(TypedDict, total=False):
    # id of the watermark
    id: str

    # Distance expressed in px or % between the top-border of the video and the watermark-image.
    top: str

    # Distance expressed in px or % between the left-border of the video and the watermark-image.
    left: str

    # Distance expressed in px or % between the bottom-border of the video and the watermark-image.
    bottom: str

    # Distance expressed in px or % between the right-border of the video and the watermark-image.
    right: str

    # Width of the watermark-image relative to the video if expressed in %. Otherwise a fixed width. NOTE: To keep intrinsic watermark-image width use `initial`.
    width: str

    # Height of the watermark-image relative to the video if expressed in %. Otherwise a fixed height. NOTE: To keep intrinsic watermark-image height use `initial`.
    height: str

    # Opacity expressed in % only to specify the degree of the watermark-image transparency with the video.
    opacity: str

class VideoWatermark(RequiredVideoWatermark, OptionalVideoWatermark):
    pass
