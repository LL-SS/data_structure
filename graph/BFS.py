from collections import deque
from subway_graph import create_station_graph

def bfs(graph, start_node):
    """시작 노드에서 bfs를 실행하는 함수"""
    queue = deque()  # 빈 큐 생성

    # 일단 모든 노드를 방문하지 않은 노드로 표시
    for station_node in graph.values():
        station_node.visited = False

    start_node.visited = True
    queue.append(start_node)

# 큐에 넣을 때 visited 처리를 해주면 나중에 겹치는 역이 adjacent_stations 리스트에 추가되지 않음
# 큐에서 꺼낼 때 visited 처리를 해주면 겹치는 역들 모두 adjacent_stations 리스트에 추가됨
# visited 속성이 꺼내기 전에는 모두 False로 설정되어 있기 때문

    while queue:
        current_node = queue.popleft()

        for adjacents in current_node.adjacent_stations:
            if adjacents.visited == False:
                adjacents.visited = True
                queue.append(adjacents)

stations = create_station_graph("./new_stations.txt")  # stations.txt 파일로 그래프를 만든다

gangnam_station = stations["강남"]

# 강남역과 경로를 통해 연결된 모든 노드를 탐색
bfs(stations, gangnam_station)

# 강남역과 서울 지하철 역들이 연결됐는지 확인
print(stations["강동구청"].visited)
print(stations["평촌"].visited)
print(stations["송도"].visited)
print(stations["개화산"].visited)

# 강남역과 대전 지하철 역들이 연결됐는지 확인
print(stations["반석"].visited)
print(stations["지족"].visited)
print(stations["노은"].visited)
print(stations["(대전)신흥"].visited)