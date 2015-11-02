# Matrix
# Copyright (c) 2011-2016, Eric Trudeau <erictrudeau@gmail.com>.  All rights reserved.
# This file and the Matrix project is licensed under the BSD 3-Clause License
# http://opensource.org/licenses/BSD-3-Clause

import os
import re
import datetime

from config.settings_emc_vnx_block import NAVISECCLI_PATH

from lib.logger import logger_init
from lib.regex import re_find

logger = logger_init('matrix.collector.linux.emc_vnx_block')


def analyzer_list(raw):
	''' 
	Index Size in KB     Last Modified            Filename
	0     157860    08/13/2015 21:42:25  APM00000001234_SPA_2015-08-14_02-38-46-GMT_M06-00.nar
	1     159413    08/14/2015 10:42:19  APM00000001234_SPA_2015-08-14_15-38-46-GMT_M06-00.nar
	2     158278    08/14/2015 23:42:14  APM00000001234_SPA_2015-08-15_04-38-44-GMT_M06-00.nar
	'''

	raw_parsed = re.findall(r'(\d+)\s+(\d+)\s+(\d{2}/\d{2}/\d{4}\s\d{2}:\d{2}:\d{2})\s+(APM(?:\d+)_SP[AB]_[-_\w]+.nar)', raw)

	r = []
	for row in raw_parsed:
		r.append({
			'index'		: row[0],
			'size_kb'	: row[1],
			'modified'	: datetime.datetime.strptime(row[2],'%m/%d/%Y %H:%M:%S'),
			'filename'	: row[3],
		})

	return r



def parse_lun_info(raw, lun_id=None):
	""" A regex parser for an individual lun. """
	''' 
	Name                        VNX5600B-DB-Logs-62
	LUN Capacity(Megabytes):    2097152
	LUN Capacity(Blocks):       4294967296
	RAID Type:                  N/A
	UID:                        60:06:01:60:93:50:36:00:BC:4B:DD:AA:75:EE:22:11
	Default Owner:              SP B
	Current owner:              SP B
	Is Thin LUN:                YES
	'''

	r								= {}
	r['lun_id']						= re_find(r'LOGICAL UNIT NUMBER (\d+)\n', raw)			# LOGICAL UNIT NUMBER 62
	r['name']						= re_find(r'Name\s+(.+)\n', raw)						# VNX5600B-DB-Logs-62
	r['capacity_mb']				= re_find(r'LUN Capacity(Megabytes):\s+(\d+)\n', raw)	# 2097152
	r['capacity_blocks']			= re_find(r'LUN Capacity(Blocks):\s+(\d+)\n', raw)		# 4294967296
	r['raid_type']					= re_find(r'RAID Type:\s+()\n', raw)					# N/A
	r['guid']						= re_find(r'UID:\s+()\n', raw)							# 60:06:01:60:93:50:36:00:BC:4B:DD:AA:75:EE:22:11
	r['default_owner']				= re_find(r'Default Owner:\s+SP ([A|B])\n', raw)		# SP B
	r['current_owner']				= re_find(r'Current owner:\s+SP ([A|B])\n', raw)		# SP B
	r['is_thin']					= re_find(r'Is Thin LUN:\s+([YES|NO])\n', raw)			# YES

	return r



def parse_luns(raw, lun_id=None):
	""" A regex parser for a list of luns. """
	''' 
	LOGICAL UNIT NUMBER 74
	Name                        VNX5600B-CAP-74 (RDM ARCHIVE01)
	LUN Capacity(Megabytes):    4194304
	...

	LOGICAL UNIT NUMBER 85
	Name                        VNX5600A-DB-Logs-85 (RDM SQLLOGS01)
	LUN Capacity(Megabytes):    256000
	...

	LOGICAL UNIT NUMBER 105
	Name                        VNX5600A-STD-105 (SRM PH)
	LUN Capacity(Megabytes):    2048
	...

	'''

	r = []
	for raw_block in [ 'LOGICAL UNIT NUMBER '+i for i in re.split(r'\n(?:LOGICAL UNIT NUMBER )', raw) ][1:]:
		r.append( parse_lun_info(raw_block) )

	return r

