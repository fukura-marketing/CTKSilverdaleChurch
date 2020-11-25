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

    SECRETS = {
      "type": "service_account",
      "project_id": "welspring-180921",
      "private_key_id": "81d43a67eebb5cc032a9021fa06d570bb2353674",
      "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDNQaBGfw3oalsx\nRO/ipwfyBhL0j3lLOU3g5TXQi2AdoQZIh39ygiN+HgvWbFVVHQFFck7l8QhjLUfI\n1wQaUUiWi7sKbAR958Aw6eKobuKJRlRBJHZfZojcopYa6+ZX+HBPQnln0hevUV9A\nzr7ivQf6gnnC65/XujDTUo3UjXIgaOrG9BcifL2g7ENyLdPe5GOHQ2OAMAAT9HAl\nQKvDSv0dAsb18zzp6UZ1QagRRNI3WrPShDnXDfelPGoKLMSmnzH2tPZfCwmvg8bQ\n1/aOjc4Y1im+BFIcMbreCtLgkcJ7ufCGsP4dHxNABKopNlfUCs55EOZ7Su1NB9H8\nQAfEmY9DAgMBAAECggEAFkSWZM+H7L0NI6088TP50rICAHJIUHbpEgsL6ZIVXWGI\n0vmQRBYGT7pmwl6Ca3d4Gdaq5Jtfs5LIBOv+z/Qdkeea5SiO3DH2Udgt9OQCw63T\nmjWgef0fwAALlOQe21BirtahYTgTxbtoQBmt799eLDlXiGQTtU3H2kVMidDGnulR\nQbcX3DMpDsOcvNvGL0oO4ZaOpruIzxv2vy2Hgsr22j/HwtJRfeEL+ysjkYE8/er3\nCN4sxCqulC8eBw/f50efcw/9P54EKqn987+UrkH8SIR9ANgmlS/iYf03uFd3d+9W\nnIgci1I0+NTLvBp7HZdhLESiTSKnefTT8kHK8q7MIQKBgQDnf+7Z3L4JY6BUd44o\nfckl95iny1TmuV9WG4Ks47sz7hRO9xBOrL+/lVY9OZomV0YsFpYo4UeDgGxayJ1u\nxtwGafitij9mOS2YZ/JgmzbH6LnVP51TFFo8xPHozR59o2LXkzxs4ZLPX40oD199\nZIzar+e8NoSlIycdRWm2y3qtuQKBgQDi+q0KdTxRg8WBpiLWHZ+E3XWUjtPFOLWV\nfwne44FTCosFVQJQ9ZBKvM9OcmPLX+bXPZQjKqa97JU4AgysGhvKKnXYpuD2Lb5c\nAJG/y35lFKWHW5RP2eG70PTY4ZNkjTQUkCA0EgrZseJHz7tfgnwyTeJt97AnBDR1\nYJO8CWeC2wKBgQDfvFIwttnnoySyXfXDhoYgLqKYELjWYHQWeXIa++HSd5ejFb7p\n+qU7WO5HL+OeiJymQZIQomGGY1jViKw3AvRlMogH2OQbPMmnUVb8LSaNoIvx4JCB\nWds4fjM6hvuf+4esx30P0hccWsHG5MyqGMLVHEsAKUSbgVTtQkfARfoj6QKBgAm3\n3ezStDBxSeWRLXCpeAkCSmR/8QVCtlOeStfmOcVKcEVcLGs2+GSazO147Fjq1EFm\n+4695sG+/WyWeeBshcAULVOHYZ5ouvvJcnQZzGGbjrLK8wCwPYADJFic3+iwOwie\nWyKfmyNTAHM+q7EdLyAgQY+fyUUCYxSbe/fTF0F9AoGAC4pJheNmm6IIhrr4DVG5\n0BUWJHFYPi5Gdq85lTiNmT19gR1h78WlwiO2ktGCZ5MilowRD6V2fbnqUp82+L/K\n8luWq+BPHBim91j46Dx1W6547xVJ7YxMImc6fnwJ7IVv8P8j1OqteDVIZlZ4OOLu\nyQBiiBcHwkiThMryDNTnje0=\n-----END PRIVATE KEY-----\n",
      "client_email": "ctk-calendar@welspring-180921.iam.gserviceaccount.com",
      "client_id": "108711096050236740052",
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://oauth2.googleapis.com/token",
      "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
      "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/ctk-calendar%40welspring-180921.iam.gserviceaccount.com"
    }
CONST = _Const()

# What is this...do we need it?

# CMS_KEY = "JL5O7yTZ5iPsJ2me15NPGSZAFWEaoIUa"
