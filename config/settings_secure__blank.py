# Matrix
# Copyright (c) 2011-2016, Eric Trudeau <erictrudeau@gmail.com>.  All rights reserved.
# This file and the Matrix project is licensed under the BSD 3-Clause License
# http://opensource.org/licenses/BSD-3-Clause

from requests.auth import HTTPBasicAuth

SECRET_KEY = ''

SECURE_DSO_AUTH_DOMAIN = ''
SECURE_DSO_AUTH_USERNAME = ''
SECURE_DSO_AUTH_PASSWORD = ''

SECURE_MITREND_AUTH_USERNAME = ''
SECURE_MITREND_AUTH_PASSWORD = ''
SECURE_MITREND_AUTH = HTTPBasicAuth(SECURE_MITREND_AUTH_USERNAME, SECURE_MITREND_AUTH_PASSWORD)
