import argparse
from operator import itemgetter
from pathlib import Path
import random
import sys
from time import sleep
from zipfile import ZipFile

import feedparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from images import BAMBOO_IMAGES, MATERIAL_IMAGES

PYBITES_FEED = 'https://pybit.es/feeds/all.rss.xml'
TOOL_URL = 'http://projects.bobbelderbos.com/featured_image/'
CANVAS_WIDTH, CANVAS_HEIGHT = 400, 200
TOP_OFFSET = '40px'
OUTPUT_ZIP = 'featured_images.zip'
DOWNLOAD_FOLDER = Path.home() / 'Downloads'

(width_id, height_id, setdimensions_id, title_id, topoffset_id,
 image_id, save_id) = ('width', 'height', 'submitDimensions',
                       'title', 'topoffset', 'bg1_url', 'btnSave')


class FeaturedImages:

    def __init__(self, title=None, feed=None,
                 images=None, max_num=None, zip_files=False):
        self.title = title
        self.feed = feed if feed else PYBITES_FEED
        self.posts = self._get_posts()

        self.images = images if images else MATERIAL_IMAGES
        self.max_num = max_num
        self.zip_files = zip_files

        self.driver = webdriver.Chrome()
        self.driver.get(TOOL_URL)

        self._set_canvas_and_top_offset_title()
        self.image_counter = 0

    def _get_posts(self):
        ret = [entry for entry in
               feedparser.parse(self.feed).entries
               if self.title is None
               or self.title.lower() in entry.title.lower()]
        if not ret:
            print('No matching posts found')
            sys.exit(1)
        return ret

    def _set_canvas_and_top_offset_title(self):
        # need to clear the field first
        self.driver.find_element_by_name(width_id).clear()
        self.driver.find_element_by_name(width_id).send_keys(CANVAS_WIDTH)
        self.driver.find_element_by_name(height_id).clear()
        self.driver.find_element_by_name(height_id).send_keys(CANVAS_HEIGHT)
        self.driver.find_element_by_name(setdimensions_id).click()
        self.driver.switch_to.alert.accept()
        # top offset title (I like Ubuntu font = default, no change needed)
        self.driver.find_element_by_xpath(
            f"//select[@name='{topoffset_id}']/option[text()='{TOP_OFFSET}']"
        ).click()

    def __call__(self):
        for i, entry in enumerate(self.posts, 1):
            self._create_image(entry.title)
            if self.max_num is not None and self.max_num == i:
                break
        print(f'{self.image_counter} images generated')

        # wait a bit for the last image to get saved
        sleep(2)

        if self.zip_files:
            self._zip_images()
            print(f'Images zipped up, file: {OUTPUT_ZIP}')

        self.driver.quit()

    def _create_image(self, title):
        background = random.choice(self.images)

        # selenium, you go too fast!
        sleep(2)

        # set title
        self.driver.find_element_by_name(title_id).clear()
        self.driver.find_element_by_name(title_id).send_keys(title)
        self.driver.find_element_by_name(title_id).send_keys(Keys.TAB)

        # random bg image
        self.driver.find_element_by_name(image_id).clear()
        self.driver.find_element_by_name(image_id).send_keys(background)
        self.driver.find_element_by_name(image_id).send_keys(Keys.TAB)
        sleep(2)

        # save image
        self.driver.find_element_by_id(save_id).click()
        self.image_counter += 1

    def _zip_images(self):
        # as downloaded via browser/selenium cannot control download
        # destination folder, grab the last N files based on the amount of
        # files we generated
        files = sorted(
            [(fi, fi.stat().st_mtime) for fi in DOWNLOAD_FOLDER.glob('*jpg')],
            key=itemgetter(1), reverse=True
        )[:self.image_counter]

        with ZipFile(OUTPUT_ZIP, 'w') as myzip:
            # arcname writes the file not the whole subdir tree
            for file_ in files:
                fname = file_[0]
                myzip.write(fname, arcname=fname)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Create a blog featured image'
    )
    parser.add_argument(
        "-t", "--title",
        help='create images for PyBites feed entries that match this title'
    )
    parser.add_argument(
        "-b", "--bamboo", action="store_true",
        help='use bamboo theme instead of material theme for background image'
    )
    parser.add_argument(
        "-f", "--feed",
        help=f'specify an RSS feed (default = PyBites)'
    )
    parser.add_argument(
        "-n", "--max_num", type=int,
        help='max number of images to be created'
    )
    parser.add_argument(
        "-z", "--zip_files", action="store_true",
        help=f'zip created files up in local directory, filename: {OUTPUT_ZIP}'
    )
    args = parser.parse_args()

    images = BAMBOO_IMAGES if args.bamboo is True else MATERIAL_IMAGES

    fi = FeaturedImages(title=args.title,
                        feed=args.feed,
                        images=images,
                        max_num=args.max_num,
                        zip_files=args.zip_files)
    fi()
