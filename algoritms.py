from math import inf

from logic import Graph

g = Graph({'a': {'a': 0, 'b': 1, 'c': 100, 'd': 31, 'e': 8},
           'b': {'a': 0, 'b': 0, 'c': 5, 'd': 1, 'e': 1},
           'c': {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 34},
           'd': {'a': 0, 'b': 0, 'c': 1, 'd': 0, 'e': 0},
           'e': {'a': 0, 'b': 1, 'c': 5, 'd': 0, 'e': 0}
           })

g.analize()


def min_path(g, start, end=None):    # Алгоритм Дийкстры
    print('Путь из', f'{start}', f'{("в " + str(end)) if end else ""}:', end='')
    to_go = list(g)
    p_vector = [start for i in to_go]
    weights = dict(zip(to_go, [(lambda i: 0 if (i is start) else inf)(i) for i in to_go]))
    cur = start
    while to_go:
        cur_paths = [g[cur][i] for i in g[cur] if g[cur][i] and i in to_go and not i is cur]
        need_to_go1 = [i for i in g[cur] if i in to_go and g[cur][i] and (not i is cur)]
        if not need_to_go1:
            break
        for path in range(len(need_to_go1)):
            if weights[cur] + cur_paths[path] < weights[need_to_go1[path]]:
                weights[need_to_go1[path]] = weights[cur] + cur_paths[path]
                p_vector.append(need_to_go1[path])
        to_go.remove(cur)
        queue = [i for i in sorted(weights, key=weights.get) if i in to_go]
        if queue:
            cur = queue[0]
    print(p_vector)
    if end:
        return weights[end]
    else:
        return weights


print(min_path(g, 'a', 'c'))

# print(g.analize_res)
