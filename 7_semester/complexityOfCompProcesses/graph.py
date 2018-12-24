from math import inf


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
    def _decrease_object_count(cls):
        cls.object_count -= 1

    @classmethod
    def _increase_object_visited(cls):
        cls.object_visited += 1

    @classmethod
    def _decrease_object_visited(cls):
        cls.object_visited -= 1

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
        if not self.is_visited:
            self.is_visited = True
            self._increase_object_visited()
