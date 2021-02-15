import unittest
from check_pwd import check_pwd

class TestCase(unittest.TestCase):
  def test1(self):
    input = '1'
    expected = False
    self.assertEqual(check_pwd(input), expected)

  def test2(self):
    input = ""
    expected = False
    self.assertEqual(check_pwd(input), expected)

  def test3(self):
    input = "11111"
    expected = False 
    self.assertEqual(check_pwd(input), expected)

  def test4(self):
    input = "12121212121212121212121212qweqweqweqwe!@#!@#!@"
    expected = False 
    self.assertEqual(check_pwd(input), expected)

  def test5(self):
    input = "77777777777777777"
    expected = False 
    self.assertEqual(check_pwd(input), expected)
  
if __name__ == '__main__':
  unittest.main()