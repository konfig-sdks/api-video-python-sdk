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


class RequiredVideoSessionReferrer(TypedDict):
    pass

class OptionalVideoSessionReferrer(TypedDict, total=False):
    # The link the viewer used to reach the video session.
    url: typing.Optional[str]

    # How they arrived at the site, for example organic or paid. Organic meaning they found it themselves and paid meaning they followed a link from an advertisement.
    medium: str

    # The source the referrer came from to the video session. For example if they searched through google to find the stream.
    source: str

    # The search term they typed to arrive at the video session.
    searchTerm: str

class VideoSessionReferrer(RequiredVideoSessionReferrer, OptionalVideoSessionReferrer):
    pass