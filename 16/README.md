## Code Challenge 16 - Query Your Favorite API

Instructions [here](http://pybit.es/codechallenge16.html).

Previous challenges and About [here](http://pybit.es/pages/challenges.html).


**Solution**

Tweaked around with Wordlink API in order to get a random word
per day. This would help in learning a new word each day. Which makes
it 30-31 words per month. 

Making a GET request call at the end point /wordOfTheDay returns a
json that has key's which give details related to the random word of
the day that gets fetched.

End User sees the output having only selective key value pairs.
Which include Word of the day, date, origin, definition, usage
etc. 


```
{
    "wordOfTheDay": "ignoration",
    "origin": "The word 'ignoration' comes from a Latin word meaning \"to not know, be ignorant of, misunderstand\".",
    "date": "2017-12-19T03:00:00.000+0000",
    "usage": "If only to illustrate that I am useful for more than lounge-lizard renditions of Mahler's 2nd, I will concur with Matthew that ignoration is in the OED and has a use fitting for most things that pass for political dialog these days: Ignoration of the Elench -- and anglicized version of ignoratio elenchi, which is the logical fallacy of refuting an argument that was not made or is irrelevant to its professed purpose.",
    "meaning": "The state of being ignorant",
    "part_of_speech": "noun",
    "source": "wiktionary"
}

```

Last leap left to actually make it worth the use. 

Get a word into your mail box Daily!!
Write a bash script eg: `do-it-all.sh` to set the following enviornment variables to configure mail service.

```
export api_key = api key which you get by sign up on wordlink
export MAIL_ACCOUNT= your mail address
export MAIL_PASSWORD= mail password
export MAILTO= recipient's mail address

``` 

Do `which Python`  on your shell it'll show the path to the folder which has Python executable installed.

Eg:

`/home/mridu/challenges/16/venv/bin/python`

Add the path to run the python file in your bash script `do-it-all.sh`.

```
/home/mridu/challenges/16/venv/bin/python /home/mridu/challenges/16/build_vocabulary.py

```

```
NOTE:

You'll have to make the bashscript executable. By changing permissions.

```

Schedule this script to run as a cron job. In order to retrieve one word per day.

On shell do `crontab -e`. Add time on which you wish to schedule the task. And give full path to file.

```
00 04 * * * challenges/16/do-it-all.sh

```

Yay! Everyday at 4:00 am you'll have a email notification containing Word Of The Day.
