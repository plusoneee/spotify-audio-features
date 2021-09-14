
class Album:
    def __init__(self):
        self.id = None
        self.uri = None
        self.name = None
        self.total = 0
        self.released = None
        self.img_url = ''
        self.preview_url = ''

    def show_info(self):
        print("\n* Album : %s\n-- ID : %s\n-- Total : %s\n-- Preview Url : %s\n-- Released Date : %s" % 
        (self.name, self.uri, self.total_tracks, self.preview_url, self.released))

    def to_dictionary(self):
        return {
            'id': self.id,
            'uri': self.uri,
            'name': self.name,
            'total': self.total_tracks,
            'released': self.released,
            'img_url': self.img_url,
            'preview_url': self.preview_url
        }
        
    @staticmethod
    def from_dictionary(results: dict):
        album = Album()
        album.id = results.get('id')
        album.uri = results.get('uri')
        album.name = results.get('name')
        album.total_tracks = results.get('total_tracks')
        album.released = results.get('release_date')

        images = results.get('images')
        if images: album.img_url = images[0].get('url')
        
        external_urls = results.get('external_urls')
        if external_urls:
            album.preview_url = external_urls.get('spotify')

        return album