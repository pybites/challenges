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
Before running the script use the following enviornment variables to configure mail service.

```
export MAIL_ACCOUNT= your mail address
export MAIL_PASSWORD= mail password
export MAILTO= recipient's mail address

``` 


TODO

1) Schedule this script to run as a cron job. In order to retrieve one word per day.

