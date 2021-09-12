
class Playlist:
    def __init__(self):
        self.name = None
        self.uri = None
        self.total = 0

    def show_info(self):
        print("\n* Playlist : %s\n-- ID : %s\n-- Total : %s" % (self.name, self.uri, self.total))
    
    def to_dictionary(self):
        return {
            'name': self.name,
            'uri': self.uri,
            'total': self.total
        }

    @staticmethod
    def from_dictionary(item: dict):
        playlist = Playlist()
        playlist.uri = item.get('uri')
        playlist.name = item.get('name')
        playlist.total = item.get('tracks', {}).get('total')

        return playlist
