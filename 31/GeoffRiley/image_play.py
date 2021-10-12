import argparse
import sys
from colorsys import rgb_to_hsv, hsv_to_rgb
from pathlib import Path
from typing import Union

from PIL import Image, ImageDraw


def process_image(in_file: Path, out_file: Path, *, frame: bool = False, thumb: Union[int, bool] = False):
    im: Image.Image
    im = Image.open(in_file)
    show_details(im)
    if frame:
        im = add_frame(im, get_dominant_colour(im))
    if thumb:
        im.thumbnail((thumb, thumb))
    im.save(out_file)


def get_dominant_colour(im: Image.Image, palette_size: int = 16) -> Union[int, tuple]:
    im_c = im.copy()
    im_p = im_c.convert('P', palette=Image.ADAPTIVE, colors=palette_size)
    palette = im_p.getpalette()
    index_colours = sorted(im_p.getcolors(), reverse=True)
    index = index_colours[0][1]
    return tuple(palette[index * 3:index * 3 + 3])


def show_details(im: Image.Image):
    print(f'Format: {im.format}, size: {im.size}, mode: {im.mode}')
    for v, k in im.info.items():
        print(f'    {v}: {k}')


def add_frame(im: Image.Image, background: tuple = (0, 0, 0)) -> Image.Image:
    foreground = get_complementary_colour(background)
    frame_extend = max(im.size) // 10
    width, height = im.size
    new_width, new_height = width + frame_extend * 2, height + frame_extend * 2
    im_f = Image.new(im.mode, (new_width, new_height), background)
    im_f.paste(im, (frame_extend, frame_extend))
    canvas = ImageDraw.Draw(im_f)
    frame_extend_border = frame_extend // 3
    tl = (frame_extend_border, frame_extend_border)
    br = (new_width - frame_extend_border, new_height - frame_extend_border)
    frame_extend_width = frame_extend // 5
    canvas.rectangle((tl, br), outline=foreground, width=frame_extend_width)
    canvas.rectangle(((0, 0), (frame_extend, frame_extend)), outline=foreground, width=frame_extend_width)
    canvas.rectangle(((new_width - frame_extend, new_height - frame_extend), (new_width, new_height)),
                     outline=foreground, width=frame_extend_width)
    canvas.rectangle(((0, new_height - frame_extend), (frame_extend, new_height)), outline=foreground,
                     width=frame_extend_width)
    canvas.rectangle(((new_width - frame_extend, 0), (new_width, frame_extend)), outline=foreground,
                     width=frame_extend_width)
    return im_f


def get_complementary_colour(colour: tuple) -> tuple:
    r, g, b = map(lambda x: x / 255., colour)
    h, s, v = rgb_to_hsv(r, g, b)
    contrast = map(lambda x: int(round(x * 255)), hsv_to_rgb(h + 0.5, s, v))
    return tuple(contrast)


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('in_file', type=Path, help='Source image file')
    parse.add_argument('out_file', type=Path, help='Destination image file')
    parse.add_argument('--frame', '-f', action='store_true')
    parse.add_argument('--thumb', '-t', default=False, type=int)
    args = parse.parse_args()
    process_image(args.in_file, args.out_file, frame=args.frame, thumb=args.thumb)


if __name__ == '__main__':
    trials = [
        'image_play -t 200 image1.png image1-t200.png',
        'image_play -t 200 image2.jpg image2-t200.png',
        'image_play -f image1.png image1-f.png',
        'image_play -f image2.jpg image2-f.png',
        'image_play -ft 200 image1.png image1-tf200.png',
        'image_play -ft 200 image2.jpg image2-tf200.png',
        'image_play -t 400 image1.png image1-t400.png',
        'image_play -t 400 image2.jpg image2-t400.png',
        'image_play -ft 400 image1.png image1-tf400.png',
        'image_play -ft 400 image2.jpg image2-tf400.png',
    ]
    for trial in trials:
        print(f'*** Run with: {trial}')
        sys.argv = trial.split()
        main()
