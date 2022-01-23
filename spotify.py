import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config

scope = "user-library-read"
client_id = config.client_id
client_secret = config.client_secret
redirect_uri = config.redirect_uri

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

print(sp.audio_analysis('0F1yb5tFzXDocAXqcljA9H'))

# 0F1yb5tFzXDocAXqcljA9H
