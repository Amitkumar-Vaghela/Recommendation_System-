import requests

def get_user_data(user_id):
    # API call to get user data from music streaming service
    response = requests.get(f'https://api.musicstreaming.com/users/{user_id}')
    user_data = response.json()
    return user_data

def get_song_data():
    # API call to get song data from music streaming service
    response = requests.get('https://api.musicstreaming.com/songs')
    song_data = response.json()
    return song_data
