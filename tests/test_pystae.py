import unittest
import requests

MUNICIPALITY_ID = 'https://municipal.systems/v1/municipalities/jers-nj/trips'

class InitializationTests(unittest.TestCase):

    def test_initialization(self):
        pass

    def test_import(self):
        try:
            import pystae
        except ImportError:
            self.fail("Failed to import pystae")
    
    def test_response(self):
        r = requests.get(MUNICIPALITY_ID)
        self.assertEqual(r.status_code, 200)

if __name__ == "__main__":
    unittest.main()