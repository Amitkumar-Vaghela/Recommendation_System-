from flask import Flask, request, jsonify
from models import User, Song
from recommendations import recommend_songs
from api_calls import get_user_data, get_song_data

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    user_id = request.json['user_id']
    num_songs = request.json['num_songs']
    user_data = get_user_data(user_id)
    song_data = get_song_data()
    recommended_songs = recommend_songs(user_data, song_data, num_songs)
    return jsonify({'recommended_songs': recommended_songs})

if __name__ == '__main__':
    app.run(debug=True)