import main
import unittest


class TestOnlineCalculator(unittest.TestCase):
    """Testing features of online calculator"""

    def setUp(self):
        """Sets up the app for testing"""

        main.app.testing = True
        self.app = main.app.test_client()

    def test_empty_page(self):
        response_data = self.app.get('/')
        self.assertEqual(b'Usage;\n<Operation>?X=<Input1>&Y=<Input2>\n', response_data.data)

    def test_addition(self):
        # integer numbers testing
        response_data = self.app.get('/add?X=5&Y=3')
        self.assertEqual(b'8 \n', response_data.data)

        # rational numbers testing
        response_data = self.app.get('/add?X=5/3&Y=3/4')
        self.assertEqual(b'2.42 \n', response_data.data)

        # when both X and Y are both floats
        response_data = self.app.get('/add?X=5.4&Y=3.4678')
        self.assertEqual(b'8.87 \n', response_data.data)

        # when X is an int and Y is float
        response_data = self.app.get('/add?X=5&Y=-3.4678')
        self.assertEqual(b'1.53 \n', response_data.data)

        # when X is a float and Y is an int
        response_data = self.app.get('/add?X=-3.4678&Y=5')
        self.assertEqual(b'1.53 \n', response_data.data)

        # when X is a fraction and Y is an int
        response_data = self.app.get('/add?X=3/4&Y=5')
        self.assertEqual(b'5.75 \n', response_data.data)

        # when X is an int and Y is a fraction
        response_data = self.app.get('/add?X=5&Y=3/4')
        self.assertEqual(b'5.75 \n', response_data.data)

        # corner cases testing
        # when X = x1/0 where x1 belongs to any integer
        response_data = self.app.get('/add?X=-5/0&Y=3/4')
        self.assertEqual(b"X's denominator shouldn't be zero! \n", response_data.data)

        # when Y = x1/0 where x1 belongs to any integer
        response_data = self.app.get('/add?X=-2&Y=4/0')
        self.assertEqual(b"Y's denominator shouldn't be zero! \n", response_data.data)

        # when X is a non-number type
        response_data = self.app.get('/add?X=x1&B=zingo')
        self.assertEqual(b"X's value should be a number (includes fraction, float, integer). \n", response_data.data)

        # when Y is a non-number type
        response_data = self.app.get('/add?X=1&Y=y1')
        self.assertEqual(b"Y's value should be a number (includes fraction, float, integer). \n", response_data.data)

    def test_subtraction(self):
        """Tests page with /sub route, testing subtraction feature of the calculator,
        right now all types of numbers being tested"""

        # integer numbers testing
        response_data = self.app.get('/sub?X=5&Y=3')
        self.assertEqual(b'2 \n', response_data.data)

        # rational numbers testing
        response_data = self.app.get('/sub?X=5/3&Y=3/4')
        self.assertEqual(b'0.92 \n', response_data.data)

        # when both X and Y are both floats
        response_data = self.app.get('/sub?X=5.4&Y=3.4678')
        self.assertEqual(b'1.93 \n', response_data.data)

        # when X is an int and Y is float
        response_data = self.app.get('/sub?X=5&Y=-3.4678')
        self.assertEqual(b'8.47 \n', response_data.data)

        # when X is a float and Y is an int
        response_data = self.app.get('/sub?X=-3.4678&Y=5')
        self.assertEqual(b'-8.47 \n', response_data.data)

        # when X is a fraction and Y is an int
        response_data = self.app.get('/sub?X=3/4&Y=5')
        self.assertEqual(b'-4.25 \n', response_data.data)

        # when X is an int and Y is a fraction
        response_data = self.app.get('/sub?X=5&Y=3/4')
        self.assertEqual(b'4.25 \n', response_data.data)

        # corner cases testing
        # when X = x1/0 where x1 belongs to any integer
        response_data = self.app.get('/sub?X=-5/0&Y=3/4')
        self.assertEqual(b"X's denominator shouldn't be zero! \n", response_data.data)

        # when Y = x1/0 where x1 belongs to any integer
        response_data = self.app.get('/sub?X=-2&Y=4/0')
        self.assertEqual(b"Y's denominator shouldn't be zero! \n", response_data.data)

        # when X is a non-number type
        response_data = self.app.get('/sub?X=x1&Y=zingo')
        self.assertEqual(b"X's value should be a number (includes fraction, float, integer). \n", response_data.data)

        # when Y is a non-number type
        response_data = self.app.get('/sub?X=1&Y=y1')
        self.assertEqual(b"Y's value should be a number (includes fraction, float, integer). \n", response_data.data)

    def test_multiplication(self):
        """Tests page with /mul route, testing multiplication feature of the calculator,
        right now all types of numbers being tested"""

        # integer numbers testing
        response_data = self.app.get('/mul?X=5&Y=3')
        self.assertEqual(b'15 \n', response_data.data)

        # rational numbers testing
        response_data = self.app.get('/mul?X=5/3&Y=3/4')
        self.assertEqual(b'1.25 \n', response_data.data)

        # when both X and Y are both floats
        response_data = self.app.get('/mul?X=5.4&Y=3.4678')
        self.assertEqual(b'18.73 \n', response_data.data)

        # when X is an int and Y is float
        response_data = self.app.get('/mul?X=5&Y=-3.4678')
        self.assertEqual(b'-17.34 \n', response_data.data)

        # when X is a float and Y is an int
        response_data = self.app.get('/mul?X=-3.4678&Y=5')
        self.assertEqual(b'-17.34 \n', response_data.data)

        # when X is a fraction and Y is an int
        response_data = self.app.get('/mul?X=3/4&Y=5')
        self.assertEqual(b'3.75 \n', response_data.data)

        # when X is an int and Y is a fraction
        response_data = self.app.get('/mul?X=5&Y=3/4')
        self.assertEqual(b'3.75 \n', response_data.data)

        # corner cases testing
        # when X = x1/0 where x1 belongs to any integer
        response_data = self.app.get('/mul?X=-5/0&Y=3/4')
        self.assertEqual(b"X's denominator shouldn't be zero! \n", response_data.data)

        # when Y = x1/0 where x1 belongs to any integer
        response_data = self.app.get('/mul?X=-2&Y=4/0')
        self.assertEqual(b"Y's denominator shouldn't be zero! \n", response_data.data)

        # when X is a non-number type
        response_data = self.app.get('/mul?X=x1&Y=zingo')
        self.assertEqual(b"X's value should be a number (includes fraction, float, integer). \n", response_data.data)

        # when B is a non-number type
        response_data = self.app.get('/mul?X=1&Y=y1')
        self.assertEqual(b"Y's value should be a number (includes fraction, float, integer). \n", response_data.data)

    def test_division(self):
        # printing integral value correctly
        response_data = self.app.get('/div?X=4&Y=2')
        self.assertEqual(b'2 \n', response_data.data)

        # integer numbers testing
        response_data = self.app.get('/div?X=5&Y=3')
        self.assertEqual(b'1.67 \n', response_data.data)

        # rational numbers testing
        response_data = self.app.get('/div?X=5/3&Y=3/4')
        self.assertEqual(b'2.22 \n', response_data.data)

        # when both X and Y are both floats
        response_data = self.app.get('/div?X=5.4&Y=3.4678')
        self.assertEqual(b'1.56 \n', response_data.data)

        # when X is an int and Y is float
        response_data = self.app.get('/div?X=5&Y=-3.4678')
        self.assertEqual(b'-1.44 \n', response_data.data)

        # when X is a float and Y is an int
        response_data = self.app.get('/div?X=-3.4678&Y=5')
        self.assertEqual(b'-0.69 \n', response_data.data)

        # when X is a fraction and Y is an int
        response_data = self.app.get('/div?X=3/4&Y=5')
        self.assertEqual(b'0.15 \n', response_data.data)

        # when X is an int and Y is a fraction
        response_data = self.app.get('/div?X=5&Y=3/4')
        self.assertEqual(b'6.67 \n', response_data.data)

        # corner cases testing
        # when X = x1/0 where x1 belongs to any integer
        response_data = self.app.get('/div?X=-5/0&Y=3/4')
        self.assertEqual(b"X's denominator shouldn't be zero! \n", response_data.data)

        # when Y = x1/0 where x1 belongs to any integer
        response_data = self.app.get('/div?X=-2&Y=4/0')
        self.assertEqual(b"Y's denominator shouldn't be zero! \n", response_data.data)

        # when X is a non-number type
        response_data = self.app.get('/div?X=x1&Y=zingo')
        self.assertEqual(b"X's value should be a number (includes fraction, float, integer). \n", response_data.data)

        # when Y is a non-number type
        response_data = self.app.get('/div?X=1&Y=y1')
        self.assertEqual(b"Y's value should be a number (includes fraction, float, integer). \n", response_data.data)

        # Extra case when Y is zero
        response_data = self.app.get('/div?X=1&Y=0')
        self.assertEqual(b"Y's value shouldn't be zero! \n", response_data.data)


if __name__ == '__main__':
    unittest.main()
