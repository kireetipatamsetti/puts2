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
