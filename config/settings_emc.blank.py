# Matrix :: Data Collector for Linux
# Copyright (c) 2014, Eric Trudeau <erictrudeau@gmail.com>.  All rights reserved.
# This file and the Matrix project is licensed under the BSD 3-Clause License
# http://opensource.org/licenses/BSD-3-Clause

from settings import BASE_DIR

EMC_CLI_COMMAND_SYNTAX = '/opt/Navisphere/bin/naviseccli -h %s %s > %s'

EMC_CLI_COMMANDS = [
	('getlun -name -capacity -type -uid', 'luns.txt'),
	('storagegroup -list -host', 'storage_groups.txt'),
	('getrg', 'raid_groups.txt'),
	('storagepool -list', 'storage_pools.txt'),
]

EMC_FRAMES = {
	"1234": {
		"ip": "10.0.12.34",
		"name4": "1234",
		"site": "site1",
		"name": "FRAME-EMC-1234"
	},
	"5678": {
		"ip": "10.0.56.78",
		"name4": "5678",
		"site": "site1",
		"name": "FRAME-EMC-5678"
	}
}


'''
import json
from devices.models import StorageDevice
frames = ['1234', '5678', ]
sd_set = StorageDevice.objects.filter(name_short__in=frames)
r = {}
for d in sd_set:
	r[d.name_short] = {
		'site'      : d.site.slug,
		'name'      : d.name,
		'name4'     : d.name_short,
		'ip'        : d.deviceconnectionethernet_set.filter(xtype__slug='spa')[0].ip_address,
	}

print 'EMC_FRAMES = %s' % json.dumps(r, indent=4)
'''
