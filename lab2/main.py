from get_char import Switch
from rockdb import RockDB
from check import Check
from ui import UI
from random_fill import RandomFillDB
from pprint import pprint

db = RockDB()
ui = UI()


def add_entity(name):
    if name == "band":
        band = ui.band_input()
        db.insert_band(band)

    elif name == "album":
        db.insert_album(ui.album_input())

    elif name == "song":
        db.insert_song(ui.song_input())


def update_entity(name):
    if name == "band":
        band_entity = ui.band_update()
        if band_entity is not None:
            db.update_band(band_entity)
            return True

    elif name == "album":
        album_entity = ui.album_update()
        if album_entity is not None:
            db.update_album(album_entity)
            return True

    elif name == "song":
        song_entity = ui.song_update()
        if song_entity is not None:
            db.update_song(song_entity)
            return True
    return False


def delete_entity(name):
    if name == "band":
        band_id = ui.get_id()
        if Check.check_band(band_id):
            db.delete_band(band_id)
        else:
            print("There is no such band in db\n")

    elif name == "album":
        album_id = ui.get_id()
        if Check.check_album(album_id):
            db.delete_album(album_id)
        else:
            print("There is no such album in db\n")

    elif name == "song":
        song_id = ui.get_id()
        if Check.check_song(song_id):
            db.delete_song(song_id)
        else:
            print("There is no such song in db\n")


def fill_rand(name):
    number = input("input number of entities: ")
    random_fill = RandomFillDB()
    if name == "band":
        random_fill.add_bands(int(number))

    elif name == "album":
        random_fill.add_albums(int(number))

    elif name == "song":
        random_fill.add_songs(int(number))


def get_db_name():
    while 1:
        choose = input(
            "Choose number\n\t"
            "1 - band,\n\t"
            "2 - album,\n\t"
            "3 - song,\n\t"
            "r - return\n"
            "Type here and press enter: ")
        for param in Switch(choose):
            if param('1'):
                return "band"
            if param('2'):
                return "album"
            if param('3'):
                return "song"
            if case('r'):
                break
            else:
                print("wrong input, try again\n")


def search(param):
    if param == "by_date":
        date1 = ui.get_date()
        date2 = ui.get_date()
        print(db.search_by_date(date1, date2))

    elif param == "by_boolean":
        reward_existence = ui.get_boolean()
        print(db.search_reward_existence(reward_existence))

    elif param == "by_word_not_belong":
        name = input("enter band name: ")
        print(db.search_by_word_not_belong(name))

    elif param == "by_phrase":
        name = input("enter name of song: ")
        print(db.search_by_phrase(name))


def get_param():
    while 1:
        choose = input("Choose number\n\t"
                       "1 - by_date,\n\t"
                       "2 - by_boolean,\n\t"
                       "3 - by_word_not_belong (in band),\n\t"
                       "4 - by_phrase (song's name)\n\t"
                       "r - return\n"
                       "Type here and press enter: ")
        for param in Switch(choose):
            if param('1'):
                return "by_date"
            if param('2'):
                return "by_boolean"
            if param('3'):
                return "by_word_not_belong"
            if param('4'):
                return "by_phrase"
            if param('r'):
                break
            else:
                print("wrong input, try again!")


while 1:
    switch = input("Choose number: \n\t"
                   "1 - add_entity\n\t"
                   "2 - fill_rand\n\t"
                   "3 - update_entity\n\t"
                   "4 - delete_entity\n\t"
                   "5 - search_in_db\n\t"
                   "6 - show all db\n\t"
                   "e - exit\n"
                   "Type here and press enter: ")
    for case in Switch(switch):
        if case('1'):
            db_name = get_db_name()
            print("Before:\n")
            pprint(db.get_table_string(db_name))
            add_entity(db_name)
            print("After:\n")
            pprint(db.get_table_string(db_name))
            print("======================================")
            break
        if case('2'):
            db_name = get_db_name()
            print("Before:\n")
            pprint(db.get_table_string(db_name))
            fill_rand(db_name)
            print("After:\n")
            pprint(db.get_table_string(db_name))
            print("======================================")
            break
        if case('3'):
            db_name = get_db_name()
            print("Before:\n")
            pprint(db.get_table_string(db_name))
            if update_entity(db_name):
                print("After:\n")
                pprint(db.get_table_string(db_name))
            print("======================================")
            break
        if case('4'):
            db_name = get_db_name()
            print("Before:\n")
            pprint(db.get_table_string(db_name))
            delete_entity(db_name)
            print("After:\n")
            pprint(db.get_table_string(db_name))
            print("======================================")
            break
        if case('5'):
            criteria = get_param()
            search(criteria)
            print("======================================")
            break
        if case('6'):
            print("Bands:\n")
            pprint(db.get_table_string("band"))
            print("Albums:\n")
            pprint(db.get_table_string("album"))
            print("Songs:\n")
            pprint(db.get_table_string("song"))
            print("======================================")
        if case('e'):
            break
        else:
            print("======================================")
            print("wrong input, try again!")

    if switch == 'e':
        break
