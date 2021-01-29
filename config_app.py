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
    CMS_AUTH = CMS_ROOT + "/christ-the-king/auth/authenticate"
    CMS_API = CMS_ROOT + "/christ-the-king/"
    VOTD = "http://www.biblegateway.com/usage/votd/rss/votd.rdf?31"
    DEVOTION = "https://wels.net/dev-daily/feed/pt-dev-daily/?redirect=no"
    CALENDAR_CHURCH = "ctk-wels.org_b2f81ihagnjief8f6v2l84glqo@group" \
                      ".calendar.google.com"
    CALENDAR_SCHOOL = "ctk-wels.org_bco7rpommo0uh96kgfc1hangs0@group" \
                      ".calendar.google.com"

CONST = _Const()
