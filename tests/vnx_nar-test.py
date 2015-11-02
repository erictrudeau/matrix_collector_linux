#!/usr/bin/env python
# Matrix
# Copyright (c) 2011-2016, Eric Trudeau <erictrudeau@gmail.com>.  All rights reserved.
# This file and the Matrix project is licensed under the BSD 3-Clause License
# http://opensource.org/licenses/BSD-3-Clause

import os
import sys
import datetime

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

from django.conf import settings
from django.utils import timezone

from lib.logger import logger_init

from emc_vnx import collectors as vnx_collectors
from emc_vnx import parsers as vnx_parsers

logger = logger_init('matrix.collector.linux.emc_vnx_block')


collector = 'emc_vnx_block'
dir_output = os.path.join(settings.LOG_ARCHIVE_BASE_DIR, collector + '__%s')


# loop over frames to download files
for frame,config in settings.EMC_VNX_BLOCK_FRAMES.items():

	logger.debug('config:%s' % config)


	###
	### NAR
	###

##	## skip 0502 for now
	if frame == '0502':
		continue

	logger.info('retrieving files from %s' % config['name'])

	# list nar files
	nar_list_raw = vnx_collectors.analyzer_list(config)
	logger.debug('nar_list_raw:%s' % nar_list_raw)


	# parse nar list
	nar_list = vnx_parsers.analyzer_list(nar_list_raw)

	# loop over nar file list
	for f in nar_list:
		logger.debug('file:%s' % f)

		# f['size_kb']
		# f['size_mb'] = f['size_kb'] / 1024
		# f['filename']
		# f['modified']

		# check if file exists



		# download
#		dir_output_nar = dir_output % 'nar'
#		emc_vnx_block.analyzer_retrieve(config, file['filename'], analyzer_dir_output)


	logger.info('nar retrieval complete.')

'''

	###
	### SP COLLECT
	###

	# list managefiles
	managefiles_list = emc_vnx_block.managefiles_list(config)
	logger.debug('managefiles_list:%s' % managefiles_list)

	# loop over managefiles list
	for file in managefiles_list:
		if file.endswith('_data.zip'):

			# file['size_kb']
			# file['filename']
			# file['modified']

			# check if exists

			# download
			spcollect_dir_output = '/opt/matrix/log_archive/emc-vnx-block__spcollect/'
			emc_vnx_block.managefiles_retrieve(config, file['filename'], spcollect_dir_output)

	logger.info('sp collect retrieval complete.')
'''
