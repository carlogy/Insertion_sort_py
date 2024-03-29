import unittest
import random

from insertion_sort import insertion_sort

class TestInsertionSort(unittest.TestCase):

    def test_sorted_list(self):
        array = list(range(0, 10))
        self.assertListEqual(
            array,
            insertion_sort(array)
        )

    def test_reverse_list(self):
        array = list(range(10000, 0, -1))
        self.assertListEqual(
            sorted(array),
            insertion_sort(array)
        )

    def test_unsorted_list(self):
        array = list(range(0, 1000))
        random.shuffle(array)

        self.assertListEqual(
            sorted(array),
            insertion_sort(array)
        )

    def test_empty_list(self):
        array = []
        self.assertListEqual(
            array,
            insertion_sort(array)
        )

    def test_single_element_list(self):
        array = [42]
        self.assertListEqual(
            array,
            insertion_sort(array)
        )
