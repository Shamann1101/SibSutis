from graph import Graph


def get_edge_sorted(vertex_list: list) -> tuple:
    edge_dict = dict()
    for vertex in vertex_list:
        for neighbour in vertex.neighbours:
            if (vertex.title, neighbour) not in edge_dict and (neighbour, vertex.title) not in edge_dict:
                edge_dict[vertex.title, neighbour] = vertex.neighbours[neighbour]

    edge_dict_sorted = dict()
    edge_list_sorted = []
    while len(edge_dict):
        cheapest_edge = min(edge_dict, key=edge_dict.get)
        edge_dict_sorted[cheapest_edge] = edge_dict.pop(cheapest_edge)
        edge_list_sorted.append(cheapest_edge)

    return edge_dict_sorted, edge_list_sorted


def kruskal(vertex_list: list, edge_list_sorted: list) -> list:
    new_vertex_list = []
    connections = []
    for i in range(len(vertex_list)):
        new_vertex_list.append(Graph(i))
        connections.append(vertex_list[i].title)

    new_graph_edges = []
    edge_list = edge_list_sorted.copy()
    edge_list.reverse()
    while len(edge_list) and len(connections) > 1:
        # print("len:", len(connections))
        skip = False
        edge = edge_list.pop()
        first_vertex, second_vertex = edge
        if not len(new_graph_edges):
            new_graph_edges.append(edge)
            connections[first_vertex] = (first_vertex, second_vertex)
            connections[second_vertex] = connections[len(connections) - 1]
            connections.pop()
            continue

        for connection in connections:
            if type(connection) == tuple and first_vertex in connection and second_vertex in connection:
                skip = True
                break

        print("connections:", connections, "edge:", edge, "skip:", skip)
        print("new_graph_edges:", new_graph_edges)

        if skip:
            continue

        index = []
        for i in range(len(connections)):
            if (type(connections[i]) == int and
                (first_vertex == connections[i] or second_vertex == connections[i])) or \
                    (type(connections[i]) == tuple and
                     (first_vertex in connections[i] or second_vertex in connections[i])):
                index.append(i)

        a = []
        for i in index:
            if type(connections[i]) == int:
                a.append(connections[i])
            elif type(connections[i]) == tuple:
                a.extend(connections[i])

        new_graph_edges.append(edge)
        connections[index[0]] = tuple(set(a))
        connections.pop(index[len(index) - 1])

        # new_vertex_list[first_vertex].neighbours[second_vertex] = vertex_list[first_vertex].neighbours[second_vertex]
        # new_vertex_list[second_vertex].neighbours[first_vertex] = vertex_list[second_vertex].neighbours[first_vertex]

    # return new_vertex_list, new_graph_edges
    return new_graph_edges


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

    _, edge_list = get_edge_sorted(vertex_list)
    # print(edge_dict)
    print('edge_list', edge_list)
    print(kruskal(vertex_list, edge_list))


if __name__ == '__main__':
    main()
