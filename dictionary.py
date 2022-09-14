grades = {}

# key-value 데이터 삽입
grades['현승'] = 80
grades['태호'] = 60
grades['영훈'] = 90
grades['지웅'] = 70
grades['동욱'] = 96

# 한 key에 여러 value 저장 시도
grades['태호'] = 100

# key를 이용하여 value 탐색
print(grades['동욱'])
print(grades['지웅'])