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


class RequiredRestreamsResponseObject(TypedDict):
    pass

class OptionalRestreamsResponseObject(TypedDict, total=False):
    # Returns the name of a restream destination.
    name: str

    # Returns the RTMP URL of a restream destination.
    serverUrl: str

    # Returns the unique key of the live stream that is set up for restreaming.
    streamKey: str

class RestreamsResponseObject(RequiredRestreamsResponseObject, OptionalRestreamsResponseObject):
    pass
