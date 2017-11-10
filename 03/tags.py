import feedparser
import operator

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    tags=[]
    blog_feed = feedparser.parse('https://pybit.es/feeds/all.rss.xml')
    for item in range(len(blog_feed.entries)):
        for i in range(len(blog_feed.entries[item].tags)):
            word=blog_feed.entries[item].tags[i]['term']
            tags.append(word)
    return tags
    

        
    
    


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
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
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    pass


if __name__ == "__main__":
    tags=get_tags()
    top_tags= get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    '''
    similar_tags = dict(get_similarities(tags))
    print()
    
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
    '''
