# Matrix Collector: Linux (CML, EMC & Brocade)
# Written by Eric_Trudeau@dell.com
# v2.0 20140326
# Copyright 2014 Eric Trudeau

import os


def ensure_dir(d):
	if not os.path.exists(d):
		os.makedirs(d)
