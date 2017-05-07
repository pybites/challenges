Podcaster
--
Script to keep track of your favorite podcasts. Simply add the RSS feed into the program and get most of the details that you could ever want about each episode.

## How to use
If you run the script with no command line arguments, you'll get the help message.

![help](img/help.png)


#### feed
The `feed` argument is used to add a new feed into the database.

`feed URL`

![feed](img/feed.png)

`feed https://pythonbytes.fm/episodes/rss`

#### episodes
The `episodes` argument is used to list all of the episodes that are available for the selected podcast.

`episodes PODID`

`episodes PODID EPISODEID DOWNLOAD`

![episodes](img/episodes.png)

![episode-list](img/episodes_list.png)

For example `episodes 1` will list all of the available podcasts. If you desire further detail about the episode you can additionally selected as so:

`episodes 1 --eid 10 `

`episodes 1 -e 10`

![episode-detail](img/episode_detail.png)

With the `episodes` argument you also have the option of downloading the episode by adding the following:

`episodes 1 --eid 10 --download`

`episodes 1 -e 10 -d`

![download](img/download.png)

If you're download is interrupted or you quit it for whatever reason. If you attempt to download the same episode again, it will pick up where it left off.

#### podcasts
The `podcasts` argument, it will list all of the podcasts that you have entered into the database. If none exists it will let you know.

![podcasts](img/podcasts.png)

You can get further detail about the podcast by specifying it by it's Podcast ID.

`podcasts -p 1`

`podcasts --pid 1`

![podcas-detail](img/podcast_detail.png)

#### preload
I've provided some preloaded podcasts for ease of use. You have the option of adding just one of them at a time or selecting them all at once.

`preload --pod1`

`preload --pod2`

`preload --pod3`

`preload --all`

![preload](img/preload.png)

#### random
The use of the `random` argument will randomly select and unplayed episode from all of the available podcasts and download it for you.
 
This option would be perfect for setting the script into your cron and setting it to download a random episode automatically for you.

![random](img/random.png)

### Podcasts Episodes
The episodes are saved to your account's Music folder under the Podcasts directory.

![enjoy](img/enjoy.png)