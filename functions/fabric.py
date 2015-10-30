# Matrix Collector: Linux (CML, EMC & Brocade)
# Written by Eric_Trudeau@dell.com
# v2.0 20140326
# Copyright 2014 Eric Trudeau

import os

if __name__ == "__main__":
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

from django.conf import settings

from fabric.api import local  #, cd, run, env, sudo
from fabric.context_managers import settings as fab_settings


def fab_run_local(cmd):
	if settings.DEBUG:
		print cmd
		return

	else:
		with fab_settings(warn_only=True):
			# run command
			return local(cmd)


