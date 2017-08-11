# Thumbler
> Proof of concept script that extracts faces as thumbnails from an image.

[![GitHub issues][issues-image]][issues-url]
[![GitHub forks][fork-image]][fork-url]
[![GitHub Stars][stars-image]][stars-url]
[![License][license-image]][license-url]
[![Twitter][twitter-image]][twitter-url]

## Installation
> DISCLAIMER: Now I must admit that I am using [Anaconda](https://www.continuum.io/) so the only hurdle I had with this was installing [OpenCV](https://github.com/opencv/opencv.git). Everything else was already installed. So the following has not been verified to work.

The usual will get you almost there:

```bash
cd [Your Projects Directory]
git clone https://github.com/clamytoe/Thumbler.git
cd Thumbler
python3.6 -m venv venv
source venv/bin/activate
pip install -r requirements
```
### Installing OpenCV
The most difficult thing to install was [OpenCV3](https://github.com/opencv/opencv.git). I've included an additional [document](opencv/OpenCV.md) on what I had to go through to get it working, hopefully it'll be of some use. I've also included a sample script so that you can test your installation. Both can be found in the *opencv* folder.

## Usage Example
The script is really simple to use. Initially I was going to put in the option to just scan a directory full of images and have it extract the faces, but since the HAAR profile that I'm using is only for frontal images, it's really picky. The size of the image seems to play a part on its results as well.

I've included some sample images that worked pretty good and also a few where some faces are not detected, just so that you can get a feel for how it works. I had to tweak the *scaleFactor* settings in some cases in order to NOT detect phantom faces.

```bash
python thumbler.py samples/beach.jpeg
Found 12 faces!
```
> All faces detected
![beach](img/beach.png)

```bash
python thumbler.py samples/mirkin.jpeg
Found 60 faces!
```
> Not all faces detected
![mirkin](img/mirkin.png)

## Saved Thumbnails
By default I'm having the extracted thumbnails saved into the Thumbler directory under **thumbs**. In that directory, a new directory is created for each image, based on the name of the image itself. So for the last two runs, my thumbs folder would look like this:

```bash
thumbs
├── beach
│   ├── face_0.jpg
│   ├── face_10.jpg
│   ├── face_11.jpg
│   ├── face_1.jpg
│   ├── face_2.jpg
│   ├── face_3.jpg
│   ├── face_4.jpg
│   ├── face_5.jpg
│   ├── face_6.jpg
│   ├── face_7.jpg
│   ├── face_8.jpg
│   └── face_9.jpg
└── mirkin
    ├── face_0.jpg
    ├── face_10.jpg
    ├── face_11.jpg
    ├── face_12.jpg
    ├── face_13.jpg
    ├── face_14.jpg
    ├── face_15.jpg
    ├── face_16.jpg
    ├── face_17.jpg
    ├── face_18.jpg
    ├── face_19.jpg
    ...

2 directories, 72 files
```

Here's a sample of the beach thumbnails:

![thumbnails](img/thumbnails.png)

## Credit
Most of the credit for this goes to [Real Python](https://realpython.com) for their [Face Recognition with Python, in under 25 lines of code](https://realpython.com/blog/python/face-recognition-with-python/) blog post!

## Release History
* 0.0.1
    * Proof of concept

## Meta

Martin Uribe – [@mohhinder](https://twitter.com/mohhinder) – clamytoe@gmail.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/clamytoe/Thumbler](https://github.com/clamytoe/Thumbler)

[issues-image]:https://img.shields.io/github/issues/clamytoe/Thumbler.svg
[issues-url]:https://github.com/clamytoe/Thumbler/issues
[fork-image]:https://img.shields.io/github/forks/clamytoe/Thumbler.svg
[fork-url]:https://github.com/clamytoe/Thumbler/network
[stars-image]:https://img.shields.io/github/stars/clamytoe/Thumbler.svg
[stars-url]:https://github.com/clamytoe/Thumbler/stargazers
[license-image]:https://img.shields.io/badge/license-MIT-blue.svg
[license-url]:https://raw.githubusercontent.com/clamytoe/Thumbler/master/LICENSE
[twitter-image]:https://img.shields.io/twitter/url/https/github.com/clamytoe/Thumbler.svg?style=social
[twitter-url]:https://twitter.com/intent/tweet?text=Wow:&url=%5Bobject%20Object%5D
