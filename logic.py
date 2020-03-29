import traceback
class Graph():
    analized = ''
    loop = False
    isolate = False
    vector = False
    isolates = []
    loops = []
    analize_res = ''
    g_map = []
    points =[]

    def __iter__(self):
        return self.g_map.__iter__()

    def keys(self):
        return self.g_map.keys()

    def __getitem__(self, item):
        return self.g_map[item]

    def __setitem__(self, key,  value):
        self.g_map[key] = value

    def __len__(self):
        return len(self.g)

    def __init__(self, g):
        self.points = []
        self.points = list(g)
        if type(g) is list:
            self.g = g
            self.g_map = []
            for i in range(len(self.g)):
                self.g_map.append([])
                for j in range(len(self.g)):
                    if j in g[i]:
                        self.g_map[i].append(j)
                    else:
                        self.g_map[i].append(None)
        else:
            self.g = g
            self.g_map = dict()
            for i in self.points:
                self.g_map[i] = dict()
                for j in self.points:
                    if j in self.g[i]:
                        self.g_map[i][j] = g[i][j]
                    else:
                        self.g_map[i][j] = None
            self.points = list(self.g_map)
            #print(self.g_map)

    def analize(self, g=None):
        self.loop = False
        self.isolate = False
        self.vector = False
        self.loops = []
        self.isolates = []
        self.points =list(self.g_map)
        points = self.points
        try:
            if not g:
                res = 'Получен '
                g = self.g_map
                self.points = list(g)
                points = self.points

            if type(g) is list:
                for i in range(len(g)):
                    if not len(g[i]) and not any([i in v for v in g]):  # Поиск изолированных вершин
                        self.isolate = True
                        self.isolates.append(i)
                    if not all(i in g[v] for v in range(len(g)) if v in g[i]):  # Является ли граф ориентированным
                        self.vector = True
                    if i in g[i]:  # Есть ли петли
                        self.loop = True
                        self.loops.append(i)
            else:          # если карта графа представлена списком
                for i in self.points:
                    if not any(list(g[i].values())) and not any([list(v.values())[points.index(i)] for v in g.values()]):  # Поиск изолированных вершин   and not any([i in  for v in g.values()]):
                        self.isolate = True
                        self.isolates.append(i)
                    if not self.vector and not all([g[i][k] == g[k][i] for k in self.points]):  # Является ли граф ориентированным проверка на not vector, позволяет не проходить это ещё раз, если итак ясно что граф ориентированный
                        self.vector = True
                    if g[i][i]:  # Есть ли петли
                        self.loop = True
                        self.loops.append(i)
                        #print("Петли ")
            if not self.vector:
                res += "не"
            res += "направленный граф\n"
            res += "В графе " + str(len(g)) + " вершин\n"
            if self.isolates:
                res += 'вершины ' + ', '.join([str(i) for i in self.isolates]) + " - Изолированные\n"
            if self.loops:
                res += "У вершины " + ', '.join([str(i) for i in self.loops]) + " Есть Петли"
            self.analize_res = res
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)
            #print(e.__traceback__.)
