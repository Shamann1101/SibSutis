from collections import defaultdict


class Heap:
    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    @staticmethod
    def new_min_heap_node(v, dist) -> list:
        return [v, dist]

    def swap_min_heap_node(self, a, b):
        self.array[a], self.array[b] = self.array[b], self.array[a]

    def min_heapify(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if (left < self.size and
                self.array[left][1] < self.array[smallest][1]):
            smallest = left

        if (right < self.size and
                self.array[right][1] < self.array[smallest][1]):
            smallest = right

        if smallest != idx:
            self.pos[self.array[smallest][0]] = idx
            self.pos[self.array[idx][0]] = smallest

            self.swap_min_heap_node(smallest, idx)

            self.min_heapify(smallest)

    def extract_min(self):
        if self.is_empty():
            return

        root = self.array[0]

        last_node = self.array[self.size - 1]
        self.array[0] = last_node

        self.pos[last_node[0]] = 0
        self.pos[root[0]] = self.size - 1

        self.size -= 1
        self.min_heapify(0)

        return root

    def is_empty(self) -> bool:
        return self.size == 0

    def decrease_key(self, v, dist):
        i = self.pos[v]

        self.array[i][1] = dist

        while (i > 0 and
               self.array[i][1] < self.array[(i - 1) // 2][1]):
            self.pos[self.array[i][0]] = (i - 1) // 2
            self.pos[self.array[(i - 1) // 2][0]] = i
            self.swap_min_heap_node(i, (i - 1) // 2)

            i = (i - 1) // 2

    def is_in_min_heap(self, v) -> bool:
        return self.pos[v] < self.size


def print_arr(dist: list, n: int):
    print("Vertex\tDistance from source")
    for i in range(n):
        print("%d\t\t%d" % (i, dist[i]))


class Graph:
    def __init__(self, height: int):
        self._height = height
        self.graph = defaultdict(list)

    @property
    def height(self) -> int:
        return self._height

    def add_edge(self, src: int, dest: int, weight: int):
        self.graph[src].insert(0, [dest, weight])
        self.graph[dest].insert(0, [src, weight])

    def dijkstra(self, src):
        v = self.height
        dist = []

        min_heap = Heap()

        for _v in range(v):
            dist.append(1e7)
            min_heap.array.append(min_heap.new_min_heap_node(_v, dist[_v]))
            min_heap.pos.append(_v)

        min_heap.pos[src] = src
        dist[src] = 0
        min_heap.decrease_key(src, dist[src])

        min_heap.size = v

        while not min_heap.is_empty():
            new_heap_node = min_heap.extract_min()
            u = new_heap_node[0]

            for p_crawl in self.graph[u]:

                _v = p_crawl[0]

                if (min_heap.is_in_min_heap(_v) and
                        dist[u] != 1e7 and
                        p_crawl[1] + dist[u] < dist[_v]):
                    dist[_v] = p_crawl[1] + dist[u]

                    min_heap.decrease_key(_v, dist[_v])

        print_arr(dist, v)


def _main():
    graph = Graph(9)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 7, 8)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 7, 11)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 8, 2)
    graph.add_edge(2, 5, 4)
    graph.add_edge(3, 4, 9)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(6, 8, 6)
    graph.add_edge(7, 8, 7)
    graph.dijkstra(0)


if __name__ == '__main__':
    _main()
