import main
import unittest

class Tests(unittest.TestCase):

    def setUp(self):
	main.app.testing = True
	self.app = main.app.test_client()

    def test_intsub(self):
	result =  self.app.get('/sub?A=3&B=5')
        self.assertEqual(b'-2.0\n', result.data)
        self.assertNotEqual(b'6.0\n',result.data)

    def test_floatsub(self):
        result =  self.app.get('/sub?A=3.3&B=3.3')
        self.assertEqual(b'0.0\n', result.data)

    def test_fracsub(self):
        result =  self.app.get('/sub?A=247747/3&B=3/3')
        self.assertEqual(b'82581.333\n', result.data)

    def test_negsub(self):
        result =  self.app.get('/sub?A=22929.29929&B=-3.3')
        self.assertEqual(b'22932.599\n', result.data)

if __name__ == '__main__':
    unittest.main()
