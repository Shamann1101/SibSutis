from math import inf


class Graph:
    _object_count = 0
    _object_visited = 0

    @classmethod
    @property
    def object_count(cls) -> int:
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
        self._is_visited = False
        self._increase_object_count()

    def __str__(self):
        return "Title: " + str(self.title)

    def __repr__(self):
        return "Title: " + str(self.title)

    def __del__(self):
        self._decrease_object_count()
        if self._is_visited:
            self._decrease_object_visited()

    @property
    def neighbours(self) -> list:
        return self._neighbours

    @neighbours.setter
    def neighbours(self, value: list):
        self._neighbours = value

    @property
    def is_visited(self) -> bool:
        return self._is_visited

    def set_visited(self):
        if not self._is_visited:
            self._is_visited = True
            self._increase_object_visited()

    @classmethod
    def find_path(cls, vertex_list: list, source_id: int, target_id: int, _print: bool = False, path: list = []) -> list:
        if cls._object_visited < cls._object_count:
            msg = "All vertices must be visited\n"
            msg += f"visited: {cls._object_visited} count: {cls._object_count}"
            raise RuntimeError(msg)
        if source_id < 0 or source_id > cls._object_count:
            raise ValueError("source_id is out os scope")
        if target_id < 0 or target_id > cls._object_count:
            raise ValueError("source_id is out os scope")

        if _print:
            print("=== Path finding ===")
        if len(path) == 0:
            path.append(target_id)
        intended_vertex = vertex_list[target_id].neighbours.copy()
        for neighbour in vertex_list[target_id].neighbours:
            if vertex_list[neighbour].calculated_weight != vertex_list[target_id].calculated_weight - \
                    vertex_list[target_id].neighbours[neighbour]:
                intended_vertex.pop(neighbour)
        if _print:
            print(intended_vertex)
        if len(intended_vertex) == 1:
            vertex = intended_vertex.popitem()
            path.append(vertex[0])
            return cls.find_path(vertex_list, source_id, vertex[0], _print, path)
        elif len(intended_vertex) > 1:
            new_path = []
            for vertex in intended_vertex:
                branch = list()
                branch.append(vertex)
                cls.find_path(vertex_list, source_id, vertex, _print, branch)  # FIXME
                new_path.append(branch)
            path.extend(new_path)
        return path
