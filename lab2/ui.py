from rockdb import RockDB
from get_char import Switch
from check import Check
from structures import Band
from structures import Album
from structures import Song


db = RockDB()


class UI:
    def band_input(self):
        b_id = input("enter band's id: ")
        name = input("enter band's name: ")
        genre = input("enter band's ganre: ")
        album_number = input("enter number of band's album: ")
        reward_existence = input("enter band's reward existence (True/False): ")
        while reward_existence != "True" and reward_existence != "False":
            reward_existence = input("Wrong input!\nTry again: ")
        reward_existence = bool(reward_existence)
        country = input("enter band's native country: ")
        band = Band(b_id, name, genre, album_number, reward_existence, country)
        return band

    def album_input(self):
        a_id = input("enter album's id: ")
        name = input("enter album's name: ")
        presentation_date = self.get_date()
        songs_number = input("enter number of songs in album: ")
        band_id = input("enter id of band which created album: ")
        while not Check.check_band(band_id):
            string = input("There is no such band\nYou can add it\n(y/n): ")
            for case in Switch(string):
                if case('y'):
                    band = self.band_input()
                    band_id = band.id
                    db.insert_band(band)
                    break
                if case('n'):
                    print("can't insert album")
                    return
                else:
                    print("wrong input, try again!")
        album = Album(a_id, name, presentation_date, songs_number, band_id)
        return album

    def song_input(self):
        s_id = input("enter song's id: ")
        name = input("enter song's name: ")
        language = input("enter song's language: ")
        album_id = input("enter id of album in which song is: ")
        while not Check.check_album(album_id):
            string = input("There is no such album\nYou can add it\n(y/n): ")
            for case in Switch(string):
                if case('y'):
                    album = self.album_input()
                    album_id = album.id
                    db.insert_album(album)
                    break
                if case('n'):
                    print("can't insert song")
                    return
                else:
                    print("wrong input, try again!")
        song = Song(s_id, name, language, album_id)
        return song

    def band_update(self):
        b_id = input("enter band's id: ")
        if Check.check_band(b_id):
            name = input("enter band's name: ")
            genre = input("enter band's ganre: ")
            album_number = input("enter number of band's album: ")
            reward_existence = input("enter band's reward existence (True/False): ")
            while reward_existence != "True" and reward_existence != "False":
                reward_existence = input("Wrong input!\nTry again: ")
            reward_existence = bool(reward_existence)
            country = input("enter band's native country: ")
            band = Band(b_id, name, genre, album_number, reward_existence, country)
            return band
        else:
            print("No such band in db")
            return None

    def album_update(self):
        a_id = input("enter album's id: ")
        if Check.check_album(a_id):
            name = input("enter album's name: ")
            presentation_date = self.get_date()
            songs_number = input("enter number of songs in album: ")
            band_id = input("enter id of band which created album: ")
            while not Check.check_band(band_id):
                string = input("There is no such band\nYou can add it\n(y/n): ")
                for case in Switch(string):
                    if case('y'):
                        band = self.band_input()
                        band_id = band.id
                        db.insert_band(band)
                        break
                    if case('n'):
                        print("can't insert album")
                        return
                    else:
                        print("wrong input, try again!")
            album = Album(a_id, name, presentation_date, songs_number, band_id)
            return album
        else:
            print("No such album in db")
            return None

    def song_update(self):
        s_id = input("enter song's id: ")
        if Check.check_song(s_id):
            name = input("enter song's name: ")
            language = input("enter song's language: ")
            album_id = input("enter id of album in which song is: ")
            while not Check.check_album(album_id):
                string = input("There is no such album\nYou can add it\n(y/n): ")
                for case in Switch(string):
                    if case('y'):
                        album = self.album_input()
                        album_id = album.id
                        db.insert_album(album)
                        break
                    if case('n'):
                        print("can't insert song")
                        return
                    else:
                        print("wrong input, try again!")
            song = Song(s_id, name, language, album_id)
            return song
        else:
            print("No such song in db")
            return None

    def get_boolean(self):
        is_active = input("enter if band has music rewards (True/False): ")
        while is_active != "True" and is_active != "False":
            is_active = input("Wrong input!\nTry again: ")

        return is_active

    def get_id(self):
        return input("input id: ")

    def get_date(self):
        date = input("enter timestamp(format: %Y-%m-%d): ")
        while not Check.test_timestamp(date):
            date = input("Wrong input!\nTry again: ")
        return date
