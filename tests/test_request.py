from SimConnectExpansion import Request
from unittest import TestCase
from unittest.mock import Mock

import logging

LOGGER = logging.getLogger(__name__)

class TestSimple(TestCase):
	def test_init_request(self):
		self.assertTrue(True)
