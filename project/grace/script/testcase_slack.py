import os
import sys

from stve.exception import *

from grace.utility import *
from grace.utility import LOG as L
from grace.script import testcase_base


class TestCase_Slack(testcase_base.TestCase_Unit):

    def slack_message(self, message, channel=None):
        if channel == None: channel = self.get("slack.channel")
        try:
            self.slack.message(message, channel)
        except SlackError as e:
            L.warning(str(e))

    def slack_upload(self, filepath, channel=None):
        if channel == None: channel = self.get("slack.channel")
        try:
            L.warning(os.path.exists(filepath))
            self.slack.upload(filepath, channel, filetype="image/png")
        except SlackError as e:
            L.warning(str(e))
            raise e
