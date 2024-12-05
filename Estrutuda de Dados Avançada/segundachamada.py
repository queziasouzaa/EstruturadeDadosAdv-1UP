import json

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#arvore Binaria de Busca (BST)
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)

    #realiza o percurso em pré-ordem (pre-order traversal)
    def pre_order_traversal(self):
        result = []
        self._pre_order_traversal(self.root, result)
        return result

    def _pre_order_traversal(self, node, result):
        if node:
            result.append(node.value)  # visita o nó atual
            self._pre_order_traversal(node.left, result)  # visita o filho da esquerda
            self._pre_order_traversal(node.right, result)  # visita o filho da direita

    #realiza o percurso em pós-ordem (post-order traversal)
    def post_order_traversal(self):
        result = []
        self._post_order_traversal(self.root, result)
        return result

    def _post_order_traversal(self, node, result):
        if node:
            self._post_order_traversal(node.left, result)  # visita o filho da esquerda
            self._post_order_traversal(node.right, result)  # visita o filho da direita
            result.append(node.value)  # visita o nó atual

def main():
    with open('arvore.json', 'r') as file:
        data = json.load(file)
        values = data["values"]

    bst = BinarySearchTree()
    for value in values:
        bst.insert(value)

    pre_order_values = bst.pre_order_traversal()
    print("Valores na ordem pre-ordem:", pre_order_values)

    post_order_values = bst.post_order_traversal()
    print("Valores na ordem pos-ordem:", post_order_values)

if __name__ == "__main__":
    main()
