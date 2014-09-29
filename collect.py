#!/usr/bin/env python
# Matrix :: Data Collector for Linux
# Copyright (c) 2014, Eric Trudeau <erictrudeau@gmail.com>.  All rights reserved.
# This file and the Matrix project is licensed under the BSD 3-Clause License
# http://opensource.org/licenses/BSD-3-Clause

import os
import shutil

if __name__ == "__main__":
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import datetime
from fabric.api import local, cd, run, env, sudo
from fabric.context_managers import settings as fab_settings

from django.conf import settings
from django.utils import timezone

from functions import *

timestamp = timezone.now()
timestamp_pretty = timestamp.strftime('%Y%m%d-%H%M%S')


def run_collector(collector, config):

	PACKAGE = 'matrix_package__%s__%s' % (collector, timestamp_pretty)
	PACKAGE_DIR = os.path.abspath(os.path.join(settings.DATA_DIR, 'tmp', PACKAGE))


	for name,config in config.items():

		dir_item = os.path.abspath(os.path.join(PACKAGE_DIR, config['name4']))
		ensure_dir(dir_item)

		for command,outfile in getattr(settings, '%s_CLI_COMMANDS' % collector.upper()):

			if collector == 'cml':
				cmd = settings.CML_CLI_COMMAND_SYNTAX % (settings.CML_CLI_DIR, settings.CML_CLI_DIR, config['name4'], command, dir_item, outfile)

			elif collector == 'emc':
				cmd = settings.EMC_CLI_COMMAND_SYNTAX % (config['ip'], command, os.path.join(dir_item, outfile))

			elif collector == 'brocade':
				cmd = settings.BROCADE_CLI_COMMAND_SYNTAX % (config['ssh-key'], config['username'], config['ip'], command, os.path.join(dir_item, outfile))


			if settings.DEBUG:
				print cmd
			else:
				with fab_settings(warn_only=True):
					# run command
					local(cmd)


	# create tgz
	cmd = 'cd %s; tar -czf %s/%s.tgz %s' % (settings.TMP_DIR, settings.ARCHIVE_DIR, PACKAGE, PACKAGE)
	if settings.DEBUG:
		print cmd
	else:
		# run command
		local(cmd)

		# delete uncompressed
		shutil.rmtree(PACKAGE_DIR)



if __name__ == "__main__":

	# collect cml
	run_collector('cml', settings.CML_FRAMES)

	# collect emc
	run_collector('emc', settings.EMC_FRAMES)

	# collect brocade
	run_collector('brocade', settings.BROCADE_SWITCHES)



