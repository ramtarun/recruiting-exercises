import unittest
from deliverr_code import *


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual([{'owd': {'apple': 1}}],
                         inventory_allocator({'apple': 1}, [{'name': 'owd', 'inventory': {'apple': 1}}]))

    def test_case_2(self):
        self.assertEqual([{ 'dm': { 'apple': 5 }}, { 'owd': { 'apple': 5 } }],
                         inventory_allocator({ 'apple': 10 },
                                             [{ 'name': 'owd', 'inventory': { 'apple': 5 } },
                                              { 'name': 'dm', 'inventory': { 'apple': 5 }}]))

    def test_case_3(self):
        self.assertEqual([],
                         inventory_allocator({ 'apple': 1 }, [{ 'name': 'owd', 'inventory': { 'apple': 0 } }]))

    def test_case_4(self):
        self.assertEqual([],
                         inventory_allocator({ 'apple': 2 }, [{ 'name': 'owd', 'inventory': { 'apple': 1 } }]))


if __name__ == '__main__':
    unittest.main()
