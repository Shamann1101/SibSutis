import argparse

from graph import Graph


def floyd(weight_matrix):
    """
    Algorithm for finding shortest paths in a weighted graph with positive or negative edge weights
    :param weight_matrix:
    :return: two-dimensional list with weights, two-dimensional list with paths
    """
    error_msg = ""
    try:
        if len(weight_matrix) < 1:
            error_msg = "Weight matrix is empty"
            raise ValueError
        elif len(weight_matrix) != len(weight_matrix[0]):
            error_msg = "Weight matrix must be quadratic"
            raise ValueError
    except ValueError:
        print(error_msg)
    else:
        path_matrix = [0] * len(weight_matrix)
        for line in range(len(weight_matrix)):
            path_matrix[line] = [line] * len(weight_matrix)
            path_matrix[line][line] = None

        for k in range(len(weight_matrix)):
            for i in range(len(weight_matrix)):
                for j in range(len(weight_matrix)):
                    if weight_matrix[i][k] and weight_matrix[k][j] and i != j:
                        if weight_matrix[i][k] + weight_matrix[k][j] < weight_matrix[i][j] or weight_matrix[i][j] == 0:
                            weight_matrix[i][j] = weight_matrix[i][k] + weight_matrix[k][j]
                            path_matrix[i][j] = k

        return weight_matrix, path_matrix


def find_path(path_matrix, source_id, target_id):
    """
    Returns shortest way from source vertex to target vertex
    :param path_matrix:
    :param source_id:
    :param target_id:
    :return:
    """
    error_msg = ""
    try:
        if len(path_matrix) < 1:
            error_msg = "Path matrix is empty"
            raise ValueError
        elif len(path_matrix) != len(path_matrix[0]):
            error_msg = "Path matrix must be quadratic"
            raise ValueError
    except ValueError:
        print(error_msg)
    else:
        target = target_id
        path_list = [target]
        while path_matrix[source_id][target] is not None:
            path_list.append(path_matrix[source_id][target])
            target = path_matrix[source_id][target]
        return path_list


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

    weight_matrix_initial = [0] * len(vertex_list)
    for line in range(len(weight_matrix_initial)):
        weight_matrix_initial[line] = [0] * len(vertex_list)
        for vertex in range(len(weight_matrix_initial[line])):
            value = vertex_list[line].neighbours.get(vertex)
            if value:
                weight_matrix_initial[line][vertex] = value

    wm, pm = floyd(weight_matrix_initial)
    if args.print:
        print("Weights matrix:")
        for line in wm:
            print(line)
        print()
        print("Path matrix:")
        for line in pm:
            print(line)
        print()

    source_vertex = int(args.source) if args.source and 0 <= args.source < Graph.object_count else 0
    target_vertex = int(args.target) if args.target and 0 <= args.target < Graph.object_count else 4

    path = find_path(pm, source_vertex, target_vertex)
    print("Path:", path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Floyd’s algorithm')
    parser.add_argument('source', type=int, nargs='?', help='Source vertex')
    parser.add_argument('target', type=int, nargs='?', help='Target vertex')
    parser.add_argument('--print', action='store_true', help='Print log')
    args = parser.parse_args()

    main()
