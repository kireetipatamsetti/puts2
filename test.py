import main
import unittest

class Tests(unittest.TestCase):
	
	def setUp(self):
		main.app.testing = True
		self.app = main.app.test_client()

	def test_intadd(self):
		result =  self.app.get('/div?A=5&B=1')
            	self.assertEqual(b'5.0\n', result.data)
            	self.assertNotEqual(b'6.0\n',result.data)

if __name__ == '__main__':
    unittest.main()
