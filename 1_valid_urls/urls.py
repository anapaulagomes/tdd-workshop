"""
Problem:

You should write a method to check whether
an URL is valid or not, considering that it
should begin with http to be a valid one.

Extension:

Would be nice to know if the website exists or not.
You can add this feature creating a request
to an URL if it is valid.
"""

def is_valid(url):
    return url.startswith('http://') or url.startswith('https://')
