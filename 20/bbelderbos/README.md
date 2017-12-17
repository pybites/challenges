## PyBites Code Challenge 20

Resouce class and Book/Video classes that inherit from it. Goal is to send a daily SMS (Twilio API) with pages (Book) or minutes (Video) to consume.

## Usage 

	$ python plan.py  --help
	Usage: plan.py [OPTIONS]

	Options:
	--resource TEXT       resource type (book, video)
	--title TEXT          title of resource
	--total_units TEXT    total units resource (book = pages, video = min)
	--units_per_day TEXT  total units (book = pages, video = min) per day
	--start_in_days TEXT  number of days from now we kick this off (optional)
	--to_phones TEXT      list of phone numbers to notify
	--help                Show this message and exit.

## Dependencies

* twilio
* schedule
* click
