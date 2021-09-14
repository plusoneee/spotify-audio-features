
from libs.artist import Aritst
from libs.album import Album
from libs.track import Track
from libs.playlist import Playlist
import pandas as pd

class Exportor:
    def __init__(self):
        pass

    @staticmethod
    def dictionary_to_df(track: dict):
        return pd.json_normalize(track, sep='_')

    def export_to_csv(frames: list, filename='features', index=False):
        result = pd.concat(frames, ignore_index=True)
        result.to_csv(f'{filename}.csv', index=False)
        print('---'*50)
        print(f'\n* File {filename}.csv was Exported. Preview:')
        print(result.head())
        print('---'*50)


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
                
                # track_aritst.show_info()
                # track_album.show_info()
                
                # parse track infomation and track audio features
                track  = Track.info_from_dictionary(_trackInfo)
                _features = sp.audio_features(track.track_id)
                track = Track.features_from_dictionary(_features[0], track)

                tracksItems.append({
                    'artist' : track_aritst.to_dictionary(),
                    'album': track_album.to_dictionary(),
                    'track': track.to_dictionary()
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
            
        album = Album.from_dictionary(_album_dict)
        artist = Aritst.from_dictionary(_artist_dict)

        if 'artists' in trackinfo: del trackinfo['artists'] # delete key
        if 'album' in trackinfo: del trackinfo['album'] # delete key
        
        return artist, album