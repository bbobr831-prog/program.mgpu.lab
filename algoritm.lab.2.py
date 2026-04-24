#Лабораторная работа по алгоритмизации №2
#ФИО: Бобр Богдан Александрович 
#Группа: ЦИБ-251
# Задание: Данные:
#1)Граф. Вершины и Ребра: 6 верш: (1,2), (2,3), (3,4), (5,6) 
#2)Дерево. Элементы для построения: {8, 12, 3, 10, 1, 14,20}
#3)Дерево. Найти /Удалить:  Найти: 3, Уд.: 12
#4)Куча.Массив для Heap Sort: [12, 8, 3, 10, 1, 14,20]

#1. ГРАФЫ:
def adjacency_matrix(n, edges):
    """
    Алгоритм: создание матрицы смежности.
    Сложность: O(N^2)
    """
    matrix = [[0]*n for _ in range(n)]
    for u, v in edges:
        matrix[u-1][v-1] = 1
        matrix[v-1][u-1] = 1
    return matrix


def incidence_matrix(n, edges):
    """
    Алгоритм: создание матрицы инцидентности.
    Сложность: O(N * M)
    """
    m = len(edges)
    matrix = [[0]*m for _ in range(n)]

    for j, (u, v) in enumerate(edges):
        matrix[u-1][j] = 1
        matrix[v-1][j] = 1

    return matrix


def find_components(n, edges):
    """
    Алгоритм: поиск компонент связности (DFS).
    Сложность: O(N + M)
    """
    graph = {i: [] for i in range(1, n+1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    components = []

    def dfs(v, comp):
        visited.add(v)
        comp.append(v)
        for nei in graph[v]:
            if nei not in visited:
                dfs(nei, comp)

    for v in graph:
        if v not in visited:
            comp = []
            dfs(v, comp)
            components.append(comp)

    return components


# ДАННЫЕ
n = 6
edges = [(1,2), (2,3), (3,4), (5,6)]

print("Матрица смежности:")
for row in adjacency_matrix(n, edges):
    print(row)

print("\nМатрица инцидентности:")
for row in incidence_matrix(n, edges):
    print(row)

print("\nКомпоненты связности:")
print(find_components(n, edges))

#2. ДЕРЕВО (BST):
class BSTNode:
    """
    Узел бинарного дерева поиска.
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    """
    Бинарное дерево поиска.
    """
    def __init__(self):
        self.root = None

    def insert(self, key):
        """
        Алгоритм: вставка в BST.
        Сложность: O(log N) в среднем, O(N) в худшем.
        """
        def _insert(node, key):
            if not node:
                return BSTNode(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)
            return node

        self.root = _insert(self.root, key)

    def search(self, key):
        """
        Алгоритм: поиск в BST.
        Сложность: O(log N) / O(N)
        """
        node = self.root
        while node:
            if node.key == key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def delete(self, key):
        """
        Алгоритм: удаление узла из BST.
        Сложность: O(log N) / O(N)
        """
        def _delete(node, key):
            if not node:
                return None
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left

                # минимум справа
                temp = node.right
                while temp.left:
                    temp = temp.left
                node.key = temp.key
                node.right = _delete(node.right, temp.key)

            return node

        self.root = _delete(self.root, key)


# ДАННЫЕ
bst = BST()
elements = [8, 12, 3, 10, 1, 14, 20]

for el in elements:
    bst.insert(el)

print("\nПоиск 3:", bst.search(3))

bst.delete(12)
print("Удалили 12. Поиск 12:", bst.search(12))

#3. HEAP SORT:

def heapify(arr, n, i):
    """
    Алгоритм: восстановление кучи.
    Сложность: O(log N)
    """
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Алгоритм: пирамидальная сортировка.
    Сложность: O(N log N)
    """
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


# ДАННЫЕ
arr = [12, 8, 3, 10, 1, 14, 20]
print("\nHeap Sort:", heap_sort(arr))
