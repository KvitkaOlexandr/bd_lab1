import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from structures import Band
from structures import Album
from structures import Song
from structures import Base


class RockDB:
    _engine_ = create_engine('postgresql://postgres:SK10909090@localhost:5432/postgres')
    _Session_ = sessionmaker(bind=_engine_)

    def __init__(self):
        _engine_ = create_engine('postgresql://postgres:SK10909090@localhost:5432/postgres')
        _Session_ = sessionmaker(bind=_engine_)
        Base.metadata.create_all(_engine_)
        self._session_ = _Session_()

    def close(self):
        self._session_.close()

    '''band'''

    def get_band(self, band_id):
        return self._session_.query(Band).get(band_id)

    def insert_band(self, band: Band):
        self._session_.add(band)
        self._session_.commit()

    def insert_list_of_bands(self, band_list):
        for band in band_list:
            self.insert_band(band)

    def update_band(self, band: Band):
        self.insert_band(band)

    def delete_band(self, band_id):
        self._session_.query(Band).filter_by(id=band_id).delete()
        self._session_.commit()

    '''ALBUM'''

    def get_album(self, album_id):
        return self._session_.query(Band).get(album_id)

    def insert_album(self, album: Album):
        self._session_.add(album)
        self._session_.commit()

    def insert_list_of_albums(self, album_list):
        for album in album_list:
            self.insert_album(album)

    def update_album(self, album: Album):
        self.insert_album(album)

    def delete_album(self, album_id):
        self._session_.query(Album).filter_by(id=album_id).delete()
        self._session_.commit()

    '''Song'''

    def get_song(self, song_id):
        return self._session_.query(Song).get(song_id)

    def insert_song(self, song: Song):
        self._session_.add(song)
        self._session_.commit()

    def update_song(self, song: Song):
        self.insert_song(song)

    def delete_song(self, song_id):
        self._session_.query(Song).filter_by(id=song_id).delete()
        self._session_.commit()

    '''get all'''

    def get_table_string(self, table_name):
        return self._session_.query(Base.metadata.tables[table_name]).all()

    '''search'''

    def search_reward_existence(self, reward_existence):
        search = self._session_.query(Band)\
            .filter(Band.reward_existence == reward_existence)\
            .all()
        strings = ""
        for res in search:
            strings += str(res.__dict__) + "\n"
        return strings

    def search_by_date(self, left, right):
        search = self._session_.query(Album) \
            .filter(Album.presentation_date >= left,
                    Album.presentation_date < right) \
            .all()
        strings = ""
        for res in search:
            strings += str(res.__dict__) + "\n"
        return strings

    def search_by_word_not_belong(self, word):
        sql = f"""SELECT * FROM band WHERE to_tsvector(name) @@ to_tsquery('!{word}');"""
        search = self._session_.execute(sql).fetchall()
        strings = ""
        for res in search:
            strings += str(dict(res.items())) + "\n"
        return strings

    def search_by_phrase(self, phrase):
        sql = f"""SELECT * FROM song 
                  WHERE to_tsvector(name) @@ phraseto_tsquery('english', '{phrase}');"""
        search = self._engine_.execute(sql).fetchall()
        strings = ""
        for res in search:
            strings += str(dict(res.items())) + "\n"
        return strings

    def get_random_band_id(self):
        rand_index = random.randint(0, self._session_.query(Band).count())
        return self._session_.query(Band)[rand_index]

    def get_random_album_id(self):
        rand_index = random.randint(0, self._session_.query(Album).count())
        return self._session_.query(Album)[rand_index]

    def get_random_song_id(self):
        rand_index = random.randint(0, self._session_.query(Song).count())
        return self._session_.query(Song)[rand_index]
