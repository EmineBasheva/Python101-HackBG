import unittest
from panda import Panda


class PandaTest(unittest.TestCase):

    def setUp(self):
        self.panda = Panda('pan', 'panda@panmail.com', 'male')

    def test_is_create_new_class_Panda(self):
        self.assertTrue(isinstance(self.panda, Panda))

    def test_name(self):
        self.assertEqual(self.panda.name(), 'pan')

    def test_email(self):
        self.assertEqual(self.panda.email(), 'panda@panmail.com')

    def test_not_valid_email(self):
        with self.assertRaises(Exception):
            panda = Panda('pan', 'pandapanmail.com', 'male')

    def test_gender(self):
        self.assertEqual(self.panda.gender(), 'male')

    def test_is_male(self):
        self.assertTrue(self.panda.isMale())

    def test_is_female(self):
        self.assertFalse(self.panda.isFemale())

    def test_str_dunder(self):
        self.assertEqual(str(self.panda), "pan_male")

    def test_two_diferent_pandas_are_equal(self):
        panda2 = Panda('puh', 'puuuh@mail.com', 'female')
        self.assertFalse(self.panda == panda2)

    def test_two_pandas(self):
        panda2 = Panda('pan', 'panda@panmail.com', 'male')
        self.assertTrue(self.panda == panda2)

    # def test_is_hashable(self):
    #   panda2 = Panda('puh', 'puuuh@mail.com', 'female')

    #   all_pandas = {}

    #   all_pandas[self.panda] = 1
    #   all_pandas[panda2] = 2

    #   answer = {pan_male: 1, puh_female: 2}
    #   print(all_pandas)
    #   print(answer)
    #   # self.assertEqual(all_pandas, answer)

if __name__ == '__main__':
    unittest.main()