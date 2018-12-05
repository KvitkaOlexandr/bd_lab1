class Band:
    id = ""
    name = ""
    genre = ""
    album_number = 0
    reward_existence = ""
    country = ""

    def __init__(self,
                 band_id,
                 band_name,
                 band_genre,
                 band_album_number,
                 band_reward_existence,
                 band_country):
        self.id = band_id
        self.name = band_name
        self.genre = band_genre
        self.album_number = band_album_number
        self.reward_existence = band_reward_existence
        self.country = band_country


class Album:
    id = ""
    name = ""
    presentation_date = ""
    songs_number = 0
    band_id = ""

    def __init__(self,
                 album_id,
                 album_name,
                 album_presentation_date,
                 album_songs_number,
                 album_band_id):
        self.id = album_id
        self.name = album_name
        self.presentation_date = album_presentation_date
        self.songs_number = album_songs_number
        self.band_id = album_band_id


class Song:
    id = ""
    name = ""
    language = ""
    album_id = ""

    def __init__(self,
                 song_id,
                 song_name,
                 song_language,
                 song_album_id):
        self.id =  song_id
        self.name = song_name
        self.language = song_language
        self.album_id = song_album_id


