# Matrix
# Copyright (c) 2011-2016, Eric Trudeau <erictrudeau@gmail.com>.  All rights reserved.
# This file and the Matrix project is licensed under the BSD 3-Clause License
# http://opensource.org/licenses/BSD-3-Clause

import os
import re

from config.settings_emc_vnx_block import NAVISECCLI_PATH

from lib.fab import fab_run_local
from lib.logger import logger_init

logger = logger_init('matrix.collector.linux.emc_vnx_block')


def analyzer_list(config):
	''' 
	naviseccli -h 10.11.22.33 analyzer -archive -list
	Index Size in KB     Last Modified            Filename
	0     157860    08/13/2015 21:42:25  APM00000001234_SPA_2015-08-14_02-38-46-GMT_M06-00.nar
	1     159413    08/14/2015 10:42:19  APM00000001234_SPA_2015-08-14_15-38-46-GMT_M06-00.nar
	2     158278    08/14/2015 23:42:14  APM00000001234_SPA_2015-08-15_04-38-44-GMT_M06-00.nar
	'''

	cmd = '''%s -h %s analyzer -archive -list''' % (NAVISECCLI_PATH, config['spa-ip'])

	raw = fab_run_local(cmd)

	return raw
#	return analyzer_list_parse(raw)
	


def analyzer_retrieve(config, filename, dir_output):
	'''
	naviseccli -h 10.11.22.33 analyzer -archive -file APM00000001234_SPA_2015-08-13_13-38-44-GMT_M06-00.nar -path /data/matrix/log_archive/emc-block__nar/ -o
	'''

	cmd = '''%s -h %s analyzer -archive -o -file %s -path %s''' % (NAVISECCLI_PATH, config['spa-ip'], filename, dir_output)

	return fab_run_local(cmd)



def nar_new(config):
	''' 
	naviseccli -h 10.11.22.33 analyzer -archive -new
	Archive name:  APM00000001234_SPA_2015-08-21_00-52-31-GMT_M00-00.nar
	'''

	cmd = '''%s -h %s analyzer -archive -new''' % (NAVISECCLI_PATHconfig['spa-ip'])

	r = fab_run_local(cmd)

	try:
		return r.split(':')[1].strip()
	except AttributeError:
		return None



def nar_statusnew(config):
	''' 
	naviseccli -h 10.11.22.33 analyzer -archive -statusnew APM00000001234_SPA_2015-08-21_00-52-31-GMT_M00-00.nar
	done:  No
	fileSize:  0
	'''

	r = None

	return r



def spcollect_start(config):
	''' 
	naviseccli -h 10.11.22.33 spcollect

	'''

	cmd = '''%s -h %s spcollect''' % (NAVISECCLI_PATH, config['spa-ip'])

	return fab_run_local(cmd)



def managefiles_list(config):
	''' 
	naviseccli -h 10.11.22.33 managefiles -list
	Index Size in KB     Last Modified            Filename
	0     207       08/17/15 19:00:18    128.221.1.250_configlayout.xml
	1     528       08/19/15 07:40:26    admin_tlddump.txt
	2     68701     08/13/15 02:37:44    APM00000001234_SPA_2015-08-13_07-01-43_35f001_data.zip
	3     73517     08/13/15 19:06:59    APM00000001234_SPA_2015-08-13_23-35-10_35f001_data.zip
	4     73025     08/15/15 20:39:19    APM00000001234_SPA_2015-08-16_00-53-39_35f001_data.zip
	5     69134     08/20/15 19:06:14    APM00000001234_SPA_2015-08-20_23-34-42_35f001_data.zip
	6     23367     08/20/15 19:00:00    APM00000001234_SPA_2015-08-20_23-34-42_RP.zip
	7     0         08/21/15 02:39:42    APM00000001234_SPA_2015-08-21_07-36-19_runlog.txt
	'''

	cmd = '''%s -h %s managefiles -list''' % (NAVISECCLI_PATH, config['spa-ip'])

	raw = fab_run_local(cmd)

	return analyzer_list_parse(raw)



def managefiles_retrieve(config, filename, dir_output):
	''' 
	naviseccli -h 10.11.22.33 managefiles -retrieve -path /data/matrix/log_archive/emc-block__spcollect/ -file APM00000001234_SPA_2015-08-20_23-34-42_35f001_data.zip -o
	'''

	cmd = '''%s -h %s managefiles -retrieve -path %s -file %s -o''' % (NAVISECCLI_PATH, config['spa-ip'], dir_output, filename)

	return fab_run_local(cmd)



def lun_info(config):
	''' 
	naviseccli -h 1.2.3.4 getlun (<lun-id>) -name -capacity -type -uid -default -owner -isthinlun
	Name                        VNX5600B-DB-Logs-62
	LUN Capacity(Megabytes):    2097152
	LUN Capacity(Blocks):       4294967296
	RAID Type:                  N/A
	UID:                        60:06:01:60:93:50:36:00:BC:4B:DD:AA:75:EE:22:11
	Default Owner:              SP B
	Current owner:              SP B
	Is Thin LUN:                YES
	'''

	cmd = '''%s -h %s getlun -name -capacity -type -uid -default -owner -isthinlun''' % (NAVISECCLI_PATH, config['spa-ip'])

	raw = fab_run_local(cmd)

	return parse_luns(raw)
	


