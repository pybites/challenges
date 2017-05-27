=======
PODCAST
=======

This is a script for the PyBites challenge `17 <http://pybit.es/codechallenge17.html>`_!
It is fetching the podcast feeds of `Podcast.__init__ <https://www.podcastinit.com/>`_!

Emails settings
===============
Use the following environment variables to configure the mail service::

    $ export MAIL_ACCOUNT="sender@email.com"
    $ export MAIL_PASSWORD="sender_password"
    $ export MAILTO="recipient@email.com"

Cron Job settings
=================
Place podcast.py into /etc/cron.weekly::

    $ cp podcast.py /etc/cron.weekly

Make it executable::

    $ chmod a+x podcast.py

Dependencies
============
This scripts requires the feedparser module, to install it
- On Fedora::
    
    $ sudo dnf install python3-feedparser

- With pip::

    $ sudo pip install feedparser