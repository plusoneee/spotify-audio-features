
class Aritst:
    def __init__(self):
        self.artist_id = None
        self.uri = None
        self.name = None
        self.genres = None
        self.img_url = ''
    
    def to_dictionary(self):
        return {
            'artist_id': self.artist_id,
            'artist_uri': self.uri,
            'name': self.name,
            'genres': self.genres,
            'img_url': self.img_url
        }
    
    @staticmethod
    def from_dictionary(results: dict):
        artist = Aritst()

        artist.artist_id = results.get('id')
        artist.uri = results.get('uri')
        artist.name = results.get('name')
        artist.genres = str(results.get('genres'))
        if results.get('images'):
            artist.img_url = results.get('images')[0]['url']

        return artist