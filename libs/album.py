
class Album:
    def __init__(self):
        self.album_id = None
        self.uri = None
        self.name = None
        self.total_tracks = 0
        self.released = None
        self.img_url = ''
        self.preview_url = ''

    def to_dictionary(self):
        return {
            'album_id': self.album_id,
            'album_uri': self.uri,
            'name': self.name,
            'total_tracks': self.total_tracks,
            'released': self.released,
            'img_url': self.img_url,
            'preview_url': self.preview_url
        }
        
    @staticmethod
    def from_dictionary(results: dict):
        album = Album()
        album.album_id = results.get('id')
        album.uri = results.get('uri')
        album.name = results.get('name')
        album.total_tracks = results.get('total_tracks')
        album.released = results.get('release_date')

        images = results.get('images')
        if images: album.img_url = images[0].get('url')
        
        external_urls = results.get('external_urls')
        album.preview_url = external_urls.get('spotify')

        return album