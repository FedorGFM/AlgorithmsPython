# создание нодов, создание бинарного дерева, добавление значения, удаление значения, подсчет количества элементов.

# Class Node: Конструктор атрибутов для Node. 
# нода может быть левой или правой 
# определяем значение ноды целочисленное

class Node:
    def __init__(self, value, left=None, right=None) -> None: # Инициализация дерева 
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):  # Метод для строкового представления узла
        res = f'значение нашего узла: {self.value}'
        if self.left:
            res += f' значение левого: {self.left.value}'
        if self.right:
            res += f' значение правого: {self.right.value}'
        return res

class Tree: # Класс представлюящий дерево.
    def __init__(self, root=None): # Инициализирует состояние объекта.
        self.root = root

    def search(self, node, data, parent=None): #  Поиск узла с заданным значением в дереве. value - Значение для поиска. Returns - Найденный узел или None, если узел не найден
        if node is None or data == node.value:
            return node, parent

        if data > node.value:
            return self.search(node.right, data, node)
        if data < node.value:
            return self.search(node.left, data, node)

    def add_node(self, value): # Метод добавления узла.
        res = self.search(self.root, value)
        if res[0] is None:
            new_node = Node(value)
            if value > res[1].value:
                res[1].right = new_node
            else:
                res[1].left = new_node
        else:
            print('Ой все, такое значение уже есть')

    def height(self, node):
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1

    def balance_factor(self, node): 
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return left_height - right_height

    def rotate_left(self, node) -> None: # Левый поворот поддерева относительно заданного узла. node (Node): Узел, относительно которого выполняется поворот.
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root

    def rotate_right(self, node) -> None: #  Правый поворот поддерева относительно заданного узла. node (Node): Узел, относительно которого выполняется поворот.
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    def rebalance(self, node) -> None: # Ребаланс node
        if self.balance_factor(node) > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if self.balance_factor(node) < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def add_node_balanced(self, value): # Реализация балансировки дерева.
        self.root = self._add_node_balanced(self.root, value)

    def _add_node_balanced(self, node, value): # Добавление узла балансировки.
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._add_node_balanced(node.left, value)
        else:
            node.right = self._add_node_balanced(node.right, value)
        return self.rebalance(node)
    
    def delete_node(self, value): # Удаление узла из дерева. 1. Находим узел с заданным значением. 2. Вызываем функцию для удаления узла.
        self.root = self._delete_node(self.root, value)

    def _delete_node(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_node(node.left, value)
        elif value > node.value:
            node.right = self._delete_node(node.right, value)
        else:
            # Узел только с одним дочерним элементом, или без него
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Узел с двумя детьми
            successor = self._get_successor(node.right)
            node.value = successor.value
            node.right = self._delete_node(node.right, successor.value)

        return self.rebalance(node)

    def _get_successor(self, node):
        while node.left is not None:
            node = node.left
        return node

# Создание начальной вершины
initial_node = Node(15)
tree_1 = Tree(initial_node)

# Добавление узлов с автоматической балансировкой
tree_1.add_node_balanced(16)
tree_1.add_node_balanced(17)
tree_1.add_node_balanced(14)

# Удаление узла
tree_1.delete_node(16)

# Вывод информации о дереве и его узлах
print(tree_1.root)  # Вывод информации о корневом узле
print(tree_1.root.left)  # Вывод информации о левом узле
print(tree_1.root.right)  # Вывод информации о правом узле