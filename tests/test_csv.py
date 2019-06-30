import unittest

from app.csv_io import readCSV

class SomeCSVTestCase(unittest.TestCase):
    def setUp(self):
        self.version = "1.0.0"
    def tearDown(self):
        self.version = None

    def test_readCSV(self):
        data = readCSV('tests/test.csv')
        index = data.count().keys()
        self.assertEqual(len(index), 3)
        self.assertEquals(index[0], 'animal')
        self.assertEquals(index[1], 'uniq_id')
        self.assertEquals(index[2], 'water_need')


