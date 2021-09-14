
class Aritst:
    def __init__(self):
        self.id = None
        self.uri = None
        self.name = None
    
    def to_dictionary(self):
        return {
            'id': self.id,
            'uri': self.uri,
            'name': self.name
        }

    def show_info(self):
        print("\n* Artist : %s\n-- ID : %s" % 
        (self.name, self.uri))
    
    @staticmethod
    def from_dictionary(results: dict):
        artist = Aritst()
        artist.id = results.get('id')
        artist.uri = results.get('uri')
        artist.name = results.get('name')
        return artist