import main
import unittest

class Tests(unittest.TestCase):

    def setUp(self):
	main.app.testing = True
	self.app = main.app.test_client()

    def test_intdiv(self):
	result =  self.app.get('/div?A=3&B=5')
        self.assertEqual(b'0.6\n', result.data)
        self.assertNotEqual(b'6.0\n',result.data)

    def test_floatdiv(self):
        result =  self.app.get('/div?A=3.3&B=3.3')
        self.assertEqual(b'1.0\n', result.data)

    def test_fracdiv(self):
        result =  self.app.get('/div?A=247747/3&B=3/3')
        self.assertEqual(b'82582.333\n', result.data)

    def test_negdiv(self):
        result =  self.app.get('/div?A=22929.29929&B=-3.3')
        self.assertEqual(b'-6948.273\n', result.data)

    def test_zerodivisionerror(self):
        result = self.app.get('/div?A=1/0&B=1')
        self.assertEqual(b'None', result.data)

if __name__ == '__main__':
    unittest.main()
