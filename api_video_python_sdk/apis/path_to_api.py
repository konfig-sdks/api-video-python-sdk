import typing_extensions

from api_video_python_sdk.paths import PathValues
from api_video_python_sdk.apis.paths.auth_api_key import AuthApiKey
from api_video_python_sdk.apis.paths.auth_refresh import AuthRefresh
from api_video_python_sdk.apis.paths.videos import Videos
from api_video_python_sdk.apis.paths.videos_video_id_source import VideosVideoIdSource
from api_video_python_sdk.apis.paths.watermarks import Watermarks
from api_video_python_sdk.apis.paths.watermarks_watermark_id import WatermarksWatermarkId
from api_video_python_sdk.apis.paths.videos_video_id_thumbnail import VideosVideoIdThumbnail
from api_video_python_sdk.apis.paths.videos_video_id import VideosVideoId
from api_video_python_sdk.apis.paths.videos_video_id_status import VideosVideoIdStatus
from api_video_python_sdk.apis.paths.upload_tokens import UploadTokens
from api_video_python_sdk.apis.paths.upload_tokens_upload_token import UploadTokensUploadToken
from api_video_python_sdk.apis.paths.upload import Upload
from api_video_python_sdk.apis.paths.live_streams import LiveStreams
from api_video_python_sdk.apis.paths.live_streams_live_stream_id import LiveStreamsLiveStreamId
from api_video_python_sdk.apis.paths.live_streams_live_stream_id_thumbnail import LiveStreamsLiveStreamIdThumbnail
from api_video_python_sdk.apis.paths.videos_video_id_captions_language import VideosVideoIdCaptionsLanguage
from api_video_python_sdk.apis.paths.videos_video_id_captions import VideosVideoIdCaptions
from api_video_python_sdk.apis.paths.videos_video_id_chapters_language import VideosVideoIdChaptersLanguage
from api_video_python_sdk.apis.paths.videos_video_id_chapters import VideosVideoIdChapters
from api_video_python_sdk.apis.paths.players import Players
from api_video_python_sdk.apis.paths.players_player_id import PlayersPlayerId
from api_video_python_sdk.apis.paths.players_player_id_logo import PlayersPlayerIdLogo
from api_video_python_sdk.apis.paths.analytics_videos_plays import AnalyticsVideosPlays
from api_video_python_sdk.apis.paths.analytics_live_streams_plays import AnalyticsLiveStreamsPlays
from api_video_python_sdk.apis.paths.webhooks import Webhooks
from api_video_python_sdk.apis.paths.webhooks_webhook_id import WebhooksWebhookId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.AUTH_APIKEY: AuthApiKey,
        PathValues.AUTH_REFRESH: AuthRefresh,
        PathValues.VIDEOS: Videos,
        PathValues.VIDEOS_VIDEO_ID_SOURCE: VideosVideoIdSource,
        PathValues.WATERMARKS: Watermarks,
        PathValues.WATERMARKS_WATERMARK_ID: WatermarksWatermarkId,
        PathValues.VIDEOS_VIDEO_ID_THUMBNAIL: VideosVideoIdThumbnail,
        PathValues.VIDEOS_VIDEO_ID: VideosVideoId,
        PathValues.VIDEOS_VIDEO_ID_STATUS: VideosVideoIdStatus,
        PathValues.UPLOADTOKENS: UploadTokens,
        PathValues.UPLOADTOKENS_UPLOAD_TOKEN: UploadTokensUploadToken,
        PathValues.UPLOAD: Upload,
        PathValues.LIVESTREAMS: LiveStreams,
        PathValues.LIVESTREAMS_LIVE_STREAM_ID: LiveStreamsLiveStreamId,
        PathValues.LIVESTREAMS_LIVE_STREAM_ID_THUMBNAIL: LiveStreamsLiveStreamIdThumbnail,
        PathValues.VIDEOS_VIDEO_ID_CAPTIONS_LANGUAGE: VideosVideoIdCaptionsLanguage,
        PathValues.VIDEOS_VIDEO_ID_CAPTIONS: VideosVideoIdCaptions,
        PathValues.VIDEOS_VIDEO_ID_CHAPTERS_LANGUAGE: VideosVideoIdChaptersLanguage,
        PathValues.VIDEOS_VIDEO_ID_CHAPTERS: VideosVideoIdChapters,
        PathValues.PLAYERS: Players,
        PathValues.PLAYERS_PLAYER_ID: PlayersPlayerId,
        PathValues.PLAYERS_PLAYER_ID_LOGO: PlayersPlayerIdLogo,
        PathValues.ANALYTICS_VIDEOS_PLAYS: AnalyticsVideosPlays,
        PathValues.ANALYTICS_LIVESTREAMS_PLAYS: AnalyticsLiveStreamsPlays,
        PathValues.WEBHOOKS: Webhooks,
        PathValues.WEBHOOKS_WEBHOOK_ID: WebhooksWebhookId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.AUTH_APIKEY: AuthApiKey,
        PathValues.AUTH_REFRESH: AuthRefresh,
        PathValues.VIDEOS: Videos,
        PathValues.VIDEOS_VIDEO_ID_SOURCE: VideosVideoIdSource,
        PathValues.WATERMARKS: Watermarks,
        PathValues.WATERMARKS_WATERMARK_ID: WatermarksWatermarkId,
        PathValues.VIDEOS_VIDEO_ID_THUMBNAIL: VideosVideoIdThumbnail,
        PathValues.VIDEOS_VIDEO_ID: VideosVideoId,
        PathValues.VIDEOS_VIDEO_ID_STATUS: VideosVideoIdStatus,
        PathValues.UPLOADTOKENS: UploadTokens,
        PathValues.UPLOADTOKENS_UPLOAD_TOKEN: UploadTokensUploadToken,
        PathValues.UPLOAD: Upload,
        PathValues.LIVESTREAMS: LiveStreams,
        PathValues.LIVESTREAMS_LIVE_STREAM_ID: LiveStreamsLiveStreamId,
        PathValues.LIVESTREAMS_LIVE_STREAM_ID_THUMBNAIL: LiveStreamsLiveStreamIdThumbnail,
        PathValues.VIDEOS_VIDEO_ID_CAPTIONS_LANGUAGE: VideosVideoIdCaptionsLanguage,
        PathValues.VIDEOS_VIDEO_ID_CAPTIONS: VideosVideoIdCaptions,
        PathValues.VIDEOS_VIDEO_ID_CHAPTERS_LANGUAGE: VideosVideoIdChaptersLanguage,
        PathValues.VIDEOS_VIDEO_ID_CHAPTERS: VideosVideoIdChapters,
        PathValues.PLAYERS: Players,
        PathValues.PLAYERS_PLAYER_ID: PlayersPlayerId,
        PathValues.PLAYERS_PLAYER_ID_LOGO: PlayersPlayerIdLogo,
        PathValues.ANALYTICS_VIDEOS_PLAYS: AnalyticsVideosPlays,
        PathValues.ANALYTICS_LIVESTREAMS_PLAYS: AnalyticsLiveStreamsPlays,
        PathValues.WEBHOOKS: Webhooks,
        PathValues.WEBHOOKS_WEBHOOK_ID: WebhooksWebhookId,
    }
)
