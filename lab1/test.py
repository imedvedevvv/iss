import unittest

import forward_index
import inverted_index
import search_forward
import search_inverted


class TestForwardIndex(unittest.TestCase):
    def test_forward_index_many(self):
        text = 'Test test (some) OTHER-words'
        result = forward_index.forward_index(text)
        self.assertEqual(result, ['other', 'some', 'test', 'words'])

    def test_forward_index_one(self):
        text = 'Test'
        result = forward_index.forward_index(text)
        self.assertEqual(result, ['test'])

    def test_forward_index_none(self):
        text = ''
        result = forward_index.forward_index(text)
        self.assertEqual(result, [])


class TestInvertedIndex(unittest.TestCase):
    def test_inverted_index_many(self):
        text = 'Test test (some) OTHER-words'
        dict = {
            'some': ['file1']
        }
        inverted_index.inverted_index(text, dict, 'file2')
        self.assertDictEqual(dict, {
            'some': ['file1', 'file2'],
            'test': ['file2'],
            'other': ['file2'],
            'words': ['file2']
        })

    def test_inverted_index_one(self):
        text = 'Test'
        dict = {
            'some': ['file1']
        }
        inverted_index.inverted_index(text, dict, 'file2')
        self.assertEqual(dict, {
            'some': ['file1'],
            'test': ['file2']
        })

    def test_inverted_index_none(self):
        text = ''
        dict = {
            'some': ['file1']
        }
        inverted_index.inverted_index(text, dict, 'file2')
        self.assertEqual(dict, {
            'some': ['file1']
        })


class TestSearchForward(unittest.TestCase):
    def test_search_forward_present_many(self):
        index = {
            'file1': ['some', 'test', 'word'],
            'file2': ['test'],
        }
        result = search_forward.search_forward(index, 'test')
        self.assertEqual(result, ['file1', 'file2'])

    def test_search_forward_present_one(self):
        index = {
            'file1': ['some', 'test', 'word'],
            'file2': ['nottest'],
        }
        result = search_forward.search_forward(index, 'test')
        self.assertEqual(result, ['file1', ])

    def test_search_forward_absent(self):
        index = {
            'file1': ['some', 'nottest', 'word'],
            'file2': ['nottest'],
        }
        result = search_forward.search_forward(index, 'test')
        self.assertEqual(result, [])


class TestSearchInverted(unittest.TestCase):
    def test_search_inverted_present_many(self):
        index = {
            'test': ['file1', 'file3'],
            'nottest': ['file2'],
        }
        result = search_inverted.search_inverted(index, 'test')
        self.assertEqual(result, ['file1', 'file3'])
        
    def test_search_inverted_present_one(self):
        index = {
            'test': ['file1'],
            'nottest': ['file2'],
        }
        result = search_inverted.search_inverted(index, 'test')
        self.assertEqual(result, ['file1'])

    def test_search_inverted_absent(self):
        index = {
            'nottest': ['file2'],
        }
        result = search_inverted.search_inverted(index, 'test')
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
