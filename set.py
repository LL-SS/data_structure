finished_classes = set()

# 데이터 저장
finished_classes.add('A')
finished_classes.add('B')
finished_classes.add('C')
finished_classes.add('D')
finished_classes.add('E')

# 중복 데이터 저장 시도
finished_classes.add('B')
finished_classes.add('E')

# 데이터 탐색
print('A' in finished_classes)
print('G' in finished_classes)

# 데이터 삭제
finished_classes.remove('A')
finished_classes.remove('E')

print(finished_classes)