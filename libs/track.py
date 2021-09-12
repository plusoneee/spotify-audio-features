
class Track:
    def __init__(self):
        self.track_id = None
        self.uri = None
        self.name = None
        self.preview_url = ''
        self.duration_ms = 0
        
        # audio features
        self.danceability = None
        self.energy = None
        self.loudness = None
        self.mode = None
        self.speechiness = None
        self.acousticness = None
        self.instrumentalness = None
        self.liveness = None
        self.valence = None
        self.tempo = None
        
    def to_dictionary(self):

        return {
            'track_id': self.track_id,
            'track_uri': self.uri,
            'name': self.name,
            'preview_url': self.preview_url,
            'duration_ms': self.duration_ms,
            'danceability': self.danceability,
            'energy': self.energy,
            'loudness': self.loudness,
            'mode': self.mode,
            'speechiness': self.speechiness,
            'acousticness': self.acousticness,
            'instrumentalness': self.instrumentalness,
            'liveness': self.liveness,
            'valence': self.valence,
            'tempo': self.tempo
        }

    @staticmethod
    def info_from_dictionary(results: dict, track=None):

        if track is None:
            track = Track()

        track.track_id = results.get('id')
        track.uri = results.get('uri')
        track.name = results.get('name')
        track.preview_url = results.get('preview_url')
        track.duration_ms = results.get('duration_ms')
        
        return track
    
    @staticmethod
    def features_from_dictionary(results: dict, track=None):

        if track is None:
            track = Track()

        track.danceability = results.get('danceability')
        track.energy = results.get('energy')
        track.loudness = results.get('loudness')
        track.mode = results.get('mode')
        track.speechiness = results.get('speechiness')
        track.acousticness = results.get('acousticness')
        track.instrumentalness = results.get('instrumentalness')
        track.liveness = results.get('liveness')
        track.valence = results.get('valence')
        track.tempo = results.get('tempo')

        return track