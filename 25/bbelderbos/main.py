from themoviedb import Movies, Tv

mo = Movies()
mo.get_now_playing()
mo.get_upcoming()
tv = Tv()
tv.get_on_the_air()
tv.get_popular()
