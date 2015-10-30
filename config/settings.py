# Matrix
# Copyright (c) 2011-2016, Eric Trudeau <erictrudeau@gmail.com>.  All rights reserved.
# This file and the Matrix project is licensed under the BSD 3-Clause License
# http://opensource.org/licenses/BSD-3-Clause

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from settings_secure import *
from functions import ensure_dir


# main options
COLLECT_BROCADE		= True
COLLECT_EMC_VNX		= True
COLLECT_CML			= True
COLLECT_MITREND		= True
DEBUG_OVERRIDE		= False


################################################################################

# import settings for enabled modules
if COLLECT_BROCADE: 	from settings_brocade import *
if COLLECT_CML: 		from settings_cml import *
if COLLECT_EMC_VNX: 	from settings_emc_vnx_block import *
if COLLECT_EMC_VNX: 	from settings_emc_vnx_file import *
if COLLECT_MITREND: 	from settings_cml import *


# debug mode
if DEBUG_OVERRIDE or sys.platform == 'darwin': DEBUG = True  # dev mode
else: DEBUG = False  # prod mode
	

# set directories
LOG_ARCHIVE_BASE_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'log_archive'))
ensure_dir(LOG_ARCHIVE_BASE_DIR)

TMP_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'tmp'))
ensure_dir(TMP_DIR)


#

