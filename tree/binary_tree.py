class Node:
    """이진 트리 노드 클래스"""

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

# 노드 인스턴스 생성
root_node = Node(2)
node_B = Node(3)
node_C = Node(5)
node_D = Node(7)
node_E = Node(11)

# B와 C를 root 노드의 자식으로 설정
root_node.left_child = node_B
root_node.right_child = node_C

# D와 E를 B의 자식으로 설정
node_B.left_child = node_D
node_B.right_child = node_E

# root 노드에서 왼쪽 자식 노드 받아오기
test_node_1 = root_node.left_child
print(test_node_1.data)

# 노드 B의 오른쪽 자식 노드 받아오기
test_node_2 = node_B.right_child
print(test_node_2.data)