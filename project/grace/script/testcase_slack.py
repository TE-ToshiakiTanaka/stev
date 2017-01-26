import os
import sys

from grace.utility import *
from grace.utility import LOG as L
from grace.script import testcase_base


class TestCase_Slack(testcase_base.TestCase_Unit):

    def slack_message(self, message, channel):
        try:
            self.slack.message(message, channel)
        except SlackError as e:
            L.warning(str(e))

    def slack_upload(self, filepath, channel):
        try:
            self.slack.upload(filepath, channel)
        except SlackError as e:
            L.warning(str(e))
