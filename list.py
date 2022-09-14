# 파이썬 리스트 생성
trending = []

# 특정 위치에 데이터 삽입
trending.insert(0, 'A')
trending.insert(1, 'B')
trending.insert(2, 'C')
trending.insert(3, 'D')

# 괄호를 이용한 인덱스 접근
print(trending[0])
print(trending[1])

trending[2] = 4

# in을 이용한 탐색
print('A' in trending)
print('G' in trending)

# del을 이용한 삭제
del trending[0]

print(trending)