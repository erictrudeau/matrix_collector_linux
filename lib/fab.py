# Matrix Collector: Linux (CML, EMC & Brocade)
# Written by Eric_Trudeau@dell.com
# v2.0 20140326
# Copyright 2014 Eric Trudeau

import os

if __name__ == "__main__":
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

from django.conf import settings

from lib.logger import logger_init

from fabric.api import local  #, cd, run, env, sudo
from fabric.context_managers import settings as fab_settings


logger = logger_init('matrix.collector.linux.functions.fab')

def fab_run_local(cmd):
	logger.debug('fab_run_local  cmd: %s' % cmd)

	with fab_settings(warn_only=True):
		# run command
		r = local(cmd, capture=True)

		# log output
		logger.debug('fab_run_local  output: %s' % r)

		return r
