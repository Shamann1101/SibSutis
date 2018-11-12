import argparse
from graph import Graph


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
        if args.print:
            print("=== Dijkstra's algorithm ===")
        path_list = {vertex_list[target_id]: 0}
        vertex_list[target_id].calculated_weight = 0
        while Graph.object_visited < Graph.object_count and len(path_list) > 0:
            nearest_graph = min(path_list, key=path_list.get)
            if args.print:
                print(nearest_graph)
            for neighbour in nearest_graph.neighbours:
                if vertex_list[neighbour].is_visited:
                    continue

                if args.print:
                    print("\tneighbour:", neighbour)
                calculated_weight = nearest_graph.calculated_weight + nearest_graph.neighbours[neighbour]
                if args.print:
                    print("\tcalculated_weight:", calculated_weight)

                if calculated_weight < vertex_list[neighbour].calculated_weight:
                    vertex_list[neighbour].calculated_weight = calculated_weight

                if vertex_list[neighbour] not in path_list:
                    path_list[vertex_list[neighbour]] = calculated_weight

            path_list.pop(nearest_graph)
            nearest_graph.set_visited()
            if args.print:
                print(nearest_graph, "set_visited\n")


def find_path(vertex_list, source_id, target_id, path=[]):
    msg = ""
    try:
        if Graph.object_visited < Graph.object_count:
            msg = "Need to execute `dijkstra` first"
            print(Graph.object_visited, Graph.object_count)
            raise RuntimeError
        if source_id < 0 or source_id > Graph.object_count:
            msg = "source_id is out os scope"
            raise ValueError()
        if target_id < 0 or target_id > Graph.object_count:
            msg = "target_id is out os scope"
            raise ValueError()
    except ValueError:
        print(msg)
    except RuntimeError:
        print(msg)
    else:
        if args.print:
            print("=== Path finding ===")
        if len(path) == 0:
            path.append(target_id)
        intended_vertex = vertex_list[target_id].neighbours.copy()
        for neighbour in vertex_list[target_id].neighbours:
            if vertex_list[neighbour].calculated_weight != vertex_list[target_id].calculated_weight - \
                    vertex_list[target_id].neighbours[neighbour]:
                intended_vertex.pop(neighbour)
        if args.print:
            print(intended_vertex)
        if len(intended_vertex) == 1:
            vertex = intended_vertex.popitem()
            path.append(vertex[0])
            return find_path(vertex_list, source_id, vertex[0], path)
        elif len(intended_vertex) > 1:
            new_path = []
            for vertex in intended_vertex:
                branch = list()
                branch.append(vertex)
                find_path(vertex_list, source_id, vertex, branch)
                new_path.append(branch)
            path.extend(new_path)
        return path


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

    source_vertex = int(args.source) if args.source and 0 <= args.source < Graph.object_count else 0
    target_vertex = int(args.target) if args.target and 0 <= args.target < Graph.object_count else 4

    dijkstra(vertex_list, source_vertex)

    for vertex in vertex_list:
        print(vertex, "weight:", vertex.calculated_weight)

    if args.target:
        path = find_path(vertex_list, source_vertex, target_vertex)
        print("Path:", path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Dijkstra’s algorithm')
    parser.add_argument('source', type=int, nargs='?', help='Source vertex')
    parser.add_argument('target', type=int, nargs='?', help='Target vertex')
    parser.add_argument('--print', action='store_true', help='Print log')
    args = parser.parse_args()

    main()
