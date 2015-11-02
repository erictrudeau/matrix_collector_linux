# Matrix
# Copyright (c) 2011-2016, Eric Trudeau <eric@trud.us>.  All rights reserved.
# This file and the Matrix project is licensed under the BSD 3-Clause License
# http://opensource.org/licenses/BSD-3-Clause

import re


def re_find(regex, string, value_if_not_found='---'):
	m = re.search(regex, string)

	if m and m.group(1):
		r = m.group(1)

		if r in ['true', 'TRUE', 'True', 'yes', 'YES', 'Yes', ]:
			return True
		elif r in ['false', 'FALSE', 'False', 'no', 'NO', 'No', ]:
			return False
		else:
			return r.strip()

	else:
		return value_if_not_found

