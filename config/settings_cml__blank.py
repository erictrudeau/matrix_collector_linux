# Matrix
# Copyright (c) 2011-2016, Eric Trudeau <erictrudeau@gmail.com>.  All rights reserved.
# This file and the Matrix project is licensed under the BSD 3-Clause License
# http://opensource.org/licenses/BSD-3-Clause

import os
from settings import BASE_DIR

CML_CLI_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'cml_cli'))

CML_CLI_COMMAND_SYNTAX = 'java -jar %s/CompCU.jar --defaultname %s/%s.cli -c "%s -csv %s/%s" > /dev/null'

CML_CLI_COMMANDS = [
	('alert show', 'alert_show.csv'),
	('cache show', 'cache_show.csv'),
	('cmm show', 'cmm_show.csv'),
	('consistencygroup show', 'consistencygroup_show.csv'),
	('controller show', 'controller_show.csv'),
	('diskfolder show', 'diskfolder_show.csv'),
	('mapping show', 'mapping_show.csv'),
	('os show', 'os_show.csv'),
	('replay show', 'replay_show.csv'),
	('replayprofile show', 'replayprofile_show.csv'),
	('server show', 'server_show.csv'),
	('server showhba', 'server_showhba.csv'),
	('serverfolder show', 'serverfolder_show.csv'),
	('storageprofile show', 'storageprofile_show.csv'),
	('storagetype show', 'storagetype_show.csv'),
	('system show', 'system_show.csv'),
	('user show', 'user_show.csv'),
	('usergroup show', 'usergroup_show.csv'),
	('volume show', 'volume_show.csv'),
	('volumefolder show', 'volumefolder_show.csv'),
]

CML_FRAMES = {
	"1111": {
		"ip": "11.11.11.11",
		"name4": "1111",
		"auth-file": "",
		"site": "site-a",
		"name": "FRAME-1111"
	},
	"2222": {
		"ip": "22.22.22.22",
		"name4": "2222",
		"auth-file": "",
		"site": "site-a",
		"name": "FRAME-2222"
	},
}


'''
import json
from devices.models import StorageDevice
sd_set = StorageDevice.objects.filter(device_model__make__name='Dell')
r = {}
for d in sd_set:
	r[d.name_short] = {
		'site'		: d.site.slug,
		'name'		: d.name,
		'name4'		: d.name_short,
		'ip'		: '',
		'auth-file' : '',
	}

print 'CML_FRAMES = %s' % json.dumps(r, indent=4)
'''
