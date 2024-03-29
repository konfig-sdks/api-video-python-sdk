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


class PlayerThemeAssets(BaseModel):
    # The name of the file containing the logo you want to use.
    logo: typing.Optional[str] = Field(None, alias='logo')

    # The path to the file containing your logo.
    link: typing.Optional[str] = Field(None, alias='link')
    class Config:
        arbitrary_types_allowed = True
