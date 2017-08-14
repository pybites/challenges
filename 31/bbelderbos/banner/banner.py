from collections import namedtuple
import os
import sys

from PIL import Image, ImageDraw, ImageFont

ASSET_DIR = 'assets'
DEFAULT_WIDTH = 600
DEFAULT_HEIGHT = 150
DEFAULT_CANVAS_SIZE = (DEFAULT_WIDTH, DEFAULT_HEIGHT)
DEFAULT_OUTPUT_FILE = 'out.png'
RESIZE_PERCENTAGE = 0.8
DEFAULT_TOP_MARGIN = int(((1 - 0.8) * DEFAULT_HEIGHT) / 2)
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
WHITE_TRANSPARENT_OVERLAY = (255, 255, 255, 178)
TEXT_SIZE = 24
TEXT_FONT_TYPE = os.path.join(ASSET_DIR, 'Ubuntu-R.ttf')
TEXT_PADDING_HOR, TEXT_PADDING_VERT = 10, 40

Font = namedtuple('Font', 'ttf text color size offset')
ImageDetails = namedtuple('Image', 'left top size')


class Banner:
    def __init__(self, size=DEFAULT_CANVAS_SIZE,
                 bgcolor=WHITE, output_file=DEFAULT_OUTPUT_FILE):
        '''Creating a new canvas'''
        self.size = size
        self.width = size[0]
        self.height = size[1]
        self.bgcolor = bgcolor
        self.output_file = output_file
        self.image = Image.new('RGBA', self.size, self.bgcolor)
        self.image_coords = []

    def _image_gt_canvas_size(self, img):
        return img.size[0] > self.image.size[0] or \
               img.size[1] > self.image.size[1]

    def add_image(self, image, resize=False,
                  top=DEFAULT_TOP_MARGIN, left=0, right=False):
        '''Adds (pastes) image on canvas
           If right is given calculate left, else take left
           Returns added img size'''
        img = Image.open(image)

        if resize or self._image_gt_canvas_size(img):
            size = self.height * RESIZE_PERCENTAGE
            img.thumbnail((size, size), Image.ANTIALIAS)

        if right:
            left = self.image.size[0] - img.size[0]

        offset = (left, top)
        self.image.paste(img.convert('RGBA'), offset, mask=img.convert('RGBA'))

        img_details = ImageDetails(left=left, top=top, size=img.size)
        self.image_coords.append(img_details)

    def add_text(self, font):
        '''Adds text on a given image object'''
        draw = ImageDraw.Draw(self.image)
        pillow_font = ImageFont.truetype(font.ttf, font.size)

        if font.offset:
            offset = font.offset
        else:
            # if no offset given put text alongside first image
            left_image_px = min(img.left + img.size[0]
                                for img in self.image_coords)
            offset = (left_image_px + TEXT_PADDING_HOR,
                      TEXT_PADDING_VERT)

        draw.text(offset, font.text, font.color, font=pillow_font)

    def add_background(self, image, resize=False):
        img = Image.open(image).convert('RGBA')

        overlay = Image.new('RGBA', img.size, WHITE_TRANSPARENT_OVERLAY)
        bg_img = Image.alpha_composite(img, overlay)

        if resize:
            bg_size = (self.width * RESIZE_PERCENTAGE, self.height)
            bg_img.thumbnail(bg_size, Image.ANTIALIAS)
            left = self.width - bg_img.size[0]
            self.image.paste(bg_img, (left, 0))
        else:
            self.image.paste(bg_img.resize(DEFAULT_CANVAS_SIZE,
                                           Image.ANTIALIAS), (0, 0))

    def save_image(self):
        self.image.save(self.output_file)


def generate_banner(args):
    image1 = args[0]
    image2 = args[1]
    text = args[2]
    bg = bool(args[3]) if len(args) == 4 else False

    banner = Banner()

    if bg:
        banner.add_background(image2)
    else:
        banner.add_image(image2, resize=True, right=True)

    banner.add_image(image1)

    font = Font(ttf=TEXT_FONT_TYPE,
                text=text,
                color=BLACK,
                size=TEXT_SIZE,
                offset=None)

    banner.add_text(font)

    banner.save_image()


if __name__ == '__main__':
    script = sys.argv.pop(0)
    args = sys.argv

    if len(args) not in [3, 4]:
        print('Usage: {} img1 img2 text (opt bool: 2nd img is bg)'.format(script))  # noqa E501
        sys.exit(1)

    generate_banner(args)
