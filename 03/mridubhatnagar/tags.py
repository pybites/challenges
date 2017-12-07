from difflib import SequenceMatcher
import plotly.plotly as py
import plotly.graph_objs as go

import feedparser
import operator
import itertools

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87


def get_tags():
    """Find all tags in live feed.
    Replace dash with whitespace."""
    tags=[]
    blog_feed = feedparser.parse('https://pybit.es/feeds/all.rss.xml')
    for item in range(len(blog_feed.entries)):
        for i in range(len(blog_feed.entries[item].tags)):
            word=blog_feed.entries[item].tags[i]['term']
            tags.append(word)
    return tags
    

def get_top_tags(tags):
    """
    Get the TOP_NUMBER of most common tags.
    tags: List of all the tags used by the website.
    """
    tag_list=[]
    D={}
    top_tags={}
    for words in tags:
        tag_list.append(words.lower())
        key = words.lower()
        D[key] = tag_list.count(key)
    top_tags=sorted(D.items(),key=operator.itemgetter(1), reverse=True)[:TOP_NUMBER]
    return top_tags


def get_similarities(tags):
    """
    Find set of tags pairs with similarity ratio of > SIMILAR.
    Argument:
    tags: List of all the tags used by the website.

    """
    D={}
    for word in tags:
        word=word.replace(' ','').lower()
        for words in tags:
            words=words.replace(' ','').lower()
            value = SequenceMatcher(None, word, words).ratio()
            if SIMILAR<value<1:
                D[word]=words
    return D

def visualizations(top_tags):
    '''
    Data visualization using Bar Graph.
    Argument:
    top_tags: List containing tuples.
    And tuple have tag and count respectively.

    x axis - tags
    y axis - counts
    '''
    tags=[]
    counts=[]
    for tag,count in top_tags:
        tags.append(tag)
        counts.append(count)
    data=[go.Bar(
        x=tags,
        y=counts)]
    py.plot(data, filename='basic-visualization')


if __name__ == "__main__":
    tags=get_tags()
    top_tags= get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    visualizations(top_tags)
    similar_tags=get_similarities(tags)
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))

