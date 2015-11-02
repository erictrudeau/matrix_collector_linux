# Matrix
# Copyright (c) 2011-2014, Eric Trudeau <erictrudeau@gmail.com>.  All rights reserved.
# This file and the Matrix project is licensed under the BSD 3-Clause License
# http://opensource.org/licenses/BSD-3-Clause

import logging
import logging.handlers

from django.conf import settings


#def logger_init(name=settings.LOGGING_DEFAULT_NAME, level_name=settings.LOGGING_LEVEL, console=settings.LOGGING_CONSOLE):
def logger_init(name='matrix', level_name='DEBUG', console=False):

	# get logger
	logger = logging.getLogger(name)

	# try finding logging level as defined in level_name
	try:
		logging_level = getattr(logging, level_name)
		logger.setLevel(logging_level)
		error_set_level = False

	# except on attribute error (logging level not found), then set to INFO and set flag to log the error after logging initialized later
	except AttributeError as error_set_level_e:
		logging_level = logging.INFO
		logger.setLevel(logging_level)
		error_set_level = True

	# create file handler
	logger_file = logging.FileHandler(settings.MATRIX_LOG)
	
	# set file handler logging level
	logger_file.setLevel(logging_level)

	# define log format
	formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
	
	# assign log formati to file handler
	logger_file.setFormatter(formatter)

	# add the handlers to the logger
	logger.addHandler(logger_file)

	# if console output is enabled
	if console:

		# create stream handler for outputting to the console
		logger_console = logging.StreamHandler()
		
		# set console handler to always show debug
		logger_console.setLevel(logging.DEBUG)

		# assign log format to console logger
		logger_console.setFormatter(formatter)

		# add console logger to log outputs
		logger.addHandler(logger_console)

	# if there was an error setting the logging level earlier, log it
	if error_set_level:
		logger.error('unable to set the requested logging level of %s.' % level_name)
		logger.error(error_set_level_e)

	return logger
