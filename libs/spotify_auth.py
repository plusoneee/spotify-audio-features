from spotipy import Spotify
from spotipy import SpotifyException
from spotipy import util
from dotenv import load_dotenv
import os
load_dotenv()

class SpotifyUser():
    def __init__(self):
        self.username = os.getenv("username")
        self.password = os.getenv("password")
        self.client_secret = os.getenv("client_secret")
        self.redirect_uri = os.getenv("redirect_uri")
        self.client_id = os.getenv("client_id")
        self.scope = os.getenv("scope")

    def to_dictionary(self):
        
        assert self.username is None, 'Spotify username was not load, please check the .env file'
        assert self.password is None, 'Spotify password was not load, please check the .env file'
        assert self.client_secret is None, 'Spotify client secret was not load, please check the .env file'
        assert self.client_id is None, 'Spotify client id was not load, please check the .env file'

        return {
            'username': self.username,
            'password': self.password,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_uri,
            'client_id': self.client_id,
            'scope': self.scope
        }

class SpotifyAuth:
    def __init__(self, info :SpotifyUser):
        self.info = info
    
    @property
    def sp(self):
        return self.spotify_auth()

    def spotify_auth(self):
        try:
            token = self.get_user_token()
        
        except SpotifyException as e:
            # token expired then get again
            token = self.get_user_token()
            
        return Spotify(auth=token)
        
    
    def get_user_token(self):
        token = util.prompt_for_user_token(
                        username=self.info.username,
                        scope=self.info.scope,
                        client_id=self.info.client_id,
                        redirect_uri=self.info.redirect_uri,
                        client_secret=self.info.client_secret
            )
        return token

if __name__ == '__main__':

    # how to use
    userinfo = SpotifyUser()
    sp = SpotifyAuth(userinfo).sp
    print(sp.user_playlists(userinfo.username))