from libs.spotify_auth import SpotifyUser, SpotifyAuth
from libs.spotify_parser import SpotifyParser

if __name__ == '__main__':
    user = SpotifyUser()
    sp = SpotifyAuth(user).sp
    
    # get user playlist with sp
    playlists = SpotifyParser.get_user_playlists(sp, user.username)

    # get all tracks in playlist 
    for playlist in playlists:
        playlist_tracks = SpotifyParser.get_playlist_tracks(sp, playlist.uri)        

        print(f'Got {len(playlist_tracks)} tracks in `{playlist.name}` playlist')
