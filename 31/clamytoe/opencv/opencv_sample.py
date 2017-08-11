from time import time
from numpy import uint8
from numpy.random import rand

import cv2


def fpsopencv(dat, Nf):
    tic = time()
    for i in dat:
        cv2.imshow('test', i)
        cv2.waitKey(1)  # integer milliseconds, 0 makes it wait forever
    cv2.destroyAllWindows()
    return Nf / (time() - tic)


def main():
    xy=(512, 512)
    Nf = 500
    imgs = (rand(Nf, xy[0], xy[1]) * 255).astype(uint8)
    fps = fpsopencv(imgs, Nf)

    print(f'{fps} fps')


if __name__ == '__main__':
    main()
