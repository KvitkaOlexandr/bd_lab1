import datetime

from rockdb import RockDB


class Check:

    @staticmethod
    def test_timestamp(time_str):
        try:
            datetime.datetime.strptime(time_str, '%Y-%m-%d')  # '2004-10-19'
            return True
        except ValueError:
            return False

    @staticmethod
    def check_band(band_id):
        db = RockDB()
        return db.get_band(band_id) is not None

    @staticmethod
    def check_album(album_id):
        db = RockDB()
        return db.get_album(album_id) is not None

    @staticmethod
    def check_song(song_id):
        db = RockDB()
        return db.get_song(song_id) is not None
