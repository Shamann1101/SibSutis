import argparse
from math import inf

from graph import Graph


def ford(vertex_list, target_id):
    """
    Sets vertex weights based on Ford's algorithm
    :param vertex_list: array of Graph objects
    :param target_id: source id
    :return:
    """
    message = ""
    weight_list = [list() for _ in range(len(vertex_list))]
    weight_list_result = [inf] * len(vertex_list)
    weight_list_result[target_id] = 0

    stabilization = False
    iteration = 0

    while not stabilization:
        message += "iteration: " + str(iteration) + "\n"

        weight_list[iteration] = [list() for _ in range(len(vertex_list))]
        calculated_weight = weight_list_result.copy()

        for vertex in vertex_list:
            if int(vertex.title) == target_id:
                continue
            weight_list[iteration][int(vertex.title)] = [inf] * len(vertex_list)

            for i in range(len(weight_list_result)):
                weight = inf
                if vertex.neighbours.get(i):
                    weight = vertex.neighbours[i]
                elif i == int(vertex.title):
                    weight = 0
                weight_list[iteration][int(vertex.title)][i] = weight_list_result[i] + weight
                message += str(weight_list_result[i]) + " " + str(weight) + "\n"

            calculated_weight[int(vertex.title)] = min(weight_list[iteration][int(vertex.title)])
            message += "\n"

        if calculated_weight == weight_list_result:
            stabilization = True
        else:
            weight_list_result = calculated_weight
            iteration += 1

    for string in weight_list:
        message += str(string) + "\n"

    if args.print:
        print(message)

    return weight_list_result


def main():
    vertex_list = []
    for i in range(5):
        vertex_list.append(Graph(i))
    vertex_list[0].neighbours = {vertex_list[1].title: 25,
                                 vertex_list[2].title: 15,
                                 vertex_list[3].title: 7,
                                 vertex_list[4].title: 2}
    vertex_list[1].neighbours = {vertex_list[0].title: 25,
                                 vertex_list[2].title: 6}
    vertex_list[2].neighbours = {vertex_list[0].title: 15,
                                 vertex_list[1].title: 6,
                                 vertex_list[3].title: 4}
    vertex_list[3].neighbours = {vertex_list[0].title: 7,
                                 vertex_list[2].title: 4,
                                 vertex_list[4].title: 3}
    vertex_list[4].neighbours = {vertex_list[0].title: 2,
                                 vertex_list[3].title: 3}

    source_vertex = int(args.source) if args.source and 0 <= args.source < Graph.object_count else 0

    print(ford(vertex_list, source_vertex))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ford’s algorithm')
    parser.add_argument('source', type=int, nargs='?', help='Source vertex')
    parser.add_argument('--print', action='store_true', help='Print log')
    args = parser.parse_args()

    main()
