class Node:
    """이진 탐색 트리 노드 클래스"""
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.right_child = None
        self.left_child = None


def print_inorder(node):
    """주어진 노드를 in-order로 출력해주는 함수"""
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)


class BinarySearchTree:
    """이진 탐색 트리 클래스"""
    def __init__(self):
        self.root = None

    def delete(self, data):
        """이진 탐색 트리 삭제 메소드"""
        node_to_delete = self.search(data)  # 삭제할 노드를 가지고 온다
        parent_node = node_to_delete.parent  # 삭제할 노드의 부모 노드

        # 경우 1: 지우려는 노드가 leaf 노드일 때 (코드를 쓰세요!)
        if node_to_delete.left_child is None and node_to_delete.right_child is None:
            if node_to_delete == self.root:
                self.root = None
            if parent_node.left_child == node_to_delete:
                parent_node.left_child = None
            else:
                parent_node.right_child = None

        # 경우 2: 지우려는 노드가 자식이 하나인 노드일 때:
        elif node_to_delete.left_child is None:  # 지우려는 노드가 오른쪽 자식만 있을 때:
            # 지우려는 노드가 root 노드일 때
            if node_to_delete is self.root:
                self.root = node_to_delete.right_child
                self.root.parent = None
            # 지우려는 노드가 부모의 왼쪽 자식일 때
            elif node_to_delete is parent_node.left_child:
                parent_node.left_child = node_to_delete.right_child
                node_to_delete.right_child.parent = parent_node
            # 지우려는 노드가 부모의 오른쪽 자식일 때
            else:
                parent_node.right_child = node_to_delete.right_child
                node_to_delete.right_child.parent = parent_node

        elif node_to_delete.right_child is None:  # 지우려는 노드가 왼쪽 자식만 있을 때:
            # 지우려는 노드가 root 노드일 때
            if node_to_delete is self.root:
                self.root = node_to_delete.left_child
                self.root.parent = None
            # 지우려는 노드가 부모의 왼쪽 자식일 때
            elif node_to_delete is parent_node.left_child:
                parent_node.left_child = node_to_delete.left_child
                node_to_delete.left_child.parent = parent_node
            # 지우려는 노드가 부모의 오른쪽 자식일 때
            else:
                parent_node.right_child = node_to_delete.left_child
                node_to_delete.left_child.parent = parent_node

        # 경우 3: 지우려는 노드가 2개의 자식이 있을 때
        else:
            successor = self.find_min(node_to_delete.right_child)  # 삭제하려는 노드의 successor 노드 받아오기
            node_to_delete.data = successor.data  # 삭제하려는 노드의 데이터에 successor의 데이터 저장

            # successor 노드 트리에서 삭제
            if successor is successor.parent.left_child:  # successor 노드가 왼쪽 자식일 때
                successor.parent.left_child = successor.right_child
            else:  # successor 노드가 오른쪽 자식일 때
                successor.parent.right_child = successor.right_child

            if successor.right_child is not None:  # successor 노드가 오른쪽 자식이 있을 떄
                successor.right_child.parent = successor.parent

    @staticmethod
    def find_min(node):
        """(부분)이진 탐색 트리의 가장 작은 노드 리턴"""
        # 코드를 쓰세요
        result_node = node

        while result_node.left_child is not None:
            result_node = result_node.left_child

        return result_node

    def search(self, data):
        """이진 탐색 트리 탐색 메소드, 찾는 데이터를 갖는 노드가 없으면 None을 리턴한다"""
        # 코드를 쓰세요
        searching_node = self.root

        while searching_node is not None:
            if searching_node.data == data:
                return searching_node
            else:
                if data < searching_node.data:
                    searching_node = searching_node.left_child
                else:
                    searching_node = searching_node.right_child

        return searching_node

    def insert(self, data):
        new_node = Node(data)  # 삽입할 데이터를 갖는 새 노드 생성

        # 트리가 비었으면 새로운 노드를 root 노드로 만든다
        if self.root is None:
            self.root = new_node
            return

        # 코드를 쓰세요
        parent_node = self.root # 일단 루트 노드를 부모 노드로 설정

        while new_node.parent is None: # 새로운 노드의 부모가 없을 때 까지 계속 탐색
            if new_node.data < parent_node.data:
                if parent_node.left_child is None: # 부모 노드의 왼쪽 자식이 비어 있으면 추가
                    new_node.parent = parent_node
                    parent_node.left_child = new_node
                else: # 부모 노드의 왼쪽 자식이 있으면 왼쪽 자식을 새로운 부모로 설정 후 계속 탐색
                    parent_node = parent_node.left_child

            else:
                if parent_node.right_child is None: # 부모 노드의 오른쪽 자식이 비어 있으면 추가
                    new_node.parent = parent_node
                    parent_node.right_child = new_node
                else: # 부모 노드의 오른쪽 자식이 있으면 오른쪽 자식을 새로운 부모로 설정 후 계속 탐색
                    parent_node = parent_node.right_child

    def print_sorted_tree(self):
        """이진 탐색 트리 내의 데이터를 정렬된 순서로 출력해주는 메소드"""
        print_inorder(self.root)  # root 노드를 in-order로 출력한다


bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

# 자식이 두 개 다 있는 노드 삭제
bst.delete(7)
bst.delete(11)

bst.print_sorted_tree()