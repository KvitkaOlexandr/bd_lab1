import random

import psycopg2
import pandas as pd
import psycopg2.extras

from structures import Band
from structures import Album
from structures import Song


class RockDB:
    conn = psycopg2.connect("dbname='postgres' host='localhost' user ='postgres' password='SK10909090'")
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def __init__(self):
        try:
            self.conn = psycopg2.connect("dbname='postgres' host='localhost' user ='postgres' password='SK10909090'")
        except psycopg2.Error as err:
            print("Connection error: {}".format(err))
        try:
            self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        except psycopg2.Error as err:
            print("Query error: {}".format(err))

    def close(self):
        self.cur.close()
        self.conn.close()

    def query(self, query, params):
        return self.cur.execute(query, params)

    '''band'''

    def get_band(self, band_id):
        RockDB.cur.execute(f"""SELECT * FROM band WHERE id = '{band_id}'""")
        return RockDB.cur.fetchone()

    def insert_band(self, band: Band):
        sql = "INSERT INTO band(id, name, genre, album_number, reward_existence, country) " \
              "VALUES(%s, %s, %s, %s, %s, %s);"
        RockDB.cur.execute(sql, (band.id,
                                 band.name,
                                 band.genre,
                                 band.album_number,
                                 band.reward_existence,
                                 band.country))
        RockDB.conn.commit()

    def insert_band_list(self, band_list):
        for band in band_list:
            self.insert_band(band)

    def update_band(self, band: Band):
        sql = """ UPDATE band
                    SET name = %s,
                    genre = %s,
                    album_number = %s,
                    reward_existence = %s,
                    country = %s
                    WHERE id = %s"""
        RockDB.cur.execute(sql, (band.name,
                                 band.genre,
                                 band.album_number,
                                 band.reward_existence,
                                 band.country,
                                 band.id,))
        RockDB.conn.commit()

    def delete_band(self, band_id):
        RockDB.cur.execute(f"""DELETE FROM band WHERE id = '{band_id}'""")
        RockDB.conn.commit()

    """album"""

    def get_album(self, album_id):
        RockDB.cur.execute(f"""SELECT * FROM album WHERE id = '{album_id}'""")
        return RockDB.cur.fetchone()

    def insert_album(self, album: Album):
        sql = "INSERT INTO album(id, name, presentation_date, songs_number, band_id) " \
              "VALUES(%s, %s, %s, %s, %s);"
        RockDB.cur.execute(sql, (album.id, album.name, album.presentation_date, album.songs_number, album.band_id))
        RockDB.conn.commit()

    def insert_album_list(self, album_list):
        for album in album_list:
            self.insert_album(album)

    def update_album(self, album: Album):
        sql = """ UPDATE album
                    SET name = %s,
                    presentation_date = %s,
                    songs_number = %s,
                    band_id = %s
                    WHERE id = %s"""
        RockDB.cur.execute(sql, (album.name, album.presentation_date, album.songs_number, album.band_id, album.id))
        RockDB.conn.commit()

    def delete_album(self, album_id):
        RockDB.cur.execute(f"""DELETE FROM album WHERE id = '{album_id}'""")
        RockDB.conn.commit()

        """song"""

    def get_song(self, song_id):
        RockDB.cur.execute(f"""SELECT * FROM song WHERE id = '{song_id}'""")
        return RockDB.cur.fetchone()

    def insert_song(self, song: Song):
        sql = "INSERT INTO song(id, name, language, album_id) " \
              "VALUES(%s, %s, %s, %s);"
        RockDB.cur.execute(sql, (song.id, song.name, song.language, song.album_id))
        RockDB.conn.commit()

    def update_song(self, song: Song):
        sql = """ UPDATE song
                    SET name = %s, 
                    language = %s,
                    album_id = %s
                    WHERE id = %s"""
        RockDB.cur.execute(sql, (song.name, song.language, song.album_id, song.id))
        RockDB.conn.commit()

    def delete_song(self, song_id):
        RockDB.cur.execute(f"""DELETE FROM song WHERE id = '{song_id}'""")
        RockDB.conn.commit()

    def get_table_string(self, table_name):
        sql = "SELECT * FROM {0}".format(table_name)
        return pd.read_sql(sql, self.conn)

    def search_reward_existence(self, reward_exist):
        sql = f"""SELECT * FROM band WHERE reward_existence = 
                                '{reward_exist}'"""
        return pd.read_sql(sql, self.conn)

    def search_by_date(self, left, right):
        sql = f"""SELECT * FROM album WHERE presentation_date >= 
                                '{left}' AND presentation_date < '{right}'"""
        return pd.read_sql(sql, self.conn)

    def search_by_word_not_belong(self, word):
        sql = f"""SELECT * FROM band WHERE to_tsvector(name) @@ to_tsquery('!{word}');"""
        return pd.read_sql(sql, self.conn)

    def search_by_phrase(self, phrase):
        sql = f"""SELECT * FROM song 
                  WHERE to_tsvector(name) @@ plainto_tsquery('{phrase}');"""
        return pd.read_sql(sql, self.conn)

    def get_random_band_id(self):
        RockDB.cur.execute("SELECT id FROM band")
        band_id_arr = RockDB.cur.fetchall()
        rand_index = random.randint(0, (len(band_id_arr) - 1))
        return band_id_arr[rand_index]

    def get_random_album_id(self):
        RockDB.cur.execute("SELECT id FROM album")
        album_id_arr = RockDB.cur.fetchall()
        rand_index = random.randint(0, (len(album_id_arr) - 1))
        return album_id_arr[rand_index]

    def get_random_song_id(self):
        RockDB.cur.execute("SELECT id FROM song")
        song_id_arr = RockDB.cur.fetchall()
        rand_index = random.randint(0, (len(song_id_arr) - 1))
        return song_id_arr[rand_index]






