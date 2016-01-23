import unittest

class StveTest(unittest.TestCase):

    def setUp(self):
        print('setUp')

    def test_first(self):
        print('stve test first')
        self.assertTrue(True)

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(StveTest))
    return suite
