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

from api_video_python_sdk.pydantic.player_theme_assets import PlayerThemeAssets

class PlayerTheme(BaseModel):
    player_id: str = Field(alias='playerId')

    # The name of the player theme
    name: typing.Optional[str] = Field(None, alias='name')

    # RGBA color for timer text. Default: rgba(255, 255, 255, 1)
    text: typing.Optional[str] = Field(None, alias='text')

    # RGBA color for all controls. Default: rgba(255, 255, 255, 1)
    link: typing.Optional[str] = Field(None, alias='link')

    # RGBA color for all controls when hovered. Default: rgba(255, 255, 255, 1)
    link_hover: typing.Optional[str] = Field(None, alias='linkHover')

    # RGBA color for the play button when hovered.
    link_active: typing.Optional[str] = Field(None, alias='linkActive')

    # RGBA color playback bar: played content. Default: rgba(88, 131, 255, .95)
    track_played: typing.Optional[str] = Field(None, alias='trackPlayed')

    # RGBA color playback bar: downloaded but unplayed (buffered) content. Default: rgba(255, 255, 255, .35)
    track_unplayed: typing.Optional[str] = Field(None, alias='trackUnplayed')

    # RGBA color playback bar: background. Default: rgba(255, 255, 255, .2)
    track_background: typing.Optional[str] = Field(None, alias='trackBackground')

    # RGBA color: top 50% of background. Default: rgba(0, 0, 0, .7)
    background_top: typing.Optional[str] = Field(None, alias='backgroundTop')

    # RGBA color: bottom 50% of background. Default: rgba(0, 0, 0, .7)
    background_bottom: typing.Optional[str] = Field(None, alias='backgroundBottom')

    # RGBA color for title text. Default: rgba(255, 255, 255, 1)
    background_text: typing.Optional[str] = Field(None, alias='backgroundText')

    # enable/disable player SDK access. Default: true
    enable_api: typing.Optional[bool] = Field(None, alias='enableApi')

    # enable/disable player controls. Default: true
    enable_controls: typing.Optional[bool] = Field(None, alias='enableControls')

    # enable/disable player autoplay. Default: false
    force_autoplay: typing.Optional[bool] = Field(None, alias='forceAutoplay')

    # enable/disable title. Default: false
    hide_title: typing.Optional[bool] = Field(None, alias='hideTitle')

    # enable/disable looping. Default: false
    force_loop: typing.Optional[bool] = Field(None, alias='forceLoop')

    # When the player was created, presented in ISO-8601 format.
    created_at: typing.Optional[datetime] = Field(None, alias='createdAt')

    # When the player was last updated, presented in ISO-8601 format.
    updated_at: typing.Optional[datetime] = Field(None, alias='updatedAt')

    assets: typing.Optional[PlayerThemeAssets] = Field(None, alias='assets')
    class Config:
        arbitrary_types_allowed = True
