from rockdb import RockDB
from randomizator import Random as r
from structures import Band
from structures import Album
from structures import Song

random_bands = [
        "AC/DC", "Accept", "Aerosmith", "Alice Cooper", "Avantasia",
        "Avenged Sevenfold", "Black Sabbath", "Boston", "Children of Bodom",
        "Deep Purple", "Disturbed", "Dropkick Murphys", "Eagles", "Europe",
        "Genesis", "Iron Maiden", "Led Zeppelin", "Linkin Park", "Lordi",
        "Manowar", "Metallica", "Motörhead", "Nickelback", "Nightmare",
        "Nightwish", "Queen", "Rammstein", "Powerwolf", "Sabaton", "Slipknot",
        "The Beatles", "The Cranberries", "ZZ Top"
]
random_countries = [
    "USA", "Great Britain", "Germany", "Australia", "Sweden"
]
random_language = [
    "English", "German", "Swedish"
]


class RandomFillDB:
    db = RockDB()

    def add_bands(self, n):
        for x in range(0, n):
            self.add_band()

    def add_band(self):
        self.db.insert_band(
            Band(
                str(r.generate_random_int(0, 9999)),
                random_bands[r.generate_random_int(0, len(random_bands) - 1)],
                r.generate_random_string(2, 10),
                str(r.generate_random_int(0, 50)),
                bool(r.generate_random_bool()),
                random_countries[r.generate_random_int(0, len(random_countries) - 1)]
            )
        )

    def add_albums(self, n):
        for x in range(0, n):
            self.add_album()

    def add_album(self):
        self.db.insert_album(
            Album(
                str(r.generate_random_int(0, 9999)),
                r.generate_random_string(2, 8),
                str(r.generate_random_date()),
                str(r.generate_random_int(0, 20)),
                str(r.generate_random_int(0, 9999))
                )
            )

    def add_songs(self, n):
        for x in range(0, n):
            self.add_song()

    def add_song(self):
        self.db.insert_song(
            Song(
                str(r.generate_random_int(0, 9999)),
                r.generate_random_string(3, 25),
                random_language[r.generate_random_int(0, len(random_language) - 1)],
                str(r.generate_random_int(0, 9999))
            )
        )
