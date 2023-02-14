from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date_input = input("What year would you like to travel to? Enter the year in YYYY-MM-DD fomrat.\n")
URL = "https://www.billboard.com/charts/hot-100/" + date_input
year = date_input.split(sep="-")[0]

response = requests.get(url=URL)
billboard_web_page = response.text
soup = BeautifulSoup(billboard_web_page, "html.parser")
songs_list = [song.getText().strip() for song in
              soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 "
                                              "lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 "
                                              "u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 "
                                              "u-max-width-230@tablet-only")]

songs_list.insert(0, soup.select_one("h3 a").getText().strip())


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="53d0b1e94b6d48ffb89ff3d5b0f145d9",
                                               client_secret="aa9030e3190d478eb5250255a313799d",
                                               redirect_uri="http://example.com", scope="playlist-modify-private"))
USER_ID = "31ulskholkjzfeaxxkhscsrouil4"


song_uri = []
for song in songs_list:
    result = sp.search(q=f"year:{year} track:{song}", type="track")
    try:
        uri = (result['tracks']['items'][0]['uri'])
        song_uri.append(uri)
    except IndexError:
        print(f"{song} is not available so skipped.")

playlist_id = sp.user_playlist_create(user=USER_ID, name=f"{date_input} Billboard top 100", public=False,
                                      description=f"The top 100 songs from {date_input} made programmatically using "
                                                  f"python.")['id']
sp.playlist_add_items(playlist_id=playlist_id,items=song_uri)


# 2017-05-13
