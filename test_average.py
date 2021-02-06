import unittest
from average import average

class TestAverage(unittest.TestCase):
  def test_average(self):
    self.assertEqual(average([1, 1.5, 3, 4.5, 5]), 3)
  
  def test_averageEmpty(self):
    self.assertEqual(average([]), None)
    
  def test_averageInvalid(self):
    self.assertEqual(average(["test", "test1"]), None)

if __name__ == '__main__':
    unittest.main()