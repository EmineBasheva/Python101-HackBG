import unittest
from pandaSocialNetwork import PandaSocialNetwork
from panda import Panda
import queue
import json


class TestPandaSocialNetwork(unittest.TestCase):

    def setUp(self):
        self.network = PandaSocialNetwork()
        self.panda = Panda('pan', 'panda@panmail.com', 'male')

    def test_is_create_new_class_PandaSocialNetwork(self):
        self.assertTrue(isinstance(self.network, PandaSocialNetwork))

    def test_adding_pandas(self):
        self.network.add_panda(self.panda)
        self.assertEqual(self.network.all_pandas, {self.panda: []})

    def test_adding_same_panda(self):
        self.network.add_panda(self.panda)
        with self.assertRaises(Exception):
            self.network.add_panda(self.panda)

    def test_has_panda(self):
        self.network.add_panda(self.panda)
        self.assertTrue(self.network.has_panda(self.panda))

    def test_has_not_panda(self):
        self.assertFalse(self.network.has_panda(self.panda))

    def test_are_friends(self):
        panda2 = Panda('puh', 'puuuh@mail.com', 'female')
        self.network.add_panda(self.panda)
        self.network.add_panda(panda2)
        self.network.make_friends(self.panda, panda2)

        self.assertTrue(self.network.are_friends(self.panda, panda2))

    def test_make_frends(self):
        panda2 = Panda('puh', 'puuuh@mail.com', 'female')
        self.network.add_panda(self.panda)
        self.network.add_panda(panda2)
        self.network.make_friends(self.panda, panda2)

        self.assertEqual(self.network.all_pandas, {self.panda:[panda2], panda2: [self.panda]})

    def test_PandasAlreadyFriends(self):
        panda2 = Panda('puh', 'puuuh@mail.com', 'female')
        self.network.add_panda(self.panda)
        self.network.add_panda(panda2)
        self.network.make_friends(self.panda, panda2)

        with self.assertRaises(Exception):
            self.network.make_friends(self.panda, panda2)

    def test_make_friends_and_add_in_network(self):
        panda2 = Panda('puh', 'puuuh@mail.com', 'female')
        self.network.make_friends(self.panda, panda2)

        self.assertEqual(self.network.all_pandas, {self.panda:[panda2], panda2: [self.panda]})

    def test_friends_of_panda_not_in_network(self):
        self.assertFalse(self.network.friends_of(self.panda))

    def test_friends_of_panda(self):
        panda2 = Panda('puh', 'puuuh@mail.com', 'female')
        panda3 = Panda('pooh', 'puuuh@mail.com', 'female')
        self.network.make_friends(self.panda, panda2)
        self.network.make_friends(self.panda, panda3)

        self.assertEqual(self.network.friends_of(self.panda), [panda2, panda3])

    def test_put_in_queue(self):
        q = queue.Queue()
        elements = [1, 2, 3, 4]
        self.network.put_in_queue(q, elements)

        self.assertTrue(all(elements[i] == q.get() for i in range(len(elements))))


class TestMethodsWithGraphOfFriends(unittest.TestCase):

    def setUp(self):
        self.network = PandaSocialNetwork()
        self.pandaT = Panda('Tom', 'tom@pandamail.com', 'male')
        self.panda1 = Panda('1', '1@pandamail.com', 'female')
        self.panda2 = Panda('2', '2@pandamail.com', 'male')
        self.panda3 = Panda('3', '3@pandamail.com', 'female')
        self.panda4 = Panda('4', '4@pandamail.com', 'male')
        self.panda5 = Panda('5', '5@pandamail.com', 'female')
        self.panda6 = Panda('6', '6@pandamail.com', 'male')
        self.pandaA = Panda('Ana', 'ana@pandamail.com', 'female')

        self.network.make_friends(self.pandaT, self.panda1)
        self.network.make_friends(self.pandaT, self.panda2)
        self.network.make_friends(self.pandaT, self.panda3)
        self.network.make_friends(self.panda1, self.panda4)
        self.network.make_friends(self.panda3, self.panda5)
        self.network.make_friends(self.panda3, self.panda6)
        self.network.make_friends(self.panda4, self.pandaA)
        self.network.make_friends(self.panda1, self.panda3)
        self.network.make_friends(self.panda2, self.panda3)

    def test_bfs(self):
        answer = [self.pandaT, self.panda1, self.panda4, self.pandaA]
        self.assertEqual(self.network.bfs(self.pandaT, self.pandaA), answer)

    def test_connection_level_with_3(self):
        self.assertEqual(self.network.connection_level(self.pandaT, self.pandaA), 3)

    def test_connection_level_with_1(self):
        self.assertEqual(self.network.connection_level(self.pandaT, self.panda3), 1)

    def test_are_connected_with_True(self):
        self.assertTrue(self.network.are_connected(self.pandaT, self.pandaA))

    def test_are_connected_with_False(self):
        panda = Panda('puh', 'puuuh@mail.com', 'female')
        self.assertFalse(self.network.are_connected(self.panda3, panda))

    def test_how_many_gender_in_network_with_2_female_on_level_1(self):
        self.assertEqual(self.network.how_many_gender_in_network(1, self.pandaT, 'female'), 2)

    def test_how_many_gender_in_network_with_2_male_on_level_2(self):
        self.assertEqual(self.network.how_many_gender_in_network(2, self.pandaT, 'male'), 2)

    def test_how_many_gender_in_network_with_2_male_on_level_1(self):
        self.assertEqual(self.network.how_many_gender_in_network(1, self.panda1, 'male'), 2)

    def test_save(self):
        self.network.save('network1.txt')

        network_file = open('network1.txt', 'r')
        content = json.loads(network_file.read())
        print(type(content))

        # self.assertEqual(content, self.network)

        network_file.close()



if __name__ == '__main__':
    unittest.main()