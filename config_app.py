#!/usr/bin/python3

import os
import random
"""Configuration File

Store configuration information within this file.  Do not track the file in Git

"""


class _Const(object):
    """Configuration constants"""

    def __init__(self):
        return

    NONCE = ''.join([str(random.randint(0, 9)) for i in range(32)])
    SECRET = "The truth is public domain"
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    CMS_USR = "jfukura@gmail.com"
    CMS_PSS = "309%3Pti5%X^Rlh6jOKYCVlJt%IFHQ$E%"

    CMS_ROOT = "https://ctk.welspring.faith"
    CMS_AUTH = CMS_ROOT + "/api/auth/authenticate"
    CMS_API = CMS_ROOT + "/api/"
    GCLIENT = "132609342573-4li1060cdnh0hp9vogkg245h4epk6vco.apps" \
              ".googleusercontent.com"
    GSECRET = "sh00nNHZO14OCKX9VdfF6w0c"
    VOTD = "http://www.biblegateway.com/usage/votd/rss/votd.rdf?31"
    DEVOTION = "https://wels.net/dev-daily/feed/pt-dev-daily/?redirect=no"
    CALENDAR_CHURCH = "ctk-wels.org_b2f81ihagnjief8f6v2l84glqo@group" \
                      ".calendar.google.com"
    CALENDAR_SCHOOL = "ctk-wels.org_bco7rpommo0uh96kgfc1hangs0@group" \
                      ".calendar.google.com"


CONST = _Const()

# What is this...do we need it?

# CMS_KEY = "JL5O7yTZ5iPsJ2me15NPGSZAFWEaoIUa"
