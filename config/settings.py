# Matrix :: Data Collector for Linux
# Copyright (c) 2014, Eric Trudeau <erictrudeau@gmail.com>.  All rights reserved.
# This file and the Matrix project is licensed under the BSD 3-Clause License
# http://opensource.org/licenses/BSD-3-Clause

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from settings_brocade import *
from settings_cml import *
from settings_emc import *
from settings_secure import *
from functions import ensure_dir

if os.uname()[0] == 'Darwin':
	# dev mode (osx)
	DEBUG = True

else:
	# prod mode (ubuntu)
	DEBUG = False

DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'import_data'))
ensure_dir(DATA_DIR)

ARCHIVE_DIR = os.path.abspath(os.path.join(DATA_DIR, 'archive'))
ensure_dir(ARCHIVE_DIR)

TMP_DIR = os.path.abspath(os.path.join(DATA_DIR, 'tmp'))
ensure_dir(TMP_DIR)
