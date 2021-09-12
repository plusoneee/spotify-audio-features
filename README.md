# Spotify Audio Features

* A Project for automatically get tracks audio features from user's `Spotify` playlists by calling `spotify-api`.

## Python3 requirements
```
spotipy
python-dotenv
```

## Before starting
You need to have an [Spotify](https://www.spotify.com/) account, and then create your Playlist(s).

Next, Write your (Spotify-api) personal information in `.env.example` file by following the steps below:

1. Edit the file `.env.example` .
2. Saving the edited file as `.env`.
3. You could follow these commands below:

* Copy the file and save as `.env`.
```
cp .env.example .env
```
* Fill in each field in the `.env`.

```
username = 'my_user_name'
password = 'my_spotify_password'
client_id = 'my_client_id'
client_secret = 'my_client_secret'
redirect_uri='http://localhost/'
scope = 'user-library-read'
```

## Run
```
python main.py
```

## About:

* More about Audio features at [spotipy](https://developer.spotify.com/documentation/web-api/reference/tracks/get-several-audio-features/).
