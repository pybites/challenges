from operator import itemgetter
from pathlib import Path
import random
from time import sleep
from zipfile import ZipFile

import feedparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from images import BAMBOO_IMAGES, MATERIAL_IMAGES  # noqa F401

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

    def __init__(self, images=None, title=None, max_num=None, zip_files=False):
        self.driver = webdriver.Chrome()
        self.driver.get(TOOL_URL)

        self.images = images if images else MATERIAL_IMAGES
        self.title = title
        self.max_num = max_num
        self.zip_files = zip_files

        self.posts = self._get_posts()
        self._set_canvas_and_top_offset_title()
        self.files = []

    def _get_posts(self):
        return [entry for entry in
                feedparser.parse(PYBITES_FEED).entries
                if self.title is None
                or self.title.lower() in entry.title.lower()]

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
        print(f'{i} images generated')
        if self.zip_files:
            self._zip_images()
            print(f'Images zipped up, file: {OUTPUT_ZIP}')

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

    def _zip_images(self):
        # wait a bit for the last image to get saved
        sleep(2)
        # get latest files N files (could not change Downloads destination
        # dir as used by website / tool)
        files = sorted(
            [(fi, fi.stat().st_mtime) for fi in DOWNLOAD_FOLDER.glob('*jpg')],
            key=itemgetter(1), reverse=True
        )
        if self.max_num is not None:
            files = files[:self.max_num]

        with ZipFile(OUTPUT_ZIP, 'w') as myzip:
            # arcname writes the file not the whole subdir tree
            for file_ in files:
                fname = file_[0]
                myzip.write(fname, arcname=fname)


if __name__ == '__main__':
    fi = FeaturedImages()
    fi()
