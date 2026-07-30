from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

date = input("Which year do you want to travel to? Type the date (YYYY-MM-DD): ")

url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

songs = [
    song.getText().strip()
    for song in soup.select("li ul li h3")
]

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="playlist-modify-private"
    )
)

user_id = spotify.current_user()["id"]

song_uris = []

year = date.split("-")[0]

for song in songs:
    result = spotify.search(
        q=f"track:{song} year:{year}",
        type="track",
        limit=1
    )

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} not found on Spotify.")

playlist = spotify.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False
)

spotify.playlist_add_items(
    playlist_id=playlist["id"],
    items=song_uris
)

print("Playlist created successfully!")