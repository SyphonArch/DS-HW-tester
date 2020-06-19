"""Checks the validity of shortest subway path."""
import pickle
from subway_analysis import transfer_time

subway_data = {}

for filename in ('subway.txt', 'merge.txt', 'oneway.txt'):
    with open(f"./subway_data/{filename}.connections", 'rb') as f:
        connections = pickle.load(f)
    with open(f"./subway_data/{filename}.name_to_ids", 'rb') as f:
        name_to_ids = pickle.load(f)
    with open(f"./subway_data/{filename}.analysed", 'rb') as f:
        answer_map = pickle.load(f)

    subway_data[filename] = [connections, name_to_ids, answer_map]


def check(arg, inp, out):
    arg = arg.split('/')[-1]
    connections, name_to_ids, answer_map = subway_data[arg]
    inp = inp.split('\n')
    out = out.split('\n')
    while inp[-1] != 'QUIT':
        inp.pop()
    inp.pop()

    try:
        for i, line in enumerate(inp):
            start, end = line.split()
            shortest_weight = answer_map[start][end]
            path = out[i * 2]
            weight = int(out[i * 2 + 1])

            if weight != shortest_weight or path_weight(path, name_to_ids, connections) != weight:
                return False
        return True
    except Exception as e:
        print(str(e) + "Check your output formatting!")
        return False


def path_weight(path, name_to_ids, connections):
    path = path.split()
    total_weight = 0
    for i, name in enumerate(path):
        if name[0] == '[' and name[-1] == ']':
            total_weight += transfer_time
            path[i] = name[1:-1]

    for i in range(1, len(path)):
        total_weight += edge_weight(path[i - 1], path[i], name_to_ids, connections)

    return total_weight


def edge_weight(name1, name2, name_to_ids, connections):
    ids1, ids2 = name_to_ids[name1], name_to_ids[name2]
    best_weight = float('inf')
    for id1 in ids1:
        for id2 in ids2:
            for connection in connections[id1]:
                if connection[0] == id2:
                    best_weight = min(best_weight, connection[1])
    return best_weight
