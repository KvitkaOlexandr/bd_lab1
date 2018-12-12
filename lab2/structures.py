from sqlalchemy import Column, String, Integer, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Band(Base):
    __tablename__ = "band"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    genre = Column(String)
    album_number = Column(Integer)
    reward_existence = Column(Boolean)
    country = Column(String)

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


class Album(Base):
    __tablename__ = "album"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    presentation_date = Column(Date)
    songs_number = Column(Integer)
    band_id = Column(Integer, )

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


class Song(Base):
    __tablename__ = "song"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    language = Column(String)
    album_id = Column(Integer)

    def __init__(self,
                 song_id,
                 song_name,
                 song_language,
                 song_album_id):
        self.id = song_id
        self.name = song_name
        self.language = song_language
        self.album_id = song_album_id
