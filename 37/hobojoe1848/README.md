## XML Steam Scraper

A program to parse the steam XML feed for new titles.

1. Run pull_xml.py to pull down the steam newreleases XML feed.

2. Run xml_steam_scraper.py to parse the feed and save the game names and URLs to an sqlite database. (The db will be created on first run).

3. Populate sms_recipients.py with Twilio format friendly phone numbers (+1234567890).

4. Run send_sms.py to send the numbers in the sms_recipients list a list of newly released games.

5. The program is configured such that once a game has been emailed to you, it won't be emailed again.
