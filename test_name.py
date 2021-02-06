import unittest
from name import name

class TestName(unittest.TestCase):
  def test_name(self):
    self.assertEqual(name("Nathan", "Liu"), "Nathan Liu")
  
  def test_nameEmpty(self):
    self.assertEqual(name("Nathan", ""), None)
    
  def test_nameInvalid(self):
    self.assertEqual(name(5, "test"), None)

if __name__ == '__main__':
    unittest.main()