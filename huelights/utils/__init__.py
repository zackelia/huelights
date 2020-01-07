"""Provide various helper functions."""
import json
import requests
from typing import Optional


def delete(url: str, **kwargs) -> requests.models.Response:
    """DELETE request."""
    return _request(requests.delete, url, **kwargs)


def get(url: str, **kwargs) -> requests.models.Response:
    """GET request."""
    return _request(requests.get, url, **kwargs)


def put(url: str, **kwargs) -> requests.models.Response:
    """PUT request."""
    return _request(requests.put, url, **kwargs)


def post(url: str, **kwargs) -> requests.models.Response:
    """POST request."""
    return _request(requests.post, url, **kwargs)


def _request(method, url: str, **kwargs) -> Optional[requests.models.Response]:
    # Serialize data to json
    if "data" in kwargs:
        kwargs["data"] = json.dumps(kwargs["data"])

    response = method(url, **kwargs)
    response.raise_for_status()

    return response
