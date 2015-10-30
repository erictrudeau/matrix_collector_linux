# Matrix
# Copyright (c) 2011-2016, Eric Trudeau <erictrudeau@gmail.com>.  All rights reserved.
# This file and the Matrix project is licensed under the BSD 3-Clause License
# http://opensource.org/licenses/BSD-3-Clause

import os
from settings import BASE_DIR

BROCADE_CLI_COMMAND_SYNTAX = 'ssh -i %s %s@%s %s > %s'

BROCADE_CLI_COMMANDS = [
	('zoneshow', 'zone_show.txt'),
	('version show', 'version_show.txt'),
]

BROCADE_SWITCHES = {
	'fabxa': {
		'site'		: 'site-slug',
		'fabric'	: 'a',
		'name'		: 'Site Name',
		'name4'		: '1111',
		'ip'		: '11.11.11.11',
		'username'	: 'mtx',
		'password'	: '',
		'ssh-key'	: os.path.join(BASE_DIR, 'keys', 'matrix__collector__brocade'),
	},
	'fabxb': {
		'site'		: 'site-slug',
		'fabric'	: 'b',
		'name'		: 'Site Name',
		'name4'		: '2222',
		'ip'		: '22.22.22.22',
		'username'	: 'mtx',
		'password'	: '',
		'ssh-key'	: os.path.join(BASE_DIR, 'keys', 'matrix__collector__brocade'),
	},
}
