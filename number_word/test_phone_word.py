import unittest

from phone_word import PhoneWord

class PhoneWordTest(unittest.TestCase):
    def test(self):
        self.assertTrue(True)

    def test_num_with_one_or_zero(self):
        word_list = PhoneWord(1110000).get_word_list()
        self.assertFalse(word_list)

        word_list = PhoneWord(2304567).get_word_list()
        self.assertFalse(word_list)

        word_list = PhoneWord(2345671).get_word_list()
        self.assertFalse(word_list)

    def test_phone_word_attrs(self):
        pw = PhoneWord(6477336)

        self.assertTrue(pw.max_let_index[2] == 3)

    def test_thinner_word_presence(self):
        word_list = PhoneWord(8446637).get_word_list()

        print "word_list = {0}".format(word_list)

        self.assertIn('thinner', word_list, 'word list of 8446637 does not have "thinner"')

    def test_misseen_word_presence(self):
        word_list = PhoneWord(6477336).get_word_list()

        print "word_list = {0}".format(word_list)

        self.assertIn('misseen', word_list, 'word list of 6477336 does not have "misseen"')

    def test_flowers_word_presence(self):
        word_list = PhoneWord(3569377).get_word_list()

        print "word_list = {0}".format(word_list)

        self.assertIn('flowers', word_list, 'word list of 3569377 does not have "flowers"')

if __name__ == '__main__':
    unittest.main()

