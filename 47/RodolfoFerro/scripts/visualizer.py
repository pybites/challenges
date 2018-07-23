# ===============================================================
# Author: Rodolfo Ferro Pérez
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# Script: Tweets visualizer script.
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro. Any
# explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ===============================================================

from extractor import TweetsExtractor
from analyzer import TweetsAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import pandas as pd
import numpy as np


class TweetsVisualizer():

    def __init__(self, analyzer):
        """
        Constructor function using a TweetsExtractor
        object.
        """

        # Construct object:
        self.analyzer = analyzer
        self.data = self.analyzer.data
        self.hashtags = self.analyzer.hashtags

        return

    def retweets(self):
        """
        Function to plot time series of retweets.
        """

        # We create time series for data:
        data = self.data
        tret = pd.Series(data=data['RTs'].values, index=data['Date'])

        # Lenghts along time:
        plt.title("Retweets along time")
        tret.plot(figsize=(16, 4), label="Retweets", color='g', legend=True)

        return

    def likes(self):
        """
        Function to plot time series of likes.
        """

        # We create time series for data:
        data = self.data
        tfav = pd.Series(data=data['Likes'].values, index=data['Date'])

        # Lenghts along time:
        plt.title("Likes along time")
        tfav.plot(figsize=(16, 4), label="Likes", color='b', legend=True)

        return

    def lengths(self):
        """
        Function to plot time series of lengths.
        """

        # We create time series for data:
        data = self.data
        tlen = pd.Series(data=data['len'].values, index=data['Date'])

        # Lenghts along time:
        plt.title("Lenghts along time")
        tlen.plot(figsize=(16, 4), label="Leghts", color='r', legend=True)

        return

    def create_mask(self, img_path, threshold=200):
        """
        Function to create a mask for word cloud.
        """
        def binarize_array(numpy_array, threshold=threshold):
            """Binarize a numpy array."""

            for i in range(len(numpy_array)):
                for j in range(len(numpy_array[0])):
                    if numpy_array[i][j] > threshold:
                        numpy_array[i][j] = 255
                    else:
                        numpy_array[i][j] = 0
            return numpy_array

        def binarize_image(img_path, threshold=threshold):
            """Binarize an image."""

            image_file = Image.open(img_path)
            image = image_file.convert('L')
            image = np.array(image)
            image = binarize_array(image, threshold)

            return image

        return binarize_image(img_path, threshold=threshold)

    def wordcloud(self, mask=None):
        """
        Function to plot the wordloud with hashtags.
        """

        # Create text from hashtags:
        text = ' '.join(list(self.hashtags.keys()))

        # Create wordcloud:
        wordcloud = WordCloud(mask=mask, background_color="white",
                              scale=3, colormap="viridis")
        wordcloud.generate(text)

        # Plot figure:
        plt.figure(figsize=(10, 10))
        plt.imshow(wordcloud, interpolation="bicubic")
        plt.margins(x=0, y=0)
        plt.axis("off")


if __name__ == '__main__':
    extractor = TweetsExtractor()
    analyzer = TweetsAnalyzer(extractor)
    analyzer.analyze("FerroRodolfo")
    visualizer = TweetsVisualizer(analyzer)
    visualizer.likes()
    visualizer.retweets()
    mask = visualizer.create_mask("../imgs/twird.jpg")
    visualizer.wordcloud(mask)
    plt.savefig("../imgs/wordcloud.png")
