
# 1-800-flowers
#
# mapping:
# 1 -> none
# 2 -> abc
# 3 -> def
# 4 -> ghi
# 5 -> jkl
# 6 -> mno
# 7 -> pqrs
# 8 -> tuv
# 9 -> wxyz
# 0 -> none
#
# Problem: Given a 7 digit phone number, find all the possible words that can be made from it.
# The letters correspond to the numbers on a standard phone.
#
# I'll give you:
# 7 digit number
# dictionary of words
# mapping
#
# You give me:
# A list of words in the dictionary that map to that 7 digit number

from collections import namedtuple

PositionDetails = namedtuple('PositionDetails', ['digit', 'letters'])

class PhoneWord(object):
    def __init__(self, number):
        if not str(number).isdigit():
            raise ValueError('num has non-digit chars')

        if not len(str(number)) == 7:
            raise ValueError('num does not have 7 digits')

        self.digit_list = [int(ch)
                           for ch in str(number)]

        self.digit_map = (
            (),                     (),                         ('a', 'b', 'c'),
            ('d', 'e', 'f'),        ('g', 'h', 'i'),            ('j', 'k', 'l'),
            ('m', 'n', 'o'),        ('p', 'q', 'r', 's'),       ('t', 'u', 'v'),

            ('w', 'x', 'y', 'z')
        )

        self.position_info = {pos: details
                              for pos, details in self.position_details()}

        self.max_let_index = [len(self.position_info[pos].letters) - 1
                              for pos in range(7)]

        self.word_dict_set = {word.lower()
                              for line in self.seven_letter_words()
                              for word in line.split()}

    def position_details(self):
        for pos in range(7):
            digit = self.digit_list[pos]
            letters = self.digit_map[digit]

            yield pos, PositionDetails(digit, letters)

    def seven_letter_words(self):
        with open("dictionary.txt") as f:
            yield f.read()

    def reset_tail(self, index_list, tail_start_pos):
        for pos in range(tail_start_pos, 7):
            index_list[pos] = 0

    def all_index_lists_generated(self, index_list):
        for pos in range(7):
            if index_list[pos] < self.max_let_index[pos]:
                return False

        return True

    def index_lists(self):
        index_list = [0, 0, 0, 0, 0, 0, 0]

        while True:
            yield index_list

            if self.all_index_lists_generated(index_list):
                # yielded all possible index lists
                return

            for digit_pos in reversed(range(7)):
                if index_list[digit_pos] < self.max_let_index[digit_pos]:
                    # more letters available for digit at digit_pos
                    self.reset_tail(index_list, digit_pos + 1)
                    index_list[digit_pos] += 1
                    break

    def get_letter(self, pos, let_ind):
        return self.position_info[pos].letters[let_ind]

    def index_list_word(self, index_list):
        ch_list = [self.get_letter(pos, let_ind)
                   for pos, let_ind in enumerate(index_list)]

        word = ''.join(ch_list)

        return word

    def get_word_list(self):
        if 0 in self.digit_list or 1 in self.digit_list:
            return []

        word_set = set([self.index_list_word(lst)
                        for lst in self.index_lists()
                        if self.index_list_word(lst) in self.word_dict_set
                        ])
        return word_set
