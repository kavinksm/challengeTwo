import unittest
import json
from unittest import result
from getInstMetaData import getMetadata

class testgetMetadata(unittest.TestCase):
    def test_success(self):
        try:
            print(json.dumps(getMetadata()))            
            status = True
        except:
            status = False
        self.assertTrue(status)

if __name__ == '__main__':
    unittest.main()