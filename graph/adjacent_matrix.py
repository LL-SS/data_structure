# 모든 요소를 0으로 초기화시킨 크기 6 x 6 인접 행렬
adjacency_matrix = [[0 for i in range(6)] for i in range(6)]

# 코드를 쓰세요
for i in range(6):
    for j in range(6):
        if i == 0 and (j == 1 or j == 2):
            adjacency_matrix[i][j] = 1

        elif i == 1 and (j == 0 or j == 3 or j == 5):
            adjacency_matrix[i][j] = 1

        elif i == 2 and (j == 0 or j == 5):
            adjacency_matrix[i][j] = 1

        elif i == 3 and (j == 1 or j == 4 or j == 5):
            
            adjacency_matrix[i][j] = 1

        elif i == 4 and (j == 3 or j == 5):
            adjacency_matrix[i][j] = 1

        elif i == 5 and (j == 1 or j == 2 or j == 3 or j == 4):
            adjacency_matrix[i][j] = 1

        else:
            adjacency_matrix[i][j] = 0

print(adjacency_matrix)