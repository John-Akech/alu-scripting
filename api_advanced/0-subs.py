#!/usr/bin/python3

"""
A function that queries the Reddit API and returns the number of subscribers
"""
import sys

def number_of_subscribers(subreddit):
    """ number_of_subscribers """
    if __name__ == '__main__':
            number_of_subscribers = __import__('0-subs').number_of_subscribers
            if len(sys.argv) < 2:
                print("Please pass an argument for the subreddit to search.")
            else:
                print("{:d}".format(number_of_subscribers(sys.argv[1])))
