from math import inf
from graph import Graph


def ford(vertex_list, target_id):
    weight_list = [list() for _ in range(len(vertex_list))]
    weight_list_result = [inf] * len(vertex_list)
    weight_list_result[target_id] = 0

    stabilization = False
    iteration = 0
    while not stabilization:
        print("iteration:", iteration)
        weight_list[iteration] = [list() for _ in range(len(vertex_list))]
        calculated_weight = [inf] * len(weight_list_result)
        for vertex in vertex_list:
            if int(vertex.title) == target_id:
                continue
            weight_list[iteration][int(vertex.title)] = [inf] * len(vertex_list)

            for i in range(len(weight_list_result)):
                w = inf
                if vertex.neighbours.get(i):
                    w = vertex.neighbours[i]
                elif i == int(vertex.title):
                    w = 0
                weight_list[iteration][int(vertex.title)][i] = weight_list_result[i] + w
                print(weight_list_result[i], w)

            calculated_weight[int(vertex.title)] = min(weight_list[iteration][int(vertex.title)])
            print()

        if calculated_weight == weight_list_result:
            stabilization = True
        else:
            weight_list_result = calculated_weight
            iteration += 1
    print(weight_list)
    print(weight_list_result)
    print(calculated_weight)


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

    ford(vertex_list, 0)


if __name__ == '__main__':
    main()
