import requests
from bs4 import BeautifulSoup

def get_lyrics(track_name, artist_name):
    query = f"{track_name} {artist_name} lyrics"
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    lyrics_divs = soup.select("div.BNeawe.tAd8D.AP7Wnd")  # Common in Google's lyrics box

    for div in lyrics_divs:
        if div.text.strip().count("\n") > 2:  # Likely actual lyrics
            return div.text.strip()

    return "Lyrics not found."