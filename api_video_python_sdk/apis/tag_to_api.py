import typing_extensions

from api_video_python_sdk.apis.tags import TagValues
from api_video_python_sdk.apis.tags.videos_api import VideosApi
from api_video_python_sdk.apis.tags.live_streams_api import LiveStreamsApi
from api_video_python_sdk.apis.tags.player_themes_api import PlayerThemesApi
from api_video_python_sdk.apis.tags.captions_api import CaptionsApi
from api_video_python_sdk.apis.tags.upload_tokens_api import UploadTokensApi
from api_video_python_sdk.apis.tags.chapters_api import ChaptersApi
from api_video_python_sdk.apis.tags.webhooks_api import WebhooksApi
from api_video_python_sdk.apis.tags.watermarks_api import WatermarksApi
from api_video_python_sdk.apis.tags.advanced_authentication_api import AdvancedAuthenticationApi
from api_video_python_sdk.apis.tags.analytics_api import AnalyticsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.VIDEOS: VideosApi,
        TagValues.LIVE_STREAMS: LiveStreamsApi,
        TagValues.PLAYER_THEMES: PlayerThemesApi,
        TagValues.CAPTIONS: CaptionsApi,
        TagValues.UPLOAD_TOKENS: UploadTokensApi,
        TagValues.CHAPTERS: ChaptersApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.WATERMARKS: WatermarksApi,
        TagValues.ADVANCED_AUTHENTICATION: AdvancedAuthenticationApi,
        TagValues.ANALYTICS: AnalyticsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.VIDEOS: VideosApi,
        TagValues.LIVE_STREAMS: LiveStreamsApi,
        TagValues.PLAYER_THEMES: PlayerThemesApi,
        TagValues.CAPTIONS: CaptionsApi,
        TagValues.UPLOAD_TOKENS: UploadTokensApi,
        TagValues.CHAPTERS: ChaptersApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.WATERMARKS: WatermarksApi,
        TagValues.ADVANCED_AUTHENTICATION: AdvancedAuthenticationApi,
        TagValues.ANALYTICS: AnalyticsApi,
    }
)
