from graph import Graph


def bfs(vertex_list: list, target_id: int) -> list:
    if len(vertex_list) == 0 or target_id < 0 or target_id > vertex_list[0].object_count:
        raise ValueError

    queue = vertex_list[target_id].neighbours
    visited = [target_id]

    while queue:
        vertex = queue.pop(0)
        # print('vertex', vertex)
        if vertex.is_visited:
            continue

        queue.extend(vertex.neighbours)
        visited.append(vertex.title)
        vertex.set_visited()

    return visited


def _main():
    print("Following is the Breadth-First Search")

    vertex_list = []
    for i in range(6):
        vertex_list.append(Graph(i))
    vertex_list[0].neighbours = [vertex_list[1],
                                 vertex_list[2]]
    vertex_list[1].neighbours = [vertex_list[5]]
    vertex_list[2].neighbours = [vertex_list[3],
                                 vertex_list[4]]
    vertex_list[3].neighbours = [vertex_list[5]]

    b = bfs(vertex_list, 0)
    print(b)


if __name__ == '__main__':
    _main()
