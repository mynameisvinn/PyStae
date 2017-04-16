import unittest

class InitializationTests(unittest.TestCase):

    def test_initialization(self):
        self.assertEqual(2+2, 4)

    def test_import(self):
        try:
            import pystae
        except ImportError:
            self.fail("Was not able to import the emailgraph")

if __name__ == "__main__":
    unittest.main()