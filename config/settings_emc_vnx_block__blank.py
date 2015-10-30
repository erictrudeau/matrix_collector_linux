# Matrix
# Copyright (c) 2011-2016, Eric Trudeau <erictrudeau@gmail.com>.  All rights reserved.
# This file and the Matrix project is licensed under the BSD 3-Clause License
# http://opensource.org/licenses/BSD-3-Clause

from settings import BASE_DIR

EMC_FRAMES = {
	'1111': {
		'site'		: 'site-slug',
		'name'		: 'Site Name',
		'name4'		: '1111',
		'ip'		: '11.11.11.11',
		'auth-file' : BASE_DIR + 'cml_cli/1111.cli',
	},
	'2222': {
		'site'		: 'site-slug',
		'name'		: 'Site Name',
		'name4'		: '2222',
		'ip'		: '22.22.22.22',
		'auth-file' : BASE_DIR + 'cml_cli/2222.cli',
	},
}
