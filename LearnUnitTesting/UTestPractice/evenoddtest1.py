import evenodd
import unittest

class KnownValues(unittest.TestCase):
    known_values = (
            (1, 'odd'),
            (2, 'even'),
            (3, 'odd'),
            (33, 'odd'),
            (52, 'even')
        )
    def test_check_known_values(self):
        '''should give  known result with known input'''
        for number, classification in self.known_values:
            answer = evenodd.determine(number)
            self.assertEqual(answer, classification)

class DetermineBadInput(unittest.TestCase):
    def test_not_int_input(self):
        '''non-int inputs should fail test'''
        self.assertRaises(evenodd.NotIntegerError, evenodd.determine, tree)




if __name__ == '__main__':
    unittest.main()