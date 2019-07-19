import matplotlib.pyplot as plt
import numpy as np
from .scrapper import *


def main():
    scrapper = Scrapper()
    data = scrapper.do_classify_in_threads()

    v = [2013, 2019, 0, 10]
    plt.axis(v)
    for year in data:
        height = np.array(data[year]).sum()
        plt.bar(int(year), height=height)


if __name__ == '__main__':
    main()