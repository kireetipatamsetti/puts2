import main
import unittest

class Tests(unittest.TestCase):

    def setUp(self):
	main.app.testing = True
	self.app = main.app.test_client()

    def test_intadd(self):
	result =  self.app.get('/add?A=2&B=5')
        self.assertEqual(b'7.0\n', result.data)
        self.assertNotEqual(b'6.0\n',result.data)

    def test_floatadd(self):
        result =  self.app.get('/add?A=2.3&B=3.3')
        self.assertEqual(b'5.6\n', result.data)

    def test_fracadd(self):
        result =  self.app.get('/add?A=2/3&B=3/3')
        self.assertEqual(b'1.667\n', result.data)

    def test_negadd(self):
        result =  self.app.get('/add?A=2.3&B=-3.3')
        self.assertEqual(b'-1.0\n', result.data)

if __name__ == '__main__':
    unittest.main()
