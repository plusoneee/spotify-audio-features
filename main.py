from libs.spotify_auth import SpotifyUser, SpotifyAuth
from libs.spotify_parser import SpotifyParser, Exportor
import pandas as pd

if __name__ == '__main__':
    user = SpotifyUser()
    sp = SpotifyAuth(user).sp
    
    # get user playlist with sp
    playlists = SpotifyParser.get_user_playlists(sp, user.username)

    # get all tracks in playlist 
    for playlist in playlists:
        frames = []
        playlist_tracks = SpotifyParser.get_playlist_tracks(sp, playlist.uri)        
    
        
        for track in playlist_tracks:
            frames.append(Exportor.dictionary_to_df(track))
        
        Exportor.export_to_csv(frames, playlist.name)
        # print(f'* Got {len(playlist_tracks)} tracks in `{playlist.name}` playlist.')