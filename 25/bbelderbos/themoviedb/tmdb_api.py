import time

from .tmdb_init import tmdb
from .decorators import store_results

DEFAULT_LANG = 'en'
DEFAULT_NUM_PAGES = 2
DEFAULT_MIN_VOTE_COUNT = 1


class Tmdb:

    def __init__(self, language=None, num_pages=None, min_vote_count=None):
        self.language = language or DEFAULT_LANG
        self.num_pages = num_pages or DEFAULT_NUM_PAGES
        self.min_vote_count = min_vote_count or DEFAULT_MIN_VOTE_COUNT

    @store_results
    def get_items(self, obj_method):
        results = []

        for i in range(self.num_pages):
            page = i + 1

            num_tries = 0
            resp = None

            while num_tries < 3:
                try:
                    resp = obj_method(language=self.language,
                                      page=page)
                    break
                except:
                    num_tries += 1
                    continue

            if not resp or 'results' not in resp:
                continue

            results += [r for r in resp['results']
                        if r['vote_count'] > self.min_vote_count]

            time.sleep(1)

        return results


class Movies(Tmdb):

    def __init__(self, language=None, num_pages=None):
        super().__init__(language, num_pages)
        self.movies = tmdb.Movies()

    def get_now_playing(self):
        return self.get_items(self.movies.now_playing)

    def get_upcoming(self):
        return self.get_items(self.movies.upcoming)


class Tv(Tmdb):

    def __init__(self, language=None, num_pages=None):
        super().__init__(language, num_pages)
        self.tv = tmdb.TV()

    def get_popular(self):
        return self.get_items(self.tv.popular)

    def get_on_the_air(self):
        return self.get_items(self.tv.on_the_air)


if __name__ == '__main__':
    mo = Movies('en', 3)
    resp = mo.get_now_playing()
    print(len(resp))
