# Song Recommendation System
This repository contains code for extracting song data from Spotify playlists (using Spotify's Web API) and building a song recommendation system using cosine similarity and kNN. It also includes a Streamlit app for interactively exploring similar songs. 

## Notebooks:
### Song Data Extraction.ipynb:
This notebook extracts song information from different playlists on Spotify and stores it in a CSV file. The extracted information includes:
- Track name
- Track ID: The Spotify ID for the track
- Artist name
- Album name
- Release date
- Artist genres
- Popularity: The popularity of the artist. The value will be between 0 and 100, with 100 being the most popular.
- Duration (ms): The duration of the track in milliseconds.
- Acousticness: A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.
- Danceability: Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.

- Energy: Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.
  
- Instrumentalness: Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.
  
- Key: The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1.
- Liveness: Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.
  
- Loudness: The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db.
  
- Mode: Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.
- Speechiness: Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.

- Tempo: The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
  
- Time signature: An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of "3/4", to "7/4".

- Valence: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).



### Song Recommendation System.ipynb:
This notebook loads the CSV file created in the "Song Data Extraction" notebook, finds the data for the desired song and finally uses two different approaches to find similar tracks: cosine similarity and kNN.


## Streamlit App
### song_recommender.py: 
This file contains code for a Streamlit app that allows users to input a song and artist name and get recommendations for similar songs. Using similar code to the "Song Recommendation System.ipynb" notebook.

Example of a search in the Streamlit App: 

![Screenshot of the Atreamlit App ](https://github.com/antongovi/Song-Recommendation-System/blob/aa161eef3e7aa550dd6f1f163e87016841f115a8/Streamlit%20APP/Images/Screenshot%202024-02-21%20at%2015.04.46.png)



# Contact
For any inquiries or feedback, please contact antongv7@gmail.com or www.linkedin.com/in/anton-goma/.


