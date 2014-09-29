# Matrix :: Data Collector for Linux
# Copyright (c) 2014, Eric Trudeau <erictrudeau@gmail.com>.  All rights reserved.
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
	'site1_a': {
		'site'		: 'site1',
		'fabric'	: 'site1-a',
		'name'		: 'FABRIC-SITE1-A',
		'name4'		: 'FAB1A',
		'ip'		: '10.1.1.1',
		'username'	: 'mtx',
		'ssh-key'	: os.path.join(BASE_DIR, 'keys/matrix__collector__brocade'),
	},
	'site1_b': {
		'site'		: 'site1',
		'fabric'	: 'site1-b',
		'name'		: 'FABRIC-SITE1-B',
		'name4'		: 'FAB1B',
		'ip'		: '10.1.2.1',
		'username'	: 'mtx',
		'ssh-key'	: os.path.join(BASE_DIR, 'keys/matrix__collector__brocade'),
	}
}
