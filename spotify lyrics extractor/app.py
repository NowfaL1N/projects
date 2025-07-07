from flask import Flask, render_template, request
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import lyricsgenius
import os

app = Flask(__name__)

# Set your credentials here
SPOTIPY_CLIENT_ID = "9248ac3d08204a368d5ba90aef918c19"
SPOTIPY_CLIENT_SECRET = "a17cd83dce7e4b299fc543cf7293c2f5"
GENIUS_ACCESS_TOKEN = "xrZH392YLONavB8UVDo8UBlOlxAEVVFPc_hQGM9xrXiucx782ZmhH6up86IolubG"

# Setup Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET
))

# Setup Genius API
genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN, timeout=15, retries=3)

@app.route("/", methods=["GET", "POST"])
def index():
    lyrics = None
    album_cover = None
    preview_url = None
    error = None

    if request.method == "POST":
        song = request.form["song"]
        try:
            # Search for the song on Spotify
            results = sp.search(q=song, type='track', limit=1)
            track = results['tracks']['items'][0]

            title = track['name']
            artist = track['artists'][0]['name']
            album_cover = track['album']['images'][0]['url']
            preview_url = track['preview_url']

            # Search for lyrics using Genius
            song_genius = genius.search_song(title, artist)
            if song_genius:
                lyrics = song_genius.lyrics
            else:
                lyrics = "Lyrics not found on Genius."

        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template("index.html", lyrics=lyrics, cover_url=album_cover, preview=preview_url, error=error)

if __name__ == "__main__":
    app.run(debug=True)
