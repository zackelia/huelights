""" This module provides various helper functions """
import json
import requests


def get(url):
    """ GET request from a URL """
    r = requests.get(url)
    r.raise_for_status()

    return r


def put(url, payload):
    """ PUT request to a URL with payload """
    r = requests.put(url, json.dumps(payload))
    r.raise_for_status()

    return r
