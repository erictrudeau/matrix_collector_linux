#!/bin/bash
# Matrix :: Data Collector for Linux
# Copyright (c) 2014, Eric Trudeau <erictrudeau@gmail.com>.  All rights reserved.
# This file and the Matrix project is licensed under the BSD 3-Clause License
# http://opensource.org/licenses/BSD-3-Clause

cd /data/matrix/matrix_collector_linux
/bin/bash -c ". ../venv/bin/activate; exec /bin/bash -i -c './collect.py'"
