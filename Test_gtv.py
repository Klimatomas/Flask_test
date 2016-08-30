import unittest
from source import Requests


class RequestTest(unittest.TestCase):
    def testTrending(self):
        t = Requests()
        t.trending()
        self.assertEquals(t.trending()["meta"]["status"], 200)

