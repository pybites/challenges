# 16 - Query API

> A CLI application that will return the current temperature and conditions for a user entered city.

## Quickstart

```sh
$ python cli.py --city amsterdam --country-code nl
>>>
        [*] Amsterdam, NL [*]

        __WEATHER REPORT__

        Temp: 10.9°C
        Conditions: Broken Clouds
        Last Updated: Mon Oct 07 22:24:47 2019 Local Time
>>>
```

## Usage

The application is called via `cli.py`. It accepts the following flags:

**City**:

- `--city`, or
- `-c`

**Country Code**:

- `--country-code`, or
- `-cc`

For major cities such as London, the `--country-code` flag can be omitted as it will default to the largest city of that name. To get the weather in London, Ontario the country code flag must be called.

```python
python cli.py -c london # London, GB
python cli.py -c london -cc ca # London, CA
```

**Multi-word and Hypehens**:

Hyphenated towns work as expected, for example

`python cli.py -c wilkes-barre`

Multi-word cities such as New York and Alice Springs will not be parsed correctly on the commandline without the use of an underscore. This is a restriction of `argparse`, not of the API which does accept whitespace between words.

To get the weather in New York, use an underscore:

`python cli.py -c new_york`

## Setup

See `requirements.txt` to get started.

A valid API key from [openweather][1] is required to make any calls to the endpoint.

The API key must be entered into `api_secrets.py` for the script to run.

## Behind the scenes

This application uses `requests-cache` to prevent rate limiting, or depleting the API calls in the free tier. A successful request will be written to an ephemeral sqlite database that will expire after 600 seconds.

[1]: https://home.openweathermap.org/
