# coding: utf-8
"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from api_video_python_sdk.client_custom import ClientCustom
from api_video_python_sdk.configuration import Configuration
from api_video_python_sdk.api_client import ApiClient
from api_video_python_sdk.type_util import copy_signature
from api_video_python_sdk.apis.tags.advanced_authentication_api import AdvancedAuthenticationApi
from api_video_python_sdk.apis.tags.analytics_api import AnalyticsApi
from api_video_python_sdk.apis.tags.captions_api import CaptionsApi
from api_video_python_sdk.apis.tags.chapters_api import ChaptersApi
from api_video_python_sdk.apis.tags.live_streams_api import LiveStreamsApi
from api_video_python_sdk.apis.tags.player_themes_api import PlayerThemesApi
from api_video_python_sdk.apis.tags.upload_tokens_api import UploadTokensApi
from api_video_python_sdk.apis.tags.videos_api import VideosApi
from api_video_python_sdk.apis.tags.watermarks_api import WatermarksApi
from api_video_python_sdk.apis.tags.webhooks_api import WebhooksApi



class ApiVideo(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.advanced_authentication: AdvancedAuthenticationApi = AdvancedAuthenticationApi(api_client)
        self.analytics: AnalyticsApi = AnalyticsApi(api_client)
        self.captions: CaptionsApi = CaptionsApi(api_client)
        self.chapters: ChaptersApi = ChaptersApi(api_client)
        self.live_streams: LiveStreamsApi = LiveStreamsApi(api_client)
        self.player_themes: PlayerThemesApi = PlayerThemesApi(api_client)
        self.upload_tokens: UploadTokensApi = UploadTokensApi(api_client)
        self.videos: VideosApi = VideosApi(api_client)
        self.watermarks: WatermarksApi = WatermarksApi(api_client)
        self.webhooks: WebhooksApi = WebhooksApi(api_client)
