"""Analyses subway data file and stores three dictionaries:
1. connection info
2. name-to-id mappings
3. shortest path info."""
from sys import argv
from priority_queue import PriorityQueue
import pickle

transfer_time = 5

if __name__ == '__main__':
    filename = argv[1]

    with open(filename, 'r') as f:
        data = f.read()

    data = data.split('\n')

    station_data = []
    connection_data = []

    switch = False
    for line in data:
        if line == '':
            switch = True
        elif not switch:
            station_data.append(line.split())
        else:
            connection_data.append(line.split())

    id_to_name = {}
    name_to_ids = {}
    connections = {}

    for line in station_data:
        station_id, name, *args = line
        id_to_name[station_id] = name
        connections[station_id] = []
        if name not in name_to_ids:
            name_to_ids[name] = []
        name_to_ids[name].append(station_id)

    for line in connection_data:
        start, end, weight = line
        connections[start].append((end, int(weight)))

    for name in name_to_ids:
        id_list = name_to_ids[name]
        for x in id_list:
            for y in id_list:
                if x != y:
                    connections[x].append((y, transfer_time))

    with open(f"{argv[1]}.connections", 'wb') as f:
        pickle.dump(connections, f)

    with open(f"{argv[1]}.name_to_ids", 'wb') as f:
        pickle.dump(name_to_ids, f)


    def dijkstra(source):
        dist = {source: 0}
        pq = PriorityQueue(key=lambda edge: edge[1])
        pq.push((source, 0))
        for vertex in id_to_name:
            if vertex != source:
                dist[vertex] = float('inf')
        while pq:
            u = pq.pop()
            for v in connections[u[0]]:
                alt = dist[u[0]] + v[1]
                if alt < dist[v[0]]:
                    dist[v[0]] = alt
                    pq.push((v[0], alt))
        return dist


    answer_map = {}

    for name in name_to_ids:
        answer_map[name] = {}
        for destination in name_to_ids:
            answer_map[name][destination] = float('inf')

    for i, idx in enumerate(id_to_name):
        print(f"{i + 1} / {len(id_to_name)}: {id_to_name[idx]}")
        distances = dijkstra(idx)
        for idy in distances:
            namex = id_to_name[idx]
            namey = id_to_name[idy]
            if distances[idy] < answer_map[namex][namey]:
                answer_map[namex][namey] = distances[idy]

    print("complete!")
    with open(f"{argv[1]}.analysed", 'wb') as f:
        pickle.dump(answer_map, f)
