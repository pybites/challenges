#!/usr/bin/env python3
"""
comic_snagger

Scrapes https://www.readcomics.io for comic book images
"""
import os
import shutil
import textwrap
from collections import namedtuple
from types import ModuleType
from typing import List, NamedTuple, Tuple

import requests
from bs4 import BeautifulSoup  # type: ignore
from requests.exceptions import ConnectionError

from .headers import FIREFOX_LINUX
from .log_init import setup_logging

logger: ModuleType = setup_logging()

Comic: NamedTuple = namedtuple("Comic", "title url")
LOCAL_DIR: str = "/home/mohh/Downloads/Comics/"
URL: str = "https://www.readcomics.io"
SEARCH_URL: str = f"{URL}/comic-search?key="
WIDTH: int = 70

try:
    TERM_COL: int = os.get_terminal_size()[0] - 2
    WIDTH = TERM_COL if TERM_COL < 119 else 118
except OSError:
    pass


def clear_screen() -> None:
    """
    Clears the screen
    :return: None
    """
    _: int = os.system("cls" if os.name == "nt" else "clear")  # nosec


def compress_comic(title_dir: str) -> None:
    """
    Takes the given directory and compresses it into the comic book format.

    :param title_dir: string - path to directory
    :return: None
    """
    clear_screen()
    if os.path.isdir(title_dir):
        print(f"Creating comic book file: {title_dir.split('/')[-1]}.cbz")
        shutil.make_archive(title_dir, "zip", title_dir)
        os.rename(f"{title_dir}.zip", f"{title_dir}.cbz")
        shutil.rmtree(title_dir)
    else:
        print(f"\nInvalid directory path was given:\n\t {title_dir}")
        exit(2)


def create_dir(directory: str) -> None:
    """
    Creates a directory path if it does not exists.

    :param directory: str - full path to the directory to create
    :return: None
    """
    try:
        os.makedirs(directory)
    except FileExistsError:
        pass


def display_comics(issues: List[Comic]) -> None:
    """
    Displays the comic book issues that were found.

    :param issues: list - Comic(title, url) namedtuples
    :return: None
    """
    while True:
        choice: str = get_comic_choice(issues)
        if not choice:
            for chapter in issues:
                download_comic(chapter.title, chapter.url)
            break
        else:
            try:
                picked: int = int(choice)
                download_comic(issues[picked].title, issues[picked].url)
                break
            except (ValueError, IndexError):
                clear_screen()
                print(f"\n** {choice} is not a valid entry! **\n")


def display_genres(soup: BeautifulSoup) -> None:
    """
    Displays the genres tags for the comic series.

    :param soup: BeautifulSoup - soup object for the page.
    :return: None
    """
    genres_ul = soup.find(class_="anime-genres")
    genres: List[str] = [f"[{g.text}]" for g in genres_ul.find_all("a")]
    print(f"{' '.join(genres)}\n")


def display_series_choices(search_term: str, series: List[Comic]) -> Comic:
    """
    Displays the comic book titles that were found for the series.

    If no match is found, the user is informed. Otherwise the comics found are
    listed with an index number to the left. It will then ask the user for
    their choice and the user is to enter the index number of the comic that
    they want to retrieve.

    :param search_term: str - title of comic entered by user
    :param series: list - containing Comic namedtuples
    :return: namedtuple - Comic(title, url)
    """
    if not series:
        print(f"Was not able to find any titles for: {search_term}")
        exit()

    while True:
        print(f"Found {len(series)} titles matching {search_term.title()}")
        for i, comic in enumerate(series):
            print(f" [{i}] {comic.title}")
        try:
            choice: int = int(input(f"\nWhich one would you like to get? "))  # nosec
            return series[choice]
        except (ValueError, IndexError):
            clear_screen()
            print(f"\n** {choice} is not a valid entry! **\n")


def download_comic(title: str, url: str) -> None:
    """
    Downloads the images for the comic.

    If the comic book file does not already exist, it will create the directory
    for the title and download all of the images for it into it. Once complete,
    it compresses the directory into the .CBZ format and removes the directory.

    :param title: str - title of the comic
    :param url: str - the url for the comic
    :return: None
    """
    title_dir: str = os.path.join(LOCAL_DIR, title)
    if not os.path.isfile(f"{title_dir}.cbz"):
        create_dir(title_dir)

        links = get_links(get_soup(url + "/full"))
        for link in links:
            cmd: str = generate_command(link, title_dir)
            os.system(cmd)  # nosec
        compress_comic(title_dir)
    else:
        print(f"{title_dir.split('/')[-1]}.cbz already exists, skipping.")


