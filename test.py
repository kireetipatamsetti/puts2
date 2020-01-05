import main
import unittest

class Tests(unittest.TestCase):
	
	def setUp(self):
		main.app.testing = True
		self.app = main.app.test_client()

	def test_intsub(self):
		result =  self.app.get('/sub?A=2&B=5')
            	self.assertEqual(b'-3\n', result.data)
            	self.assertNotEqual(b'6\n',result.data)

if __name__ == '__main__':
    unittest.main()
