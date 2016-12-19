import os
import sys
import logging

from stve import log

WORK_DIR = os.path.normpath(os.path.dirname(__file__))
LIB_DIR = os.path.normpath(os.path.join(WORK_DIR, "lib"))
SCRIPT_DIR = os.path.normpath(os.path.join(WORK_DIR, "script"))
TMP_DIR = os.path.normpath(os.path.join(WORK_DIR, "tmp"))
LOG_DIR = os.path.normpath(os.path.join(WORK_DIR, "log"))
BIN_DIR = os.path.normpath(os.path.join(WORK_DIR, "bin"))
REPORT_DIR = os.path.normpath(os.path.join(WORK_DIR, "report"))

PROFILE_DIR = os.path.normpath(os.path.join(WORK_DIR, "conf", "profile"))

LOG = log.Log("Grace.Project.STVE")
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)
logfile = os.path.join(LOG_DIR, "system.log")
if not os.path.exists(logfile):
    with open(logfile, 'a') as f:
        os.utime(logfile, None)

LOG.addHandler(log.Log.filehandler(logfile, log.BASE_FORMAT, logging.DEBUG))