def generate_command(link: str, directory: str) -> str:
    """
    Generates the wget command to retrieve the image.

    It takes the url link and extracts the image file name. They are just
    numbered, so any number under 10 gets padded with a leading 0 in order to
    ensure that when the files are combined into the comic book format, they
    stay in the correct order.

    :param link: str - link to the image file
    :param directory: the full path to save the image to
    :return: str - the wget command to retrieve the image
    """
    num, ext = link.rsplit("/", 1)[1].split(".")
    image: str = (
        f"{num.zfill(2)}.{ext}" if int(num) < 10 and len(num) == 1 else f"{num}.{ext}"
    )
    img: str = os.path.join(directory, image)
    return f'wget --no-verbose --show-progress -c {link} -O "{img}"'


def scrape_chosen_comic(soup: BeautifulSoup) -> BeautifulSoup:
    """
    Scrapes the site for the given comic.

    :param soup: BeautifulSoup - soup object for the page.
    :return: BeautifulSoup - soup object with chapter information
    """
    display_genres(soup)

    desc_div: BeautifulSoup = soup.find(class_="detail-desc-content")
    desc: str = desc_div.find("p").text.strip()
    print_description(desc)

    chapters_soup: BeautifulSoup = soup.find_all(class_="ch-name")
    return chapters_soup


def get_comic_choice(issues: List[Comic]) -> str:
    """
    Gets the comic choice from the user.

    It displays the comics that were found and asked the user to select one.

    :param issues: list - containing Comic namedtuples
    :return: str - input from the user
    """
    count: int = len(issues)
    descriptive, plurality = ("is", "") if count == 1 else ("are", "s")

    print(f"\nThere {descriptive} {count} comic{plurality} available:")
    for i, chapter in enumerate(issues):
        print(f" [{i}] {chapter.title}")
    return input("\nWhich one would you like? [ENTER] for all ")  # nosec


def get_links(soup: BeautifulSoup) -> List[str]:
    """
    Parses the image links from the page.

    :param soup: BeautifulSoup - soup object for the comic
    :return: list - containing the urls for the full images
    """
    images: BeautifulSoup = soup.find_all(class_="chapter_img")
    return [link["src"] for link in images]


def get_soup(url: str) -> BeautifulSoup:
    """
    Default soupifying code.

    :param url: str - url of the page to soupify
    :return: BeautifulSoup - soup object of the page
    """
    page: BeautifulSoup = requests.get(url, headers=FIREFOX_LINUX)
    if page.ok:
        soup = BeautifulSoup(page.content, "html.parser")
        return soup

    print("Something's gone wrong, sorry...")
    exit(1)


def get_title_soup() -> Tuple[str, List[Comic]]:
    """
    Searches the site for the title entered.

    Returns a list of comics for the search.

    :return: tuple - search term and a list of Comic namedtuples
    """
    clear_screen()
    search_term: str = input("Comic name: ")  # nosec
    url: str = SEARCH_URL + search_term.replace(" ", "+")
    clear_screen()
    print(f"Searching for: {search_term.title()}...")
    return search_term, search_for_series(get_soup(url))


def main() -> None:
    """
    Main entry point into the program.

    :return: None
    """
    try:
        search_term, series = get_title_soup()
        chosen: Comic = display_series_choices(search_term, series)

        clear_screen()
        print(f"Retrieving: {chosen.title}")
        issues: BeautifulSoup = scrape_chosen_comic(get_soup(chosen.url))
        chapters: List[Comic] = scrape_comics_found(issues)
        display_comics(chapters)
    except KeyboardInterrupt:
        print("\n\nProgram aborted by user. Exiting...\n")
        exit()
    except (ConnectionError, TimeoutError):
        print("\nThe connection timed out...\n")
        exit()


def print_description(desc: str) -> None:
    """
    Displays the description of the comic.

    :param desc: str - description of the comic book
    :return: None
    """
    for line in desc.split("\n"):
        blurb: str = textwrap.fill(
            line, initial_indent="  ", subsequent_indent=" ", width=WIDTH
        )
        print(f"{blurb}")


def scrape_comics_found(issues_soup: BeautifulSoup) -> List[Comic]:
    """
    Generates a list of Comic namedtuples.

    :param issues_soup: BeautifulSoup - scraped chapter info
    :return: list - containing Comic namedtuples
    """
    issues: List[Comic] = []
    for link in issues_soup:
        title = link.text
        url = link["href"]
        issues.append(Comic(title, url))

    return issues


def search_for_series(soup: BeautifulSoup) -> List[Comic]:
    """
    Scrapes for the soup object.

    :param soup: BeautifulSoup - soupified search page
    :return: list - Comic(title, url) namedtuples
    """
    comics: List[Comic] = []
    try:
        series: BeautifulSoup = soup.find_all(class_="egb-serie")
        for link in series:
            title: str = link.text
            url: str = link["href"]
            comics.append(Comic(title, url))
        return comics
    except requests.exceptions.ConnectionError:
        print("You must have an active Internet connection to use...")
        exit(1)


if __name__ == "__main__":
    main()
