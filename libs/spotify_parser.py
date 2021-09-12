
from libs.artist import Aritst
from libs.album import Album
from libs.track import Track
from libs.playlist import Playlist

class SpotifyParser:
    def __init__(self):
        pass

    @staticmethod
    def get_user_playlists(sp, username):
        results = sp.user_playlists(username)
        playlists = []
        while results:    
            for item in results['items']:
                playlists.append(
                    Playlist.from_dictionary(item)
                )
            if results['next']:
                results = sp.next(results)
            else:
                results = None
        return playlists

    @staticmethod
    def get_playlist_tracks(sp, playlist_id):
        results = sp.playlist_tracks(playlist_id)
        tracksItems = []
        while results:    
            for item in results['items']:
                _trackInfo = item.get('track')
                track_aritst, track_album = SpotifyParser.parse_track_artist_album(_trackInfo)
                
                # parse track infomation and track audio features
                track  = Track.info_from_dictionary(_trackInfo)
                _features = sp.audio_features(track.track_id)
                track = Track.features_from_dictionary(_features[0], track)

                tracksItems.append({
                    'artist' : track_aritst,
                    'album': track_album,
                    'track': track
                })

            if results['next']:
                results = sp.next(results)
            else:
                results = None

        return tracksItems

    @staticmethod
    def parse_track_artist_album(trackinfo: dict):
        
        _album_dict = trackinfo.get('album', {})            
        _artist_dict = trackinfo.get('artists', {})[0] # index 0: primary artist
        
        if 'artists' in trackinfo: del trackinfo['artists'] # delete key
        if 'album' in trackinfo: del trackinfo['album'] # delete key
            
        album = Album.from_dictionary(_album_dict)
        artist = Aritst.from_dictionary(_artist_dict)
        
        return artist, album