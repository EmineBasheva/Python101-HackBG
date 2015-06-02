import queue
from panda import Panda
import json


class PandaSocialNetwork:

    def __init__(self):
        self.all_pandas = {}

    def add_panda(self, panda):
        if panda in self.all_pandas:
            raise Exception("PandaAlreadyThere")

        self.all_pandas[panda] = []

    def has_panda(self, panda):
        return panda in self.all_pandas

    def are_friends(self, panda1, panda2):
        return panda2 in self.all_pandas[panda1] and panda1 in self.all_pandas[panda2]

    def make_friends(self, panda1, panda2):
        if panda1 not in self.all_pandas:
            self.add_panda(panda1)

        if panda2 not in self.all_pandas:
            self.add_panda(panda2)

        if self.are_friends(panda1, panda2):
            raise Exception("PandasAlreadyFriends")

        self.all_pandas[panda1].append(panda2)
        self.all_pandas[panda2].append(panda1)

    def friends_of(self, panda):
        if panda in self.all_pandas:
            return self.all_pandas[panda]
        return False

    def bfs(self, panda1, panda2):
        que = []
        que.append([panda1])

        while que:
            path = que.pop(0)
            node = path[-1]

            if node == panda2:
                return path
            for neight in self.all_pandas.get(node, []):
                new_path = list(path)
                new_path.append(neight)
                que.append(new_path)

    def connection_level(self, panda1, panda2):
        return len(self.bfs(panda1, panda2)) - 1

    def put_in_queue(self, queue, items):
        for i in range(len(items)):
            queue.put(items[i])


    def are_connected(self, panda1, panda2):
        # return connection_level(panda1, panda2) > 0
        to_check_are_friends = queue.Queue()
        self.put_in_queue(to_check_are_friends, self.all_pandas[panda1])
        # to_check_are_friends = friends_of(panda1)
        passed = [panda1]

        while not to_check_are_friends.empty():
            item = to_check_are_friends.get()

            if item == panda2:
                return True
            if item not in passed:
                passed.append(item)
                self.put_in_queue(to_check_are_friends, self.all_pandas[item])
        return False

    def how_many_gender_in_network(self, level, the_panda, gender):
        result = {}

        for panda in self.all_pandas:
            result[panda] = {}
            for other_panda in self.all_pandas:
                if panda != other_panda:
                    result[panda][other_panda] = self.connection_level(panda, other_panda)


        on_level = []
        for panda in result[the_panda]:
            if result[the_panda][panda] == level and panda.gender() == gender:
                on_level.append(panda)

        return len(on_level)

    def save(self, file_name):
        with open(file_name, 'w') as the_file:
            result = {}

            for panda in self.all_pandas:
                key = panda.name()
                result[key] = [] # self.all_pandas[panda]
                for friend in self.all_pandas[panda]:
                    attr_friend = friend.name()
                    result[key].append(attr_friend)

            # print(result)
            content = json.dumps(result)
            the_file.write(content)

    def load(self, file_name):
        with open(file_name, 'r') as the_file:
            content = json.loads(the_file.read())
            result = {}
            # for key in content:
            #     key = eval(key[1:][:-1])
                # print("---" + key)

            return content

