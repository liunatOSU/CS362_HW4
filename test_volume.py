import unittest
from volume import volume

class TestVolume(unittest.TestCase):
  def test_volume(self):
    self.assertEqual(volume(4), 64)
  
  def test_volumeNeg(self):
    self.assertEqual(volume(-4), None)
    
  def test_volumeInvalid(self):
    self.assertEqual(volume("test"), None)

if __name__ == '__main__':
    unittest.main()