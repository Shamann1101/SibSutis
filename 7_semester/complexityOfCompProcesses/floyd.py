from graph import Graph


def floyd(weight_matrix):
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
    path_list = list()
    source = source_id
    while path_matrix[source][target_id]:
        print(path_matrix[source][target_id])
        path_list.append(path_matrix[source_id][target_id])
        source = path_matrix[source][target_id]
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
    print(wm, "\n", pm)

    print(find_path(pm, 0, 4))


if __name__ == '__main__':
    main()
