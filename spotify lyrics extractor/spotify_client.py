import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Replace with your actual credentials
CLIENT_ID = '9248ac3d08204a368d5ba90aef918c19'
CLIENT_SECRET = 'a17cd83dce7e4b299fc543cf7293c2f5'

def get_spotify_client():
    credentials = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    return spotipy.Spotify(client_credentials_manager=credentials)
