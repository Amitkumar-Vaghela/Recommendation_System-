import requests

def get_user_data(user_id):
    # API call to get user data from music streaming service
    response = requests.get(f'https://musicbrainz.org/ws/2/recording?query=%22we%20will%20rock%20you%22%20AND%20arid:0383dadf-2a4e-4d10-a46a-e9e041da8eb3')
    user_data = response.json()
    return user_data

def get_song_data():
    # API call to get song data from music streaming service
    response = requests.get('https://musicbrainz.org/ws/2/recording?query=%22we%20will%20rock%20you%22%20AND%20arid:0383dadf-2a4e-4d10-a46a-e9e041da8eb3')
    song_data = response.json()
    return song_data
