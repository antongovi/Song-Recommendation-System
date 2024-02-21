import streamlit as st
import requests
import base64
import pandas as pd
import spotipy
from spotipy.client import SpotifyException
from sklearn.metrics.pairwise import cosine_similarity

# Spotify API credentials
client_id = '4bfcfc5810374447b13d593925b9fbd3'
client_secret = 'e6f4755f93f747c5acb311a4c78de8a8'

# Initialize Spotipy client
client_credentials = f"{client_id}:{client_secret}"
client_credentials_base64 = base64.b64encode(client_credentials.encode())
token_url = 'https://accounts.spotify.com/api/token'
headers = {'Authorization': f'Basic {client_credentials_base64.decode()}'}
data = {'grant_type': 'client_credentials'}
response = requests.post(token_url, data=data, headers=headers)

if response.status_code == 200:
    access_token = response.json()['access_token']
    st.write("Access token obtained successfully.")
else:
    st.write("Error obtaining access token.")
    st.stop()

sp = spotipy.Spotify(auth=access_token)

# Load tracks data
file_path = 'tracks.csv'
tracks_df = pd.read_csv(file_path)


# Function to extract track features
def extract_track_features(track_id):
    try:
        track_data = []
        track = sp.track(track_id)
        audio_features = sp.audio_features(track_id)
        artist_id = track['artists'][0]['id']
        artist = sp.artist(artist_id)

        track_info = {
            'track_name': track['name'],
            'track_id': track_id,
            'artist_name': ', '.join([artist['name'] for artist in track['artists']]),
            'album_name': track['album']['name'],
            'release_date': track['album']['release_date'],
            'artist_genre': artist['genres'][0] if audio_features and len(artist['genres']) > 0 else None,
            'popularity': track['popularity'],
            'Duration (ms)': track['duration_ms'],
            'Acousticness': audio_features[0]['acousticness'] if audio_features else None,
            'Danceability': audio_features[0]['danceability'] if audio_features else None,
            'Energy': audio_features[0]['energy'] if audio_features else None,
            'Instrumentalness': audio_features[0]['instrumentalness'] if audio_features else None,
            'Key': audio_features[0]['key'] if audio_features else None,
            'Liveness': audio_features[0]['liveness'] if audio_features else None,
            'Loudness': audio_features[0]['loudness'] if audio_features else None,
            'Mode': audio_features[0]['mode'] if audio_features else None,
            'Speechiness': audio_features[0]['speechiness'] if audio_features else None,
            'Tempo': audio_features[0]['tempo'] if audio_features else None,
            'Time Signature': audio_features[0]['time_signature'] if audio_features else None,
            'Valence': audio_features[0]['valence'] if audio_features else None
        }

        return pd.DataFrame([track_info])

    except SpotifyException as e:
        if e.http_status == 429:
            st.warning("Too many requests. Please try again later.")
        else:
            st.error("An error occurred while fetching data from Spotify.")
        st.stop()


# Function to get similar songs
def get_similar_songs(new_track_features, training_features, num_recommendations=5):
    similarity_scores = cosine_similarity(new_track_features, training_features)
    similar_song_indices = similarity_scores.argsort()[0][::-1][:num_recommendations]
    return similar_song_indices


# Streamlit app
st.title("Similar Songs Recommender")

# Input fields
track_name = st.text_input("Enter Track Name", value='Enough is Enough')
artist_name = st.text_input("Enter Artist Name", value='Post Malone')
submit_button = st.button("Submit")

# Display similar songs
if submit_button:
    # Search for track ID
    results = sp.search(q=f'track:{track_name} artist:{artist_name}', limit=1)
    if results['tracks']['items']:
        track_id = results['tracks']['items'][0]['id']
        new_track_df = extract_track_features(track_id)

        tracks_df['artist_genre'] = tracks_df['artist_genre'].str.extract(r'\[\'(.*?)\'')[0]
        all_genres = pd.concat([tracks_df['artist_genre'], new_track_df['artist_genre']]).unique()
        genre_mapping = {genre: code for code, genre in enumerate(all_genres)}
        tracks_df['artist_genre'] = tracks_df['artist_genre'].map(genre_mapping)
        new_track_df['artist_genre'] = new_track_df['artist_genre'].map(genre_mapping)

        numerical_features = ['artist_genre', 'popularity', 'Duration (ms)', 'Acousticness', 'Danceability', 'Energy',
                              'Instrumentalness', 'Key', 'Liveness', 'Loudness', 'Mode', 'Speechiness',
                              'Tempo', 'Time Signature', 'Valence']

        tracks_df_filtered = tracks_df[tracks_df['track_id'] != new_track_df['track_id'].iloc[0]]

        training_features = tracks_df_filtered[numerical_features]
        new_track_features = new_track_df[numerical_features]

        similar_song_indices = get_similar_songs(new_track_features, training_features)

        similar_songs = tracks_df.iloc[similar_song_indices]
        similar_songs.reset_index(drop=True, inplace=True)
        st.table(similar_songs[['track_name', 'artist_name']])
    else:
        st.write("No results found.")
