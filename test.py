import unittest
import json

from utils import sort_media, FILE_DATA

class Test(unittest.TestCase):

    def test_sort_media(self):

        sorted_media = sort_media(json.dumps(FILE_DATA))
        self.assertEqual(sorted_media, False)



unittest.main(verbosity=2)
