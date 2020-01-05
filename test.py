import main
import unittest

class Tests(unittest.TestCase):

    def setUp(self):
	main.app.testing = True
	self.app = main.app.test_client()

    def test_intmul(self):
	result =  self.app.get('/mul?A=3&B=5')
        self.assertEqual(b'15.0\n', result.data)
        self.assertNotEqual(b'6.0\n',result.data)

    def test_floatmul(self):
        result =  self.app.get('/mul?A=3.3&B=3.3')
        self.assertEqual(b'10.89\n', result.data)

    def test_fracmul(self):
        result =  self.app.get('/mul?A=247747/3&B=3/3')
        self.assertEqual(b'82582.333\n', result.data)

    def test_negmul(self):
        result =  self.app.get('/mul?A=22929.29929&B=-3.3')
        self.assertEqual(b'-75666.688\n', result.data)

if __name__ == '__main__':
    unittest.main()
