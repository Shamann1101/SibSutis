from math import inf
# from random import randint


class Graph:
    object_count = 0
    object_visited = 0

    @classmethod
    def get_object_count(cls):
        return cls.object_count

    @classmethod
    def get_object_visited(cls):
        return cls.object_visited

    @classmethod
    def _increase_object_count(cls):
        cls.object_count += 1

    @classmethod
    def _decrease_object_visited(cls):
        cls.object_visited -= 1

    @classmethod
    def _decrease_object_count(cls):
        cls.object_count -= 1

    def __init__(self, title):
        self.title = title
        self.neighbours = []
        self.calculated_weight = inf
        self.is_visited = False
        self._increase_object_count()

    def __str__(self):
        return "Title: " + str(self.title)

    def __del__(self):
        self._decrease_object_count()
        if self.is_visited:
            self._decrease_object_visited()

    @property
    def neighbours(self):
        # print("Getter")
        return self._neighbours

    @neighbours.setter
    def neighbours(self, value):
        # print("Setter")
        self._neighbours = value

    def set_visited(self):
        self.is_visited = True
        self._decrease_object_visited()


def dijkstra(vertex_list, target_id):
    """
    Sets vertex weights by easiest way based on Dijkstra's algorithm
    :param vertex_list: array of Graph objects
    :param target_id: source id
    :return:
    """
    try:
        if target_id < 0 or target_id > Graph.object_count:
            raise ValueError
    except ValueError:
        print("Target id out os scope")
    else:
        path_list = {vertex_list[target_id]: 0}
        vertex_list[target_id].calculated_weight = 0
        while Graph.object_visited < Graph.object_count and len(path_list) > 0:
            nearest_graph = min(path_list, key=path_list.get)
            for neighbour in nearest_graph.neighbours:
                if vertex_list[neighbour].is_visited:
                    continue

                print("neighbour:", neighbour)
                calculated_weight = nearest_graph.calculated_weight + nearest_graph.neighbours[neighbour]
                print("calculated_weight:", calculated_weight)

                if calculated_weight < vertex_list[neighbour].calculated_weight:
                    vertex_list[neighbour].calculated_weight = calculated_weight

                if vertex_list[neighbour] not in path_list:
                    path_list[vertex_list[neighbour]] = calculated_weight

            path_list.pop(nearest_graph)
            nearest_graph.set_visited()


def main():
    vertex_list = []
    for i in range(6):
        vertex_list.append(Graph(i))
    vertex_list[0].neighbours = {vertex_list[1].title: 7,
                                 vertex_list[2].title: 9,
                                 vertex_list[5].title: 14}
    vertex_list[1].neighbours = {vertex_list[0].title: 7,
                                 vertex_list[2].title: 10,
                                 vertex_list[3].title: 15}
    vertex_list[2].neighbours = {vertex_list[0].title: 9,
                                 vertex_list[1].title: 10,
                                 vertex_list[3].title: 11,
                                 vertex_list[5].title: 2}
    vertex_list[3].neighbours = {vertex_list[1].title: 15,
                                 vertex_list[2].title: 11,
                                 vertex_list[4].title: 6}
    vertex_list[4].neighbours = {vertex_list[3].title: 6,
                                 vertex_list[5].title: 9}
    vertex_list[5].neighbours = {vertex_list[0].title: 14,
                                 vertex_list[2].title: 2,
                                 vertex_list[4].title: 9}

    dijkstra(vertex_list, 0)

    for vertex in vertex_list:
        print(vertex, "weight:", vertex.calculated_weight)


if __name__ == '__main__':
    main()
