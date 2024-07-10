class User:
    def __init__(self, user_id, ratings):
        self.user_id = user_id
        self.ratings = ratings

class Song:
    def __init__(self, song_id, features):
        self.song_id = song_id
        self.features = features