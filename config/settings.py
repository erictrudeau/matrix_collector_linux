# Matrix
# Copyright (c) 2011-2016, Eric Trudeau <erictrudeau@gmail.com>.  All rights reserved.
# This file and the Matrix project is licensed under the BSD 3-Clause License
# http://opensource.org/licenses/BSD-3-Clause

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from .settings_secure import *

# logging
LOG_DIR = '/var/log'
MATRIX_LOG = os.path.join(LOG_DIR, 'matrix.log')
LOGGING_DEFAULT_NAME	= 'matrix'
LOGGING_LEVEL			= 'DEBUG'	# DEBUG, ERROR, WARN, INFO, etc
LOGGING_CONSOLE			= False		# show output to console where running script


# logging (must be after MATRIX_LOG definition!!)
from lib.logger import logger_init
logger = logger_init('matrix.settings')




from lib.dir import ensure_dir


# main options
COLLECT_BROCADE		= True
COLLECT_EMC_VNX		= True
COLLECT_CML			= False
COLLECT_MITREND		= False
DEBUG_OVERRIDE		= False


################################################################################

# import settings for enabled modules
if COLLECT_BROCADE: 	from .settings_brocade import *
if COLLECT_CML: 		from .settings_cml import *
if COLLECT_EMC_VNX: 	from .settings_emc_vnx_block import *
if COLLECT_EMC_VNX: 	from .settings_emc_vnx_file import *
if COLLECT_MITREND: 	from .settings_cml import *


# debug mode
if DEBUG_OVERRIDE or sys.platform == 'darwin': DEBUG = True  # dev mode
else: DEBUG = False  # prod mode


# set directories
LOG_ARCHIVE_BASE_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'log_archive'))
ensure_dir(LOG_ARCHIVE_BASE_DIR)

TMP_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'tmp'))
ensure_dir(TMP_DIR)


#

