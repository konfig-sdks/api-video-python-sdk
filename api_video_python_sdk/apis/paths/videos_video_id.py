from api_video_python_sdk.paths.videos_video_id.get import ApiForget
from api_video_python_sdk.paths.videos_video_id.delete import ApiFordelete
from api_video_python_sdk.paths.videos_video_id.patch import ApiForpatch


class VideosVideoId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
