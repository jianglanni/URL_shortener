from database import Database
import random
import string

class Shortener:
    def __init__(self):
        self.db = Database()

    def shorten(self, url):
        generated_url = self.generate_short_url()
        shorten = None
        while shorten is None:
            shorten = self.db.insert(url, generated_url)
            generated_url = self.generate_short_url()
        return shorten

    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(7))
        return random_string

    def get_url(self, short_url):
        return self.db.get_url(short_url)