def lun_create(config):
	''' 
	lun -create 
	[-type Thin|nonThin]
	-capacity capacity [-sq mb|gb|tb|bc]
	-poolId storagePoolID | -poolname storagePoolName
	-sp SPID
	[-aa autoAssignment]
	[-l lunNumber]
	[-name lunName]
	[-offset logicalBlockAddress]
	[-tieringPolicy noMovement|autoTier|highestAvailable|lowestAvailable]
	[-initialTier optimizePool|highestAvailable|lowestAvailable]
	[-deduplication On|Off]
	'''

	cmd = '''%s -h %s lun -create -type %s -capacity %s -sq %s -poolname %s -sp %s -l %s -name %s -tieringPolicy %s -initialTier %s -deduplication %s''' % (NAVISECCLI_PATH, config['spa-ip'])

	raw = fab_run_local()

	return parse_luns(raw)



def lun_migrate_start(config):
	''' 
	migrate -start -source number|WWN -dest number|WWN -rate low|medium|high|ASAP|value [-destroySnapshots] [-o]
	'''

	cmd = '''%s -h %s migrate -start -source %s -dest %s -rate %s''' % (NAVISECCLI_PATH, config['spa-ip'])

	raw = fab_run_local(cmd)

	return parse_luns(raw)



def lun_migrate_list(config):
	''' 
	migrate -list [-source number|WWN]
	[-dest]
	[-rate]
	[-state]
	[-percentcomplete]
	[-timeremaining]
	'''

	cmd = '''%s -h %s migrate -list''' % (NAVISECCLI_PATH, config['spa-ip'])

	raw = fab_run_local(cmd)

	return parse_luns(raw)



def lun_migrate_cancel(config):
	''' 
	migrate -cancel -source number|WWN [-o]
	'''

	cmd = '''%s -h %s migrate -cancel -source %s''' % (NAVISECCLI_PATH, config['spa-ip'])

	raw = fab_run_local(cmd)

	return parse_luns(raw)



def lun_migrate_modify(config):
	''' 
	migrate -modify -source number|WWN [-rate low|medium|high|ASAP|value] [-o]
	'''

	cmd = '''%s -h %s migrate -modify -source %s -rate %s''' % (NAVISECCLI_PATH, config['spa-ip'])

	raw = fab_run_local(cmd)

	return parse_luns(raw)



def storagepool_list(config):
	''' 
	storagepool -list [-id poolID|-name poolName][-availableCap]
	[-consumedCap] [-currentOp] [-description] [-disks] [-diskType]
	[-luns] [-opState] [-opStatus] [-prcntOp] [-rawCap] [-rtype]
	[-prcntFullThreshold] [-state] [-status] [-subscribedCap]
	[-userCap] [-prcntFull] [-autoTiering] [-tiers[-rdrivecount]
	[-loadBalance]] [-rebalance] [-fastcache]
	[-lunAllocation] [-snapshotAllocation]
	[-metadataAllocation] [-lunSubscribedCap]
	[-snapshotSubscribedCap] [-metadataSubscribedCap]
	[-compressionSavings] [-capacities]
	[-snapPoolFullThresholdEnabled] [-snapPoolFullHWM]
	[-snapPoolFullLWM] [-snapPoolFullState]
	[-snapSpaceUsedThresholdEnabled] [-snapSpaceUsedHWM]
	[-snapSpaceUsedLWM] [-snapSpaceUsedState]
	[-dedupState] [-dedupRate] [-dedupTieringPolicy]
	[-dedupInitialTier] [-efficiencySavings] [-dedupSharedCap]
	[-all]
	'''

	cmd = '''%s -h %s ...''' % (NAVISECCLI_PATH, config['spa-ip'])

	raw = fab_run_local(cmd)

	return parse_luns(raw)



def storagepool_modify(config):
	''' 
	storagepool -modify 
	-id poolID|-name poolName
	[-newName newName]
	[-description description]
	[-fastcache on|off]
	[-prcntFullThreshold threshold]
	[-autotiering scheduled|manual]
	[-snapPoolFullThresholdEnabled on|off]
	[-snapPoolFullHWMpoolFullHWM]
	[-snapPoolFullLWM poolFullLWM]
	[-snapSpaceUsedThresholdEnabled on|off]
	[-snapSpaceUsedHWMsnapSpaceUsedHWM]
	[-snapSpaceUsedLWM snapSpaceUsedLWM]
	[-dedupState Running|Paused]
	[-dedupRate Low|Medium|High]
	[-dedupTieringPolicy noMovement|autoTier|highestAvailable|lowestAvailable]
	[-dedupInitialTier optimizePool|highestAvailable|lowestAvailable]
	[-o]
	[-startDedup force]
	'''

	cmd = '''%s -h %s ...''' % (NAVISECCLI_PATH, config['spa-ip'])

	raw = fab_run_local(cmd)

	return parse_luns(raw)






