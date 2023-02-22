import argparse

from graph import Graph


def dijkstra(vertex_list: list, target_id: int):
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
        exit(1)

    scope = {}
    if args.print:
        print("=== Dijkstra's algorithm ===")
    path_list = {vertex_list[target_id]: 0}
    vertex_list[target_id].calculated_weight = 0
    while Graph.object_visited < Graph.object_count and len(path_list) > 0:
        nearest_graph = min(path_list, key=path_list.get)
        scope[nearest_graph] = {}
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
            scope[nearest_graph][neighbour] = calculated_weight

            if calculated_weight < vertex_list[neighbour].calculated_weight:
                vertex_list[neighbour].calculated_weight = calculated_weight

            if vertex_list[neighbour] not in path_list:
                path_list[vertex_list[neighbour]] = calculated_weight
        scope[nearest_graph][nearest_graph.title] = "-"
        # TODO: Edit table print
        print("{}\t {}\t| {}\t| {}\t| {}".format(nearest_graph,
                                                 scope[nearest_graph].setdefault(1, None),
                                                 scope[nearest_graph].setdefault(2, None),
                                                 scope[nearest_graph].setdefault(3, None),
                                                 scope[nearest_graph].setdefault(4, None)
                                                 ))

        path_list.pop(nearest_graph)
        nearest_graph.set_visited()
        if args.print:
            print(nearest_graph, "set_visited\n")


def main():
    vertex_list = []
    for i in range(5):
        vertex_list.append(Graph(i))
    vertex_list[0].neighbours = {vertex_list[1].title: 25,
                                 vertex_list[2].title: 15,
                                 vertex_list[3].title: 7,
                                 vertex_list[4].title: 2}
    vertex_list[1].neighbours = {vertex_list[0].title: 25,
                                 vertex_list[2].title: 8}
    vertex_list[2].neighbours = {vertex_list[0].title: 15,
                                 vertex_list[1].title: 8,
                                 vertex_list[3].title: 4}
    vertex_list[3].neighbours = {vertex_list[0].title: 7,
                                 vertex_list[2].title: 4,
                                 vertex_list[4].title: 3}
    vertex_list[4].neighbours = {vertex_list[0].title: 2,
                                 vertex_list[3].title: 3}

    source_vertex = int(args.source) if args.source and 0 <= args.source < Graph.object_count else 0
    target_vertex = int(args.target) if args.target and 0 <= args.target < Graph.object_count else 4

    dijkstra(vertex_list, source_vertex)

    for vertex in vertex_list:
        print(vertex, "weight:", vertex.calculated_weight)

    if args.target:
        path = Graph.find_path(vertex_list, source_vertex, target_vertex, True if args.print else False)
        path.reverse()
        print("Path:", path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Dijkstra’s algorithm')
    parser.add_argument('source', type=int, nargs='?', help='Source vertex')
    parser.add_argument('target', type=int, nargs='?', help='Target vertex')
    parser.add_argument('--print', action='store_true', help='Print log')
    args = parser.parse_args()

    main()
