import main
import unittest

class Tests(unittest.TestCase):
	
	def setUp(self):
		main.app.testing = True
		self.app = main.app.test_client()

	def test_intadd(self):
		result =  self.app.get('/mul?A=2&B=5')
            	self.assertEqual(b'10\n', result.data)
            	self.assertNotEqual(b'6\n',result.data)

if __name__ == '__main__':
    unittest.main()
