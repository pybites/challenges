#!/usr/bin/env python3.8
""" This is a small app to query the [Wargaming API](https://developers.wargaming.net) in order to collect,
    store, and display their world-wide World of Tanks server populations """

import math
import json
import os
import requests
import time

from collections import defaultdict
from collections import namedtuple
from datetime import datetime
from datetime import timezone
from typing import DefaultDict
from typing import NamedTuple

from config import api_key
from progressbar import progress_bar

# Current (20191213) list of regions and their associated TLDs
regions = [("na", "com"), ("ru", "ru"), ("eu", "eu"), ("asia", "asia")]  # (region, tld)


def request_data() -> DefaultDict:
    """ Request server info from Wargaming API and return Dict containing data from each region """
    data = defaultdict(dict)

    with requests.Session() as s:
        for region, tld in regions:
            r = s.get(
                f"https://api.worldoftanks.{tld}/wgn/servers/info/?application_id={api_key}&language=en"
            )

            if r.status_code == 200:
                api_resp = json.loads(r.text)

                data[region] = api_resp

    return dict(data)


def parse_data(data: dict, game_abbr: str = None) -> DefaultDict:
    """ Parse data returned from request_data() and return regional totals """
    totals = defaultdict(lambda: defaultdict(int))

    for region_name, region_info in data.items():
        for game, game_servers in region_info["data"].items():

            if game_abbr and not game_abbr == game:
                continue

            for server in game_servers:
                # Populate region totals
                totals[region_name]["user_count"] += int(server["players_online"])
                totals[region_name]["server_count"] += 1

    return totals


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def print_header() -> None:
    """ Clear screen and setup header for data """
    clear_screen()
    print(f"Current Playerbase - Bars represent 10,000 concurrent users")
    print(f"{'-' * 70}")
    print()


def print_content(game_info: DefaultDict) -> None:
    """ Walk parsed API response and create "bar chart" type display """
    for region, region_data in game_info.items():
        region_name = region.upper()
        region_count = region_data["user_count"]
        region_bar = "+" * math.ceil(float(region_data["user_count"] / 10000))
        print(f"{region_name:<10}{region_count:>10} | {region_bar}")

    print()


def timer(seconds: int, prefix: str) -> None:
    """ Simplify usage of progress_bar since many of the options are going to be the same throughout """
    remaining = seconds

    while True:
        progress = remaining / seconds * 100

        progress_bar(
            progress=progress,
            length=30,
            complete=0,
            msg_complete="Requesting new data...",
            msg_prefix=prefix
            + f' ({time.strftime("%M:%S", time.gmtime(remaining))} remaining): ',
            suppress_nl=True,
        )
        time.sleep(1)

        remaining -= 1

        if remaining < 0:
            break


def main():
    region_data = []

    while True:
        timestamp = datetime.now(timezone.utc).replace(second=0, microsecond=0)
        region_data = request_data()
        game_info = parse_data(region_data, "wot")

        print_header()
        print_content(game_info)

        try:
            timer(60, "Waiting")

        except KeyboardInterrupt:
            os.sys.exit(0)

        finally:
            print()


if __name__ == "__main__":
    main()
