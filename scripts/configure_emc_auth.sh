# Matrix :: Data Collector for Linux
# Copyright (c) 2014, Eric Trudeau <erictrudeau@gmail.com>.  All rights reserved.
# This file and the Matrix project is licensed under the BSD 3-Clause License
# http://opensource.org/licenses/BSD-3-Clause

# commands to setup emc auth
/opt/Navisphere/bin/naviseccli -address 10.0.12.34 -AddUserSecurity -user <username> -password <password> -scope 0
/opt/Navisphere/bin/naviseccli -address 10.0.56.78 -AddUserSecurity -user <username> -password <password> -scope 0

# test command
#/opt/Navisphere/bin/naviseccli -h 10.0.12.34 getlun -name -capacity -type -uid
