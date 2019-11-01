from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView
)

import pdb
import tweepy
from collections import defaultdict
import threading
import os
from .config import *

from .tweet_service import TweetService
from django.conf import settings

tweet_service = TweetService(consumer_key, consumer_secret, access_token, access_token_secret)

alltweets = tweets = tweet_service.get_tweets_from_api() # api.user_timeline(screen_name = 'python_tip', count = 13, include_rts = True)

import pdb

def home(request):
    hash_tag_freqs = tweet_service.get_hashtag_freqs(tweets)
    hash_tag_freqs_keys = tweet_service.get_hashtag_freqs(tweets).keys()

    pdb.set_trace()

    context = {
        'tweets': tweets,
        'hashtag_freq_keys': hashtag_freq_keys,
        'hashtag_freqs': hashtag_freqs
    }

    return render(request, 'python_tip/tweets.html', tweets = tweets, hashtag_freqs = hashtag_freqs)

def index(request):
    return render(request, 'python_tip/tweets.html', {'tweets': tweets})

def about(request):
    return render(request, 'python_tip/about.html', {'title': 'About'})

class TweetListView(ListView):
    # model = Tweet
    template_name = 'python_tip/tweets.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'tweets'
    ordering = ['-date_posted', '-retweet_count', '-favorite_count']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        hashtag_freqs = tweet_service.get_hashtag_freqs(tweets)
        context = super(TweetListView, self).get_context_data(**kwargs)
        # context['tweets'] = tweets,
        context['hashtag_freqs'] = hashtag_freqs,
        context['hashtag_freq_keys'] = tuple(hashtag_freqs.keys()),
        context['hashtag_freq_values'] = tuple(hashtag_freqs.values()),
        return context

    def get_queryset(self):
        query = self.request.GET.get('q', '').lstrip().rstrip().lower()
        res = list(filter( lambda x: query in list(map(lambda y: y['text'].lower(), x.entities['hashtags'])) or query in x.text.lower(), tweets))
        res = sorted(res, key=lambda x: x.retweet_count , reverse=True)
        res = sorted(res, key=lambda x: x.favorite_count , reverse=True)
        # pdb.set_trace()
        return res #{'tweets' :res, 'hashtag_freqs': hashtag_freqs}

class FilteredTweetListView(ListView):
    # model = Tweet
    template_name = 'python_tip/tweets.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'tweets'
    ordering = ['-date_posted']
    paginate_by = 5

    # queryset = Post.objects.published()
    # template_name = "index.html"

    def get_context_data(self, **kwargs):
        hashtag_freqs = tweet_service.get_hashtag_freqs(tweets)
        context = super(FilteredTweetListView, self).get_context_data(**kwargs)
        context['hashtag_freqs'] = hashtag_freqs,
        context['hashtag_freq_keys'] = tuple(hashtag_freqs.keys()),
        context['hashtag_freq_values'] = tuple(hashtag_freqs.values()),
        return context

    def get_queryset(self):
        hashtag = self.kwargs.get('hashtag').lstrip().rstrip().lower()
        query = self.request.GET.get('q', '').lstrip().rstrip().lower()
        filtered_tweets_by_hashtag = list(filter( lambda x: hashtag in list(map(lambda y: y['text'].lower(), x.entities['hashtags'])) or hashtag in x.text.lower() ,tweets))
        filtered_tweets_by_query = list(filter( lambda x: query in list(map(lambda y: y['text'].lower(), x.entities['hashtags'])) or query in x.text.lower() , filtered_tweets_by_hashtag))
        tweets_sorted_by_retweet_count = sorted(filtered_tweets_by_query, key=lambda x: x.retweet_count , reverse=True)
        res = tweets_sorted_by_favorite_count = sorted(tweets_sorted_by_retweet_count, key=lambda x: x.favorite_count , reverse=True)
        return res

