from podcast.store import Storage
from podcast.podcast import Podcast


def main():
    podcast = Podcast()
    storage = Storage()
    data = podcast.latest_feed_data()
    print(data)
    storage.add_episode(data)
    podcast.notify(data)
    storage.close()

if __name__ == "__main__":
    main()
