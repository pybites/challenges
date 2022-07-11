import hashlib
import json
import math
import os
from datetime import datetime
from pathlib import Path
from time import sleep
from typing import Any, Tuple, Union
from sys import setrecursionlimit

import requests
from urllib3.exceptions import (  # type: ignore
    MaxRetryError,
    NewConnectionError,
)

public_key: str = os.environ.get("PUBLIC_KEY", "None")
private_key: str = os.environ.get("PRIVATE_KEY", "None")

output_dir: Union[Path, Any] = Path("data")
Path.mkdir(output_dir, exist_ok=True)

endpoints: Tuple[str, str, str, str, str, str] = (
    "characters",
    "comics",
    "creators",
    "events",
    "series",
    "stories",
)
attribution_text: str = ""
recursion_limit = 1000


def get_data(
    endpoint: str, offset: int = 0, page: int = 0, total_pages: int = 1
) -> None:
    global attribution_text, recursion_limit
    if None in (public_key, private_key):
        print("Please configure a Public and Private keys before continuing!")
        exit()

    ts = f"{str(datetime.timestamp(datetime.now())).replace('.', '')}"
    hash_ = hashlib.md5(f"{ts}{private_key}{public_key}".encode("utf-8")).hexdigest()
    site = "https://gateway.marvel.com/v1/public/"
    url = f"{site}{endpoint}?limit=100&offset={offset}&ts={ts}&apikey={public_key}&hash={hash_}"
    output_file = output_dir / f"{endpoint}_{page}.json"

    if output_file.exists():
        offset += 100
        page += 1
        try:
            get_data(endpoint=endpoint, offset=offset, page=page)
        except RecursionError:
            if total_pages > recursion_limit:
                recursion_limit = total_pages
                setrecursionlimit(total_pages)
            if page < total_pages:
                get_data(
                    endpoint=endpoint,
                    offset=offset,
                    page=page,
                )
    else:
        try:
            resp = requests.get(url)
            if resp.ok and resp.json()["status"] == "Ok":
                if attribution_text == "":
                    attribution_text = resp.json()["attributionText"]
                    print(attribution_text)
                data = resp.json()["data"]
                total = data["total"]
                if total_pages == 1:
                    total_pages = math.floor(total / 100)
                if len(data["results"]) > 0:
                    print(
                        f"Saving {endpoint} page {page} of {total_pages} as {output_file}..."
                    )
                    with open(output_file, "w") as file:
                        json.dump(data["results"], file)
                if page < total_pages:
                    page += 1
                    offset += 100
                    sleep(30)
                    get_data(
                        endpoint=endpoint,
                        offset=offset,
                        page=page,
                        total_pages=total_pages,
                    )
                else:
                    char = "#"
                    msg = f"{char} Completed retrieving all {endpoint} {char}"
                    msg_width = len(msg)
                    border = char * msg_width
                    print(f"{border}\n{msg}\n{border}")
            else:
                print(resp.status_code)
                print(resp.json())
                resp.raise_for_status()
        # except RecursionError:
        #     if total_pages > recursion_limit:
        #         recursion_limit = total_pages
        #         setrecursionlimit(total_pages)
        #     if page < total_pages:
        #         get_data(
        #             endpoint=endpoint,
        #             offset=offset,
        #             page=page,
        #             total_pages=total_pages,
        #         )
        except (
            requests.exceptions.ConnectionError,
            NewConnectionError,
            MaxRetryError,
            TimeoutError,
        ) as e:
            print(f"Connection lost: {e}")
            exit()


if __name__ == "__main__":
    for category in endpoints:
        get_data(category)
