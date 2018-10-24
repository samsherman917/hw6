import re
import unittest

def sumNums(fileName):
    file = open(fileName, 'r')
    file = file.read()
    x = re.findall("(?<!\d|-)\d+(?!\d|-)", file)
    x = list(map(int, x))
    sum = 0
    for n in x:
        sum = sum + n

    return sum
 
def countWord(fileName, word):
    file = open(fileName, 'r')
    file = file.read()
    words = re.findall('(?i)' + str(word) + '(?!\w+)', file)

    return len(words)

def listURLs(fileName):
    file = open(fileName, 'r')
    file = file.read()
    urls = re.findall("\S+\.{1}\S+\.{1}\w+", file)

    return urls


class TestHW6(unittest.TestCase):
    """ Class to test this homework """

    def test_sumNums1(self):
        """ test sumNums on the first file """
        self.assertEqual(sumNums("regex_sum_42.txt"), 445833)

    def test_sumNums2(self):
        """ test sumNums on the second file """
        self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)

    def test_countWord(self):
        """ test count word on the first file """
        self.assertEqual(countWord("regex_sum_42.txt", "computer"),21)

    def test_listURLs(self):
        """ test list URLs on the first file """
        self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)

# run the tests
unittest.main(verbosity=2)
