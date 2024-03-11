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


class RequiredRestreamsRequestObject(TypedDict):
    # Use this parameter to define a name for the restream destination.
    name: str

    # Use this parameter to set the RTMP URL of the restream destination.
    serverUrl: str

    # Use this parameter to provide the unique key of the live stream that you want to restream.
    streamKey: str

class OptionalRestreamsRequestObject(TypedDict, total=False):
    pass

class RestreamsRequestObject(RequiredRestreamsRequestObject, OptionalRestreamsRequestObject):
    pass
