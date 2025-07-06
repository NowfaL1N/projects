from flask import Flask, request, render_template
import spotipy
from spotify_client import get_spotify_client
from lyrics_genius import get_lyrics


app = Flask(__name__)
sp = get_spotify_client()

@app.route('/', methods=['GET', 'POST'])
def index():
    lyrics = ''
    if request.method == 'POST':
        song = request.form['song']
        results = sp.search(q=song, type='track', limit=1)
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            track_name = track['name']
            artist_name = track['artists'][0]['name']
            lyrics = get_lyrics(track_name, artist_name)
        else:
            lyrics = 'Track not found on Spotify.'
    return render_template('index.html', lyrics=lyrics)

if __name__ == '__main__':
    app.run(debug=True)
# app.py - Main Flask application to serve the lyrics search functionality  import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="9248ac3d08204a368d5ba90aef918c19",
    client_secret="a17cd83dce7e4b299fc543cf7293c2f5"
))
