from api_video_python_sdk.paths.players_player_id.get import ApiForget
from api_video_python_sdk.paths.players_player_id.delete import ApiFordelete
from api_video_python_sdk.paths.players_player_id.patch import ApiForpatch


class PlayersPlayerId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
