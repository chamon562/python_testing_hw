import unittest

from cars import Cars

class TestCars(unittest.TestCase):
    """Test for Employee class"""

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    def setUp(self):
        print('setUp')
        self.toyota = Cars('Toyota', 'Supra', 236000000000)
    
    def tearDown(self):
        print('tearDown\n')

    def test_fullcar(self):
        self.assertEqual(self.toyota.full_car, 'Toyota Supra')

if __name__ == '__main__':
    unittest.main()