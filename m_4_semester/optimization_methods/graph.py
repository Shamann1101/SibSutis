from math import inf


class Graph:
    _object_count = 0
    _object_visited = 0

    @classmethod
    @property
    def object_count(cls):
        return cls._object_count

    @classmethod
    @property
    def object_visited(cls):
        return cls._object_visited

    @classmethod
    def _increase_object_count(cls):
        cls._object_count += 1

    @classmethod
    def _decrease_object_count(cls):
        cls._object_count -= 1

    @classmethod
    def _increase_object_visited(cls):
        cls._object_visited += 1

    @classmethod
    def _decrease_object_visited(cls):
        cls._object_visited -= 1

    def __init__(self, title: str):
        self.title = title
        self._neighbours = []
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
    def neighbours(self) -> list:
        return self._neighbours

    @neighbours.setter
    def neighbours(self, value: list):
        self._neighbours = value

    def set_visited(self):
        if not self.is_visited:
            self.is_visited = True
            self._increase_object_visited()
