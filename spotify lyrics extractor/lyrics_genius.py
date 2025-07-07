from dotenv import load_dotenv
import os
import lyricsgenius
from requests.exceptions import Timeout, RequestException

load_dotenv()  # ✅ This loads .env

GENIUS_ACCESS_TOKEN = os.getenv("GENIUS_ACCESS_TOKEN")
if not GENIUS_ACCESS_TOKEN:
    raise Exception("GENIUS_ACCESS_TOKEN is not set in .env!")

genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)
genius.timeout = 15

def get_lyrics(track_name, artist_name=None):
    try:
        song = genius.search_song(title=track_name, artist=artist_name)
        if song:
            return song.lyrics
        else:
            return "Lyrics not found."
    except Timeout:
        return "Error: Genius API timed out. Try again."
    except RequestException as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"
