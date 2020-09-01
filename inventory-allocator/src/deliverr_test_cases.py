import unittest
from deliverr_code import inventory_allocator

expected_output = []
actual_output = []
outputs_set = False


def format_output(output, output_type='expected'):
    global expected_output, actual_output, outputs_set
    if output_type == 'expected':
        expected_output = output
    else:
        actual_output = output
        outputs_set = not outputs_set
    if outputs_set:
        for i in expected_output:
            if i not in actual_output:
                return False
        return True


class MyTestCase(unittest.TestCase):
    # Order can be shipped using one warehouse
    def test_case_1(self):
        self.assertEqual(format_output([{'owd': {'apple': 1}}]),
                         format_output(inventory_allocator({'apple': 1}, [{'name': 'owd', 'inventory': {'apple': 1}}])),
                         'actual')

    # Order can be shipped using multiple warehouses
    def test_case_2(self):
        self.assertEqual(format_output([{'dm': {'apple': 5}}, {'owd': {'apple': 5}}]),
                         format_output(inventory_allocator({'apple': 10},
                                                           [{'name': 'owd', 'inventory': {'apple': 5}},
                                                            {'name': 'dm', 'inventory': {'apple': 5}}])),
                         'actual')

    # Order cannot be shipped because there is no inventory
    def test_case_3(self):
        self.assertEqual(format_output([]),
                         format_output(inventory_allocator({'apple': 1}, [{'name': 'owd', 'inventory': {'apple': 0}}])),
                         'actual')

    # Order cannot be shipped because there is not enough inventory
    def test_case_4(self):
        self.assertEqual(format_output([]),
                         format_output(inventory_allocator({'apple': 2}, [{'name': 'owd', 'inventory': {'apple': 1}}])),
                         'actual')

    # Order with different items can be shipped using multiple warehouses
    def test_case_5(self):
        self.assertEqual(format_output([{'owd': {'apple': 1}}, {'qwe': {'oranges': 4}}]),
                         format_output(inventory_allocator({'apple': 1, 'oranges': 4},
                                                           [{'name': 'owd', 'inventory': {'apple': 1}},
                                                            {'name': 'qwe', 'inventory': {'oranges': 4}}])),
                         'actual')

    # Order with different items can be shipped across multiple warehouses when there is a shortage in inventory
    def test_case_6(self):
        self.assertEqual(format_output([{'owd': {'apple': 1, 'oranges': 2}}, {'qwe': {'oranges': 2}}]),
                         format_output(inventory_allocator({'apple': 1, 'oranges': 4},
                                                           [{'name': 'owd', 'inventory': {'apple': 1, 'oranges': 2}},
                                                            {'name': 'qwe', 'inventory': {'oranges': 4}}])),
                         'actual')

    # Order cannot be shipped because inventory doesnt fulfill partial order, in this case bananas order isn't fulfilled
    def test_case_7(self):
        self.assertEqual(format_output([]),
                         format_output(inventory_allocator({'apple': 1, 'oranges': 4, 'bananas': 5},
                                                           [{'name': 'owd', 'inventory': {'apple': 1, 'oranges': 2}},
                                                            {'name': 'qwe', 'inventory': {'oranges': 4}}])),
                         'actual')

    # Order can be shipped with fewer inventories leaving out expensive inventories thereby saving cost
    def test_case_8(self):
        self.assertEqual(format_output([{'owd': {'apple': 1, 'oranges': 2}}, {'wer': {'oranges': 2, 'bananas': 5}}]),
                         format_output(inventory_allocator({'apple': 1, 'oranges': 4, 'bananas': 5},
                                                           [{'name': 'owd', 'inventory': {'apple': 1, 'oranges': 2}},
                                                            {'name': 'wer', 'inventory': {'oranges': 2, 'bananas': 5}},
                                                            {'name': 'qwe', 'inventory': {'oranges': 4}}])),
                         'actual')


if __name__ == '__main__':
    unittest.main()
